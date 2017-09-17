# Take a bet
# bet takes color
# bet takes number
# bet takes bet amount

# spin the wheel - generate the number
# random module rand.int
# check the result - did the bet match the result of the spin
# if win - pay accordingly
# if loss - keep money

# functions should do one thing only!!!!
import random
random.seed(0)

bank_account = 1000
bet_amount = 10
bet_color = 'red'
bet_num = 24

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def take_bet(color, number):
    total_bet = []
    total_bet.append(color)
    total_bet.append(number)
    # print('After this bet, you have ' + str(bank_account - bet_amount) + ' left to bet.')
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
    '''returns total amount won or lost by user based on results of roll. '''
    pay_result = 0
    if string == 'jackpot':
        pay_result = (bet_amount * 100)
    elif string == 'big win':
        pay_result = (bet_amount * 10)
    elif string == 'win':
        pay_result = (bet_amount * 2)
    else:
        pay_result =  (-bet_amount)
    return pay_result

def play_game():
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:
    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly. """
    global bank_account
    # returns an array [color, num, amount]
    player_bet = take_bet(bet_color, bet_num)
    # returns an array [color, num]
    dealer_roll = roll_ball()
    # returns a str
    did_player_win = check_results(player_bet, dealer_roll)
    winnings = payout(did_player_win)
    bank_account += winnings
    print('The amount you won this round is ' + str(winnings))
    print('Your new bank ammount is ' + str(bank_account) + '. Thanks for playing, come back and play anytime!')
