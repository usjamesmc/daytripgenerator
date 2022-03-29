# random lists of destination, restaurant, mode of transportation, form of entertainment

# ['miami, houston, nashville, atlanta, cleveland']
import random
def trip_location(random_destination):
    word = random.choice(random_destination)
    print(word)
    user_input = input("Is this destination okay?")
    if user_input == 'no' and word == 'miami' or 'houston' or 'nashville' or 'atlanta' or 'cleveland':
        random_destination.remove(word)
        word = random.choice(random_destination)
        print(word)
        input('Is this destination okay?')
    # elif user_input == 'no' and word == 'miami' or 'houston' or 'nashville' or 'atlanta' or 'cleveland':
    #     random_destination.remove(word)
    #     word = random.choice(random_destination)
    #     print(word)
    #     input('Is this destination okay?')
    # elif user_input == 'no' and word == 'miami' or 'houston' or 'nashville' or 'atlanta' or 'cleveland':
    #     random_destination.remove(word)
    #     word = random.choice(random_destination)
    #     print(word)
    #     input('Is this destination okay?')
    # elif user_input == 'no' and word == 'miami' or 'houston' or 'nashville' or 'atlanta' or 'cleveland':
    #     random_destination.remove(word)
    #     word = random.choice(random_destination)
    #     print(word)
    #     input('Is this destination okay?')
    # elif user_input == 'no' and word == 'miami' or 'houston' or 'nashville' or 'atlanta' or 'cleveland':
    #     print('Sorry, no more selections')
        
    else:
    
        print('yes')

    
trip_location(['miami', 'houston', 'nashville', 'atlanta', 'cleveland'])


# def trip_eatery(random_restaurant):
#     place_to_eat = random.choice(random_restaurant)
#     print(place_to_eat)
#     user_input = input('Is this restaurant okay?')
#     if user_input == 'no' and place_to_eat == 'applebees' or 'chilis' or 'red robin' or 'cookout' or 'sonic':
#         random_restaurant.remove(place_to_eat)
#         place_to_eat = random.choice(random_restaurant)
#         print(place_to_eat)
#         input('Is this restaurant okay?')
#     else:
#         print('yes')

# trip_eatery(['applebees', 'chilis', 'red robin', 'cookout', 'sonic'])