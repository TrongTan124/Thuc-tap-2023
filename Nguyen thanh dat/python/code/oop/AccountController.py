from Validate import Validate
from Account import Account
import hashlib


class AccountController:

    def add_account(self, list_acc):
        validator = Validate()
        md5_hash = hashlib.md5()
        username = validator.validate_string("Enter username")
        password_pre_en = validator.validate_string("Enter password")
        password = self.encrypMD5(password_pre_en)
        name = validator.validate_string("Enter name")
        phone = validator.validate_phone("Enter phone")
        email = validator.validate_email("Enter email")
        address = validator.validate_string("Enter address")
        dob = validator.validate_dob("Enter date of birth")
        account = Account(username, password, name, phone, email, address, dob)
        list_acc.extend(account)
        print("Success")

    def find_account_by_username(self, list_acc, username):
        for acc in list_acc:
            if(acc.username == username):
                return acc
        return None

    def encrypMD5(self, input_pass):
        # Create an MD5 hash object
        md5_hash = hashlib.md5()
        # Encode the user's input as bytes
        user_input_bytes = input_pass.encode('utf-8')
        # Update the hash object with the user's input bytes
        md5_hash.update(user_input_bytes)
        # Get the hashed password as a hexadecimal string
        hashed_password = md5_hash.hexdigest()
        return hashed_password

    def login(self, list_acc):
        validator = Validate()
        username = validator.validate_string("Enter username")
        account = self.find_account_by_username(list_acc, username)
        password_en = validator.validate_string("Enter password")
        password = self.encrypMD5(password_en)

        if account is None:
            print("Username or password is incorrect")
        else:
            if account.password == password:
                print("Welcome, user", account.username)
                is_change_pass = validator.validate_YN("Do you want to change your password? (Y/N)")
                if is_change_pass:
                    is_change_pass(account)
            else:
                print("Username or password is incorrect")
    
    def change_pass(self, account):   
        validator = Validate() 
        old_pass = validator.validate_string("Enter old password")
        new_pass = validator.validate_string("Enter new password")
        re_enter_pass = validator.validate_string("Re-enter new password")
                
        if account.password != self.encrypMD5(old_pass):
            print("Old password does not match the current password")
        elif new_pass != re_enter_pass:
            print("New password and re-entered password do not match")
        else:
            pass_W = self.encrypMD5(new_pass)
            account.update_pass(pass_W)
            print("Password changed successfully")

    def menu(self, list_acc):
        while True:
            validator = Validate()
            choice = validator.validate_choice("Enter choice between 1-3", 1, 3)
            if(choice == 1):
                self.add_account(list_acc)
            elif(choice == 2):
                self.login(list_acc)
            else:
                return

   