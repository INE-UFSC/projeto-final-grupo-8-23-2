import os
import sys


green = (58, 190, 50)
red = (255, 17, 0)
brown = (150, 75, 0)
pink = (206, 53, 137) # #DE4083
white = (255, 255, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)
pink_low_alpha = (206, 53, 137, 100)


if sys.platform == 'win32':
    separator = '\\'
else:
    separator = '/'

def get_file_path(file_path):
    current_path = os.path.dirname(file_path).split(separator)
    return separator.join(current_path[0:current_path.index('src')]) + f'{separator}resources'

