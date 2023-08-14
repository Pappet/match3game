import random

# Color Codes for simpler use

# Use it with:
# Color.Black
# etc.

White = (255, 255, 255)
LightGray = (211, 211, 211)
Gray = (169, 169, 169)
DarkGray = (128, 128, 128)
Black = (0, 0, 0)

Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

Yellow = (255, 255, 0)
Cyan = (0, 255, 255)
Magenta = (255, 0, 255)

Brown = (210, 105, 30)
Purple = (128, 0, 128)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
