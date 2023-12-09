# Day 9 Part I of advent of code calendar

result = 0


def reduce_suite(suite):
    it = iter(suite)
    it2 = iter(suite[1:])
    for elem in it:
        try:
            yield next(it2) - elem
        except StopIteration:
            return


def all_equal(suite):
    it = iter(suite)
    first = next(it)
    return all(first == x for x in it)

with open("9/input.txt", "r") as file:
    suites = [[int(n) for n in line.split()] for line in file]

for suite in suites:
    decompositions = [suite]
    reduced = list(reduce_suite(suite))
    decompositions.append(reduced)
    
    while not all_equal(reduced):
        reduced = list(reduce_suite(reduced))
        decompositions.append(reduced)
    
    decompositions.reverse()
    prediction = 0
    for s in decompositions:
        prediction += s[-1]
    
    result += prediction

print(result)
    
