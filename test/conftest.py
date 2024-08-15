import os

import pytest


@pytest.fixture
def testdir():
    return os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def fixdir(testdir):
    return f'{testdir}/fixtures'


@pytest.fixture
def b3data(fixdir):
    path = f'{fixdir}/b3-sample-historical-data.txt'
    with open(path, 'r') as f:
        return [line.replace('\n', '') for line in f.readlines()]
