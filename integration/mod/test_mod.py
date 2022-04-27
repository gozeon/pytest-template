import pytest

def setup_module():
    print('setup_module')

def teardown_module():
    print('teardown_module')


def test_func():
    """module 钩子"""
    assert 1 == 1
