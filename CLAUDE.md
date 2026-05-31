# CLAUDE.md

Guidance for working in this curated skills repository.

## What This Repo Is

A minimal skills.sh-format library focused on:
- C4 architecture skills
- DDD skills
- problem discovery

The `skills` path is a symlink to `.agent-skills`.

## Active Skills

- c4-model
- c4-level1-context
- c4-level2-container
- c4-level3-component
- c4-level4-code
- ddd-core
- ddd-tactical
- ddd-patterns
- problem-discovery
- router

## Commands

```bash
make validate
make package
make help
```

## Important Notes

- `Makefile` uses `SKILL_CREATOR_DIR` for external scripts (`quick_validate.py`, `package_skill.py`).
- Update `SKILL_CREATOR_DIR` to your local path before running validate/package.
- `dist/` stores packaged `.skill` artifacts.
- `skills.json` is the installable catalog source of truth.
