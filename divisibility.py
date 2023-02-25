class personal:
    def get(self):
        self.name=input("Enter your name ")
        self.address=input("Enter your address ")
        self.age=input("Enter your age ")
        self.phone=input("Enter your phone ")
    def set(self):
        print("name:",self.name)
        print("address:",self.address)
        print("age:",self.age)
        print("phone:",self.phone)

myself=personal()
myself.get()
myself.set()
print("Enter your family members")
family=personal()
family.get()
family.set()
print("Enter your friends")
friends=personal()
friends.get()
friends.set()
