from random import randint

# In this game, we are going to have multiple patterns to fill in
# The modes are:
# 1. Every-day life
# 2. Christmas Eve
# 3. Fortnite
# 4. Regular
# 5. 
# 6.
# 7.
# 8.
# 9.
# 10. Random
# 0. end the game
# 55. random pattern

pattern = 1

while int(pattern) in {1,2,3,4,5,6,7,8,9,10}:

    pattern = input("Select a pattern \n    1: Every-day life\n    2: Christmas eve\n    3: Fortnite\n    4: regular\n    5:\n    55: Random pattern\n    0: to end:")

    if int(pattern) == 55:
        pattern = randint(1,10)

    if int(pattern) == 1 :

        color = input("Enter a color:")
        youtuber = input("Enter a youtuber:")
        videogame = input("Enter a videogame:")
        car_brand = input("Enter a car brand:")
        chocolate_brand = input("Enter a chocalate brand:")
        country_name_in_europe = input("Enter a country name in Europe:")
        pizza_restaurant = input("Enter a pizza restaurant:")

        print("I like " + color)
        print("This youtuber said: subscribe to " + youtuber)
        print("Let's play some videogames, " + videogame + " is the best.")
        print("I have a " + car_brand + ", it's the best!")
        print("Let's buy some chocalate, " + chocolate_brand + " tastes good.")
        print("I went to " + country_name_in_europe + " before, it is massive!")
        print("Let's go eat lunch, " + pizza_restaurant + " has a good menu")

    elif int(pattern) == 2 :

        christmas_movie = input("Enter a christmas movie:")
        number = input("Enter a number:")
        drink = input("Enter a drink:")
        decoration = input("Enter a decoration:")
        gift = input("Enter a gift:")
        color_number = input("Enter a color or a number:")
        size = input("Enter a size:")

        print("I watched " + christmas_movie + number + " times")
        print("I like to drink " + drink)
        print("I like to put up " + decoration)
        print("I would like to recieve a " + gift)
        print("I like to build " + color_number + " snowmans")
        print("I like my christmas tree to be " + size)

    elif int(pattern) == 3 :

        weapon = input("Enter a weapon:")
        mode = input("Enter a gamemode:")
        location = input("Enter a location:")
        vehicle = input("Enter a vehicle:")

        print("I normaly use " + weapon)
        print("Let's play " + mode)
        print("-Where are we dropping? -Let's drop " + location)
        print("I found a " + weapon)
        print("let's get away from the storm with " + vehicle)

    elif int(pattern) == 4 :

        wishlist = input("Enter an adjective:")

        print("")

    elif int(pattern) == 5 :

        wishlist = input("Enter a random word:")

        print("")

    elif int(pattern) == 6 :

        wishlist = input("Enter an item from your wishlist:")

        print("")

    elif int(pattern) == 7 :

        wishlist = input("Enter your favorite weapon:")

        print("")

    elif int(pattern) == 8 :

        wishlist = input("Enter an adjective:")

        print("")

    elif int(pattern) == 9 :

        wishlist = input("Enter a random word:")

        print("")

    elif int(pattern) == 10 :

        wishlist = input("Enter a random word:")

        print("")

print("Thank you for playing!")