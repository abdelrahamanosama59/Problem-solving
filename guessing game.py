import random 

class player :
    def __init__(self):
        self.name = ''
        self.points = 0
    def choose_name(self):
        while True:
            name = input("Enter Your name (letters only) : ")
            if name.isalpha() :
                self.name = name
                break
            print("Invalid name ! Try again ")

class list:
    def list_size(self):
        while True:
         self.listsize = int(input("Enter the size of the list (ODD) generated randomly : "))
         if self.listsize % 2 == 1 and self.listsize > 0:
           break
         print("Invalid size")
    def generate_list(self):
        return  [random.randint(0,101) for _ in range(self.listsize)]


class game:
    def __init__(self):
        self.players = [player() , player()]
        self.gamelist = list()
        self.size = self.gamelist.list_size()
        self.current_player = 0
        self.random_list = self.gamelist.generate_list()

    def start_game(self):
        self.players[0].choose_name()
        self.players[1].choose_name()
        self.play_turn()
    
    def get_value(self):
        while True:
            value = int(input("Enter number between 0 and 100 : "))
            if 0<=value<=100:
                break
            print("Invalid Input Number ! please try again")
        return value

    def check_win(self , value):
        if value in self.random_list:
            self.random_list.remove(value)
            self.players[self.current_player].points += 1
        if self.players[self.current_player].points == 0.5+self.gamelist.listsize/2:
            print(f'player {self.current_player+1} : {self.players[self.current_player].name} has won')
            return True
    def play_turn(self):
        flag = False
        while True:
            print(f"NOW , your turn player {self.current_player+1} , {self.players[self.current_player].name}")
            value = self.get_value()
            flag = self.check_win(value)
            print(f"The points for player 1 [{self.players[0].name}] : {self.players[0].points}")
            print(f"The points for player 2 [{self.players[1].name}] : {self.players[1].points}")
            if flag:
               break
            else:
             if self.current_player == 0:
                self.current_player = 1
             elif self.current_player == 1:
                self.current_player = 0

        return

play = game()
print(play.random_list)
play.start_game()