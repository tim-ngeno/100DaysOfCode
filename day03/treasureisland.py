print("Ahoy! Welcome to The Treasure Island!.\n\n\
Your mission is to find the hidden treasure.")
crossroad = input("You are at a crossroad. Which way do you go? \
Pick 'left' or 'right'.\n").lower()

if crossroad == 'left':
    swim = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat, or type 'swim' to swim across.\n").lower()
    if swim == 'wait':
        door = input("You arrive at the island unharmed. There is an old mansion with 3 doors: one red, one yellow and another blue. Pick a door.\n").lower()
        if door == 'blue':
            print('You entered a room full of wild bees and were stung to death. Game over! ')
        elif door == 'red':
            print("You have entered the Golden Room. (Yes, it's real gold). Unfortunately the glitter killed you. Game over!")
        elif door == 'yellow':
            print("This is a room full of foood and drink. Eat and enjoy your victory\nYou won!")
        else:
            print("You can't be colorblind to text and expect to win Carol, go home!!")
    elif swim == 'swim':
        print('Unfortunately you were eaten by hungry mesozoan sharks. Game over!')
    else:
        print("You died because of a spelling error!!!!#$>?? Wow that's a first!")

elif crossroad == 'right':
    print("You were hit by a train! Oops, Game over!")
else:
    print("Wrong choice. You die!")
