import sys

def get_input():
    file = open("input.txt", "r")
    array = []
    for index, line in enumerate(file):
        if len(sys.argv) > 1 and index > int(sys.argv[1]):
            break
        array.append(line[:-1])
    file.close()
    return array

def top_relative_pattern(line_index, character_index):
    return { 'line_index': line_index - 1, 'character_index': character_index }

def bottom_relative_pattern(line_index, character_index):
    return { 'line_index': line_index + 1, 'character_index': character_index }

def right_relative_pattern(line_index, character_index):
    return { 'line_index': line_index, 'character_index': character_index + 1 }

def left_relative_pattern(line_index, character_index):
    return { 'line_index': line_index, 'character_index': character_index - 1 }

def top_left_relative_pattern(line_index, character_index):
    return { 'line_index': line_index - 1, 'character_index': character_index - 1 }

def top_right_relative_pattern(line_index, character_index):
    return { 'line_index': line_index - 1, 'character_index': character_index + 1 }

def bottom_left_relative_pattern(line_index, character_index):
    return { 'line_index': line_index + 1, 'character_index': character_index - 1}

def bottom_right_relative_pattern(line_index, character_index):
    return { 'line_index': line_index + 1, 'character_index': character_index + 1}

def get_pattern_relative_characters(line_index, character_index, problem_input, pattern):
    pattern_result = pattern(line_index, character_index)
    current_line_index = pattern_result['line_index']
    current_character_index = pattern_result['character_index']
    relative_characters = []
    amount_of_calls = 0
    max_while_calls = 1000
    while amount_of_calls < max_while_calls and current_line_index < len(problem_input) and current_line_index >= 0 and current_character_index < len(problem_input[current_line_index]) and current_character_index >= 0:
        amount_of_calls = amount_of_calls + 1
        current_character = problem_input[current_line_index][current_character_index]
        if not current_character.isnumeric():
            relative_characters.append({
                'line_index': current_line_index,
                'character_index': current_character_index,
                'character': current_character
            })
        pattern_result = pattern(current_line_index, current_character_index)
        current_line_index = pattern_result['line_index']
        current_character_index = pattern_result['character_index']
    return relative_characters

def get_numbers_and_characters_from_input():
    problem_input = get_input()
    for line_index, line in enumerate(problem_input):
        current_character_index = 0
        current_number_as_string = ""
        while character_index < len(line):
            if line[current_line_index].isnumeric():
                current_number_as_string = current_number_as_string + line[current_line_index]

def get_relative_characters():
    problem_input = get_input()
    relative_characters = []
    for line_index, line in enumerate(problem_input):
        for character_index, character in enumerate(line):
            top_relative_characters = get_pattern_relative_characters(line_index, character_index, problem_input, top_relative_pattern)
            bottom_relative_characters = get_pattern_relative_characters(line_index, character_index, problem_input, bottom_relative_pattern)
            right_relative_characters = get_pattern_relative_characters(line_index, character_index, problem_input, right_relative_pattern)
            left_relative_characters = get_pattern_relative_characters(line_index, character_index, problem_input, left_relative_pattern)
            top_left_relative_characters = get_pattern_relative_characters(line_index, character_index, problem_input, top_left_relative_pattern)
            top_right_relative_characters = get_pattern_relative_characters(line_index, character_index, problem_input, top_right_relative_pattern)
            bottom_left_relative_characters = get_pattern_relative_characters(line_index, character_index, problem_input, bottom_left_relative_pattern)
            bottom_right_relative_characters = get_pattern_relative_characters(line_index, character_index, problem_input, bottom_right_relative_pattern)
            relative_characters.append({
                'line_index': line_index,
                'character_index': character_index,
                'character': character,
                'top_relative_characters': top_relative_characters,
                'bottom_relative_characters': bottom_relative_characters,
                'right_relative_characters': right_relative_characters,
                'left_relative_characters': left_relative_characters,
                'top_left_relative_characters': top_left_relative_characters,
                'top_right_relative_characters': top_right_relative_characters,
                'bottom_left_relative_characters': bottom_left_relative_characters,
                'bottom_right_relative_characters': bottom_right_relative_characters
            })
    return relative_characters

