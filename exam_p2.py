def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('babynames/yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    list_of_name_details = []
    with open(file_name) as f:
        for line in f:
            list_of_name_details.append(line.strip().split(','))
    
    return list_of_name_details

def total_births(year):
    """
    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    proper_file = 'babynames/yob'+str(year)+'.txt'
    proper_details = process_file(proper_file)
    births = 0

    for i in proper_details:
        births += int(i[2])

    return births

def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a float number, the proportion of babies with the given name and given gender to total births in given year
    """
    proper_file = 'babynames/yob'+str(year)+'.txt'
    proper_details = process_file(proper_file)
    total_babies = total_births(year)
    babies_with_name = 0

    for i in proper_details:
        if i[0] == name.capitalize() and i[1] == gender:
            babies_with_name = i[2]

    return int(babies_with_name)/total_babies

def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the
    proportions of the same name with same gender in all years)
    """
    years = range(1880, 2011)
    year_with_highest_proportion = 0

    for year in years:
        year_proportion = proportion(name, gender, year)
        if year_proportion > year_with_highest_proportion:
            highest_year = year
            year_with_highest_proportion = year_proportion

    return highest_year


def main():
    print("Let's find out which year my name had the highest proportion among all names with the same gender")
    my_name = input('My name is: ')
    my_gender = input("My gender is (M or F): ")
    
    print(f'The year in which my name, {my_name}, had the highest proportion among all names with the same gender, {my_gender}, in all years from 1880 to 2010:')
    print(highest_year(my_name, my_gender))
    input("Press enter to close program")

if __name__ == '__main__':
    main()
