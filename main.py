import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

quit = False
range = 100

while not quit:
    random_number = random.randint(1,range)
    count = 1
    number = -1
    while number != random_number:
        number = input("Guess a number between 1 and {}: ".format(range))
        if not number.isdigit():
            print("Guess a number ya goof!")
        else:
            number = int(number)
            count = count + 1
            print("That ain't it fam.")
            print("\U0001F923") 
            if number > random_number:
                print("Too high bro, decrease altitude!")
            elif number < random_number:
                print("Too low, might wanna invest in a trampoline for that integer dude.")
    print("Lucky guess, maybe hit up the Blackjack tables!")
    print("Only took you {} tries, not too shabby.".format(count))
    print("\U0001f600") 
    play_again = input("\nWanna give it another shot (yes or no) ?")
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y":
        quit = False
    else:
        quit = True

print("\n\nSee you, space cowboy.")