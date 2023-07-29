import string

class Registration():

    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password

    @property
    def login(self):
        print(self.__login)

    @login.setter
    def login(self, value):
        if str(value).count("@") > 0:
            if str(value).count(".") > 0:
                print("Login is valid")
                self.__login = value
            else:
                raise ValueError("Login must included at least one'.'")
        else:
            raise ValueError("Login must included at least one'@'")
        
    @property
    def password(self):
        print(self.__password)

    @password.setter
    def password(self, value):
        if isinstance(value, str):
            if len(value) >= 5 and len(value) <= 11:
                if self.is_include_digit(value):
                    if self.is_include_all_register(value):
                        if self.is_include_only_latin(value):
                            if self.check_password_dictionary(value):
                                self.__password= value
            else:
                raise ValueError("Парольдолжен быть длиннее 4 и меньше 12 символов")
        else:
            raise TypeError("Пароль должен быть строкой")



    @staticmethod
    def is_include_digit(value):
        for i in value:
            try:
                int(i)
                return True
            except:pass
        raise ValueError("Пароль должен содержать хотябы одну цифру")
    
    @staticmethod
    def is_include_all_register(value):
        up = []
        low = []
        for i in value:
            if str.isupper(i):
                up = True
            elif str.islower(i):
                low = True
        if up == True and low == True:
            return True
        else:
            raise ValueError("Пароль должен содержать заглавные буквы")
        
    @staticmethod
    def is_include_only_latin(value):
        for i in value:
            if i in string.ascii_letters or i in string.digits:
                pass
            else:
                raise ValueError("Пароль должен содержать только латинский алфавит")
        return True

    @staticmethod
    def check_password_dictionary(value):
        with open("easy_passwords.txt", "r") as file:
            line = file.readlines()
            for i in line:
                if value == i.replace("\n", ""):
                    raise ValueError("Ваш пароль содержиться в списке самых лёгких паролей")
        return True
    
user = Registration(login="hello@gmail.com", password="YouGetBan1")
user.login
user.password
