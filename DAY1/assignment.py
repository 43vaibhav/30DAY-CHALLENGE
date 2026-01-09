year= int(input("what year were you born?"))
# adding int() converts the strings form str to int
age = 2026 - year
print(age)# this gives an error because in python everything we take as input in terminal is read as a string so first we need to convert it into int cos we can perform operations on different data structures or types


pounds = float(input("how much do you weigh?"))
weight = pounds * 0.454
print("holy shit!! you are ", weight, " kgs")# using comms instead of + is very useful cos here python automatically converts different data types
