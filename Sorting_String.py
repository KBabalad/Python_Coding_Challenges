# in this challenge we are going to sort the words according to alphatical occurance
# input: String of words separated by spaces
# output of words string back sorted alphabetically

def string_sort(input_string):
    words = input_string.split()# splitting the senstence into different words using space and make them as a items of list
    words = [w.lower() + w for w in words]  # making sure they are in lower case for each of there replica
    words.sort()
    words = [w[len(w)//2:] for w in words] # floor division with no fraction and do it in a loop of words in the list
    print(' '.join(words))

if __name__ == '__main__':
    user_input = input("Enter the string with spaces \n")
    user_input = str(user_input)
    string_sort(user_input)


