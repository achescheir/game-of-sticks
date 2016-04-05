
def get_choice(number_of_sticks, player_name):
    output = 0
    while output <1 or output > min(number_of_sticks,3):
        try:
            output = int(input(player_name +': How many do you want to pick up (1-{})?'.format(min(number_of_sticks,3))))
        except ValueError:
            print("Numbers only please.")
            continue
        if output <1 or output > min(number_of_sticks,3):
            print('Numbers from 1 to {} only please'.format(min(number_of_sticks,3)))
    return output

def get_pile_size(min_size, max_size):
    size = min_size-1
    while size < min_size or size > max_size:
        try:
            size = int(input("How big should the pile be ({} - {})?".format(min_size , max_size)))
        except:
            print("Numbers only please.")
            raise
            continue
        if size < min_size or size > max_size:
            print('Numbers from {} to {} only please'.format(min_size,max_size))
    return size

def main():

    stick_pile = get_pile_size(10, 100)
    player_names = ['Player 1','Player 2']
    player_index = 0
    while True:
        print('There are', stick_pile, 'sticks in the pile.')
        sticks_chosen=get_choice(stick_pile, player_names[player_index])
        stick_pile -= sticks_chosen
        if stick_pile <= 0:
            print('Game over, you lose {}!!'.format(player_names[player_index]))
            break
        player_index += 1
        if player_index == len(player_names):
            player_index = 0

if __name__ == '__main__':
    main()
