from datetime import datetime, timezone

from flask import Flask, jsonify, request


app = Flask(__name__)


COMPLAINTS = {
    "cmp-100": {
        "id": "cmp-100",
        "creator_id": "resident-1",
        "status": "closed",
        "closed_at": "2026-07-20T10:00:00+00:00",
        "unresolved": True,
        "reopen_reason": None,
        "reopened_at": None,
    },
    "cmp-200": {
        "id": "cmp-200",
        "creator_id": "resident-2",
        "status": "closed",
        "closed_at": "2026-07-01T10:00:00+00:00",
        "unresolved": True,
        "reopen_reason": None,
        "reopened_at": None,
    },
    "cmp-300": {
        "id": "cmp-300",
        "creator_id": "resident-1",
        "status": "closed",
        "closed_at": "2026-07-20T10:00:00+00:00",
        "unresolved": False,
        "reopen_reason": None,
        "reopened_at": None,
    },
}


def parse_iso(value):
    return datetime.fromisoformat(value)


def utc_now():
    override = request.headers.get("X-Demo-Now")
    if override:
        return parse_iso(override)
    return datetime.now(timezone.utc)


@app.get("/complaints/<complaint_id>")
def get_complaint(complaint_id):
    complaint = COMPLAINTS.get(complaint_id)
    if complaint is None:
        return jsonify({"error": "complaint not found"}), 404

    return jsonify(complaint)


@app.post("/complaints/<complaint_id>/reopen")
def reopen_complaint(complaint_id):
    complaint = COMPLAINTS.get(complaint_id)
    if complaint is None:
        return jsonify({"error": "complaint not found"}), 404

    user_id = request.headers.get("X-User-Id")
    if user_id != complaint["creator_id"]:
        return jsonify({"error": "only the complaint creator may reopen it"}), 403

    payload = request.get_json(silent=True) or {}
    reason = str(payload.get("reason", "")).strip()
    if not reason:
        return jsonify({"error": "reopening reason is required"}), 400

    if complaint["status"] != "closed":
        return jsonify({"error": "only closed complaints may be reopened"}), 409

    if not complaint["unresolved"]:
        return jsonify({"error": "only unresolved complaints may be reopened"}), 409

    closed_at = parse_iso(complaint["closed_at"])
    days_since_close = (utc_now() - closed_at).days
    if days_since_close > 7:
        return jsonify({"error": "complaint can be reopened only within seven days"}), 409

    complaint["status"] = "reopened"
    complaint["reopen_reason"] = reason
    complaint["reopened_at"] = utc_now().isoformat()

    return jsonify(complaint), 200

