from string import ascii_letters
import sys

LETTER_TEMPLATE = ':parrot-{}:'
SEPARATOR = '  '


def parrotize_letter(letter):
    if letter == ' ':
        return SEPARATOR * 2
    if letter not in ascii_letters:
        return SEPARATOR
    return LETTER_TEMPLATE.format(letter.lower())


def parrotize_string(string):
    return ''.join(map(parrotize_letter, string))


def cli_print():
    print(parrotize_string(' '.join(sys.argv[1:])))


if __name__ == '__main__':
    cli_print()
