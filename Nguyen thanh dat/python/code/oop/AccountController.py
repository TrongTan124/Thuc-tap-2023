from Validate import Validate
from Account import Account
import hashlib
class AccountController:
    def addAccount(self,listAcc):
        validator = Validate()
        md5_hash = hashlib.md5()
        username = validator.validateString("Enter username")
        passwordPreEn = validator.validateString("Enter password")
        password = self.encrypMD5(passwordPreEn)
        name = validator.validateString("Enter name")
        phone = validator.validatePhone("Enter phone")
        email = validator.validateEmail("Enter email")
        address = validator.validateString("Enter address")
        dob = validator.validateDob("Enter date of birth")
        account = Account(username,password,name,phone,email,address,dob)
        listAcc.append(account)
        print("Success")
    def findAccountByUSerName(self,listAcc,username):
        for acc in listAcc:
            if(acc.username == username):
                return acc
        return None
    def encrypMD5(self, inputPass):
        # Create an MD5 hash object
        md5_hash = hashlib.md5()

        # Encode the user's input as bytes
        user_input_bytes = inputPass.encode('utf-8')

        # Update the hash object with the user's input bytes
        md5_hash.update(user_input_bytes)

        # Get the hashed password as a hexadecimal string
        hashed_password = md5_hash.hexdigest()
        return hashed_password
    def login(self,listAcc):
        validator = Validate()
        username = validator.validateString("Enter user name")
        account = self.findAccountByUSerName(listAcc,username)
        passwordEn = validator.validateString("Enter password")
        password = self.encrypMD5(passwordEn)
        if(account == None):
            print("Usename or password wrong")
        else:
            if(account.password == password):
                print("welcom user ",account.username)
                isChangePass = validator.validateYN("You want to change pass Y/N")
                if(isChangePass):
                    oldpass = validator.validateString("Enter old password")
                    newpass = validator.validateString("Enter new password")
                    reEnterpass = validator.validateString("re enter new password")
                    if(account.password != self.encrypMD5(oldpass)):
                        print("old password not match current password")
                    elif(newpass !=reEnterpass):
                        print("newpass and reEnterpass not match")
                    elif(newpass == reEnterpass and account.password == self.encrypMD5(oldpass)):
                        passW = self.encrypMD5(newpass)
                        account.updatePass(passW)
                        print("success")
            else:
                print("username or password wrong")
                
    def menu(self,listAcc):
        while True:
            validator = Validate()
            choice  =validator.validateChoice("Enter choice between 1-3",1,3)
            if(choice == 1):
                self.addAccount(listAcc)
            elif(choice == 2):
                self.login(listAcc)
            else:
                return
            