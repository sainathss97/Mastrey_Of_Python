import re
# Todo 1: Input password
password = input("Enter the password:\n")
# Todo 2: check input length
if len(password) < 8 or len(password) > 16:
    raise Exception(f"Password Greater or less than required length")
else:
    # Todo 3: Password validation with regex
    password_checker = re.compile(r'([A-Za-z0-9!@#$%^&*()\-_=+{};:,<.>]{8,16})')
    check = password_checker.match(password)
    if check:
        print(f"Password {'*'*len(password)} is a match")
    else:
        print(f"Password {'*' * len(password)} is not  a match")
