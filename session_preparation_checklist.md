# AI Usage in Software Engineering Project: Session Preparation

## 1. Session Setup

- Decide session length: 90 minutes preferred, 60 minutes if time is limited.
- Keep the teaching guide open: `AI_Augmented_Software_Engineering_Teaching_Guide.docx`.
- Prepare screen sharing in advance and make sure font size is readable.
- Keep one AI assistant ready, such as Codex, Claude Code, GitHub Copilot, Aider, Continue, or browser chat.
- Prepare a disposable Git branch for all live edits.
- Keep terminal ready with:
  - Git
  - Python
  - pytest
  - a linter
  - project dependencies installed

## 2. Sample Repository

Prepare a small demo repository before the session. It should contain:

- One backend route.
- One test file.
- One OpenAPI file.
- One README.
- A simple domain such as complaint management.
- A clean Git history or at least one clean starting commit.
- A disposable branch for the live demo.

Suggested demo feature:

> A resident can reopen a closed complaint within seven calendar days when the issue is unresolved. A reopening reason is required. Only the complaint creator may reopen it.

## 3. Demo Data

Prepare short, realistic sample inputs:

- Interview notes about maintenance complaints.
- One weak user story to improve.
- One real-looking user story for ambiguity review.
- A few acceptance criteria.
- A small API contract example.
- A failing or missing test case.
- A small code change that can be implemented during the session.

Avoid using:

- Real student personal data.
- Real passwords, API keys, or secrets.
- Identifiable interview recordings.
- Private production code.
- Confidential project material.

## 4. Prompts to Keep Ready

Keep these prompt categories ready for copy-paste:

- Evidence-first requirements analysis.
- Weak user story review.
- Ambiguity hunter.
- Traceability table builder.
- Domain model reviewer.
- Architecture decision helper.
- UI consistency reviewer.
- API behaviour analyst.
- OpenAPI author.
- Test designer.
- Implementation agent.
- Four-way consistency reviewer.
- Staged diff commit reviewer.
- PR writer.
- Code-review subagent.

## 5. Teaching Flow

Prepare to explain this core message throughout the session:

> AI should strengthen the software-engineering process, not replace it. Students remain responsible for requirements, architecture, tests, security, Git history, and every submitted line of code.

Use this workflow as the main structure:

1. Interview evidence
2. User stories
3. Acceptance criteria
4. Domain model
5. API contract
6. Tests
7. Implementation
8. Review
9. User feedback

## 6. Live Demo Checklist

Before starting the session, verify that you can:

- Open the sample repository.
- Run the existing tests.
- Run the linter.
- Create and switch to a demo branch.
- Ask the AI assistant for a small artifact, not a full project.
- Show a bad prompt and explain why it is risky.
- Show a better prompt focused on one engineering artifact.
- Generate or review tests before implementation.
- Inspect the AI-generated code before accepting it.
- Show a staged diff.
- Create a clear commit message.
- Draft a PR description.

## 7. Student Activities to Prepare

Prepare short exercises for students:

- Identify hidden decisions in a vague "build everything" prompt.
- Review a weak user story.
- Find ambiguities in a reopening-complaint feature.
- Convert acceptance criteria into a traceability table.
- Identify leading interview questions.
- Ask AI to design tests before implementation.
- Review an AI-generated diff for risks.

## 8. Responsible AI Policy Points

Prepare a short policy slide or talking points covering:

- AI output must be reviewed by the student.
- AI cannot invent user research evidence.
- AI should not receive secrets or personal data.
- AI-generated code must be tested.
- Git history should clearly show human review.
- Students must understand every submitted line of code.
- Use free or local tools where possible.
- Choose the smallest useful AI task instead of asking AI to build the whole project.

## 9. Backup Plan

Prepare for tool or network failure:

- Save important prompts locally.
- Keep expected outputs ready in notes.
- Have screenshots or copied outputs for key demos.
- Keep the sample repository in a working state.
- Prepare to explain the workflow even if the AI tool is unavailable.
- Keep a second AI tool option available if possible.

## 10. Final Pre-Session Check

- Laptop charged and charger available.
- Internet connection tested.
- Browser tabs cleaned up.
- Terminal opened in the sample repository.
- Demo branch created.
- AI assistant signed in.
- No private files visible during screen sharing.
- Teaching guide and checklist open.
- Timer or rough schedule ready.
