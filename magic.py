from logic import sql_functions
from assets import sql_login

class functions():
    def __init__(self):
        self.user = sql_login.user

    def getuser(self):
        print(self.user)