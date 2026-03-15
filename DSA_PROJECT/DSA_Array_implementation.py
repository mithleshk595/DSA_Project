binary_tree_array = [1, 2, 3, 4, 5, 6, 7]

def left_child(index):
    return 2 * index + 1

def right_child(index):
    return 2 * index + 2

def get_data(index):
    if 0 <= index < len(binary_tree_array):
        return binary_tree_array[index]
    else:
        return None
    
    print("Binary Tree represented as an array:")
    for i in range(len(binary_tree_array)):
        print(get_data(i), end= '')

    



