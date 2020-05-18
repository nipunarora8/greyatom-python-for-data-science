# --------------
# Code starts here

# Create the lists 

class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
# Concatenate both the strings
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

# Append the list
new_class =[]
for i in class_1:
    new_class.append(i)
for j in class_2:
    new_class.append(j)


new_class.append('Peter Warden')

# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary

courses = {
    'Math':65,
    'English':70,
    'History':80,
    'French':70,
    'Science':60
}

print(courses)

# Slice the dict and stores  the all subjects marks in variable


# Store the all the subject in one variable `Total`
total=sum(courses.values())
# Print the total

print(total)
# Insert percentage formula
percentage=total/5
# Print the percentage
print(percentage)



# Create the Dictionary
 
mathematics = {'Geoffrey Hinton':78,
            'Andrew Ng':95,
            'Sebastian Raschka':65,
            'Yoshua Benjio':50,
            'Hilary Mason':	70,
            'Corinna Cortes':66,
            'Peter Warden': 75
}

topper  = max(mathematics,key = mathematics.get)
print(topper)

# Given string
first_name,last_name=topper.split(' ')

full_name = last_name+ " " + first_name

# Create variable first_name 

# Create variable Last_name and store last two element in the list

# Concatenate the string

# print the full_name
print(full_name)
# print the name in upper case
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


