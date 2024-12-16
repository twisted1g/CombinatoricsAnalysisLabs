from collections import Counter


def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    index = list(range(r))

    yield tuple(pool[i] for i in index)
    while True:
        for i in reversed(range(r)):
            if index[i] != i + n - r:
                break
        else:
            return
        index[i] += 1
        for j in range(i+1, r):
            index[j] = index[j-1] + 1
        yield tuple(pool[i] for i in index)


def product(iterables, repeat):
    pools = [tuple(pool) for pool in iterables] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]

    for prod in result:
        yield tuple(prod)


def permute_unique(counter, path, length, file):
    if len(path) == length:
        file.write("".join(path) + "\n")
        return

    for char in counter:
        if counter[char] > 0:
            counter[char] -= 1
            permute_unique(counter, path + [char], length, file)
            counter[char] += 1


def generate_permutations(word, output_file):
    counter = Counter(word)
    length = len(word)

    with open(output_file, "w", encoding="utf-8") as file:
        permute_unique(counter, [], length, file)