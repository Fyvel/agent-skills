# Makefile for AI Agent Skills

# Paths
SKILL_CREATOR_ROOT = .agents/skills/skill-creator
SKILL_CREATOR_DIR = $(SKILL_CREATOR_ROOT)/scripts
SOURCE_DIR = .agent-skills
DIST_DIR = dist

# Scripts
PACKAGE_SCRIPT = PYTHONPATH=$(SKILL_CREATOR_ROOT) python3 $(SKILL_CREATOR_DIR)/package_skill.py

# Find all skill directories (excluding hidden ones)
SKILLS = $(shell find $(SOURCE_DIR) -maxdepth 1 -mindepth 1 -type d)

.PHONY: all package validate clean help

all: package

## package: Pack all skills into .skill files in dist/
package: clean
	@mkdir -p $(DIST_DIR)
	@echo "📦 Packaging all skills..."
	@$(foreach skill,$(SKILLS), $(PACKAGE_SCRIPT) $(skill) $(DIST_DIR);)
	@echo "✅ All skills packaged successfully in $(DIST_DIR)/"

## validate: Run validation check on all skills
validate:
	@echo "🔍 Validating all skills..."
	@$(foreach skill,$(SKILLS), PYTHONPATH=$(SKILL_CREATOR_ROOT) python3 -m scripts.quick_validate $(skill);)
	@echo "✅ Validation complete."

## clean: Remove all packaged skills from dist/
clean:
	@echo "🧹 Cleaning $(DIST_DIR)..."
	@rm -rf $(DIST_DIR)/*.skill
	@if [ -d "./--validate-only" ]; then rm -rf "./--validate-only"; fi

## help: Show this help message
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^##' Makefile | sed -e 's/## //'
