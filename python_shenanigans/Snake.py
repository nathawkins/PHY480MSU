class veryBigSnake:

    def __init__(self):
        self.name = "Peter Python"
        self.type= "Python"
        print("New snake in da house!")

    def set_snake_name(self,name):
        self.name = name

    def set_snake_type(self,type):
        self.type = type

    def who_am_i(self):
        print("My name is ", self.name,", I'm a ", self.type," and I'm perfect for you! Take me home today!")

alpha = veryBigSnake()
alpha.set_snake_name("Julie")
alpha.set_snake_type("Dead")
alpha.who_am_i()
