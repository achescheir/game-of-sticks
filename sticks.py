import random

class StickGame:
    def __init__(self, number_of_sticks, players):
        self.number_of_sticks = number_of_sticks
        self.players = players

    def play(self):
        player_index = random.choice(range(len(self.players)))
        for player in self.players:
            player.start_game()
        while True:
            sticks_chosen = self.players[player_index].get_choice(self.number_of_sticks)
            self.number_of_sticks -= sticks_chosen
            if self.number_of_sticks <= 0:
                self.players[player_index].lose()
                break
            player_index += 1
            if player_index >= len(self.players):
                player_index = 0
        loser = player_index
        while True:
            player_index += 1
            if player_index >= len(self.players):
                player_index = 0
            if player_index == loser:
                break
            self.players[player_index].win()

class Player:
    def get_choice(self, number_of_sticks):
        pass

    def lose(self):
        pass

    def win(self):
        pass

    def start_game(self):
        pass

class User_Player(Player):
    def __init__(self, name):
        self.name = name

    def get_choice(self,number_of_sticks):
        print('There are', number_of_sticks, 'sticks in the pile.')
        output = 0
        while output <1 or output > min(number_of_sticks,3):
            try:
                output = int(input(self.name +': How many do you want to pick up (1-{})? '.format(min(number_of_sticks,3))))
            except ValueError:
                print("Numbers only please.")
                continue
            if output <1 or output > min(number_of_sticks,3):
                print('Numbers from 1 to {} only please'.format(min(number_of_sticks,3)))
        return output

    def lose(self):
        print("Sorry, {} you lose.".format(self.name))

class AI_Player(Player):
    def __init__(self, name, verbose=True):
        self.name = name
        self.hats = {}
        self.this_game = {}
        self.verbose = verbose

    def default_hat(self):
        return [1,2,3]

    def get_choice(self,number_of_sticks):
        hat_contents = self.hats.get(number_of_sticks, self.default_hat())
        my_choice = random.choice(hat_contents)
        self.this_game[number_of_sticks] = my_choice
        if self.verbose:
            print("There are {} sticks in the pile.".format(number_of_sticks))
            print("{}: How many do you want to pick up (1-{})? {}".format(self.name, min(number_of_sticks, 3), my_choice))
        return my_choice

    def start_game(self):
        self.this_game = {}

    def win(self):
        for each_hat in self.this_game:
            if each_hat in self.hats:
                self.hats[each_hat].append(self.this_game[each_hat])
            else:
                self.hats[each_hat] = self.default_hat()
                self.hats[each_hat].append(self.this_game[each_hat])
        self.this_game = {}

    def lose(self):
        for each_hat in self.this_game:
            if each_hat in self.hats:
                self.hats[each_hat].remove(self.this_game[each_hat])
        for each_hat in self.hats:
            for each_ball in range(1,4):
                if each_ball not in self.hats[each_hat]:
                    self.hats[each_hat].append(each_ball)
        if(self.verbose):
            print("Sorry {}, you lose.".format(self.name))
        self.this_game = {}


def get_pile_size(min_size, max_size):
    size = min_size-1
    while size < min_size or size > max_size:
        try:
            size = int(input("How big should the pile be ({} - {})? ".format(min_size , max_size)))
        except ValueError:
            print("Numbers only please.")
            continue
        if size < min_size or size > max_size:
            print('Numbers from {} to {} only please'.format(min_size,max_size))
    return size

def main():
    starting_pile = get_pile_size(10,100)
    game_type = 'not in pea'
    while game_type not in 'pea':
        user_input = input("Do you want to play against another (P)layer, an (E)asy AI or and (A)vanced AI? ")
        game_type = user_input[0].lower()
    players = []
    if game_type == 'a':
        players.append(AI_Player("TrainingAI",False))
        players.append(AI_Player("AI",False))
        print("Training....")
        for x in range(1000):
            game = StickGame(starting_pile,players)
            game.play()
        players[0] = User_Player("Player 1")
        players[1].verbose = True
    elif game_type == 'e':
        players.append(User_Player("Player 1"))
        players.append(AI_Player("AI"))
    elif game_type == 'p' :
        players = [User_Player("Player 1"),User_Player("Player 2")]
    while True:
        game = StickGame(starting_pile,players)
        game.play()
        if input("Play again? ")[0].lower() == 'n':
            break
    # for x in range(1,26):
    #     this_hat = players[1].hats.get(x,[1,2,3])
    #     ones = sum([1 for x in this_hat if x ==1])
    #     twos = sum([1 for x in this_hat if x ==2])
    #     threes = sum([1 for x in this_hat if x ==3])
    #     print("{}> 1:{}    2:{}    3:{}".format(x,ones,twos,threes))



if __name__ == '__main__':
    main()
