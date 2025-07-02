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
        print("{}, your number is too high".format(guess_name))
    elif guess_number < too_low:
        print("{}, your number is too low".format(guess_name))
    else:
        print("{}, you are soooo close, try again!".format(guess_name))

    guess_number = int(input("Input guess number "))

