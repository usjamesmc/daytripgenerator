# add another user input for which paramater needs changed if no after first change
import random
def trip_location(random_destination):
    city = random.choice(random_destination)
    print(city)
                
trip_location(['miami', 'houston', 'nashville', 'atlanta', 'cleveland'])

def trip_food(random_restaurant):
    restaurant = random.choice(random_restaurant)
    print(restaurant)
                    
trip_location(['applebees', 'chilis', 'red robin', 'dennys', 'sonic'])

def trip_transportation(random_transportation):
    ride = random.choice(random_transportation)
    print(ride)
                    
trip_transportation(['bus', 'bike', 'train', 'boat', 'helicopter'])

def trip_entertainment(random_entertainment):
    fun = random.choice(random_entertainment)
    print(fun)
                   
trip_entertainment(['movie', 'concert', 'hockey game', 'comedy show', 'car show'])

def trip_arrangement(random_destination, random_transportation, random_entertainment, random_restaurant):
    user_input = input('Is this trip for you?')
    if user_input == ('no'):
        user_input_b = input('Which parameter needs changed?')
        if user_input_b == 'miami':
            random_destination.remove('miami')
            city = random.choice(random_destination)
            print(city)
            user_input_c = input('Now is this trip for you?')
            while user_input_c == 'no':
                random_destination.remove(city)
                city = random.choice(random_destination)
                print(city)
                input('Now is this trip for you?')
            else:
                print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
            
        elif user_input_b == 'houston':
            random_destination.remove('houston')
            city = random.choice(random_destination)
            print(city)
            user_input_c = input('Now is this trip for you?')
            while user_input_c == 'no':
                random_destination.remove(city)
                city = random.choice(random_destination)
                print(city)
                input('Now is this trip for you?')
            else:
                print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
        elif user_input_b == 'nashville':
            random_destination.remove('nashville')
            city = random.choice(random_destination)
            print(city)
            user_input_c = input('Now is this trip for you?')
            while user_input_c == 'no':
                random_destination.remove(city)
                city = random.choice(random_destination)
                print(city)
                input('Now is this trip for you?')
            else:
                print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
        elif user_input_b == 'atlanta':
            random_destination.remove('atlanta')
            city = random.choice(random_destination)
            print(city)
            user_input_c = input('Now is this trip for you?')
            while user_input_c == 'no':
                random_destination.remove(city)
                city = random.choice(random_destination)
                print(city)
                input('Now is this trip for you?')
            else:
                print("Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?")
        elif user_input_b == 'cleveland':
            random_destination.remove('cleveland')
            city = random.choice(random_destination)
            print(city)
            user_input_c = input('Now is this trip for you?')
            while user_input_c == 'no':
                random_destination.remove(city)
                city = random.choice(random_destination)
                print(city)
                input('Now is this trip for you?')
            else:
                print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
        else:
            if user_input_b == 'bus':
                random_transportation.remove('bus')
                ride = random.choice(random_transportation)
                print(ride)
                user_input_c = input('Now is this trip for you?')
                while user_input_c == 'no':
                    random_transportation.remove(ride)
                    ride = random.choice(random_transportation)
                    print(ride)
                    input('Now is this trip for you?')
                else:
                    print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
            elif user_input_b == 'bike':
                random_transportation.remove('bike')
                ride = random.choice(random_transportation)
                print(ride)
                user_input_c = input('Now is this trip for you?')
                while user_input_c == 'no':
                    random_transportation.remove(ride)
                    ride = random.choice(random_transportation)
                    print(ride)
                    input('Now is this trip for you?')
                else:
                    print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
            elif user_input_b == 'train':
                random_transportation.remove('train')
                ride = random.choice(random_transportation)
                print(ride)
                user_input_c = input('Now is this trip for you?')
                while user_input_c == 'no':
                    random_transportation.remove(ride)
                    ride = random.choice(random_transportation)
                    print(ride)
                    input('Now is this trip for you?')
                else:
                    print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
            elif user_input_b == 'boat':
                random_transportation.remove('boat')
                ride = random.choice(random_transportation)
                print(ride)
                user_input_c = input('Now is this trip for you?')
                while user_input_c == 'no':
                    random_transportation.remove(ride)
                    ride = random.choice(random_transportation)
                    print(ride)
                    input('Now is this trip for you?')
                else:
                    print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')   
            elif user_input_b == 'helicopter':
                random_transportation.remove('helicopter')
                ride = random.choice(random_transportation)
                print(ride)
                user_input_c = input('Now is this trip for you?')
                while user_input_c == 'no':
                    random_transportation.remove(ride)
                    ride = random.choice(random_transportation)
                    print(ride)
                    input('Now is this trip for you?')
                else:
                    print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
            else:
                print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
                if user_input_b == 'movie':
                    random_entertainment.remove('movie')
                    fun = random.choice(random_entertainment)
                    print(fun)
                    user_input_c = input('Now is this trip for you?')
                    while user_input_c == 'no':
                        random_entertainment.remove(fun)
                        fun = random.choice(random_entertainment)
                        print(fun)
                        input('Now is this trip for you?')
                    else:
                        print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
                elif user_input_b == 'concert':
                    random_entertainment.remove('concert')
                    fun = random.choice(random_entertainment)
                    print(fun)
                    user_input_c = input('Now is this trip for you?')
                    while user_input_c == 'no':
                        random_entertainment.remove(fun)
                        fun = random.choice(random_entertainment)
                        print(fun)
                        input('Now is this trip for you?')
                    else:
                        print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
                elif user_input_b == 'hockey game':
                    random_entertainment.remove('hockey game')
                    fun = random.choice(random_entertainment)
                    print(fun)
                    user_input_c = input('Now is this trip for you?')
                    while user_input_c == 'no':
                        random_entertainment.remove(fun)
                        fun = random.choice(random_entertainment)
                        print(fun)
                        input('Now is this trip for you?')
                    else:
                        print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
                elif user_input_b == 'comedy show':
                    random_entertainment.remove('comedy show')
                    fun = random.choice(random_entertainment)
                    print(fun)
                    user_input_c = input('Now is this trip for you?')
                    while user_input_c == 'no':
                        random_entertainment.remove(fun)
                        fun = random.choice(random_entertainment)
                        print(fun)
                        input('Now is this trip for you?')
                    else:
                        print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
                elif user_input_b == 'car show':
                    random_entertainment.remove('car show')
                    fun = random.choice(random_entertainment)
                    print(fun)
                    user_input_c = input('Now is this trip for you?')
                    while user_input_c == 'no':
                        random_entertainment.remove(fun)
                        fun = random.choice(random_entertainment)
                        print(fun)
                        input('Now is this trip for you?')
                    else:
                        print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
                else:
                    if user_input_b == 'red robin':
                        random_restaurant.remove('red robin')
                        restaurant = random.choice(random_restaurant)
                        print(restaurant)
                        while user_input_c == 'no':
                            random_restaurant.remove(restaurant)
                            restaurant = random.choice(random_restaurant)
                            print(restaurant)
                            input('Now is this trip for you?')
                        else:
                            print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
                    elif user_input_b == 'applebees':
                        random_restaurant.remove('applebees')
                        restaurant = random.choice(random_restaurant)
                        print(restaurant)
                        while user_input_c == 'no':
                            random_restaurant.remove(restaurant)
                            restaurant = random.choice(random_restaurant)
                            print(restaurant)
                            input('Now is this trip for you?')
                        else:
                            print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
                    elif user_input_b == 'dennys':
                        random_restaurant.remove('dennys')
                        restaurant = random.choice(random_restaurant)
                        print(restaurant)
                        while user_input_c == 'no':
                            random_restaurant.remove(restaurant)
                            restaurant = random.choice(random_restaurant)
                            print(restaurant)
                            input('Now is this trip for you?')
                        else:
                            print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
                    elif user_input_b == 'sonic':
                        random_restaurant.remove('sonic')
                        restaurant = random.choice(random_restaurant)
                        print(restaurant)
                        while user_input_c == 'no':
                            random_restaurant.remove(restaurant)
                            restaurant = random.choice(random_restaurant)
                            print(restaurant)
                            input('Now is this trip for you?')
                        else:
                            print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
                    elif user_input_b == 'chilis':
                        random_restaurant.remove('chilis')
                        restaurant = random.choice(random_restaurant)
                        print(restaurant)
                        user_input_c = input('Now is this trip for you?')
                        while user_input_c == 'no':
                            random_restaurant.remove(restaurant)
                            restaurant = random.choice(random_restaurant)
                            print(restaurant)
                            input('Now is this trip for you?')
                        else:
                            print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
                    else:
                        print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')
    else:
        print('Congratulations! Enjoy your trip going to a {fun}, by {ride}, eating at {restaurant}, in {city}?')   
            
trip_arrangement(['miami', 'houston', 'nashville', 'atlanta', 'cleveland'], ['bus', 'bike', 'train', 'boat', 'helicopter'], ['movie', 'concert', 'hockey game', 'comedy show', 'car show'], ['applebees', 'chilis', 'red robin', 'dennys', 'sonic'])