"""
goshoooo
"""
def add_prefix_un(word):
    return 'un'+word

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    return (' :: '+vocab_words[0]).join(vocab_words)


def remove_suffix_ness(word):
    if word[-5:] == 'iness':
        return word[:-5] + 'y'
    return word[:-4]

def adjective_to_verb(sentence, index):
    return (sentence.replace('.', '')).split()[index] + 'en'
