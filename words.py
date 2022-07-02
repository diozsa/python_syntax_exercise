def print_upper_words(words, must_start_with):
    """Prints each word on sep line, in UPPERCASING.
    It filters the list of strings from the first argument
    and prints only words that start
    with each letters contained in the second argument
    """

    for letter in must_start_with:
        for word in words:
            if word.startswith(letter):
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with=["h", "y"])

