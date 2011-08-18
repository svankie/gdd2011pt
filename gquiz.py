# -*- coding: utf-8 -*-

# exercise material copied from quiz site.
text_a, text_b = map(file.read, map(open, ['text_a.txt', 'text_b.txt']))
# the infamous 'foo letters'.
foo = ('h', 'b', 'w', 'l', 's')
# our arbitrary alphabet.
alpha = 'cmztgxqjfwkslbpvhndr'

def calculate_prepositions(text):
    prepositions = [qualified for qualified in text.split() \
        if len(qualified) == 4 and qualified[-1] in foo and 'p' not in qualified]
    return len(prepositions)


def calculate_verbs(text):
    verbs = [qualified for qualified in text.split() \
        if len(qualified) >= 7 and qualified[-1] in foo]
    first_person = [verb for verb in verbs if not verb.startswith(foo)]
    return len(verbs), len(first_person)


def create_vocabulary(text):
    return " ".join(sorted(set(text.split()), key=lambda w: [alpha.index(c) for c in w]))


def calculate_distinct_and_interesting(pseudonumbers):
    def is_interesting(pseudonumber):
        return (pseudonumber >= 665180) and (pseudonumber % 4 == 0)

    magic_bag = []
    for pseudonumber in pseudonumbers.split():
        mdigits = []
        for digit in pseudonumber:
            mdigits.append(alpha.index(digit))

        total, base = 0, 1
        for digit in mdigits:
            total += digit * base
            base *= 20

        if is_interesting(total):
            magic_bag.append(pseudonumber)

    return len(set(magic_bag))


if __name__ == '__main__':
    print u"El texto B tiene %d preposiciones." % calculate_prepositions(text_b)
    print u"El texto B tiene %d verbos y %d son en primera persona." % calculate_verbs(text_b)
    print u"El vocabulario del texto B es: %s\n\n" % create_vocabulary(text_b)
    print u"El texto B tiene %d números interesantes _distintos_." % calculate_distinct_and_interesting(text_b)
