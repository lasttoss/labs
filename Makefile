.PHONY: help gen check

help:
	@echo "gen     regenerate README.md from catalog.yaml"
	@echo "check   fail if README.md is stale (used by CI)"

gen:
	python3 gen_catalog.py

check:
	python3 gen_catalog.py --check
