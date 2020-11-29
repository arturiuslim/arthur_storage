def check_password(username, password, password_length=8,
		   check_username=True, spec_sym=True):
	if len(password) < password_length:
		return False
	elif check_username and username in password:
		return False
	else:
		return True
	
#def test_check_password_func():
#	assert check_password('user', '12345678') == True, "For user USER this password is correct"
#	assert check_password('user', '12345678', password_length=10) == False
#	assert check_password('user', '12345678user') == False
