def create_list_from_file(file_name):
    """
    file_name: name of a file
    Returns a list containing words taken from file_name
    """
    list_from_file = []
    with open(file_name) as f:
        for line in f:
            word = line.strip()
            list_from_file.append(word)

    return list_from_file

def value_of_letters():
    """
    Returns dictionary of each letter of alphabet and its corresponding value
    """
    letter_values = dict()
    values = 0
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        values += 1
        letter_values[letter] = values

    return letter_values

def value_of_name(name):
    """
    name: str representing the name of a student
    Returns an int which represents the value of the name
    """
    name_value = 0
    letter_values = value_of_letters()
    for letter in name.lower():
        if letter in letter_values:
            name_value += letter_values[letter]

    return name_value

def rank_class_roster(class_roster):
    """
    class_roster: list of names, in this case representing the class roster list
    Returns a dictionary that ranks the list by most valuable name
    """
    rank_class_roster_dict = dict()
    for name in class_roster:
        rank_class_roster_dict[name] = value_of_name(name)

    return sorted(rank_class_roster_dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)

def get_most_valuable_name(class_roster):
    """
    class_roster: list of names, in this case representing the class roster list
    Returns most valuable name from the list
    """
    most_valuable_name = rank_class_roster(class_roster)[0]
    return f'The most valuable name in our class is {most_valuable_name[0]} and his/her name has a value of {most_valuable_name[-1]}'

def find_positive_words_same_value(name, positive_words_list):
    """
    name: str representing the name of a student, in this case my name (Arteen)
    positive_words_list: list of positive words
    Returns a list of positive words with the same value as my name
    """
    positive_words_same_value = []
    my_value = value_of_name(name)
    for word in positive_words_list:
        if value_of_name(word) == my_value:
            positive_words_same_value.append(word)

    return None if len(positive_words_same_value) == 0 else positive_words_same_value


def main():
    print("We define the value of a name as the total value of all the letters of the first name where 'a' is 1, 'b' is 2, ... 'z' is 26")
    my_name = input('My name is: ')
    my_value = value_of_name(my_name)
    print(f'My name has a value of {my_value}.')
    class_roster = create_list_from_file('roster.txt')
    positive_words_list = create_list_from_file('positive-words.txt')
    
    # print(get_most_valuable_name(class_roster))
    print(f'These are the positive words that have the same value as my name, {my_name} ({my_value}): ')
    print(find_positive_words_same_value(my_name, positive_words_list))
    input("Press enter to close program")


if __name__ == '__main__':
    main()
