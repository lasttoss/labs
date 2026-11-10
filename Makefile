.PHONY: help gen check

help:
	@echo "gen     regenerate README.md from catalog.yaml"
	@echo "check   fail if README.md is stale (used by CI)"
	@echo "links   verify every published repo URL answers 200"

gen:
	python3 gen_catalog.py

check:
	python3 gen_catalog.py --check

links:
	./check_links.sh
