import os
import sys


green = (58, 99, 50)
red = (255, 17, 0)
brown = (150, 75, 0)
pink = (206, 53, 137) # #DE4083


if sys.platform == 'linux':
    separator = '/'
else:
    separator = '\\'

def get_file_path(file_path):
    current_path = os.path.dirname(file_path).split(separator)
    return separator.join(current_path[0:current_path.index('src')]) + f'{separator}resources'

