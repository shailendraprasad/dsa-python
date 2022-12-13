string_to_reverse = "prasad"


def string_reverse_iterative(S):
    s = list(S)
    start, stop = 0, len(s)
    while start <= stop - 1:
        s[start], s[stop - 1] = s[stop - 1], s[start]
        start, stop = start + 1, stop - 1
    return "".join(s)


print(string_reverse_iterative(string_to_reverse))
