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
        pizza_restaurant = input("Enter a pizza reataurant:")

        print("I like " + color)
        print("This youtuber said: subscribe to " + youtuber)
        print("Let's play some videogames, " + videogame + " is the best.")
        print("I have a " + car_brand + ", is the best!")
        print("Let's buy some chocalate, " + chocolate_brand + " tastes good.")
        print("I went to " + country_name_in_europe + " before, it is masive!")
        print("Let's go eat lunch, " + pizza_restaurant + " has a good menu")

    elif int(pattern) == 2 :

        wishlist = input("Enter an item from your wishlist:")

        print("")

    elif int(pattern) == 3 :

        wishlist = input("Enter your favorite weapon:")

        print("")

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