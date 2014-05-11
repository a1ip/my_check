def verify_anagrams(word_1, word_2):
    """Function is comparing both word sorted
    in alphabetic order. Words are lowercased and
    only alphas are taken in account."""
    eq = (lambda w:
          sorted([c for c in
                 w.lower() if 
                 c.isalpha()]))
    return eq(word_1) == eq(word_2)


if __name__ == "__main__":
    assert verify_anagrams("abc", "Cba") == True, "Jednoduche"
    assert verify_anagrams("ab c", "Cba") == True, "Jednoduche s mezerami"
    assert verify_anagrams("abx", "Cba") == False, "Spatne"
