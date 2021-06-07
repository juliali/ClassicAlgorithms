def greatest_common_divisor(a, b):
    if a < 0 or b < 0:
        print("Error: this function doesn't accept negative integer.")
        return -1

    if a == 0 or b == 0:
        return 0

    larger = a
    smaller = b

    if a < b:
        larger = b
        smaller = a

    residue = larger % smaller

    while residue != 0:
        larger = smaller
        smaller = residue

        residue = larger % smaller

    return smaller


print(greatest_common_divisor(10, 5))
print(greatest_common_divisor(115, 46))
print(greatest_common_divisor(18, 24))
