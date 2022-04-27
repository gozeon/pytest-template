import pytest

def setup_function():
    print("setup_function")

def teardown_function():
    print("teardown_function")

def test_func():
    """function 钩子"""
    assert 1 == 1
