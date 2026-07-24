# Backup Outputs

Use these if the AI tool or network fails during the session.

## Evidence-first analysis: expected output

Supported problems:

- Residents cannot see complaint status.
- Residents repeat complaints when status is unclear.
- Managers struggle to count unresolved issues.
- Reopened or recurring issues are not clearly connected to the original complaint.

Unsupported assumptions:

- Push notifications are required.
- AI classification is required.
- Automatic assignment is required.
- A dashboard is the only solution.

Candidate story:

> As a resident, I want to view the current status of my complaint so that I know whether action is being taken.

Acceptance criteria:

- The resident can view the current complaint status.
- Every status change records a timestamp.
- Only authorised staff can change status.
- An invalid complaint ID returns `404`.

## Ambiguity hunter: expected questions

- Who is allowed to reopen a complaint?
- What does "within seven days" mean exactly?
- Does the seven-day window include the closure day?
- Can a resolved complaint be reopened?
- Is a reopening reason required?
- Can the complaint be reopened more than once?
- Does reopening reset assignment?
- Should reopening create an audit event?
- What error should the API return after the deadline?

## Traceability sample

| Story ID | Acceptance criterion | UI element | API endpoint | Business rule | Test ID | Evidence required |
| --- | --- | --- | --- | --- | --- | --- |
| US-REOPEN-1 | Only creator can reopen | Reopen button visibility | `POST /complaints/{id}/reopen` | Creator ownership check | `test_non_creator_cannot_reopen_complaint` | User role and ownership policy |
| US-REOPEN-1 | Reason required | Reason text area | `POST /complaints/{id}/reopen` | Non-empty reason | `test_reason_is_required` | Complaint follow-up workflow |
| US-REOPEN-1 | Seven-day limit | Disabled reopen action after deadline | `POST /complaints/{id}/reopen` | Deadline from closure timestamp | `test_complaint_cannot_be_reopened_after_seven_days` | Product policy |

## PR description sample

### Summary

Adds a complaint reopening endpoint for closed unresolved complaints.

### Requirement

Residents can reopen their own closed unresolved complaint within seven calendar days when they provide a reason.

### Tests run

- `pytest`
- `ruff check .`

### Risks

- Demo uses in-memory data, so persistence and audit logging are intentionally out of scope.

### Manual review checklist

- Confirm authorization rule.
- Confirm seven-day policy.
- Confirm error codes.
- Confirm no unrelated behaviour changed.

