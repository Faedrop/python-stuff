print("ceci est une calculatrice hh \n")
while True:
    x = int(input("x= "))
    y = float(input("y = "))
    def multi():
        print(x*y) 
    def sub():
        print(x-y)
    def add():
        print(x+y)
    def div():
        if y>0:
            z= x/y
            float(z)
            print(z)
    def out():
            print("ur out")
    def default():
        print("hh try again")
    option ={
        1:multi,
        2:sub,
        3:add,
        4:div,
        5:out
    }
    choice = int(input(" 1.multi \n 2.sub \n 3.add \n 4.div \n 5.out \n"))
    option.get(choice, default)()
    if choice == 5: 
        break  
    else:
        option.get(choice, default)()
