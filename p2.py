# A little bit of scaffolding if you want to use it

def process_file(file_name='yob1880.txt'):
    """
    Given a file name, returns a list of lists [name, gender, births]

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('babynames/yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    f = open(f'babynames/{file_name}')
    list=[]
    for line in f:
        a = line.strip()
        ind_list = a.split(",")
        list.append(ind_list)
    return list






def total_births(year):
    """
    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    list = process_file(file_name=f'yob{year}.txt')
    total_births = 0
    for person in list: 
        births = int(person[-1]) 
        total_births+=births
    return year, total_births






def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a float number, the proportion of babies with the given name and given gender to total births in given year
    """
    list = process_file(file_name=f'yob{year}.txt')
    total_births = 0
    specific_births = 0
    for person in list:
        births = int(person[-1])
        p_name = person[0]
        p_gender = person[1]
        total_births+=births
        if p_name == name and p_gender == gender:
            specific_births=births
    # percentage = f'{specific_births/total_births*100:.2f} %' 
    percentage = specific_births/total_births*100
    return percentage




def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the
    proportions of the same name with same gender in all years)
    """
    master =[]
    for year in range(1880, 2011):
        list = process_file(file_name=f'yob{year}.txt')
        for person in list:
            if person[0]==name and person[1]==gender:
                percentage = proportion(person[0], person[1], year)
                master.append((percentage, year))
    master.sort()
    return master[-1]





def main():
    # print(process_file(file_name='yob1880.txt'))
    # print(total_births(1880))
    # print(proportion('Mary','F',1880))
    # # print(highest_year('Mary', 'F'))


    pass  # delete this line and replace with your code here


if __name__ == '__main__':
    main()
