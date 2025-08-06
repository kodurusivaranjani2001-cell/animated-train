class jathara:
    def __init__(self):
        self.village="ramapuram"
        self.house="beside high school"
        self.darshanam="gangamma,"
        self.family="killing goats to gangamma"
        self.menu=["rice","mutton curry","chicken curry","sweets"]
        self.purse=[1000]
        self.toys=500
        self.sweets=500


    def guest_coming(self):
        print( "sithaya went to : ",{self.village,self.house})
    @staticmethod
    def communication():
        mingled_with=["mother","grand ma","children"]
        mingled_with.append("father and some village people")
        print(mingled_with)
    def temple(self):
        
        print(self.darshanam ,self.family)
    def food(self):
        u_had = input(f"Enter what you had from menu {self.menu}: ")
        print(u_had)
    def expences(self):
        self.total=self.toys+self.sweets
        self.balance=self.purse[0] - self.total
        print(self.balance)
        if self.balance >= 50:
            print(" remaining balance is: ",self.balance)
        else :
            print("no money")
        
    
        


        

sithaya=jathara()
sithaya.guest_coming()
jathara.communication()
sithaya_day=jathara()
sithaya.food()

sithaya_day.temple()
sithaya.expences()








