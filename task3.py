# LICUN LIU --- 30901235 --- 1/6/2020 --- 5/6/2020

# Explain: The results match the predictions,
#           In scenario A, the curve increases very quickly. This is because meeting
#               possibility is high and zero patient HP is low
#           In scenario B, the curve increases slowly or decreases to zero.
#               This is because meeting possibility is low and zero patient HP is 49,
#               which means zero patient is likely to cure and do not have infectiousness.
#           In scenario C, the curve turns to zero.
#               This is because meeting probability is very low, and the viral is unlikely
#               to spread in this circumstance.

import matplotlib.pyplot as plt
from a2_30901235_task2 import *


def visual_curve(days, meeting_probability, patient_zero_health):

    result = run_simulation(days, meeting_probability, patient_zero_health)
    # Calling the run_simulation function
    print(result)

    plt.plot(result)
    plt.xlabel('Days')
    plt.ylabel('Count')
    plt.show()
    # Using functionality from matplotlib, plot a curve

if __name__ == '__main__':

    days = int(input("Please input the number of days to run the simulation (Positive integer):"))
    meeting_probability = float(input("Please input the meeting_probability (Between 0 and 1):"))
    patient_zero_health = float(input("Please input the health of Patient Zero (Between 0 and 100):"))
    # Prompting the user for these values

    test_result = visual_curve(days, meeting_probability, patient_zero_health)
