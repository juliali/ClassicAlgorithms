def calculate_pm_value(str):
    str_len = str.__len__()
    prefix_set = set()
    suffix_set = set()
    for tmp_len in range(1, str_len):
        prefix_set.add(str[0:tmp_len])
        suffix_set.add(str[tmp_len:str_len])

    value = 0
    for prefix in prefix_set:
        if suffix_set.__contains__(prefix) and prefix.__len__() > value:
            value = prefix.__len__()

    return value


def generate_pmt(w):
    if not w:
        return None

    m = w.__len__()

    pmt = [list(w), list(range(m)), list(range(m))]

    for index in range(0, m):
        tmp_str = w[0:index + 1]
        value = calculate_pm_value(tmp_str)
        pmt[1][index] = index
        pmt[2][index] = value

    return pmt


def kmp_match(s, w, pmt):

    if pmt is None:
        print("The word is empty. No PMT generated!")
        return -1

    if not s:
        print("Input s str is invalid!")
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
                if delta == 0:
                    si += 1
                else:
                    value = pmt[2][wi - 1]
                    si = si + delta - value
                    delta = 0
                    wi = 0

    print(s, w, "no match")
    return


def do_match(s, w):
    pmt = generate_pmt(w)
    kmp_match(s, w, pmt)
    return


do_match('aaa', 'aaaaa')
do_match('aaa', '')
do_match('', 'a')
do_match("ababababcdcdcd", "abababc")
do_match('ababababcdcdcd', "cd")
do_match('ababababcdcdcd', "bc")
do_match("ababcd", "cc")
do_match("There is a dog on the ground.", "ground")
