# import algorithms as al
#
# #Task1
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
# result = al.get_unnamed_partitions(4, alphabet)
# al.write_to_file(result, 'answer1.txt')
# print(len(result))
#
# #Task2
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
# result = list(al.get_named_partitions(4, alphabet))
# al.write_to_file(result, 'answer2.txt')
# print(len(result))
#
# #Task3
# alphabet = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
# result = list(al.get_unnamed_partitions_with_one_element(4, 9, 'a'))
# al.write_to_file(result, 'answer3.txt')
# print(len(result))
#
# #Task4
# alphabet = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
# result = list(al.get_named_partitions_with_one_element(4, 9, 'a'))
# al.write_to_file(result, 'answer4.txt')
# print(len(result))
#
# #Task5
# alphabet = [str(n) for n in range(1, 10)]
# result = list(al.get_all_cycles(set_count=3, alphabet=alphabet))
# al.write_to_file(result, 'answer5.txt')
# print(len(result))
#
# #Task6
# print(al.number_of_connected_labeled_graphs(7))
#
# #Task7
# print(al.number_of_labeled_eulerian_graphs(7))
#
# #Task8
# print(al.number_of_labeled_graphs_with_colors(7, 3))
#
# # Task9
# print(al.number_of_labeled_eulerian_graphs_with_vertex(7, 11))