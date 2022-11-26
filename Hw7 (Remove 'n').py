# Remove first 'n' characters from a string(n == numbers)
from datetime import datetime
character = input('enter a word\n')


def remove_chars(character, y):
    x = character[y:]
    return x


print(remove_chars(character, 2))
print(remove_chars(character, 4))
now = datetime.now()
time = now.strftime("%H:%M:%S")
print('Time:', time)
DMY = now.strftime("%D/%M/%Y")
print('Date:', DMY)
