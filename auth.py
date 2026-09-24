def login(username, password):
    if username == "admin" and password == "admin123":
        print("User authenticated successfully")
        return True
    else:
        print("Authentication failed")
        return False
