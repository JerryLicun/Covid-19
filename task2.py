# LICUN LIU --- 30901235 --- 1/6/2020 --- 5/6/2020

from a2_30901235_task1 import *
import random

class Patient(Person):
    def __init__(self, first_name, last_name, health):
        self.fname = first_name
        self.lname = last_name
        self.health = health
        self.friend = []
        # create a list to store friend

    # Returns the patient's current health points
    def get_health(self):
        return self.health

    # Changes the patient's current health points
    def set_health(self, new_health):
        self.health = new_health
        return self.health

    # Returns a Boolean result about contagious
    def is_contagious(self):
        round(self.health)
        if self.health < 50:
            return True
        else:
            return False

    # This method infects the Patient object with a viral load.
    def infect(self, viral_load):
        if self.health >= 50:     # Health point > 50
            self.health = self.health - (2.0 * viral_load)
            if self.health > 0:
                pass
            else:
                self.health = 0
            return self.health

        if 29 < self.health < 50: # Health point between 29 and 50
            self.health = self.health - (1.0 * viral_load)
            if self.health > 0:
                pass
            else:
                self.health = 0
            return self.health

        if self.health <= 29:     # Health point < 29
            self.health = self.health - (0.1 * viral_load)
            if self.health > 0:
                pass
            else:
                self.health = 0
            return self.health
        if self.health < 0:
            self.health = 0
            return self.health

    # Recover some health points (one night’s sleep)
    def sleep(self):
        self.health = self.health + 5

    # Calculate the viral load
    def Viral(self):
        Lv = 5 + (pow((self.health - 25), 2) / 62)
        return Lv

# Return a list with the daily number of contagious cases
def run_simulation(days, meeting_probability, patient_zero_health):
    infect_num = []         # Create a List about infect number

    created_object = load_patients(75)                  # load person data
    created_object[0].set_health(patient_zero_health)   # patient zero health point

    for num in range(1, days + 1):      # Cycle every day
        for i in created_object:        # Cycle the created patient
            for j in i.get_friends():   # Cycle the patient's friend
                if random.random() < meeting_probability:  # if they are meeting

                    if round(i.get_health()) < 50 and round(j.get_health())<50:
                    # if i,j both unhealthy
                        i_viral_load = i.Viral()
                        j_viral_load = j.Viral()
                        j.infect(i_viral_load)
                        i.infect(j_viral_load)

                    if round(i.get_health()) < 50 and round(j.get_health()) >= 50:
                    # if i is unhealthy and j is healthy
                        i_viral_load = i.Viral()
                        j.infect(i_viral_load)

                    if round(i.get_health()) >= 50 and round(j.get_health()) < 50:
                    # if i is healthy and j is unhealthy
                        j_viral_load = j.Viral()
                        i.infect(j_viral_load)

        count = 0   # Create a counter
        for i in created_object:           # Cycle every person in the List
            if round(i.get_health()) < 50: # if contagious
                count += 1
        infect_num.append(count)
        # Store how many people are now contagious

        for i in created_object:           # Cycle every person in the List
            if i.get_health() < 95:
                i.sleep()
            else:
                i.set_health(100)
        # Sleep to recover some health

    return infect_num
    # Return a list with the daily number of contagious cases


# return a list of all the Patient objects that have been created
def load_patients(initial_health):
    created_object = []  # create a List to store Patient objects

    file = open("./a2_sample_set.txt", 'r')     # open file
    for line in file:                           # read line one by one
        line = line.rstrip("\n").split(': ')    # Eliminating the '\n' ; spilt follow ': '
        name = line[0].split(" ")               # split first name and last name
        created_object.append(Patient(name[0],name[1],initial_health))# store created object into the list
    file.close()                                # close file

    i = -1      # Create a counter

    file = open("./a2_sample_set.txt", 'r')     # open file
    for line in file:                           # read line one by one
        i = i +1
        line = line.rstrip("\n").split(': ')    # Eliminating the '\n' ; spilt follow ': '
        friend = line[1].split(', ')            # split every friend name

        for name in friend:                     # Read every friend name in a line
            for person in created_object:       # Read every created Patient object
                if person.get_name() == name:
                    created_object[i].add_friend(person)
                    # Use add_friend method, add each friend to that Patient object

    file.close()             # close file
    return created_object    # return a list of all the Patient objects that have been created


if __name__ == '__main__':

    test_result = run_simulation(40, 1, 1)
    print(test_result)

