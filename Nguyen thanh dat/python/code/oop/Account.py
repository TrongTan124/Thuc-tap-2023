

class Account:
    def __init__(self, username, password, name, phone, email, address, dob):
        self.username = username
        self.password = password
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.dob = dob

    def update_pass(self, password):
        self.password = password

