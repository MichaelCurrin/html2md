SHELL = /bin/bash


default: install

all: install check


h help:
	@grep '^[a-z]' Makefile


install:
	poetry install --no-root

update:
	poetry update

g install-global:
	pipx install . --force


fmt:
	poetry run black .
	poetry run isort .

fmt-check:
	poetry run black . --diff --check
	poetry run isort . --diff --check-only

check:
	poetry build
	$(MAKE) fmt-check
