import random

max_lines = 3
max_bet = 100
min_bet = 1

rows = 3
cols = 3

symbol_count = {
    "A": 2, 
    "B": 4, 
    "C": 6, 
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_spin(row, col, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for column in columns:
            print( "|" , column[row] , "|", " ", end="")
        print()

def get_number_of_lines():
    while True:
        lines = input("Enter the Number of Lines to bet On(1-3): ")
        if lines.isdigit():
            lines = int(lines)
            if max_lines >= lines >= 1:
                print(f"you have now betting on {lines} Lines")
                break
            else:
                print("The line number must be grater than 0 and between 1-3!")
                continue
        else: 
            print("Please Enter a Valid line number!!")
            continue
    return lines

def deposit():
    while True:
        amount = input("What amount you Want to Deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"you have now ${amount} in your account")
                break
            else:
                print("The Amount must be grater than 0!")
                continue
        else: 
            print("Please Enter a Valid Amount!!")
            continue
    return amount

def get_bet():
    while True:
        amount = input("What amount you Want to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if max_bet >= amount >= min_bet:
                print(f"you have now ${amount} active bet")
                break
            else:
                print("The Amount must be grater than 1!")
                continue
        else: 
            print("Please Enter a Valid Amount!!")
            continue
    return amount   

def spin(balance):
    num_lines = get_number_of_lines()
    while True: 
        bet = get_bet()
        total_bet = bet * num_lines
        if total_bet > balance:
            print(f"Your Balance is Insuficient!\nyour total bet is ${total_bet} and your account balance is ${balance}")
            continue
        else:
            break
    
    print(f"you are betting ${bet} on {num_lines}, your total bet is: ${total_bet}")

    slots = get_spin(rows, cols, symbol_count)
    print_slot(slots)
    winnings, winning_lines = check_winnings(slots, num_lines, bet, symbol_value) 
    print(f"You won ${winnings}.")
    print(f"you won on:", *winning_lines)  
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"current balance is: ${balance}")
        answer = input("press Enter to play:(q to quit) ").lower()
        if answer == 'q':
            break
        balance += spin(balance)
    print(f"You are left with ${balance}")

main()
