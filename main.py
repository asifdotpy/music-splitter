from spleeter.separator import Separator

# Create a separator with the 'spleeter:2stems' configuration
separator = Separator('spleeter:2stems')

# Use the separator to separate the vocals and accompaniment of a song
separator.separate_to_file('ami-parina-ar-parina.mp3', 'output')

