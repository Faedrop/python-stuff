# a choose-your-character fight game lol
# ennemy 
class Enemy :
    type = "terrorist"
    def __init__(self):
        self.hp = 100
    def damage_Alex(self,att1 = 10):
            self.hp -= att1
            print("damage dealt!",self.hp,"left.")

    def damage_Ben(self,att2 = 5):
        self.hp -= att2
        print("damage dealt!",self.hp,"left.")
        
    def damage_Mira(self,att3 = 8):
        self.hp -= att3
        print("damage dealt!",self.hp,"left.")
    def deadge(self):
        print("he is dead!")
        

# the players,we will have 3 characters that can be chosen

class Alex:
        def Alex_Attack(self,attack1 = 10):
            self.attack1 = attack1
            print("alex attacked! dealing",self.attack1," in damage!")
        class Player1:
            Names = "Alex"
            SpeAbility = "water attack"
            def __init__(self):
                    self.Alex = Alex()
class Ben:
        def Ben_Attack(self,attack2 = 5):
            self.attack2 = attack2
            print("Ben attacked! dealing",self.attack2," in damage!")
       
        class Player2:
            Names = "ben"
            SpeAbility = "wind attack"
            def __init__(self):
                    self.Ben = Ben()
class Mira:
        def Mira_Attack(self,attack3 = 8):
            self.attack3 = attack3
            print("Mira attacked! dealing",self.attack3," in damage!")
        class Player3:
            Names = "Mira"
            SpeAbility = "fire attack"
            def __init__(self):
                    self.Mira = Mira()

class Impact:
    def __init__(self,alex,ben,mira,enemy):
        self.alex = alex
        self.ben = ben
        self.mira = mira
        self.enemy = enemy
    
    def Alex_Ulti(self,Q1=25):
        self.Q1 = Q1
        self.enemy.hp -= self.Q1
        print("ultimate!", self.enemy.hp, " hp left")
        
    def Ben_Ulti(self,Q2=20):
        self.Q2 = Q2
        self.enemy.hp -= self.Q2
        print("ultimate!", self.enemy.hp, " hp left")

    def Mira_Ulti(self,Q3=28):
        self.Q3 = Q3
        self.enemy.hp -= self.Q3
        print("ultimate!", self.enemy.hp, " hp left")
# magic 
if __name__ == "__main__":
    Enemy1 = Enemy()
    PlayerX= Alex()
    PlayerY = Ben()
    PlayerZ = Mira()
    x = Impact(PlayerX, PlayerY, PlayerZ, Enemy1)
    attack1_count = 0
    attack2_count = 0
    attack3_count = 0
    print("theres an enemy nearby. watch out! they saw you!")
    while True:
            choice = input("choose your player: \n 1.Alex \n 2.Ben \n 3.Mira \n")
            if choice == '1':
                        while attack1_count != 3: 
                            attack1 = input("attack with ALEX ? press 0 \n")
                            if attack1 == "0":
                                    PlayerX.Alex_Attack()
                                    Enemy1.damage_Alex()
                                    attack1_count += 1
                        if attack1_count == 3:
                                    ult = input("use ultimate!,press 9 \n")
                                    x.Alex_Ulti() 
                    
            elif choice == "2":
                        while attack2_count != 3:  
                            attack2 = input("attack with BEN ? press 0 \n")
                            if attack2 == "0":
                                    PlayerY.Ben_Attack()
                                    Enemy1.damage_Ben()
                                    attack2_count += 1
                        if attack2_count == 3:
                                    ult = input("use ultimate!,press 9 \n")
                                    x.Ben_Ulti()

            elif choice == "3":
                        while attack3_count != 3:  
                            attack3 = input("attack with BEN ? press 0 \n")
                            if attack3 == "0":
                                    PlayerZ.Mira_Attack()
                                    Enemy1.damage_Mira()
                                    attack3_count += 1
                        if attack3_count == 3:
                                    ult = input("use ultimate!,press 9 \n")
                                    x.Mira_Ulti()
            else: 
               print("hh")

            if Enemy1.hp <= 0 :
                print("its dead")
                break
            
        