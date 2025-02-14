from collections import Counter
from collections import defaultdict #altra cosa utile

seq = ["aldo", "giovanni", "giacomo", "aldo"]
res = Counter(seq)

print(res)

def count(seq):
    """Count the elements in the given seq"""
    counter = {}
    for el in seq:
        if el in counter:
            counter[el] += 1
        else:
            counter[el] = 1
    return counter