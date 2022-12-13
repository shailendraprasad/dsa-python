from ds.arraystack import ArrayStack


def match_braces(expression):
    lefty = '{[('
    righty = '}])'

    S = ArrayStack()
    for c in expression:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False

            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


print(match_braces('{mycode[paintbox] {further down}'))
