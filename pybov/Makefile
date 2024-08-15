SHELL := /bin/bash
PY_PATH := /usr/bin/python3
PYTEST_PATH := ${PY_PATH} -m pytest
SRC_DIR := src/
TEST_DIR := test/
MYPY_PATH := ${PY_PATH} -m mypy
MYPY_ARGS := --strict

.PHONY: test/code
test/code:
	${MYPY_PATH} ${MYPY_ARGS} ${SRC_DIR}

.PHONY: test/unit
test/unit:
	${PYTEST_PATH} ${TEST_DIR}

.PHONY: test
test: test/code test/unit

poetry/%:
	@$(MAKE) $* PY_PATH="poetry run python"

.PHONY: test/code test/unit test
