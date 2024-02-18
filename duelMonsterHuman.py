# monster - fighter duel
#monster stuff
class Monster:
    type = "hydra"
    def __init__(self,attack = "bite",hp = 100):
        self.attack = attack
        self.hp = hp
    
    def damage_hydra(self):
        self.hp -= 20
        print("ouch! fighter dealt 15 damage")
        print("Monster's hp  now is : ",self.hp)

# human stuff
class Human:
    value = "fighter"
    
    def __init__(self,weapon="sword",attack = "stab",hp = 100):
        self.weapon = weapon
        self.hp = hp

    def damage_fighter(self):
        self.hp -= 25
        print("ouch! hydra dealt 10 damage")
        print("fighter's hp  now is : ",self.hp)
# where the magic occurs
if __name__ == "__main__":
    Monster1 = Monster()
    Human1 = Human()
    while True:
        choice = input("control : Monster (1) // Human (2) \n")
        if choice == '1' :
                while True:
                    attackX = input(" Monster attack ! press 7 \n")
                    if attackX == '7':
                            Human1.damage_fighter()
                    else:
                            print("error")
                    if Human1.hp == 0 :
                        print("RIP fighter")
                        break
        elif choice == '2':
                while True:
                    attackY = input(" Human attack ! press 7 \n")
                    if attackY == '7':
                            Monster1.damage_hydra()
                    else:
                            print("error")
                    if Monster1.hp == 0 :
                        print("RIP Hydra")
                        break
        else:
            print("error")
       
        play = input("play again? press 1. \n end game? press 2. ")
        if play == '1':
            print("again!!")
        elif play == '2':
            print("another time!")
            break
        else:
            print("error")
        