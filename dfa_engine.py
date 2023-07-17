from dfa_check import *
from pathlib import Path
import sys


def checkString(createdDFA, string):
    response = "accept"
    state = createdDFA['start']

    string_finish = 0
    for i in range(0, len(string)):
        letter_exists = 0
        for j in range(0, int(len(createdDFA[state]))):

            if string[i] == createdDFA[state][j]:

                state = createdDFA[state][j+1]
                letter_exists = 1
                break

        if letter_exists == 0:
            response = "reject"
            break

    for finish_state in createdDFA["finish"]:
        if finish_state == state:
            string_finish = 1

    if string_finish == 0:
        response = "reject"

    return response


def createDFA(directory):

    DFA = {
        "sigma": [],
        "states": [],
        "transitions": []
    }

    readFile(DFA, directory)

    createdDFA = {}
    createdDFA["finish"] = []
    for j in range(0, int(len(DFA['states']))):

        if DFA['states'][j] == "S":
            createdDFA["start"] = DFA['states'][j-1]

        if DFA['states'][j] == "F":
            createdDFA["finish"].append(DFA['states'][j-1])

    i = 0

    for transition in range(0, int(len(DFA['transitions'])/3)):

        createdDFA[DFA["transitions"][i]] = []

        i += 3

    i = 0
    for transition in range(0, int(len(DFA['transitions'])/3)):
        createdDFA[DFA["transitions"][i]].append(DFA["transitions"][i+1])
        createdDFA[DFA["transitions"][i]].append(DFA["transitions"][i+2])
        i += 3
    return createdDFA


nr_arguments = len(sys.argv)

if nr_arguments != 3:
    print("Number of arguments are invalid")
    sys.exit(2)

directory = Path(__file__).with_name(sys.argv[1])
directory = directory.absolute()
createdDFA = {}

if validate(directory) is False:
    print("The dfa configuration file is invalid!")
else:
    createdDFA = createDFA(directory)
    print(checkString(createdDFA, sys.argv[2]))
