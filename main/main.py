def check_vowels(letter):
    """
    Checks is letter is a vowel (both upper case and lower case is checked)
    :param letter:
    :return: True/False
    """
    return letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def transform(letter):
    """
    Transforms string to the respective numeric alphabet position. It is case-insensitive.

    :param letter:
    :return: True/False
    """
    if type(letter) != str or not check_vowels(letter):
        raise Exception("Invalid input string, input must be a vowel and a string.")
    return str(ord(letter.lower()) - ord('a') + 1)


def main():
    """
    Tranforms input string by converting their vowels to the respective numeric alphabet position.
    Assumption the following function is case-insensitive and will provide the same output for lower case and upper case vowels
    :return: Print total consonants and formatted string
    """
    inp_str = "National Center for Supercomputing Applications"
    inp_str = list(inp_str)
    consonants = 0
    for i, letter in enumerate(inp_str):
        if check_vowels(letter):
            inp_str[i] = transform(letter)
        else:
            consonants += 1

    print(''.join(inp_str))
    print("The total number of consonants ", consonants)


if __name__ == '__main__':
    main()
