def find_anagrams(word, candidates):
    return [can for can in candidates if sorted(can.lower()) == sorted(word.lower()) and can.lower() != word.lower()]