from typing import Dict, Tuple, Iterable
from itertools import product
import string
import random

# 8-bit colors
COLORS_AMOUNT = 256
MAX_COLORS_TO_COMPUTE = 36
ITERATION_NUM = 3
MAX_TEXT_LENGTH = round(MAX_COLORS_TO_COMPUTE / ITERATION_NUM)

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
    text_length = len(text)
    choices_per_letter = round(MAX_TEXT_LENGTH / text_length)
    difference = MAX_TEXT_LENGTH - (choices_per_letter * text_length)
    text_iteration = []

    for i in range(text_length):
        if difference > i:
            text_iteration.append(choices_per_letter + 1)
            continue

        if (difference + i) < 0:
            text_iteration.append(choices_per_letter - 1)
            continue

        text_iteration.append(choices_per_letter)

    # iterate over a fix range
    for _ in range(ITERATION_NUM):
        text_colors = []

        for idx, letter in enumerate(text):
            # use letters to get colors in each iteration.
            # add cartain amount of colors per letter randomly.
            # no matter how big or small is the text,
            # always display the same amount of colors.
            color_choice = random.choices(
                colors_by_letters.get(letter, (0,)),
                k=text_iteration[idx]
            )
            text_colors.extend(color_choice)

        letter_tuples.append(text_colors)

    return product(*letter_tuples)

def generate_colors_output(text: str) -> str:
    final_string: str = ''

    # use text to generate numbers based on the letters indexes
    # use those numbers to insert blank points to create shapes
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
        print('The text maximum length should be {} characters'.format(MAX_TEXT_LENGTH))
