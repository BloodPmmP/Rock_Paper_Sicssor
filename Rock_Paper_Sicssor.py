import random

continue_choice = 1
class rps:
    def __init__(self, computer, player):
        self.comp = computer
        self.player = player

    def game(self):
            if self.comp == self.player:
                return None
            if self.comp == 'r':
                if self.player == 's':
                    return False
                elif self.player == 'p':
                    return True
            if self.comp == 'p':
                if self.player == 'r':
                    return False
                elif self.player == 's':
                    return True
            if self.comp == 's':
                if self.player == 'p':
                    return False
                elif self.player == 'r':
                    return True
    def getComputer(self):
        return self.comp
    def getPlayer(self):
        return self.player

while(continue_choice==1):
    randNo = random.randint(1, 3)
    if randNo == 1:
        comp ='r'
    elif randNo == 2:
        comp ='p'
    elif randNo == 3:
        comp ='s'
    You = input("Your Turn: Rock(r) Paper(p) Sicssor(s)?\n: ")
    a = rps(comp, You)
    print("Computer Choose: " + a.getComputer())
    print("You Choose: " + a.getPlayer())

    if a == None:
        print("Game is tie")
    elif a:
        print("You Won")
    else:
        print("You Loose")

    continue_choice=int(input("Do you want to play again\n1.Yes\n2.No\n: "))
    if continue_choice == 2:
        print("Thank You for playing this game")
