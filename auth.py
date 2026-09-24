def authenticate(username, password):
    print("Authentication system")


def login(username, password):
    if username and password:
        print("Authentication successful")
        return True
    else:
        print("Authentication failed")
        return False


if __name__ == "__main__":
    login("student", "password")
