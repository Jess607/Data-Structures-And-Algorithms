#Here, we try to find the needle string in haystack and return its index, if we can't find needle in haystack we return -1
def index_of_first_occurrence_in_string(haystack, needle):
    if needle in haystack:
            return haystack.index(needle)
    return -1