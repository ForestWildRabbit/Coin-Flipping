from random import randint
import matplotlib.pyplot as plt


MAX_COIN_FLIPS_PER_SIMULATION = 100
WINNING_MULTIPLIER = 1.9


def create_bet_graph():
    x_list = []  # number of attempts
    y_list = []  # bet value
    x = 1
    y = 1
    total_y = 0
    for _ in range(10):
        x_list.append(x)
        y_list.append(y)
        plt.text(x - 0.26, y - 1, f"{round(y_list[-1], 2)}",
                 fontdict={'size': 10},
                 horizontalalignment='center'
                 )

        total_y += y
        bet_multiplier = 1 / (WINNING_MULTIPLIER - 1)
        y = total_y * bet_multiplier

        x += 1

    plt.plot(x_list, y_list, marker='o', markersize=7)

    plt.xlabel("attempt number")
    plt.ylabel("bet_value")
    plt.title("Coin Flipping")
    plt.show()


def flip():
    random_number = randint(0, 1)
    if random_number % 2 == 0:
        return 'heads'
    return 'tails'


def simulate(balance):
    total_flips = 0
    prediction = 'heads'
    bet = 1
    sequence_bet = 0
    winning_multiplier = 1.9

    while total_flips < MAX_COIN_FLIPS_PER_SIMULATION:
        # print(f'{balance = }, {bet = }')
        balance -= bet
        sequence_bet += bet
        flip_result = flip()
        total_flips += 1
        if flip_result == prediction:
            balance += bet * winning_multiplier
            bet = 1
            sequence_bet = 0

        else:
            min_bet_multiplier = 1 / (winning_multiplier - 1)
            bet = sequence_bet * min_bet_multiplier

        if balance < bet:
            print(f'lost with {balance = } and {bet = }')
            return balance

    return balance


def main():

    initial_balance = 100000
    total_balance = initial_balance
    n = 100
    for _ in range(n):
        balance = total_balance // n
        total_balance -= balance
        total_balance += simulate(balance)
    print('-' * 40)
    print(f'{total_balance = }')

    # create_bet_graph()


if __name__ == '__main__':
    main()
