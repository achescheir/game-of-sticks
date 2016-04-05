stick_pile=10
while True:
    print('There are', stick_pile, 'sticks in the pile')
    sticks_chosen=int(input('How many do you want to pick up (1-3)'))
    stick_pile -= sticks_chosen
    if stick_pile <= 0:
        print('Game over, you lose!!')
        break
