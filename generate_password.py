""""
Generate password is a program where you will genarate random passwords for a secure account
we are not using random in this as it is said in the module that random should not be used for security
so we are introducing a new module call'd the secrets
"""

import secrets

def generate_passwords(num_words):
    with open('All_words_Passwords.txt', 'r') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range (num_words)]
    pass_word = ' '.join(words)
    print(pass_word)
    return ' '.join(words)


if __name__ == '__main__':
    generate_passwords(10)
