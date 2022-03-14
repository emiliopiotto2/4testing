import pytest
from main import *

def test_capital_case():
    assert(capital_case('flag')=='Flag')