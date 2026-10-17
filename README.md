# AI-Augmented Software Engineering Workshop

A facilitator-ready workshop for using AI responsibly across an IITM Software Engineering course project—from evidence-based requirements to API contracts, tests, implementation review, and final submission checks.

The central idea is simple: AI can accelerate a small, well-defined engineering task, but the student remains responsible for evidence, design decisions, correctness, privacy, and every submitted line.

## What is included

| Area | Contents |
| --- | --- |
| `prompts/` | 20 focused prompts for requirements, design, OpenAPI, testing, implementation, review, and milestone checks |
| `demo_data/` | Interview notes, weak stories, API examples, test-design notes, and a complaint-reopening scenario |
| `sample_repo/` | A minimal Flask complaint API, OpenAPI contract, and automated tests |
| `facilitator_notes/` | Teaching flow, course mapping, rubric checklist, responsible-AI policy, milestone playbook, and backup outputs |

## Workshop flow

```text
interview evidence
  -> requirements critique
  -> acceptance criteria and traceability
  -> domain/API design
  -> tests before implementation
  -> small reviewed code change
  -> staged-diff and PR review
  -> milestone/rubric check
```

The prepared prompts explicitly tell the model not to invent user-research evidence and encourage students to ask for critiques, alternatives, and checks rather than outsourcing an entire project.

## Run the complaint-management demo

The sample implements one bounded story: a complaint creator may reopen an unresolved, closed complaint within seven calendar days when a reason is supplied.

```bash
cd sample_repo
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
flask --app app run
```

The tests cover the successful path, ownership, required reason, seven-day boundary, and unresolved-status rule. `openapi.yaml` documents the same endpoint so the workshop can compare requirements, contract, tests, and code.

## Suggested use

1. Start with `facilitator_notes/course_alignment.md` and the milestone playbook.
2. Use the deliberately weak story in `demo_data/` to demonstrate an evidence-first review.
3. Compare the resulting criteria with the OpenAPI contract and tests in `sample_repo/`.
4. Make one disposable-branch change and use the staged-diff, PR, and code-review prompts.
5. Close with `facilitator_notes/responsible_ai_policy.md`.

## Responsible-use boundaries

- Do not send secrets, passwords, private data, or identifiable interview recordings to an AI service.
- Do not allow a model to fabricate user research, test evidence, or completed work.
- Review and test generated code, and understand it before submission.
- Prefer the smallest useful AI task.
- When model output conflicts with course or project requirements, the requirements win.

## Scope

This repository is teaching material, not a full production complaint platform. The demo uses in-memory state and a header-based user identity solely to keep the live exercise inspectable. It has no persistent database, authentication service, or deployment configuration.
