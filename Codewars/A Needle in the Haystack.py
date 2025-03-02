def find_needle(haystack):
    for i, item in enumerate(haystack):
        if item == "needle":
            return i
