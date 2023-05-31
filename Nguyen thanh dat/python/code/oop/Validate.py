import re
class Validate:
    PHONE_REGEX = r'^[0-9#]{10,11}$'
    EMAIL_REGEX = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$'
    DOB_REGEX = r'^\d{2}/\d{2}/\d{4}$'
    @classmethod
    def validateString(cls,mess):
        print(mess)
        while(True):
            string = input()
            if(len(string) == 0):
                print("String is empty, enter again")
            else:
                return string
    @classmethod    
    def validatePhone(self,mess):
        print(mess)
        while(True):
            string = self.validateString("")
            if( not re.match(self.PHONE_REGEX, string) ):
                print("Enter phone is number and len between 10-11")
            else:
                return string
    @classmethod
    def validateEmail(self,mess):
        print(mess)
        while(True):
            string = self.validateString("")
            if(not re.match(self.EMAIL_REGEX, string) ):
                print("Enter email in format example@ex.com")
            else:
                return string
    @classmethod
    def validateNumber(self,mess):
        print(mess)
        while True:
            try:
                number = int(input())
                if number < 0:
                    print("You have entered a number larger than zero!")
                else:
                    return number
            except ValueError:
                print("You must enter a number")
    @classmethod
    def validateChoice(self,mess, min, max):
        print(mess)
        while True:
            number = self.validateNumber("Enter a number")
            if number < min or number > max:
                print("You have entered a number out of range")
            else:
                return number
    @classmethod
    def validateDob(self,mess):
        print(mess)
        while True:
            dob = self.validateString("")
            if( not re.match(self.DOB_REGEX, dob)):
                print("You have enter date of birth in format dd/mm/yyyy")
            else:
                return dob    
    @classmethod
    def validateYN(self,mess):
        print(mess)
        while True:
            string = self.validateString("")
            if(string == "Y"):
                return True
            elif(string == "N"):
                return False
            else:
                print("You just have enter Y or N")
    
    