# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input().rstrip())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here
length_of_circular_linked_list = int(input())
# print()
circular_linked_list = list(map(int, input().strip().split(" ")))
d = {}
j = 0
for i in range(length_of_circular_linked_list):
    if circular_linked_list[i] not in d.keys():
        d[circular_linked_list[i]] = 1
        circular_linked_list[j] = circular_linked_list[i]
        j = j + 1
print(j)
for i in range(j):
    print(circular_linked_list[i], end=" ")
