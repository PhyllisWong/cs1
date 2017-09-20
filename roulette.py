
import random
random.seed(0)

'''Add a feature to have the user input color, number, and amount'''
bank_account = 1000
bet_amount = 0
bet_color = None
bet_num = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


def ask_bet_color():
    global bet_color
    ask_color = input('Place your bet on red or black: ')
    if (ask_color == 'red'):
        bet_color = 'red'
    elif (ask_color == 'black'):
        bet_color = 'black'
    else:
        print('That is not a color, please select between red or black')
        ask_bet_color()
    return


def ask_bet_num():
    global bet_num, green, red, black
    ask_num = input('Pick a number between 0 and 38: ')
    num = int(ask_num)
    if (num in green) or (num in red) or (num in black):
        bet_num = num
    else:
        print('That is not a number between 0 and 38')
        ask_bet_num()
    return

def ask_bet_amount():
    global bet_amount
    amount = input('How much do you want to bet in dollars: ')
    bet_amount = amount
    return


def take_bet(color, number):
    total_bet = []
    total_bet.append(color)
    total_bet.append(number)
    return total_bet


def roll_ball():
    '''returns a random number between 0 and 37'''
    results = []
    ball_num = random.randint(0, 37)
    if (ball_num in green):
        results.append('green')
    elif (ball_num in red):
        results.append('red')
    elif (ball_num in black):
        results.append('black')
    results.append(ball_num)
    print('The dealer rolled ' + str(results))
    return results


def check_results(arr1, arr2):
    '''Compares bet_color to color rolled.'''
    result = 0
    if (arr1[0] == arr2[0]):
        print('You won the color matching')
        result += 1
        return ('win')
    elif (arr1[1] == arr2[1]):
        print('You won the number matching')
        result += 2
        return ('big win')
    elif (arr1[0] == arr2[0] and arr1[1] == arr2[1]):
        print('You won the jackpot, congratulations!')
        result += 3
        return ('jackpot')
    else:
        return ('lost')


def payout(string):
    global bet_amount
    '''returns total amount won or lost by user based on results of roll.'''
    pay_result = 0
    if string == 'jackpot':
        pay_result = (bet_amount * 100)
    elif string == 'big win':
        pay_result = (bet_amount * 10)
    elif string == 'win':
        pay_result = (bet_amount * 2)
    else:
        pay_result = (bet_amount * -1)
    return pay_result


def ask_to_play_again():
    play_again = input('Would you like to play again? y or n')
    if (play_again == 'y'):
        play_game()
    elif (play_again == 'n'):
        quit()


def play_game():
    '''This is the main function for the game.'''
    global bank_account
    ask_bet_color()
    ask_bet_num()
    ask_bet_amount()
    # returns an array [color, num, amount]
    player_bet = take_bet(bet_color, bet_num)
    # returns an array [color, num]
    dealer_roll = roll_ball()
    # returns a str
    did_player_win = check_results(player_bet, dealer_roll)
    # returns an int
    cash = payout(did_player_win)
    #bank_account += cash
    winningStatement = 'The amount you won this round is ' + str(cash)
    print(winningStatement)
    print('Your new bank amount is $' + str(bank_account))
    ask_to_play_again()
    return

play_game()
