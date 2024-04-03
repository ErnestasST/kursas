from random import randint

def generate_numbers():
    return "".join([str(randint(0, 9)) for _ in range(4)])

def check_cows_bulls(generated_numbers, player_prediction):
    cows, bulls = 0, 0
    for index, value in enumerate(player_prediction):

        if value == generated_numbers[index]:
            bulls += 1
        elif value in generated_number:
            cows += 1

    print(cows, bulls)
def main():
    generated_number = generate_numbers()
    try_number = int(input("how many guesses?: "))
    try_number = 2

    for x in range(try_number):
        player_prediction = input("try to guess it")
        print(player_prediction)

    print(generated_number, try_number)
    return "game over"

# main()
generated_number = "1234"
player_prediction = "1234"
check_cows_bulls(generated_number, player_prediction)