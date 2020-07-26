#LICUN LIU --- 30901235 --- 1/6/2020 --- 5/6/2020

class Person:

    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.friend = []
        #create a list to store friend

    # Add a reference to another Person object.
    def add_friend(self, friend_person):
        self.friend.append(friend_person)

    # Return a string containing the person’s first and last name concatenated together
    def get_name(self):
        self.name = self.fname + ' ' + self.lname
        return self.name

    # Return person name
    def get_friends(self):
        return self.friend


def load_people():
    created_object = []       # create a List to store Person objects

    file = open("./a2_sample_set.txt", 'r')             # open file
    for line in file:                                   # read line from file one by one
        line = line.rstrip("\n").split(': ')            # Eliminating the '\n' ; spilt follow ': '
        name = line[0].split(" ")                       # split first name and last name
        created_object.append(Person(name[0],name[1]))  # store created object into the list
    file.close()                                        # close file

    i = - 1     # Create a counter

    file = open("./a2_sample_set.txt", 'r')     # open file
    for line in file:                           # read line from file one by one
        line = line.rstrip("\n").split(': ')    # Eliminating the '\n' ; spilt follow ': '
        friend = line[1].split(', ')            # split every friend name into a list
        i = i +1

        for name in friend:                     # Read every friend name in a line
            for person in created_object:       # Read every created Person object
                if person.get_name() == name:
                    created_object[i].add_friend(person)
                    # Use add_friend method, add each friend to that Person object

    file.close()                                # close file
    return created_object                       # return a list of all the Person objects that have been created

if __name__ == '__main__':
    created_object = load_people()

