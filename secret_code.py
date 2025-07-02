secret_name = input("Hi, please, enter your name (You are the person who will say the secret number): ")
guess_name = input("Hi, please, enter your name (You are the person who will guess the secret number): ")
secret_number = int(input("Input secret number "))

guess_number = int(input("Input guess number "))
attempts = 1
too_high = secret_number + 10
too_low = secret_number - 10

while 1 > 0:
    if guess_number == secret_number:
        print("Congrats {}! You guessed the number in {} attempts.".format(guess_name, attempts))
        break

    attempts += 1
    if guess_number > too_high:
        print("Too high")
    elif guess_number < too_low:
        print("Too low")
    else:
        print("You are soooo close, try again!")

    guess_number = int(input("Input guess number "))

