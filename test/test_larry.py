import pytest
import sys
from larry import add, reciprocal


class TestAdd:

    def test_basic(self):
        assert add(3, 5) == 8


class TestReciprocal:

    def test_basic(self):
        assert reciprocal(5.) == 0.2


if __name__ == '__main__':
    pytest.main([__file__, "-s"])
