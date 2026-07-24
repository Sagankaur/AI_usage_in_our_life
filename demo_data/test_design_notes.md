# Test Design Notes

Ask students which tests should exist before implementation.

## Required cases

- Creator can reopen a closed unresolved complaint within seven days.
- Non-creator cannot reopen the complaint.
- Reopening reason is required.
- Complaint cannot be reopened after seven days.
- Resolved complaint cannot be reopened.
- Invalid complaint ID returns `404`.
- Already reopened complaint should not be reopened again.

## Discussion question

Which of these cases are business rules, and which are API validation rules?

