import pytest
from check_password_example.py import check_password
#check_password_example.py

def test_check_password_func():
        assert check_password('user', '12345678') == True, "For user USER this password is correct"
        assert check_password('user', '12345678', password_length=10) == False
        assert check_password('user', '12345678user') == False

