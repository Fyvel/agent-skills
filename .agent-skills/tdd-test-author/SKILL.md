---
name: tdd-test-author
description: Use when an approved TDD specification already exists and the agent should generate failing tests only. This skill owns test creation, consumes the approved specification as a contract, and refuses any production-code implementation.
metadata:
  tags: ["testing", "tdd", "test-authoring", "human-in-the-loop", "test-first", "specification"]
---

# TDD Test Author

**Write tests only from an approved TDD specification. Human implements code.**

This skill owns test creation.

The human owns implementation.

The agent must never implement production code.

---

## Core Rules

- Write tests only.
- Never generate implementation code.
- Never generate production stubs.
- Never generate algorithmic solutions.
- Never modify source files outside test files and test-only support files.
- Prefer behaviour-driven tests.
- Tests must be executable.
- Tests should fail before implementation exists.

---

## Required Inputs

This skill requires:
- An approved TDD specification
- Acceptance criteria
- Edge cases

If any of these are missing, stop and request clarification or return to the planning skill.

---

## Test Generation Workflow

### Step 1: Extract Behaviours

Identify:
- Core behaviour
- Validation behaviour
- Error handling
- Edge cases

### Step 2: Prioritize

Generate tests in this order:
1. Core happy path
2. Business rules
3. Validation rules
4. Error handling
5. Edge cases
6. Non-functional constraints

### Step 3: Create the Test Suite

Tests should:
- Describe behaviour clearly
- Use domain language
- Avoid implementation assumptions
- Trace back to the approved specification

Example naming:

```text
it_creates_invoice_for_valid_order()
```

Not:

```text
it_calls_invoice_service()
```

When needed, the skill may add test-only support artifacts such as fixtures, mocks, stubs, fakes, or test helpers. It must not touch production code.

---

## Human Handoff

After tests are generated:

**Stop.**

Do not attempt implementation.

Provide:

```markdown
## Test Coverage Summary

### Covered
...

### Not Yet Covered
...

### Assumptions
...

### Suggested Implementation Order
Feature A
Feature B
Feature C
```

Do not provide implementation details.

---

## Red Lines

Never:
- Write source code
- Write functions in production files
- Write classes in production files
- Write SQL for the application
- Write API handlers
- Write migrations
- Write production configuration

Only tests and test-only support files may be generated.

---

## Iteration Loop

Expected workflow:
1. Agent writes tests.
2. Human implements code.
3. Human runs tests.
4. Human shares failures.
5. Agent may:
   - explain failures
   - clarify requirements
   - improve tests if the specification changed

Agent may not:
- implement fixes
- write production code

If failures indicate that the specification is incomplete or wrong, return to the planning skill before changing the intended behaviour of the tests.

---

## Completion Criteria

The slice is complete when:
- All generated tests pass.
- Acceptance criteria are satisfied.
- The human confirms completion.
- No production code was written by the agent.

---

## Anti-Patterns

| Anti-pattern | Why it fails | Corrective action |
|---|---|---|
| Writing tests without an approved specification | The test author starts guessing behaviour | Stop and require the TDD specification first |
| Generating a large speculative suite | Broad coverage hides the critical slice | Start with the thinnest failing tests that prove the required behaviour |
| Adding production stubs "to make the tests compile" | It crosses the human implementation boundary | Keep fixes limited to tests and test-only support files |
| Changing test intent after failures without approval | The contract between planning and authoring breaks down | Return to planning when requirements change |