def combine_numbers():
    problem_input = get_input()
    characters_and_relatives = get_relative_characters()
    combined_numbers_indexes = []
    characters_numbers_and_relatives = []
    for character_and_relatives_index, character_and_relatives in enumerate(characters_and_relatives):
        line_index = character_and_relatives['line_index']
        character_index = character_and_relatives['character_index']
        character = character_and_relatives['character']
        top_relative_characters = character_and_relatives['top_relative_characters']
        bottom_relative_characters = character_and_relatives['bottom_relative_characters']
        right_relative_characters = character_and_relatives['right_relative_characters']
        left_relative_characters = character_and_relatives['left_relative_characters']
        top_left_relative_characters = character_and_relatives['top_left_relative_characters']
        top_right_relative_characters = character_and_relatives['top_right_relative_characters']
        bottom_left_relative_characters = character_and_relatives['bottom_left_relative_characters']
        bottom_right_relative_characters = character_and_relatives['bottom_right_relative_characters']
        if character.isnumeric():
            if not {'line_index': line_index, 'character_index': character_index} in combined_numbers_indexes:
                combined_number_as_string = ""
                current_character_index = character_index
                relatives = []
                line = problem_input[line_index]
                while current_character_index < len(line) and line[current_character_index].isnumeric():
                    combined_number_as_string = combined_number_as_string + line[current_character_index]
                    next_character_and_relatives = characters_and_relatives[character_and_relatives_index + (current_character_index - character_index)]
                    next_top_relative_characters = next_character_and_relatives['top_relative_characters']
                    next_bottom_relative_characters = next_character_and_relatives['bottom_relative_characters']
                    next_left_relative_characters = next_character_and_relatives['left_relative_characters']
                    next_right_relative_characters = next_character_and_relatives['right_relative_characters']
                    next_top_left_relative_characters = next_character_and_relatives['top_left_relative_characters']
                    next_top_right_relative_characters = next_character_and_relatives['top_right_relative_characters']
                    next_bottom_left_relative_characters = next_character_and_relatives['bottom_left_relative_characters']
                    next_bottom_right_relative_characters = next_character_and_relatives['bottom_right_relative_characters']
                    relatives.append({
                        'top_relative_characters': next_top_relative_characters,
                        'bottom_relative_characters': next_bottom_relative_characters,
                        'right_relative_characters': next_right_relative_characters,
                        'left_relative_characters': next_left_relative_characters,
                        'top_left_relative_characters': next_top_left_relative_characters,
                        'top_right_relative_characters': next_top_right_relative_characters,
                        'bottom_left_relative_characters': next_bottom_left_relative_characters,
                        'bottom_right_relative_characters': next_bottom_right_relative_characters
                    })
                    combined_numbers_indexes.append({'line_index': line_index, 'character_index': current_character_index})
                    current_character_index = current_character_index + 1

                characters_numbers_and_relatives.append({
                    'character': int(combined_number_as_string),
                    'is_number': True,
                    'relatives': relatives
                })
        else :
            characters_numbers_and_relatives.append({
                'character': character,
                'is_number': False,
                'relatives': [{
                    'top_relative_characters': top_relative_characters,
                    'bottom_relative_characters': bottom_relative_characters,
                    'right_relative_characters': right_relative_characters,
                    'left_relative_characters': left_relative_characters,
                    'top_left_relative_characters': top_left_relative_characters,
                    'top_right_relative_characters': top_right_relative_characters,
                    'bottom_left_relative_characters': bottom_left_relative_characters,
                    'bottom_right_relative_characters': bottom_right_relative_characters
                }]
            })
    return characters_numbers_and_relatives

def get_relative(relatives_array, at_x_element):
    if at_x_element >= len(relatives_array):
        return {
            'line_index': -1,
            'character_index': -1,
            'character': '',
        }
    return relatives_array[at_x_element]

def contains_special_character_at_x_element(relatives_array, at_x_element = 0):
    return {'condition': len(relatives_array) > 0 and not relatives_array[at_x_element]['character'] in ['.'],
    'relative': get_relative(relatives_array, at_x_element)}

def add_to_special_relatives_with_part_numbers_if_wanted(relative_and_condition, part_number, special_relatives_with_part_numbers):
    special_relatives_with_part_numbers_copy = special_relatives_with_part_numbers
    passed_condition = False
    if relative_and_condition['condition']:
        passed_condition = True
        special_relatives_with_part_numbers_key = str(relative_and_condition['relative']['line_index']) + ', ' + str(relative_and_condition['relative']['character_index'])
        if special_relatives_with_part_numbers_key in special_relatives_with_part_numbers_copy.keys():
            special_relatives_with_part_numbers_copy[special_relatives_with_part_numbers_key].append(part_number)
        else:
            special_relatives_with_part_numbers_copy[special_relatives_with_part_numbers_key] = [part_number]
    return {
        'return_array': special_relatives_with_part_numbers_copy,
        'condition_passed': passed_condition
    }


