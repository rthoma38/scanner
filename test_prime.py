# test_prime.py
import pytest
from prime import is_prime  # Assuming you have a function named is_prime in prime.py

def test_is_prime():
    assert is_prime(5) == True
    assert is_prime(4) == False
