def match(s, w):
    if not s or not w:
        print("Input is invalid!")
        return -1

    n = len(s)
    m = len(w)

    if m > n:
        print("The word cannot be longer than the s str.")
        return -1

    si = 0
    wi = 0
    delta = 0
    while si + delta < n:
        if wi < m:
            if s[si + delta] == w[wi]:
                wi += 1
                if wi == m:
                    print(s, w, "matched at:", si)
                    return si
                else:
                    delta += 1
            else:
                si += 1
                wi = 0
                delta = 0

    print(s, w, "no match")
    return -1


match('aaa', 'aaaaa')
match('aaa', '')
match('', 'a')
match('ababababca', 'ca')
match('ababababca', 'bc')
match("ababcd", "abcd")
match("ababcd", "cc")
match("ababababcd", "ababc")
match("There is a dog on the ground.", "ground")