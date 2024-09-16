# Python Slot Machine
import random

def  spinRow():
    symbols = ['🍓', '🍉', '🍊', '🔔', '⭐']

    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    #     return results

    # return[random.choice(symbol) for symbol in range(3)]
    return[random.choice(symbols) for _ in range(3)]

def printRow(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def getPayout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍓":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍊":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    
    return 0

def main():
    balance = 100
    print("******************************")
    print("Welcome to Python Slot Machine")
    print("Symbol: 🍓 🍉 🍊 🔔⭐")
    print("******************************")


    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spinRow()
        print("Spinning...\n")
        printRow(row)

        payout = getPayout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        playAgain = input("Do you want to spin again? (Y/N): ").upper()

        if playAgain == "Y":
            continue
        if playAgain == "N":
            break
    print(f"Game over! Your final balance is ${balance}")

if __name__ == "__main__":
    main()