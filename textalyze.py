import sys
import re

def item_counts(items):
    counts = {}

    for item in items:
        if item not in counts:
            counts[item] = 0

        counts[item] += 1

    return counts

def sanitize(string):
    return re.sub(r'[^a-zA-Z]+', '', string).lower()

def counts_to_frequency(counts):
    total = sum(counts.values())

    return {item: count / total for (item, count) in counts.items()}

def read_file(filename):
    with open(filename) as f:
        return f.read()

if len(sys.argv) < 2:
    sys.exit('Please supply a filename to parse.')
else:
    filename = sys.argv[1]

print(counts_to_frequency(item_counts(sanitize(read_file(filename)))))
# print(item_counts([1,2,1,2,1]) == {1: 3, 2: 2})
# print(item_counts(['a','b','a','b','a','ZZZ']) == {'a': 3, 'b': 2, 'ZZZ': 1})
# print(item_counts([]) == {})
# print(item_counts(['hi', 'hi', 'hi']) == {'hi': 3})
# print(item_counts([True, None, 'dinosaur']) == {True: 1, None: 1, 'dinosaur': 1})
# print(item_counts(['a','a','A','A']) == {'a': 2, 'A': 2})
