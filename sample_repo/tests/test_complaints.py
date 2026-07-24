import copy

import pytest

import app as complaint_app


@pytest.fixture(autouse=True)
def reset_complaints():
    original = copy.deepcopy(complaint_app.COMPLAINTS)
    yield
    complaint_app.COMPLAINTS.clear()
    complaint_app.COMPLAINTS.update(original)


@pytest.fixture
def client():
    complaint_app.app.config.update(TESTING=True)
    return complaint_app.app.test_client()


def test_creator_can_reopen_unresolved_closed_complaint_with_reason(client):
    response = client.post(
        "/complaints/cmp-100/reopen",
        json={"reason": "Leak is still visible after repair"},
        headers={
            "X-User-Id": "resident-1",
            "X-Demo-Now": "2026-07-24T10:00:00+00:00",
        },
    )

    assert response.status_code == 200
    body = response.get_json()
    assert body["status"] == "reopened"
    assert body["reopen_reason"] == "Leak is still visible after repair"
    assert body["reopened_at"] is not None


def test_non_creator_cannot_reopen_complaint(client):
    response = client.post(
        "/complaints/cmp-100/reopen",
        json={"reason": "Issue is unresolved"},
        headers={"X-User-Id": "resident-2"},
    )

    assert response.status_code == 403


def test_reason_is_required(client):
    response = client.post(
        "/complaints/cmp-100/reopen",
        json={"reason": "   "},
        headers={"X-User-Id": "resident-1"},
    )

    assert response.status_code == 400


def test_complaint_cannot_be_reopened_after_seven_days(client):
    response = client.post(
        "/complaints/cmp-200/reopen",
        json={"reason": "Issue still exists"},
        headers={
            "X-User-Id": "resident-2",
            "X-Demo-Now": "2026-07-24T10:00:00+00:00",
        },
    )

    assert response.status_code == 409


def test_resolved_complaint_cannot_be_reopened(client):
    response = client.post(
        "/complaints/cmp-300/reopen",
        json={"reason": "Need another check"},
        headers={
            "X-User-Id": "resident-1",
            "X-Demo-Now": "2026-07-24T10:00:00+00:00",
        },
    )

    assert response.status_code == 409

