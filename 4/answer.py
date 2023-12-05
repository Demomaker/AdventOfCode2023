import sys
def get_array():
    file = open("input.txt", "r")
    array = []
    for index, line in enumerate(file):
        if len(sys.argv) > 1 and index > int(sys.argv[1]):
            break
        array.append(line[:-1])
    file.close()
    return array

def remove_extra_whitespace():
    array = get_array()
    new_array = []
    for line in array:
        new_line = line
        current_wide_whitespace_index = new_line.find("  ")
        while current_wide_whitespace_index >= 0:
            new_line = new_line[0: current_wide_whitespace_index] + new_line[current_wide_whitespace_index + 1 : len(new_line)]
            current_wide_whitespace_index = new_line.find("  ")
        new_array.append(new_line)
    return new_array

def get_variables():
    array = remove_extra_whitespace()
    variables = []
    for card_line in array:
        card_number = card_line[len("Card "):card_line.find(":")]
        winning_numbers = card_line[card_line.find(":") + 1:card_line.find("|")].strip().split(" ")
        my_numbers = card_line[card_line.find("|") + 1:len(card_line)].strip().split(" ")
        variables.append({
            'card_number': card_number,
            'winning_numbers': winning_numbers,
            'my_numbers': my_numbers
        })
    return variables
    
def get_corresponding_numbers():
    variables = get_variables()
    corresponding_numbers = {}
    for variable_dict in variables:
        for index, number in enumerate(variable_dict['my_numbers']):
            if number in variable_dict['winning_numbers']:
                index_in_winning_numbers = variable_dict['winning_numbers'].index(number)
                if (index_in_winning_numbers > -1) :
                    corresponding_numbers_key = variable_dict['card_number']
                    if corresponding_numbers_key in corresponding_numbers.keys():
                        existing_value = corresponding_numbers[corresponding_numbers_key]
                        existing_value["good_numbers"].append({
                            'number': variable_dict['winning_numbers'][index_in_winning_numbers],
                            'winning_numbers_array_position': index_in_winning_numbers,
                            'my_numbers_array_position': index,
                        })
                        corresponding_numbers[corresponding_numbers_key] = existing_value
                    else :
                        corresponding_numbers[variable_dict['card_number']] = {
                            'good_numbers': [{
                                'number': variable_dict['winning_numbers'][index_in_winning_numbers],
                                'winning_numbers_array_position': index_in_winning_numbers,
                                'my_numbers_array_position': index,
                            }]
                        }
    return corresponding_numbers
    
def get_amount_of_points():
    corresponding_numbers = get_corresponding_numbers()
    amount_of_points = []
    for game_number in corresponding_numbers.keys():
        corresponding_number = corresponding_numbers[game_number]
        points = 0
        index = 0
        while index < len(corresponding_number['good_numbers']):
            if points == 0:
                points = 1
            else :
                points = 2 * points
            index = index + 1
        amount_of_points.append(points)
    return amount_of_points

def get_matching_cards():
    corresponding_numbers = get_corresponding_numbers()
    variables = get_variables()
    matching_cards = {}
    for game_number in range(1, len(variables) + 1):
        if not str(game_number) in corresponding_numbers:
            matching_cards[str(game_number)] = []
            continue

        corresponding_number = corresponding_numbers[str(game_number)]
        amount_of_matching_cards = len(corresponding_number['good_numbers'])
        matching_card_number = int(game_number)
        scratch_cards = []
        while matching_card_number < amount_of_matching_cards + int(game_number):
            matching_card_number = matching_card_number + 1
            scratch_cards.append(matching_card_number)
        matching_cards[str(game_number)] = scratch_cards

    return matching_cards

def find_index_in_matching_cards(matching_cards, number):
    for index, matching_card in enumerate(matching_cards):
        for card_number in matching_card.keys():
            if str(card_number) == str(number):
                return index
    return -1

def multiply_matching_cards():
    matching_cards = get_matching_cards()
    cards_count = {str(i): 0 for i in range(1, len(matching_cards) + 1)}
    
    def calculate_copies(number, numbers):
        cards_count[str(number)] += 1
        for card_number in numbers:
            calculate_copies(str(card_number), matching_cards[str(card_number)])

    for card in matching_cards.keys():
        number = card
        numbers = matching_cards[card]
        calculate_copies(number, numbers)
    return sum(list(cards_count.values()))


print(multiply_matching_cards())