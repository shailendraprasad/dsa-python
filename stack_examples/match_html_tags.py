from ds.arraystack import ArrayStack


def is_html_matched(raw):
    S = ArrayStack()
    j = raw.find('<')

    while j != -1:
        k = raw.find('>', j + 1)
        if k == -1:
            return False
        tag = raw[j + 1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False  # mismatched delimiter
        j = raw.find('<', k + 1)  # find next ’<’ character (if any)
    return S.is_empty()


print(is_html_matched("<sample>help</sample><b></b>"))
