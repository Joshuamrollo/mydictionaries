def main(): 
    file_name = input('enter text file name: ')
    word_dict = {}

    file = open(file_name, mode="r")
    
    text = file.read().split()

    for word in text:
        if word not in word_dict:
            word_dict[word] = 0
        else:
            word_dict[word] += 1

    file.close()

    for key, value in word_dict.items():
        print(key + ": " + str(value))


main()