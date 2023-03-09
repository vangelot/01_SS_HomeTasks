class User:
    emails = []
    counter_object = 0
    def __init__(self, email, age, user_type, data_access, username):
        if email not in self.emails:
            self.__email = email
            #self.__class__.emails.append(email)
            self.emails.append(email)
        else:
            raise Exception("this email already exists")
        self.__email = email
        self.__age = age
        self.__user_type = user_type
        self.__data_access = data_access
        self.username = username
        self.__class__.counter_object += 1

    def showi(self):
        print(self.i)
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age in range(18,120):
            self.__age = age
        else:
            print("wrong data: ", age, " is incorrect age")
    def access_detect(self):
        if self.__user_type in ["superuser", "moderator"]:
            print("access granted !!!")
        else:
            print("access denied !!!")

a = User("chuli@ukr.net", 35, "admin", 2, "vangelot")
b = User("aaa@ukr.net", 35, "moderator", 2, "vangelot")

while True:
    try:
        email = input("input email to create instance: ")
        c = User(email, 30, "moderator", 2, "vangelot")
        break
    except:
        print('wrong email')

a.age = 20
a.age = 130
print(a.email, b.email, c.email)
print(a.age)
a.access_detect()
b.access_detect()
print(User.emails)
print(c.emails)
print(a.emails)

print("Objects created: ", User.counter_object)
