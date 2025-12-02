SRC_DIR := ./src
TEST_DIR := ./test
PYTHON_PATH := /usr/bin/python
MYPY_PATH := /usr/bin/mypy
MYPY_OPTS := --strict

.PHONY: test/typehints
test/typehints:
	${MYPY_PATH} ${MYPY_OPTS} ${SRC_DIR}

.PHONY: test
test: test/typehints
	PYTHONPATH=${SRC_DIR} ${PYTHON_PATH} -m pytest ${TEST_DIR}
