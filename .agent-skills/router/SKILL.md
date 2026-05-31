---
name: router
description: Dispatch to the right skill based on user intent. Trigger when user says "use the right skill", "skill router", or when multiple retained skills could apply.
metadata:
  tags: ["routing", "dispatch", "meta", "orchestration"]
---

# Skill Router

Dispatch to the correct skill using a simple 3-layer cascade.

## Layer 1: Hook Hint (auto)
Check if `[skill-router]` hint appears in context.
If yes: use the suggested skill directly.

## Layer 2: Memory Recall
```
Invoke: memory-recall
Query: "skill routing [topic keywords from user message]"
```
If memory returns a routing pattern, use it.

## Layer 3: Intent Matching

Map user intent to available local skills.

### Architecture Track
| Intent | Skill |
|--------|-------|
| C4 overview (which level?) | `c4-model` |
| System context diagram | `c4-level1-context` |
| Container/service diagram | `c4-level2-container` |
| Component/internal diagram | `c4-level3-component` |
| Class/ER diagram | `c4-level4-code` |

### DDD Track
| Intent | Skill |
|--------|-------|
| Strategic DDD, bounded context | `ddd-core` |
| Aggregate, entity, value object | `ddd-tactical` |
| CQRS, event sourcing, saga | `ddd-patterns` |

### Discovery Track
| Intent | Skill |
|--------|-------|
| Validate problem/demand | `problem-discovery` |

### TDD Track
| Intent | Skill |
|--------|-------|
| Clarify a feature idea into a testable specification, TDD planning, or HITL refinement before tests exist | `tdd-planning` |
| Write tests only from an approved TDD specification | `tdd-test-author` |

## Dispatch Protocol

1. Identify matched skill from table.
2. Announce: "Using `<skill>` to `<purpose>`."
3. Invoke the matched skill.
4. Follow its instructions.

## Memory Integration

After completing a routed task:
- If routing was non-obvious or user confirmed it worked, store a pattern.
- Store format: `"[intent keywords] -> [skill-name] -> worked for [context]"`.

## When Multiple Skills Match

Pick most specific:
- `c4-level1-context` over `c4-model`
- `ddd-tactical` over `ddd-core` when aggregate/entity/value object appears
- `tdd-planning` over `tdd-test-author` unless the user already has an approved TDD specification or explicitly asks for test writing only
- Ask user only if two options are truly equal
