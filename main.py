import combinatorial_algorithms as ca


def write_words_to_file(words, filename):
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + '\n')


def generate_words_task1(n, k, m):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k']
    valid_words = []
    for word_tuple in ca.product(alphabet, n):
        word = ''.join(word_tuple)

        if word.count('f') == k and word.count('c') == m:
            if word[-1] not in ['a', 'e'] and word[-2] not in ['a', 'e']:
                valid_words.append(word)

    return valid_words


def generate_words_task2(n, m):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k']
    valid_words = []

    for word_tuple in ca.product(alphabet, n):
        word = ''.join(word_tuple)

        count = sum(1 for letter in word if letter not in ['a', 'e'])
        if count <= m:
            valid_words.append(word)

    return valid_words


def generate_words_task3(n, m):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k']
    valid_words = []

    for alph in ca.combinations(alphabet, m):
        for word_tuple in ca.product(alph, n):
            word = ''.join(word_tuple)
            count = len({letter for letter in word})

            if count == m:
                valid_words.append(word)

    return valid_words


def find_solution_task4():
    solutions = []
    for x_1 in range(1, 8):
        for x_2 in range(1, 7):
            for x_3 in range(1, 6):
                for x_4 in range(1, 5):
                    for x_5 in range(1, 4):
                        if x_1 + x_2 + x_3 + x_4 + x_5 == 20:
                            solutions.append(f"{x_1} + {x_2} + {x_3} + {x_4} + {x_5}")
    return solutions


# #Task1
# answer = generate_words_task1(5, 2, 3)
# write_words_to_file(answer, 'answer.txt')

# #Task2
# answer = generate_words_task2(3, 2)
# write_words_to_file(answer, 'answer.txt')
#
# #Task3
# answer = generate_words_task3(8, 3)
# write_words_to_file(answer, 'answer.txt')

# #Task4
# answer = find_solution_task4()
# write_words_to_file(answer, 'answer.txt')
#
# #Task4
# ca.generate_permutations('БЕЗНАКАЗАННО', 'answer.txt')



