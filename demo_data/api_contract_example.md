# API Contract Example

Endpoint:

```http
POST /complaints/{complaintId}/reopen
```

Headers:

```http
X-User-Id: resident-1
Content-Type: application/json
```

Request body:

```json
{
  "reason": "Leak is still visible after repair"
}
```

Successful response:

```json
{
  "id": "cmp-100",
  "creator_id": "resident-1",
  "status": "reopened",
  "closed_at": "2026-07-20T10:00:00+00:00",
  "unresolved": true,
  "reopen_reason": "Leak is still visible after repair",
  "reopened_at": "2026-07-24T10:00:00+00:00"
}
```

