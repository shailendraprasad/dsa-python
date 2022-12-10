number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sum_binary(S, start, stop):
    if start >= stop:
        return 0

    if start == stop - 1:
        return S[start]

    else:
        mid = (start + stop) // 2
        return sum_binary(S, start, mid) + sum_binary(S, mid, stop)


print(sum_binary(number_array, 0, 9))
