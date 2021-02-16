"""
Saving a dictionary type in python is important because the dictionary is saved to a memory and vanishes later as
soon as the program is exceuted and closed. What if you need the dictionary later? In that case you should save the
dictionary to a file path and retrive it later when you need the dictionary and wanna use the dictionary.
"""

import pickle

def save_dict_to_file(dict_var, file_path):
    with open(file_path,'wb') as file:
        pickle.dump(dict_var,file)
    print("loading dictionary to file success")

def load_from_dict(file_path):
    with open(file_path, 'rb') as file:
        print(pickle.load(file))
    print("retriving dictionary success")

if __name__ == '__main__':
    dict_var = {1: "Lion", 2: "Lepord", 3 : "Cheetah", 4: "Cat" }
    file = ('test_dict.pickle')
    save_dict_to_file(dict_var,file)
    recovered = load_from_dict(file)
    print(recovered)

