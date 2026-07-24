# Presenter Runbook

Session name:

**AI-Augmented Software Engineering for the IITM Project: From User Research to Tested APIs and Final Review**

Purpose:

Teach students how to use AI responsibly across the IITM Software Engineering Project, from Milestone 1 user research to Sprint APIs, pytest, code review, issue tracking, and final submission.

Core message to repeat:

> AI should strengthen the software engineering process, not replace it. Students remain responsible for requirements, design, tests, code, security, Git history, and every submitted line of code.

## Before the Session

Open these files:

- `facilitator_notes/course_alignment.md`
- `facilitator_notes/milestone_ai_playbook.md`
- `facilitator_notes/teaching_flow.md`
- `demo_data/interview_notes.md`
- `demo_data/weak_user_story.md`
- `demo_data/reopen_complaint_story.md`
- `sample_repo/app.py`
- `sample_repo/openapi.yaml`
- `sample_repo/tests/test_complaints.py`
- `prompts/`

Open a terminal in:

```text
AI_usage_in_our_life/sample_repo
```

Try these commands before class:

```bash
python --version
git --version
pytest --version
ruff --version
```

If `pytest` or `ruff` are missing, run:

```powershell
.\setup_windows.ps1
```

## 90-Minute Session Plan

### 0-5 min: Opening and Session Goal

Show:

- `facilitator_notes/course_alignment.md`

Say:

- This session is not about asking AI to build the full project.
- It is about using AI to improve each software engineering artifact.
- The IITM project is evaluated through milestones, so AI use must support those milestones.

Key point:

> Do not ask AI to build the project. Ask AI to create, critique, or verify one artifact at a time.

### 5-10 min: Connect to IITM Project Requirements

Show:

- Course options in `facilitator_notes/course_alignment.md`

Explain:

- Students can choose Community Services Platform or Civic Services Platform.
- The demo uses Civic Services Platform, specifically complaint management.
- The same AI workflow applies to apartment associations, clubs, libraries, volunteer groups, facility booking, waste collection, and permit tracking.

Mention common expectations:

- At least two user roles.
- Multiple related workflows.
- Well-defined APIs.
- Automated tests.
- Future growth and change.

### 10-22 min: Milestone 1 - User Requirements

Show:

- `demo_data/interview_notes.md`
- `prompts/01_evidence_first_requirements.md`
- `prompts/16_milestone_1_reviewer.md`

Say:

- Milestone 1 is about identifying users, real pain points, and SMART user stories.
- AI can organize interview notes, but it must not invent interviews, quotes, recordings, or user feedback.

Live demo:

1. Paste the interview notes into the evidence-first prompt.
2. Ask AI to separate facts, interpretations, and unsupported assumptions.
3. Point out that "dashboard", "notifications", and "AI classification" are not automatically justified unless the evidence supports them.

Student activity:

- Ask students: "What features would be unsafe to claim from these notes?"

Expected answers:

- Push notifications.
- AI classification.
- Automatic assignment.
- Dashboard.
- Payment workflow.

### 22-32 min: SMART User Stories

Show:

- `demo_data/weak_user_story.md`
- `prompts/02_weak_story_reviewer.md`

Say:

- IITM requires user stories in this format:
  - As a [type of user],
  - I want [an action],
  - So that [a benefit/value].

Live demo:

1. Show the weak story:
   > As a user, I want an AI-powered dashboard with notifications so that the system is easy.
2. Ask AI to review it before rewriting it.
3. Discuss why it is weak:
   - vague user,
   - bundled features,
   - unclear value,
   - not measurable,
   - unsupported use of AI.

Better version to show:

> As a resident, I want to view the current status of my complaint so that I know whether action is being taken.

### 32-42 min: Milestone 2 - Scheduling and Design

Show:

- `facilitator_notes/milestone_ai_playbook.md`
- `prompts/17_milestone_2_design_reviewer.md`

Say:

- Milestone 2 asks for schedule, components, class diagram, database design, scrum minutes, frontend pages, Gantt chart, Kanban board, and README.
- AI is useful as a reviewer here.
- The design must trace back to Milestone 1 user stories.

Explain AI use:

- Ask AI to review whether components match user stories.
- Ask AI to find missing class relationships.
- Ask AI to turn user stories into sprint tasks.
- Ask AI to format real scrum notes.

Warning:

- Do not invent scrum meetings.
- Do not generate diagrams that are disconnected from user stories.

### 42-58 min: Sprint 1 and Sprint 2 - APIs, YAML, and Tests

Show:

