from typing import Dict, Tuple, Iterable
import string
from itertools import product

# 8-bit colors
COLORS_AMOUNT = 256
MAX_TEXT_LENGTH = 6

letters = list(string.ascii_lowercase)
colors = tuple(range(COLORS_AMOUNT))

# Amount of colors per letter
colors_per_letter = round(COLORS_AMOUNT / len(letters))

# Extract chunks of colors and assign them to each letter
colors_by_letters: Dict[str, Tuple[int, ...]] = {
    letters[idx]: colors[color_code:color_code + colors_per_letter]
    for idx, color_code in enumerate(
        range(0, len(colors), colors_per_letter)
    )
}

def combine_colors(text: str) -> Iterable[Tuple[int, ...]]:
    letter_tuples: List[Tuple[int, ...]] = []

    for letter in text:
        letter_tuples.append(colors_by_letters.get(letter, (0,)))

    return product(*letter_tuples)

def generate_colors_output(text: str) -> str:
    final_string: str = ''

    for colors_product in combine_colors(user_text):
        for color_code in colors_product:
            final_string += '\033[48;5;{}m  '.format(color_code)

    final_string += '\033[0m'

    return final_string

while True:
    user_text: str = input("Enter text:")

    if len(user_text) <= MAX_TEXT_LENGTH:
        output = generate_colors_output(user_text)
        print(output)
    else:
        print('The text maximum length should be 6 characters')
