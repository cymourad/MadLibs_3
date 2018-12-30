# In this game, we are going to have multiple patterns to fill in
# The modes are:
# 1. Every-day life
# 2. Christmas Eve
# 3. Fortnite
# 4. Regular
# 5. 

pattern = 1

while int(pattern) in {1,2,3,4,5}:

    pattern = input("Select pattern (1: Every-day life <---> 2: Christmas eve <---> 3: Fortnite <---> 4: regular <---> 5:) or any other number to end:")

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

print("Thank you for playing!")