- `demo_data/reopen_complaint_story.md`
- `sample_repo/openapi.yaml`
- `prompts/08_api_behaviour_analyst.md`
- `prompts/18_sprint_api_yaml_reviewer.md`
- `prompts/19_course_test_case_formatter.md`

Say:

- Sprint 1 and Sprint 2 focus on API endpoints, test cases, and user testing.
- IITM specifically asks for Swagger-compatible YAML.
- YAML must include error handling, user-story mapping, and API descriptions.
- Test cases must include API, inputs, expected output, actual output, and result.

Live demo:

1. Show the reopening complaint user story.
2. Show the API endpoint:
   `POST /complaints/{complaintId}/reopen`
3. Show the YAML description mapping it to `US-CIVIC-REOPEN-001`.
4. Ask AI to review whether the YAML covers error cases.

Important error cases:

- Missing reason: `400`
- Non-creator: `403`
- Complaint not found: `404`
- Not eligible for reopening: `409`

### 58-68 min: pytest and Implementation

Show:

- `sample_repo/tests/test_complaints.py`
- `sample_repo/app.py`
- `prompts/10_test_designer.md`
- `prompts/11_implementation_agent.md`
- `prompts/12_four_way_consistency_reviewer.md`

Say:

- Tests should be designed before implementation.
- AI can generate or review tests, but students must understand what each test proves.
- Implementation must match user story, YAML, and tests.

Live demo:

Run:

```bash
pytest
```

Then explain the tests:

- Creator can reopen.
- Non-creator cannot reopen.
- Reason is required.
- Reopen deadline is enforced.
- Resolved complaint cannot be reopened.

If pytest is unavailable:

- Use `facilitator_notes/backup_outputs.md`.
- Explain expected test behaviour without running the tool.

### 68-78 min: Git, Issue Tracking, and Code Review

Show:

- `prompts/13_staged_diff_commit_reviewer.md`
- `prompts/14_pr_writer.md`
- `prompts/15_code_review_subagent.md`

Say:

- Final submission asks for issue tracking and code review evidence.
- Students should not treat Git as only a place to upload final code.
- Each meaningful change should connect to a user story or issue.

Live demo commands:

```bash
git status
git diff
git diff --staged
```

Explain:

- AI can review a staged diff.
- AI can draft a commit message.
- AI can draft a PR description.
- The student still owns whether the change is correct.

### 78-85 min: Final Submission Readiness

Show:

- `facilitator_notes/rubric_checklist.md`
- `prompts/20_final_submission_reviewer.md`

Say:

- Final submission includes working code, README, report, tools used, issue tracking, code review screenshots, presentation slides, and demo video.
- AI can check for missing evidence, but it cannot create fake evidence.

Ask students to check:

- Can someone else run your project from the README?
- Are your user stories, design, APIs, tests, and implementation consistent?
- Do you have screenshots for issue tracking and review?
- Is your final report consistent with earlier milestones?

### 85-90 min: Responsible AI Policy and Closing

Show:

- `facilitator_notes/responsible_ai_policy.md`

Say:

- AI output must be reviewed.
- AI must not receive secrets or personal data.
- AI must not invent interviews or user feedback.
- AI-generated code must be tested.
- Students must understand every submitted line.

Close with:

> Use AI as a reviewer, assistant, and consistency checker. Do not use it as a replacement for engineering judgement.

## 60-Minute Short Version

Use this if time is limited.

| Time | Segment |
| --- | --- |
| 0-5 min | Session goal and course alignment |
| 5-18 min | Milestone 1: evidence and SMART user stories |
| 18-28 min | Milestone 2: design and schedule review |
| 28-43 min | Sprint APIs, Swagger YAML, and test cases |
| 43-52 min | pytest, implementation, and consistency review |
| 52-57 min | Git, PR, issue tracking evidence |
| 57-60 min | Responsible AI policy |

## Files to Use During Class

Recommended order:

1. `facilitator_notes/course_alignment.md`
2. `demo_data/interview_notes.md`
3. `prompts/01_evidence_first_requirements.md`
4. `demo_data/weak_user_story.md`
5. `prompts/02_weak_story_reviewer.md`
6. `facilitator_notes/milestone_ai_playbook.md`
7. `demo_data/reopen_complaint_story.md`
8. `sample_repo/openapi.yaml`
9. `sample_repo/tests/test_complaints.py`
10. `sample_repo/app.py`
11. `facilitator_notes/rubric_checklist.md`
12. `facilitator_notes/responsible_ai_policy.md`

## One-Line Summary for Students

Use AI to produce and review one project artifact at a time: evidence, story, design, API contract, test, implementation, review, and final submission checklist.

