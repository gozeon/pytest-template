import pytest

class TestClass:
    def setup_class(self):
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')
    
    def test_A(self):
        """class 钩子"""
        assert 1 == 1
