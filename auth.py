def authenticate(username, password):
    print("Authentication system")


def login(username, password):
    if username == "student" and password == "password":
        print("Login successful")
    else:
        print("Invalid username or password")


if __name__ == "__main__":
    login("student", "password")