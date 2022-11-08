def recite(start, take=1):
    last_two = ['No more bottles of beer on the wall, no more bottles of beer.', 'Go to the store and buy some more, 99 bottles of beer on the wall.']
    lyrics = []

    if start == 0:
        lyrics.extend(last_two)
    else:
        for i in range(start, start-take, -1):
            if i != start:
                lyrics.append('')
            
            if i != 0:
                first_sen = '{0} bottle{1} of beer on the wall, {0} bottle{1} of beer.'
                first_sen = first_sen.format(i, "" if i == 1 else "s")
                
                second_sen = f'Take {"one" if i != 1 else "it"} down and pass it around, '
                if i == 1:
                    second_sen += 'no more bottles of beer on the wall.'
                else:
                    second_sen += f'{i-1} bottle{"" if i == 2 else "s"} of beer on the wall.'
                    
                lyrics.extend([first_sen, second_sen])
            else:
                lyrics.extend(last_two)
    
    return lyrics