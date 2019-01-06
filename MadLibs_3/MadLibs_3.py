from random import randint

# In this game, we are going to have multiple patterns to fill in from random import randint
# The modes are:
# 1. Every-day life
# 2. Christmas Eve
# 3. Fortnite
# 4. Regular
# 5. Food
# 6. Animals
# 7. Colors
# 8. Sports
# 9. Clothes
# 0. end the game
# 55. random pattern

pattern = 1

while int(pattern) in {1,2,3,4,5,6,7,8,9}:

    pattern = input("Select a pattern: \n    1: Every-day life\n    2: Christmas eve\n    3: Fortnite\n    4: Regular\n    5: Food\n    6: Animals\n    7: Colors\n    8: Sports\n    9: Clothes\n    55: Random pattern\n    0: to end:")

    if int(pattern) == 55:
        pattern = randint(1,9)

    # Every-day Life
    elif int(pattern) == 1 :

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

    # Christmas Eve
    elif int(pattern) == 2 :

        christmas_movie = input("Enter a christmas movie:")
        number = input("Enter a number:")
        drink = input("Enter a drink:")
        decoration = input("Enter a decoration:")
        gift = input("Enter a gift:")
        color_number = input("Enter a color or a number:")
        size = input("Choose one: Small    Medium    Large:")

        print("I watched " + christmas_movie + " " + number + " times")
        print("I like to drink " + drink)
        print("I like to put up " + decoration)
        print("I would like to recieve a " + gift)
        print("I like to build " + color_number + " snowmans")
        print("I like my christmas tree to be " + size)

    # Fortnite
    elif int(pattern) == 3 :

        weapon = input("Enter a weapon:")
        mode = input("Enter a gamemode:")
        location = input("Enter a location:")
        vehicle = input("Enter a vehicle:")
        player = input("Enter a player:")
        other_player = input("Enter a player on you team:")
        way_to_win = input("Enter a way to win:")

        print("I normaly use " + weapon)
        print("Let's play " + mode)
        print("-Where are we dropping? -Let's drop " + location)
        print("I found a " + weapon)
        print("let's get away from the storm with " + vehicle)
        print(player + " is on me!")
        print("thank you " + other_player + " for reviving me")
        print("we finaly got a win by " + way_to_win)

    # Regular
    elif int(pattern) == 4 :

        adjective = input("Enter an adjective:")
        plural_noun = input("Enter a plural noun:")
        noun = input("Enter a noun:")
        city = input("Enter a city's name:")
        transportation = input("Enter a method of transportation:")

        print("I like to sleep " + adjective)
        print(plural_noun + " are bad")
        print(noun + " is the best")
        print("I will hate to live in " + city)
        print("I want to be a " + transportation)

    # Food
    elif int(pattern) == 5 :

        ff_restaurant = input("Enter a fast-food reataurant:")
        canned_food = input("Enter a canned food item:")
        sauce = input("Enter a type of sauce:")
        smelly_sauce("Enter a smelly sauce:")
        type_of_pasta("ENter a type of pasta:")
        drink_2 = input("Enter a drink:")

        print("the helthiest food I eat is at " + ff_restaurant)
        print("I used to live in a can of " + canned_food)
        print("I want to dive in " + sauce + " sauce")
        print("my mom said I smell like " + smelly_sauce + " sauce")
        print("my hair looks like " + type_of_pasta)
        print("I wish I can shower in " + drink_2)

    # Animals
    elif int(pattern) == 6 :

        short_animal = input("Enter a short animal:")
        fat_animal = input("Enter a fat animal:")
        dirty_animal = input("Enter a dirty animal:")
        loud_animal = input("Enter a loud animal:")
        slow_animal = input("Enter a slow animal:")
        carnivore = input("Enter a carnivore:")

        print(short_animal + " is twice my size")
        print("I am fater than the " + fat_animal)
        print("before I showered, I looked like the " + dirty_animal)
        print("when I sleep i snore like the " + loud_animal)
        print("when I run as fast as I can, it's slower than the " + slow_animal)
        print("I eat like the " + carnivore)

    # Colors
    elif int(pattern) == 7 :

        color_2 = input("Enter a color:")
        light_color = input("Enter a light color:")
        guirly_color = input("Enter a guirly:")
        cool_color = input("Enter a cool color:")
        joyful_color = input("Enter a joyful color:")
        color_3 = input("Enter one other color:")

        print("I wish I am " + color_2)
        print("the sky is " + light_color)
        print("my favorite color is " + guirly_color)
        print("I like spray-panting with " + cool_color)
        print("I stare at " + joyful_color + " everyday")
        print("in christmas time, I like to decorate my house with " + color_3)

    # Sports
    elif int(pattern) == 8 :

        running_sport = input("Enter a running sport:")
        running_shoes = input("Enter a running shoe mark (ex.:Nike) :")
        shooting_sport = input("Enter a shooting sport:")
        shooting_side = input("Enter your shooting side (Left or right) :")
        ball_sport = input("Enter a ball sport:")
        method_shooting = input("Enter something you use to shoot a ball")

        print("I do " + running_sport + " with " + running_shoes + " shoes")
        print("when I play " + shooting_sport + " I use my " + shooting_side + " side")
        print("my favorite ball sport is " + ball_sport)
        print("I use the " + method_shooting + " to shoot the ball")

    # Clothes
    elif int(pattern) == 9 :

        size_2 = input("Enter a size (Ex.: Small    Medium    Large):")
        clothes_color =input("Enter a color:")
        type_of_clothes = input("Enter the type of clothes: sportive or normal:")
        accessories = input("Enter an Accessories:")
        halloween = input("Enter a Haloween costume:")
        seasonal = input("Enter a sesonal were:")
        place = input("Enter a place:")

        print("all my clothes are " + size_2)
        print("I prefer the " + clothes_color + " because it's an artist's choice")
        print(type_of_clothes + " clothes are very tight")
        print("the "  + accessories + " make me look cool")
        print("I go to " + place + " with " + halloween + " costume")
        print("I were " + seasonal + " during summer")

print("Thank you for playing!")