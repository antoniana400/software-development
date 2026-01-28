def stringManipulationReverse(word):
    # must use slicing
    _ = word[::-1]
    return word


def StringManipulationUpperLowerLowered(word):
    # must use .upper() to build the clue; must use .lower() for the answer
    _ = word.upper()
    return word.lower()


def StringManipulationTitleCase(word):
    # must use .title()
    sentence = f"{word} is great"
    return sentence.title()


def StringManipulationSwapcase(text):
    # must use .swapcase()
    return text.swapcase()


def StringManipulationStrip(sample):
    # must use .strip()
    return sample.strip()


def StringManipulationLstrip(sample):
    # must use .lstrip('-')
    return sample.lstrip("-")


def StringManipulationCentre(text):
    # must use .center(width, fillchar)
    return text.center(20, "-")


def StringManipulationStartsEnds(word, pre, suf):
    # must use .startswith() and .endswith()
    start = "yes" if word.startswith(pre) else "no"
    end = "yes" if word.endswith(suf) else "no"
    return (start, end)


def StringManipulationFindIndex(s, sub):
    # must use .find() and .index()
    pos_find = s.find(sub)
    pos_index = s.index(sub)
    return (pos_find, pos_index)


def StringManipulationCount(word, ch):
    # must use .count(ch)
    return word.count(ch)


def StringManipulationSplitJoin(csv):
    # must use .split(',') and '-'.join(...)
    return "-".join(csv.split(","))


def StringManipulationSplitlinesJoin(poem):
    # must use .splitlines() and ';'.join(lines)
    return ";".join(poem.splitlines())


def StringManipulationZfill(n):
    # must use .zfill(5)
    return n.zfill(5)


def StringManipulationCharTests(s):
    # must call all seven tests in this order
    return (
        s.isalpha(),
        s.isdigit(),
        s.isalnum(),
        s.isspace(),
        s.islower(),
        s.isupper(),
        s.istitle()
    )
