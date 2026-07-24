# Student Activities

## Activity 1: Hidden Decisions

Prompt to show:

> Build a complete complaint-management application using Flask and React. Include authentication, dashboards, APIs, tests, documentation, and deployment.

Ask students to list hidden decisions the AI would need to invent.

Expected answers:

- User roles
- Complaint states
- Authentication
- Assignment
- Notifications
- Reopening rules
- Deletion policy
- Audit history
- Privacy rules
- API errors
- Deployment assumptions

## Activity 2: Weak Story Review

Use `demo_data/weak_user_story.md`.

Task:

- Identify problems in the story.
- Rewrite it as one testable story.
- Add three acceptance criteria.

## Activity 3: Ambiguity Review

Use `demo_data/reopen_complaint_story.md`.

Task:

- Ask the AI for unanswered questions.
- Choose three questions that require user research.
- Choose three assumptions that can be defined as product policy.

## Activity 4: Traceability Table

Task:

- Convert the reopening feature into a table connecting criteria, UI, API, business rules, and tests.

## Activity 5: Test Before Code

Task:

- List tests before implementation.
- Compare the list with `sample_repo/tests/test_complaints.py`.

## Activity 6: Review the Diff

Task:

- Review staged changes.
- Find missing tests or accidental behaviour changes.
- Suggest a commit message.

