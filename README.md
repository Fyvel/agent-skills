# Focused C4 + DDD Skills Library

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: skills.sh](https://img.shields.io/badge/Format-skills.sh-green.svg)](https://skills.sh)

A curated private skills library focused on:
- C4 architecture modeling
- Domain-Driven Design (DDD)
- Problem discovery before solutioning

This repository is intentionally minimal so you can add skills incrementally over time.

## Retained Guides

- [Antigravity Workflow](./docs/antigravity-workflow.md)
- [DDD + C4 Mapping](./docs/ddd-c4-mapping.md)
- [Second Brain Knowledge Compression](./docs/second-brain-knowledge-compression.md)

## Retained Installable Skills

### C4
- [c4-model](./.agent-skills/c4-model)
- [c4-level1-context](./.agent-skills/c4-level1-context)
- [c4-level2-container](./.agent-skills/c4-level2-container)
- [c4-level3-component](./.agent-skills/c4-level3-component)
- [c4-level4-code](./.agent-skills/c4-level4-code)

### DDD
- [ddd-core](./.agent-skills/ddd-core)
- [ddd-tactical](./.agent-skills/ddd-tactical)
- [ddd-patterns](./.agent-skills/ddd-patterns)

### Discovery
- [problem-discovery](./.agent-skills/problem-discovery)

### Routing
- [router](./.agent-skills/router)

## Install

### skills.sh compatible tools

```bash
npx skills add fyvel/agent-skills
```

Install only specific skills from this library:

```bash
# list available skill names
npx skills add fyvel/agent-skills --list

# only C4
npx skills add fyvel/agent-skills --skill c4-model c4-level1-context c4-level2-container c4-level3-component c4-level4-code

# only DDD
npx skills add fyvel/agent-skills --skill ddd-core ddd-tactical ddd-patterns
```

## Build and Validate

```bash
make validate
make package
```

Note: `Makefile` currently expects local scripts from `skill-creator`. Update `SKILL_CREATOR_DIR` for your environment before running these commands.

## Repository Structure

```text
.agent-skills/    # Skill source files
skills -> .agent-skills
skills.json       # Installable skill catalog
skills-lock.json  # Lock/hash metadata
dist/             # Packaged .skill archives
```

## License

MIT License - see [LICENSE](LICENSE).
