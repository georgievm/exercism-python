def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = text.split()
    for word in words:
        if vowels.count(word[0]) == 1 or word.startswith('xr') or word.startswith('yt'): # rule 1
            text = text.replace(word, word+'ay')
        elif word[0:2] == 'qu': # rule 3
            text = text.replace(word, word[2:]+word[:2]+'ay')
        elif word[1:3] == 'qu': # rule 3
            text = text.replace(word, word[3:]+word[:3]+'ay')
        else: # rule 2 & 4
            vow_or_y_pos = 0
            for letter in word:
                if vowels.count(letter) == 1 or letter == 'y':
                    vow_or_y_pos = word.index(letter)
                    break
            if vow_or_y_pos == 0:
                text = text.replace(word, word[vow_or_y_pos+1:]+word[0]+'ay')
            text = text.replace(word, word[vow_or_y_pos:]+word[:vow_or_y_pos]+'ay')
    return text
