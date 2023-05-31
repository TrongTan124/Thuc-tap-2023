from Account import Account
from Validate import Validate
from AccountController import AccountController 

controller = AccountController()

if __name__ == '__main__':
    listAcc = []
    passs = controller.encrypMD5("123")
    listAcc.append(Account("hidro",passs,"dat","0123456789","h@gmail.com","abc","21/06/2002"))
    listAcc.append(Account("hidro1",passs,"dat","0123456789","h@gmail.com","abc","21/06/2002"))
    controller.menu(listAcc)