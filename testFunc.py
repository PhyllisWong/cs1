def ask_bet_color():
    global bet_color
    ask_color = input('Would you like to bet on red or black?')
    if (ask_color == 'red'):
        bet_color = 'red'
    elif (ask_color == 'black'):
        bet_color = 'black'
    else:
        print('That is not a color, please select between red or black')
        ask_bet_color()
    return
