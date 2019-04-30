# hw3pr2.py
# Andrew Marks


def encipher(S, n):
    """
    takes a String S, rotates each letter by n spaces and returns the new rotated String
    :param S: string
    :param n: int, number of places to rotate
    :return: new String of rotated letters
    """
    new = ''
    for i in S:
        c = rot(i, n)
        new = new + c
    return new


def rot(c, n):
    """
    takes a character sees if it is a letter and rotates it
    :param c: char, single letter
    :param n: int, number of places to rotate c
    :return: char, that has been rotated n places
    """
    if 'a' <= c <= 'z':
        l = ord(c) + n
        if l > ord('z'):
            l -= 26
        return chr(l)
    elif 'A' <= c <= 'Z':
        l = ord(c) + n
        if l > ord('Z'):
            l -= 26
        return chr(l)
    else:
        return c


assert encipher('xyza', 1) == 'yzab'
assert encipher('Z A', 1) == 'A B'
assert encipher('*ab?', 1) == '*bc?'
assert encipher('This is a string!', 1) == 'Uijt jt b tusjoh!'
assert encipher('Caesar cipher? I prefer Caesar salad.', 25) == 'Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.'


def decipher(S):
    L = [encipher(S, n) for n in range(26)]
    score = 0
    LOL = []
    for i in L:
        for j in i:
            score += letProb(j)
        LOL = LOL + [score]

    high_score = max(LOL)
    for i in range(len(LOL)):
        print(L[i], LOL[i])
        if LOL[i] == high_score:
            return L[i]
    return LOL


# table of probabilities for each letter...
def letProb(c):
    """If c is the space character or an alphabetic character,
       we return its monogram probability (for english),
       otherwise we return 1.0.  We ignore capitalization.
       Adapted from
       http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0


code = encipher("Hello World", 4)
print(decipher(code))
print('------------------------------------------------------------')
print(decipher('Onyx balks'))


def blsort(L):
    c = 0
    LC = []
    for i in L:
        if i == 0:
            c += 1
    for i in range(len(L)):
        if c > i:
            LC += [0]
        else:
            LC += [1]
    return LC


def gensort(L):
    LC = []
    for i in range(len(L)):
        LC.append(min(L))
        L.remove(LC[i])
    return LC


def jscore (S, T):
    c = 0
    match = [False] * len(T)
    for ch in S:
        for i in range(len(T)):
            if ch == T[i] and match[i] is False:
                match[i] = True
                c += 1
                break
    return c
