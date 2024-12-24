import math
from math import comb


def c(k, n):
    if k > n:
        return 0
    return math.factorial(n) / (math.factorial(n-k) * math.factorial(k))


def number_of_connected_labeled_graphs(n):
    if n == 1:
        return 1
    return 2**c(2, n) - sum(k * c(k,n) * 2**c(2, n-k) * number_of_connected_labeled_graphs(k)
                            for k in range(1, n))/n


def number_of_labeled_eulerian_graphs(n):
    if n == 1:
        return 1
    if n == 2:
        return 0
    return 2**c(2, n-1) - sum(k * c(k, n) * 2**c(2, n-k-1) * number_of_labeled_eulerian_graphs(k)
                              for k in range(1, n))/n


def number_of_labeled_graphs_with_colors(n, k):
    if k > n:
        return 0
    if k == 1:
        return 1
    return sum(c(m, n) * 2 ** (m*(n-m)) * number_of_labeled_graphs_with_colors(m, k-1)
               for m in range(1, n))/k


def write_to_file(iter_obj, filename):
    with open(filename, 'w') as file:
        for line in iter_obj:
            file.write(str(line) + '\n')


def get_unnamed_partitions(set_count, alphabet):
    def get_partitions(current=None, alphabet_subset=None):
        if alphabet_subset is None:
            alphabet_subset = list(alphabet)
        if current is None:
            current = []

        if len(alphabet_subset) == 0:
            if len(current) == set_count:
                yield current
            return

        element = alphabet_subset[0]
        if len(current) < set_count:
            for i in range(len(current) + 1):
                new_partition = [set(part) for part in current]

                if i < len(current):
                    new_partition[i].add(element)
                    yield from get_partitions(new_partition, alphabet_subset[1:])
                else:
                    new_partition.append({element})
                    yield from get_partitions(new_partition, alphabet_subset[1:])
        else:
            for i in range(len(current)):
                new_partition = [set(part) for part in current]
                new_partition[i].add(element)
                yield from get_partitions(new_partition, alphabet_subset[1:])

    return list(get_partitions(alphabet_subset=alphabet))


def get_named_partitions(set_count, alphabet):
    def swap(partitions, a, b):
        temp = partitions[a]
        partitions[a] = partitions[b]
        partitions[b] = temp

    for partitions in get_unnamed_partitions(set_count, alphabet):
        count_swap = [0] * set_count
        yield partitions

        i = 0
        while True:
            if i >= set_count:
                break
            if count_swap[i] < i:
                swap_index = 0 if i % 2 == 0 else count_swap[i]
                swap(partitions, swap_index, i)
                yield partitions

                count_swap[i] += 1
                i = 0
            else:
                count_swap[i] = 0
                i += 1


def get_unnamed_partitions_with_one_element(set_count, set_size, element):
    partition_sizes = [1] * (set_count - 1) + [set_size - (set_count - 1)]

    while partition_sizes[0] <= set_size // set_count:
        partition = []
        for set_index in range(set_count):
            partition.append([element] * partition_sizes[set_index])

        yield partition

        index = set_count - 2

        if index < 0:
            return

        partition_sizes[index] += 1
        partition_sizes[index + 1] -= 1

        while index > 0 and partition_sizes[index] > partition_sizes[set_count - 1]:
            index -= 1
            partition_sizes[index] += 1
            total_sum = 0
            for i in range(set_count - 1):
                if i > index:
                    partition_sizes[i] = partition_sizes[index]
                total_sum += partition_sizes[i]
            partition_sizes[set_count - 1] = set_size - total_sum


def get_named_partitions_with_one_element(set_count, set_size, element):
    partition_sizes = [1] * set_count

    while partition_sizes[0] <= set_size:
        index = set_count - 1
        if index < 0:
            return

        current_sum = sum(partition_sizes[:-1])

        if set_size - current_sum > 0:
            partition = list([element] * partition_sizes[set_index] for set_index in range(set_count))
            yield partition
            index -= 1

        while partition_sizes[index] > set_size or partition_sizes[index] < 1:
            partition_sizes[index] = 1
            index -= 1
        partition_sizes[index] += 1


def get_all_cycles(set_count, current=None, alphabet=None):
    if alphabet is None:
        alphabet = []
    if current is None:
        current = []

    if len(alphabet) == 0:
        if len(current) == set_count:
            yield current
        return
    element = alphabet[0]

    if len(current) < set_count:
        for i in range(len(current) + 1):
            new_partition = [list(subset) for subset in current]

            if i < len(current):
                count = len(new_partition[i])
                for j in range(count):
                    if element not in new_partition[i]:
                        new_partition[i].insert(j, element)
                    yield from get_all_cycles(set_count, new_partition, alphabet[1:])
            else:
                new_partition.append([element])
                yield from get_all_cycles(set_count, new_partition, alphabet[1:])

    else:
        for i in range(len(current)):
            new_partition = [list(subset) for subset in current]

            count = len(new_partition[i])
            for j in range(count):
                if element not in new_partition[i]:
                    new_partition[i].insert(j, element)

                yield from get_all_cycles(set_count, new_partition, alphabet[1:])


def number_of_labeled_eulerian_graphs_with_vertex(n, k):
    degrees = [(0, 0) for _ in range(n + 1)]

    max_degree = comb(n, 2)
    for i in range(n + 1):
        first = max_degree - (i * (n - i))
        second = i * (n - i)
        degrees[i] = (first, second)
    total_sum = 0
    index = 0
    for degree in degrees:
        ratio = 0
        for i in range(min(degree[0], degree[1], k) + 1):
            if i % 2 == 0:
                ratio += comb(degree[0], k - i) * comb(degree[1], i)
            else:
                ratio -= comb(degree[0], k - i) * comb(degree[1], i)
        total_sum += ratio * comb(n, index)
        index += 1
    return total_sum // (2 ** n)

