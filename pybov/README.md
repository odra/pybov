# pybov

## Dependencies

### Development

The following packages are required (using Fedora package names):

- python3-pytest
- python3-pytest-sugar
- mypy

Optional dependencies to easily run tests or build the package:

- make
- poetry

## Testing

The package is tested using pytest, which can be easily used via the provided Makefile
(if dependencies are installed in the host system):

```
$ make test
```

The following make command can be used to use poetry's scripts/binaries instead:

```
$ make test PYTHON_PATH="poetry run python" MYPY_PATH="poetry run mypy"
```

This project also test typehints using `mypy` in strict mode (`--strict`).
