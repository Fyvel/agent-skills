#!/usr/bin/env python3
"""
Skill router hook for fyvel-skills.
Reads user prompt from stdin (UserPromptSubmit hook payload or raw text),
matches intent to the curated skill set, and prints a hint line.
"""

import json
import sys

SKILL_ROUTES = [
    {
        "skill": "fyvel-skills:c4-model",
        "keywords": ["c4", "architecture overview", "which c4 level", "architecture map"],
    },
    {
        "skill": "fyvel-skills:c4-level1-context",
        "keywords": ["context diagram", "system context", "c4 level 1", "level 1"],
    },
    {
        "skill": "fyvel-skills:c4-level2-container",
        "keywords": ["container diagram", "c4 level 2", "level 2", "service topology"],
    },
    {
        "skill": "fyvel-skills:c4-level3-component",
        "keywords": ["component diagram", "c4 level 3", "level 3", "module breakdown"],
    },
    {
        "skill": "fyvel-skills:c4-level4-code",
        "keywords": ["class diagram", "er diagram", "uml", "c4 level 4", "level 4"],
    },
    {
        "skill": "fyvel-skills:ddd-core",
        "keywords": ["bounded context", "strategic ddd", "ubiquitous language", "domain decomposition"],
    },
    {
        "skill": "fyvel-skills:ddd-tactical",
        "keywords": ["aggregate", "entity", "value object", "repository", "domain service"],
    },
    {
        "skill": "fyvel-skills:ddd-patterns",
        "keywords": ["cqrs", "event sourcing", "saga", "outbox", "anti-corruption layer", "acl"],
    },
    {
        "skill": "fyvel-skills:problem-discovery",
        "keywords": ["validate problem", "problem discovery", "is there demand", "customer interview", "landing page test", "smoke test"],
    },
]


def match_skills(prompt: str) -> list[str]:
    prompt_lower = prompt.lower()
    matched = []
    seen = set()
    for route in SKILL_ROUTES:
        if route["skill"] in seen:
            continue
        for kw in route["keywords"]:
            if kw in prompt_lower:
                matched.append(route["skill"])
                seen.add(route["skill"])
                break
    return matched[:3]


def read_prompt() -> str:
    raw = sys.stdin.read()
    if not raw.strip():
        return ""

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return raw

    return str(data.get("prompt") or data.get("message") or raw)


def main() -> None:
    prompt = read_prompt()
    if not prompt:
        return

    matched = match_skills(prompt)
    if not matched:
        return

    skills_hint = ", ".join(matched)
    print(f"[skill-router] Relevant fyvel-skills detected: {skills_hint}")
    if len(matched) > 1:
        print("[skill-router] Invoke the most specific one.")


if __name__ == "__main__":
    main()
