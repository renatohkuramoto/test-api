def convert_snake_case_to_camel_case(snake_str: str) -> str:
    def format_word(char: str, index: int) -> str:
        next_index = index + 1
        if char and len(char) > next_index and char[next_index].isupper():
            return char
        elif '.' not in char:
            return char.title()
        else:
            return char.capitalize()
    components = snake_str.split('_')
    return components[0] + ''.join(format_word(char, index) for index, char in enumerate(components[1:]))