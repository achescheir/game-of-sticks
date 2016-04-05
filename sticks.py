import random

class StickGame:
    def __init__(self, number_of_sticks, players):
        self.number_of_sticks = number_of_sticks
        self.players = players

    def play(self):
        player_index = 0
        while True:
            sticks_chosen = self.players[player_index].get_choice(self.number_of_sticks)
            self.number_of_sticks -= sticks_chosen
            if self.number_of_sticks <= 0:
                self.players[player_index].lose()
                break
            player_index += 1
            if player_index >= len(self.players):
                player_index = 0

class Player:
    def get_choice(self, number_of_sticks):
        pass

    def lose(self):
        pass

    def win(self):
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
    def __init__(self,verbose=True):
        self.hats = {}
        self.this_game = {}
        self.verbose = verbose

    def default_hat(self):
        return [1,2,3]

    def get_choice(self,number_of_sticks):
        hat_contents = self.hats.get(number_of_sticks,default_hat())
        my_choice = random.choice(hat_contents)
        this_game[number_of_sticks] = my_choice
        if verbose:
            prit
        return my_choice



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
    players = []
    for name in ["Player 1", 'Player 2']:
        players.append(User_Player(name))
    game = StickGame(get_pile_size(10,100),players)
    game.play()


if __name__ == '__main__':
    main()
