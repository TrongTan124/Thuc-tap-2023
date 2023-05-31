import re
 
 
class Validate:
    PHONE_REGEX = r'^[0-9#]{10,11}$'
    EMAIL_REGEX = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$'
    DOB_REGEX = r'^\d{2}/\d{2}/\d{4}$'
    
    @classmethod
    def validate_number(self, mess):
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
    def validate_choice(self, mess, min, max):
        print(mess)
        while True:
            number = self.validate_number("Enter a number")
            if number < min or number > max:
                print("You have entered a number out of range")
            else:
                return number
            
    @classmethod
    def validate_string(cls, mess):
        print(mess)
        while(True):
            string = input()
            if(len(string) == 0):
                print("String is empty, enter again")
            else:
                return string
            
    @classmethod
    def validate_YN(self, mess):
        print(mess)
        while True:
            string = self.validate_string("")
            if(string == "Y"):
                return True
            elif(string == "N"):
                return False
            else:
                print("You just have enter Y or N")
    
    @classmethod    
    def validate_phone(self, mess):
        print(mess)
        while(True):
            string = self.validate_ptring("")
            if( not re.match(self.PHONE_REGEX, string) ):
                print("Enter phone is number and len between 10-11")
            else:
                return string
            
    @classmethod
    def validate_email(self,mess):
        print(mess)
        while(True):
            string = self.validate_string("")
            if(not re.match(self.EMAIL_REGEX, string)):
                print("Enter email in format example@ex.com")
            else:
                return string
            
    @classmethod
    def validate_dob(self, mess):
        print(mess)
        while True:
            dob = self.validate_string("")
            if( not re.match(self.DOB_REGEX, dob)):
                print("You have enter date of birth in format dd/mm/yyyy")
            else:
                return dob    
                  


