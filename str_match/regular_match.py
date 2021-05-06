def match(s, w):
    s_str = list(s)
    w_str = list(w)

    si = 0
    wi = 0
    delta = 0
    while si + delta < len(s_str):
        if wi < len(w_str):
            if s_str[si + delta] == w_str[wi]:
                wi += 1
                if wi == len(w_str):
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

match('ababababca', 'ca')
match('ababababca', 'bc')
match("ababcd", "abcd")
match("ababcd", "cc")
match("ababababcd", "ababc")
match("There is a dog on the ground.", "ground")