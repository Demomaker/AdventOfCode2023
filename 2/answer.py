import sys

def get_games_array():
    file = open("input.txt", "r")
    array = []
    for index, line in enumerate(file):
        array.append(line[:-1])
    file.close()
    return array

def get_game_number(game):
    number_start_index = game.find("Game ") + len("Game ")
    number_end_index = game.find(":", number_start_index)
    return int(game[number_start_index:number_end_index])

def get_cube_amount(text, cube_name, cube_reverse_name):
    end_index = text.find(cube_name)
    text_reverse = text[::-1]
    end_index_reverse = text_reverse.find(cube_reverse_name)
    start_index_reverse = text_reverse.find(" ", text_reverse.find(" ", end_index_reverse) + len(" ")) + len(" ")
    start_index = len(text) - start_index_reverse
    amount_as_string = text[start_index:end_index].strip()
    if amount_as_string == "":
        return 0
    return int(amount_as_string)


def get_amount_of_red_cubes(text):
    return get_cube_amount(text, "red", "der")

def get_amount_of_green_cubes(text):
    return get_cube_amount(text, "green", "neerg")

def get_amount_of_blue_cubes(text):
    return get_cube_amount(text, "blue", "eulb")

def get_cube_subsets(game):
    cube_subsets = []
    cube_subsets_start_index = game.find(":") + len(":")
    current_subset_index = cube_subsets_start_index
    next_subset_index = game.find(";", current_subset_index + 1) + len(";")
    while current_subset_index > 0:
        current_subset_content_text = game[current_subset_index:next_subset_index]
        if next_subset_index <= 0:
            current_subset_content_text = game[current_subset_index:]
        amount_of_red_cubes = get_amount_of_red_cubes(current_subset_content_text)
        amount_of_blue_cubes = get_amount_of_blue_cubes(current_subset_content_text)
        amount_of_green_cubes = get_amount_of_green_cubes(current_subset_content_text)
        cube_subsets.append({
            'green': amount_of_green_cubes,
            'blue': amount_of_blue_cubes,
            'red': amount_of_red_cubes
        })
        current_subset_index = next_subset_index
        next_subset_index = game.find(";", current_subset_index + 1) + len(";")
    return cube_subsets

def convert_games_array_to_variables():
    games_array = get_games_array()
    games_variables = []
    for index, game in enumerate(games_array):
        if len(sys.argv) > 1 and index > int(sys.argv[1]):
            break
        print(game)
        game_number = get_game_number(game)
        cube_subsets = get_cube_subsets(game)
        game_variables = {
            'game_number': game_number,
            'cube_subsets': cube_subsets
        }
        games_variables.append(game_variables)
    return games_variables

def get_maximum(cube_subsets, cube_type):
    maximum = 0
    for cube_subset in cube_subsets:
        if cube_subset[cube_type] > maximum:
            maximum = cube_subset[cube_type]
    return maximum


def get_red_maximum(game_variables):
    return get_maximum(game_variables['cube_subsets'], 'red')

def get_green_maximum(game_variables):
    return get_maximum(game_variables['cube_subsets'], 'green')

def get_blue_maximum(game_variables):
    return get_maximum(game_variables['cube_subsets'], 'blue')

def get_cube_maximums():
    games_variables = convert_games_array_to_variables()
    games_and_maximums = []
    for game_variables in games_variables:
        maximums = {
            'red': get_red_maximum(game_variables),
            'green': get_green_maximum(game_variables),
            'blue': get_blue_maximum(game_variables)
        }
        games_and_maximums.append({
            'game_number': game_variables['game_number'],
            'maximums': maximums
        })
    return games_and_maximums

def passes_threshold(maximums, cube_type, threshold):
    return maximums[cube_type] <= threshold[cube_type]

def get_valid_games(threshold):
    games_and_maximums = get_cube_maximums()
    valid_games = []
    for game in games_and_maximums:
        maximums = game['maximums']
        if passes_threshold(maximums, 'red', threshold) and passes_threshold(maximums, 'blue', threshold) and passes_threshold(maximums, 'green', threshold):
            valid_games.append(int(game['game_number']))
    return valid_games

def get_total_from_valid_game_numbers(threshold):
    valid_games = get_valid_games(threshold)
    return sum(valid_games)

def get_powers_of_game_maximums():
    games_and_maximums = get_cube_maximums()
    powers_of_game_maximums = []
    for game in games_and_maximums:
        maximums = game['maximums']
        power = int(maximums['red']) * int(maximums['blue']) * int(maximums['green'])
        powers_of_game_maximums.append(power)
    return powers_of_game_maximums

def get_sum_of_powers():
    games_and_powers = get_powers_of_game_maximums()
    return sum(games_and_powers)

print(get_sum_of_powers())