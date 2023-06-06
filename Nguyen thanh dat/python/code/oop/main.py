from Account import Account
from Validate import Validate
from AccountController import AccountController 

controller = AccountController()

if __name__ == '__main__':
    list_acc = []
    passs = controller.encrypMD5("123")
    list_acc.append(Account("hidro",passs,"dat","0123456789","h@gmail.com","abc","21/06/2002"))
    list_acc.append(Account("hidro1",passs,"dat","0123456789","h@gmail.com","abc","21/06/2002"))
    controller.menu(list_acc)