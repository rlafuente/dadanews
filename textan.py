#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice, shuffle


def get_word_matches(word, lines):
    matches = []
    for headline in HEADLINES_FILE:
        words = headline.split(" ")
        if word in words:
            matches.append(headline)
    return matches


def test_common_word(word, lines):
    # verifica se a palavra de ligação pode ser usada
    matches = get_word_matches(word, lines)
    if not len(matches) > 1:
        return False
    return True


def get_dada_headline(lines, wordlist):
    # escolher uma palavra para dividir e ver se podemos usar
    common_word = choice(wordlist).strip()
    while not test_common_word(common_word, lines):
        common_word = choice(wordlist).strip()

    # apanhar duas linhas e combiná-las
    matches = get_word_matches(common_word, lines)
    shuffle(matches)
    line1 = matches.pop()
    line2 = matches.pop()
    # assegurar que não são iguais
    while not line1 != line2:
        line1 = matches.pop()
        line2 = matches.pop()

    # repartir as linhas e recombiná-las de seguida
    part1 = line1.split(" %s " % common_word)[0].strip()
    part2 = line2.split(" %s " % common_word)[-1].strip()

    output = "%s %s %s" % (part1, common_word, part2)
    return output

if __name__ == "__main__":
    WORDLIST_PT = open("wordlist-pt.txt", "r").readlines()
    HEADLINES_FILE = open("headlines-pt.txt", "r").readlines()
    print get_dada_headline(HEADLINES_FILE, WORDLIST_PT)
