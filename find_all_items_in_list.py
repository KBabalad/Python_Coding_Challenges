"""
In this program we are going to search the list items, if we find the item we are searching is found we will return
the indices of where the item was found and the list it was found(as in python we can store a list inside a list- multidimensional list)
"""

def search_all_items(search_list, item):
    indices = list() # create an empty list where we store the indices of the search item
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i],list):
            for index in search_all_items(search_list[i], item):
                indices.append([i] + index)
    print(indices)


if __name__ == '__main__':
    usr_input_0 = input("Input the list of items \n")
    usr_input_1 = input("Item you want to search in a list \n")
    usr_input_0 = (usr_input_0)
    print(f":Searching list {usr_input_0}")
    print(f"searching element in list {usr_input_1}")
    search_all_items(usr_input_0, usr_input_1)


