#!/usr/local/bin/python3
#testing out python
print("Python is fun!")

#using variables
message = "Python is fun!"
print(message)

#using the title method
name = "suzy strickler"
print(name.title())

#using variables in strings
first_name = "suzy"
last_name = "strickler"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"My name is, {full_name.title()}!")

#Manipulating Lists
states = ['New York', 'Pennsylvania', 'Hawaii']
print(states)
print(states[0]) #access an element in a list
states[0] = 'Texas'  #change a list element
print(states)
states.insert(0, 'Montana') #insert an element
print(states)
popped_states = states.pop(1) #remove an element
print(popped_states)
print(states)

#Loops
states = ['New York', 'Pennsylvania', 'Hawaii']
for state in states:
    print(state)
    print("All states in list printed")

#Loops - if statements
states = ['New York', 'Pennsylvania', 'Hawaii']
for state in states:
    if state == 'Hawaii':
        print(state.upper())
    elif state == 'Montana':
        print(state.lower())
    else: print(state.title())

#Dictionaries
plants = {'color': 'blue', 'height': 10}
print(plants['color'])
plants['sepal'] = 3  #add a new key-value pair
print(plants)
del plants['color']  #remove a key-value pair
print(plants)

#example of a function
def weather():
    """Find out the weather"""
    answer = input("How is the weather?")
    print(answer)
weather()

#reading in a file
fasta_file = open("/home/bioinfo/Data/sample1.fasta", "r")
if fasta_file.mode == "r":
    contents = fasta_file.read()
    outF = open("/home/bioinfo/Data/test_out.fasta", "w")
    outF.write(contents)
fasta_file.close()
outF.close()
