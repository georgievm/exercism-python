def recite(start, end):
    full_verse = ['horse and the hound and the horn that belonged to',
                'farmer sowing his corn that kept',
                'rooster that crowed in the morn that woke',
                'priest all shaven and shorn that married',
                'man all tattered and torn that kissed',
                'maiden all forlorn that milked',
                'cow with the crumpled horn that tossed',
                'dog that worried',
                'cat that killed',
                'rat that ate',
                'malt that lay in',
                'house that Jack built.']

    return ['This is the ' + ' the '.join(full_verse[-verse_no:]) for verse_no in range(start, end+1)]
