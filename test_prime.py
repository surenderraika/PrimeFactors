Step 1 
import pytest
from prime import generate_prime_factors

def test_non_integer_input():
    with pytest.raises(ValueError):
        generate_prime_factors("string")

  Step 2 
def test_input_1():
    assert generate_prime_factors(1) == []

Step 3 
def test_input_2():
    assert generate_prime_factors(2) == [2]

Step 4 
def test_input_3():
    assert generate_prime_factors(3) == [3]

Step 5 
def test_input_4():
    assert generate_prime_factors(4) == [2, 2]

Step 6 
def test_input_6():
    assert generate_prime_factors(6) == [2, 3]

Step 7 
def test_input_8():
    assert generate_prime_factors(8) == [2, 2]

Step 8 
def test_input_9():
    assert generate_prime_factors(9) == [3, 3] 

