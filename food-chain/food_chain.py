def recite(start_verse, end_verse):
    song = []
    animals = ['fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse']
    second_row = ['It wriggled and jiggled and tickled inside her.', 'How absurd to swallow a bird!', 'Imagine that, to swallow a cat!', 'What a hog, to swallow a dog!', 'Just opened her throat and swallowed a goat!', 'I don\'t know how she swallowed a cow!']
    last_row = ['I don\'t know why she swallowed the fly. Perhaps she\'ll die.', 'She\'s dead, of course!']

    for n in range(start_verse, end_verse+1):
        i = n - 1
        # 1st row
        song += [f'I know an old lady who swallowed a {animals[i]}.']

        # 2nd row
        if 1 <= i <= 6:
            song += [second_row[i-1]]

        # the middle
        if n != 8:
            while i != 0:
                extra = ' that wriggled and jiggled and tickled inside her' if animals[i-1] == 'spider' else ''
                song += [f'She swallowed the {animals[i]} to catch the {animals[i-1]}{extra}.']
                i -= 1

        # last row
        song += [last_row[0] if n != 8 else last_row[1]]

        # add separator if needed
        if n != end_verse:
            song +=['']

    return song
