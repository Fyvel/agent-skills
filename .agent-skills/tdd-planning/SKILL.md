---
name: tdd-planning
description: Use when a developer has a feature idea that must be refined into a testable specification before any tests are written. This skill owns requirements discovery only, drives ambiguity toward explicit decisions, and requires explicit human approval before handoff to test authoring.
metadata:
  tags: ["testing", "tdd", "planning", "requirements", "human-in-the-loop", "specification"]
---

# TDD Planning

**Convert an idea into a testable specification through structured human-in-the-loop refinement.**

This skill prepares a feature for Test-Driven Development without designing the implementation.

The separation of responsibilities is intentional:
- **Requirements discovery:** this skill owns clarification and specification.
- **Test generation:** a separate skill owns test writing.
- **Human implementation:** the developer owns production code.

The objective is to create a specification that is precise enough that tests can be written without ambiguity.

---

## Core Rules

- Never assume missing requirements.
- Ask questions instead of inventing behaviour.
- Drive ambiguity toward explicit decisions.
- Focus on observable outcomes.
- Avoid discussing implementation approaches unless explicitly requested.
- Do not write production code.
- Do not write tests.
- Do not enter implementation mode.

---

## Planning Workflow

### Step 1: Understand the Goal

Extract:
- Problem being solved
- User personas or actors
- Desired outcomes
- Constraints
- Success criteria

If any of these are unclear, ask questions before proceeding.

### Step 2: Discover Behaviour

For each capability, clarify:
- Inputs
- Outputs
- State transitions
- Failure modes
- Edge cases

Continue questioning until the behaviour is explicit enough that a test author would not need to guess intent.

### Step 3: Define Acceptance Criteria

For every feature slice, create objectively testable criteria for:
- Happy path
- Validation behaviour
- Error behaviour
- Boundary conditions

Bad:

```text
Fast response
```

Good:

```text
Response returned within 2 seconds for requests under 100 items
```

### Step 4: Produce the TDD Handoff Specification

Generate a handoff document with:
- Feature Summary
- Functional Requirements
- Non-Functional Requirements
- Acceptance Criteria
- Edge Cases
- Out of Scope
- Open Questions

The handoff is complete only when it is stable enough for a separate test-authoring skill to consume without guessing behaviour.

---

## Handoff Criteria

Only hand off when:
- Requirements are stable for the first slice.
- No unresolved behaviour exists for the tests to be written.
- Acceptance criteria are objectively testable.
- The human explicitly approves the handoff.

**Required approval phrase:**

```text
Handoff to TDD
```

If the approval phrase is not present, remain in planning.

---

## Output Format

When handoff is approved, produce:

```markdown
## TDD Specification

### Goal
...

### Feature Summary
...

### Functional Requirements
...

### Acceptance Criteria
...

### Edge Cases
...

### Non-Functional Requirements
...

### Out Of Scope
...

### Open Questions
...

### Test Author Guidance
Describe expected observable behaviours only.
Never include implementation suggestions.
```

---

## Anti-Patterns

| Anti-pattern | Why it fails | Corrective action |
|---|---|---|
| Filling in missing details from intuition | The tests will encode guesses instead of requirements | Ask the missing question explicitly |
| Mixing specification with solution design | The human loses control of implementation decisions | Keep discussion on behaviour and observable outcomes |
| Handing off with unresolved open questions | The test author must invent behaviour | Stay in planning until the first slice is stable |
| Writing tests during planning | It collapses requirements discovery and test generation into one role | Stop and complete the TDD specification first |
