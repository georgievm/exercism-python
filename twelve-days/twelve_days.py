def recite(start, end):
    ORDINALS = {1: 'first', 2: 'second', 3: 'third',
                4: 'fourth', 5: 'fifth', 6: 'sixth',
                7: 'seventh', 8: 'eighth', 9: 'ninth',
                10: 'tenth', 11: 'eleventh', 12: 'twelfth'}
    VERSES = ['twelve Drummers Drumming, ', 'eleven Pipers Piping, ', 'ten Lords-a-Leaping, ', 'nine Ladies Dancing, ', 'eight Maids-a-Milking, ', 'seven Swans-a-Swimming, ', 'six Geese-a-Laying, ', 'five Gold Rings, ', 'four Calling Birds, ', 'three French Hens, ', 'two Turtle Doves, and ', 'a Partridge in a Pear Tree.']
    
    all_lyrics = []
    for lyr_no in range(start, end+1):
        header = f"On the {ORDINALS[lyr_no]} day of Christmas my true love gave to me: "
        rest_vers = ''.join(VERSES[-lyr_no:])
        
        all_lyrics += [header + rest_vers]

    return all_lyrics