def get_part_numbers():
    characters_numbers_and_relatives = combine_numbers()
    special_relatives_with_part_numbers = {}
    for character_numbers_and_relatives in characters_numbers_and_relatives:
        if character_numbers_and_relatives['is_number']:
            for relative_dict in character_numbers_and_relatives['relatives']:
                top_relatives_has_special_character = contains_special_character_at_x_element(relative_dict['top_relative_characters'])
                bottom_relatives_has_special_character = contains_special_character_at_x_element(relative_dict['bottom_relative_characters'])
                left_relatives_has_special_character = contains_special_character_at_x_element(relative_dict['left_relative_characters'])
                right_relatives_has_special_character = contains_special_character_at_x_element(relative_dict['right_relative_characters'])
                top_left_relatives_has_special_character = contains_special_character_at_x_element(relative_dict['top_left_relative_characters'])
                top_right_relatives_has_special_character = contains_special_character_at_x_element(relative_dict['top_right_relative_characters'])
                bottom_left_relatives_has_special_character = contains_special_character_at_x_element(relative_dict['bottom_left_relative_characters'])
                bottom_right_relatives_has_special_character = contains_special_character_at_x_element(relative_dict['bottom_right_relative_characters'])
                
                ret_val = add_to_special_relatives_with_part_numbers_if_wanted(top_relatives_has_special_character, character_numbers_and_relatives['character'], special_relatives_with_part_numbers)
                if ret_val['condition_passed']:
                    special_relatives_with_part_numbers = ret_val['return_array']
                    break

                ret_val = add_to_special_relatives_with_part_numbers_if_wanted(bottom_relatives_has_special_character, character_numbers_and_relatives['character'], special_relatives_with_part_numbers)
                if ret_val['condition_passed']:
                    special_relatives_with_part_numbers = ret_val['return_array']
                    break

                ret_val = add_to_special_relatives_with_part_numbers_if_wanted(left_relatives_has_special_character, character_numbers_and_relatives['character'], special_relatives_with_part_numbers)
                if ret_val['condition_passed']:
                    special_relatives_with_part_numbers = ret_val['return_array']
                    break

                ret_val = add_to_special_relatives_with_part_numbers_if_wanted(right_relatives_has_special_character, character_numbers_and_relatives['character'], special_relatives_with_part_numbers)
                if ret_val['condition_passed']:
                    special_relatives_with_part_numbers = ret_val['return_array']
                    break

                ret_val = add_to_special_relatives_with_part_numbers_if_wanted(top_left_relatives_has_special_character, character_numbers_and_relatives['character'], special_relatives_with_part_numbers)
                if ret_val['condition_passed']:
                    special_relatives_with_part_numbers = ret_val['return_array']
                    break

                ret_val = add_to_special_relatives_with_part_numbers_if_wanted(top_right_relatives_has_special_character, character_numbers_and_relatives['character'], special_relatives_with_part_numbers)
                if ret_val['condition_passed']:
                    special_relatives_with_part_numbers = ret_val['return_array']
                    break

                ret_val = add_to_special_relatives_with_part_numbers_if_wanted(bottom_left_relatives_has_special_character, character_numbers_and_relatives['character'], special_relatives_with_part_numbers)
                if ret_val['condition_passed']:
                    special_relatives_with_part_numbers = ret_val['return_array']
                    break

                ret_val = add_to_special_relatives_with_part_numbers_if_wanted(bottom_right_relatives_has_special_character, character_numbers_and_relatives['character'], special_relatives_with_part_numbers)
                if ret_val['condition_passed']:
                    special_relatives_with_part_numbers = ret_val['return_array']
                    break
    return special_relatives_with_part_numbers

def get_gear_ratios():
    special_relatives_with_part_numbers = get_part_numbers()
    gear_ratios = []
    for part_numbers in special_relatives_with_part_numbers.values():
        if len(part_numbers) <= 1:
            continue
        current_index = 0
        gear_ratio = 1
        while current_index < len(part_numbers):
            gear_ratio = gear_ratio * int(part_numbers[current_index])
            current_index = current_index + 1
        gear_ratios.append(gear_ratio)
    return gear_ratios

print(sum(get_gear_ratios()))