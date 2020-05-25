from typing import Dict, Tuple
import string

COLORS_AMOUNT = 256

letters = list(string.ascii_lowercase)
colors = tuple(range(COLORS_AMOUNT))

# Amount of colors per letter
colors_per_letter = round(COLORS_AMOUNT / len(letters))

# Extract chunks of colors and assign them to each letter
colors_by_letters: Dict[str, Tuple[str, ...]] = {
    letters[idx]: colors[color_code:color_code + colors_per_letter]
    for idx, color_code in enumerate(
        range(0, len(colors), colors_per_letter)
    )
}

print(colors_by_letters)
