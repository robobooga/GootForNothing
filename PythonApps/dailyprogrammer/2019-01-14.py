#!/usr/bin/python3

# https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/

def balanced_bonus(txt):
    d = {}
    for c in txt:
        d[c] = d.get(c, 0) + 1

    if len(d.values()) > 0:
        expect = next(iter(d.values()))
        return all(val == expect for val in d.values())
    else:
        return True

print(balanced_bonus("xxxyyyzzz"))
print(balanced_bonus("abccbaabccba"))
print(balanced_bonus("xxxyyyzzzz"))
print(balanced_bonus("abcdefghijklmnopqrstuvwxyz"))
print(balanced_bonus("pqq"))
print(balanced_bonus("fdedfdeffeddefeeeefddf"))
print(balanced_bonus("www"))
print(balanced_bonus("x"))
print(balanced_bonus(""))
