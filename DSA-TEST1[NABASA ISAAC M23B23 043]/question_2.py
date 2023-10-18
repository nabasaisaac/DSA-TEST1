"""Task 1"""

catholic_martyrs = ['Achileo Kiwanuka', 'Adolphus Ludig Mukasa', 'Ambrosius', 'Kibuuka', 'Anatoli',
                    'Kiriggwajjo', 'Andrew Kaggwa', 'Antanansio', 'Bazzekuketta', 'Bruno', 'Sserunkuuma',
                    'Charles Lwanga', 'Denis', 'Ssebuggwawo', 'Wasswa', 'Gonzaga Gonza', 'Gyavira Musoke',
                    'Yowana Mukiibi', 'Yusufu Lugalama', 'Zakayo Lubega', 'James', 'Buuzaabalyaawo',
                    'John Maria', 'Muzeeyi', 'Joseph Mukasa', 'Kizito', 'Lukka', 'Baanabakintu',
                    'Matiya Mulumba', 'Mbaga Tuzinde', 'Mugagga Lubowa', 'Mukasa', 'Kiriwawanvu',
                    'Nowa Mawaggali', 'Ponsiano', 'Ngondwe']

anglican_martyrs = ['Aaron Lubega', 'Apollo Kivebulaya', 'Eria Sebukyala', 'Fredrick Kizza', 'George Kizza',
                    'James Hannington', 'Janani Luwum', 'Joseph', 'Balikuddembe', 'Kizito', 'Mark Kakumba',
                    'Matia Mulumba', 'Nuhu Mbegu', 'Robert', 'Munyagayirwa', 'Samwiri Mukasa',
                    'Yefusa Namayanja', 'Yohana Mukasa', 'Yosefu Lugalama', 'Yowana Kitaka', 'Yowana Maria',
                    'Mukasa']

"""Task 2"""
print('These are the martyrs in the both groups of Catholic and Anglican')
for martyr in catholic_martyrs:  # looping through the names
    if martyr in anglican_martyrs:  # If the name is in list of anglican_martyrs, it will be deleted
        print(martyr)         # Identifying the duplicate names in both lists
        del martyr  # A line of code that deletes the that martyr in both groups


"""Task 3"""
def martyr_count(name):    # Defining the function with name argument
    if name in catholic_martyrs:
        return f'{name} belongs to group of Catholic'   # if the name is in catholic list, we shall return this statement
    elif name in anglican_martyrs:
        return f'{name} belongs to group of Anglican'   # if the name is in Anglican list, we shall return this statement
    else:
        return f'{name} does not belong to any group, please try again '


"""Task 4"""
"""By running the above code, Kizito is under a group of Catholic"""

# Asking a user to enter the name, this name will be changed to title form by .title(),
# since the names in the lists are in the title form
# .strip() will also help us remove unwanted extra spaces
name = input('Enter the name of the martyr to know his or her group: ').strip().title()
print(martyr_count(name))   # Calling and printing out what is in the function


"""Task 5"""
# A function that returns true if the name entered from the user is in both groups
def testing(name2):
    if name2 in catholic_martyrs and anglican_martyrs:
        return True
    else:
        return False


name2 = input('Enter the name to see whether it is in both groups: ')
print(testing(name2))  # Calling and printing the function






