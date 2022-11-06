def find_anagrams(word, candidates):
    anagrams, word_l = [], word.lower()
    for cand in candidates:
        cand_l = cand.lower()
        if cand_l != word_l and sorted(cand_l) == sorted(word_l):
            anagrams.append(cand)
    return anagrams
