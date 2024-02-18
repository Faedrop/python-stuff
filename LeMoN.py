# i basically want to fill or empty a basket of lemons 
class Basket:
    container =  "LeMon"
    color = "yellow"

    def __init__(self,size = "small",mass="unknown",number=0):
            self.size = size
            self.mass = mass 
            self.number = number # i guess we starting with 0 lemons

    def add_number(self):
                self.number += 1
                print("lemon added!! Now theres: ",self.number,"lemons !! ")
    
    def add_mass(self):
        if self.number == 5 :
            print("heavy,we good to go! ")
        else:
             print("still light,add more !")

if __name__ == "__main__":
        Basket1 = Basket()
        print("we have a basket of",Basket1.container,"they are : ",Basket1.color)
        while True:
            choice = input("add lemon until heavy,press 1 \n")
            if choice == '1':
                Basket1.add_number()
                Basket1.add_mass()
                
                
                if Basket1.number == 5:
                    Basket1.add_mass()
                    break
            
            else:
                print("Error")
           


