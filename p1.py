

##Question 1 
def get_roster(roster = open('roster.txt')):
    name_list= []
    for line in roster: 
        name= line.strip()
        name_list.append(name.lower())
    return name_list



def get_alphabetvalue(name):
    name_value = 0
    for letter in name:
        value = ord(letter)-96 
        name_value+= value
    return name_value



def get_namevaluelist():
    name_list = get_roster(roster= open('roster.txt'))
    value_list ={}
    for name in name_list: 
        value_list[name]=get_alphabetvalue(name)
    return value_list



def get_most_valuable(): 
    value_list = get_namevaluelist()
    list =[]
    for key, value in value_list.items():
        list.append((value, key))
    list.sort()
    return list[-1]



#Question 2 
def get_positive_list():
    name_list = get_roster(roster= open('positive-words.txt'))
    value_list ={}
    for name in name_list: 
        value_list[name]=get_alphabetvalue(name)
    return value_list



def get_same_value_list():
    positive_list = get_positive_list()
    list = []
    for key, value in positive_list.items():
        if value == 68:
            list.append((key))
    return ', '.join(list)



def main():
    print(get_roster())
    print(get_alphabetvalue('bananas'))
    print(get_namevaluelist())
    print(get_most_valuable())
    # print(get_positive_list())
    # print(get_same_value_list())
    pass


if __name__ == '__main__':
    main()
