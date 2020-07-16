"""Get every other group of 2 numbers, if even"""
import random
NUM = 100


def get_two_group(the_list):
    new_list = []
    next_list = []
    final_list = []
    a_list = []
    the_group = []

    for i in range(0, len(the_list), 2):
        new_list.append(i)

    for j in range(1, len(the_list), 2):
        next_list.append(j)

    # print(new_list)
    # print(next_list)

    for i, j in zip(new_list, next_list):
        final_list.append([i, j])

    # print(final_list)

    for i in range(0, len(final_list), 2):
        a_list.append(final_list[i])

    # print(a_list)

    for i in range(len(a_list)):
        for j in range(2):
            the_group.append(a_list[i][j])

    return the_group


print(get_two_group([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Set some random length list.
print(get_two_group(random.sample(range(NUM), NUM)))

