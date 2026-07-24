# Reopen Complaint Story

Use this for ambiguity review, API design, test design, and implementation.

## User story

As a resident, I want to reopen my closed complaint within seven days so that unresolved issues can be reviewed again.

## Acceptance criteria

- Only the complaint creator can reopen the complaint.
- The complaint must currently be closed.
- The complaint must be unresolved.
- The complaint can be reopened only within seven calendar days of closure.
- The resident must provide a reopening reason.
- A successful reopening changes the complaint status to `reopened`.
- A successful reopening records the reopening reason and timestamp.
- An invalid complaint ID returns `404`.
- An unauthorised resident receives `403`.
- An ineligible complaint receives `409`.

