

# # Sets##################################
# # Sets are unordered collections of unique elements
# # Sets are mutable
# # Sets are defined by curly braces {}
# #example of sets
# set1 = {1, 2, 3, 4, 5}  # set of integers
# set2 = {'apple', 'banana', 'cherry'}  # set of strings
# set3 = {1, 2, 3, 'apple', 'banana'}  # mixed set
# set4 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}  # duplicate elements are removed


# #access elements in a set
# print(1 in set1) # output:true
# print("apple" in set2) # output true


# # add elements to a set
# set1.add(6)
# print(set1) # Outputs: {1,2,3,4,5,6}
# set2.add("pineapple")
# print(set2)
# set3.add("cherry")
# print(set3)
# set4.add(7)
# print(set4)

# #remove elements from a set
# print(set1.remove(6)) # Outputs: {1,2,3,4,5}
# print(set1)  # Outputs: {1,2,3,4,5}

# #check if an element is in a set
# print(1 in set1) # outputs:true

# #find the length of a set
# print(len(set1)) # output:5

# #clear a set
# set1.clear() # output: set()
# print(set1)
# set2.clear() # output: set()
# print(set2)

# #tuples##################################
# # Tuples are ordered collections of elements
# # Tuples are immutable
# # Tuples are defined by parentheses ()
# #example of tuples
# tuple1 = (1, 2, 3, 4, 5)  # tuple of integers
# tuple2 = ('apple', 'banana', 'cherry')  # tuple of strings
# tuple3 = (1, 2, 3, 'apple', 'banana')  # mixed tuple
# tuple4 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)  # duplicate elements are allowed


# #access elements in a tuple
# print(tuple1[0]) # Output: 1
# print(tuple2[1]) # Output: "banana"
# print(tuple3[3]) # Output: "apple"

# #find the length of a tuple
# print(len(tuple1)) # Output: 5
# print(len(tuple2)) # Output: 3

# #count the number of occurrences of an element in a tuple
# print(tuple4.count(1)) # Output: 2
# print(tuple4.count(6)) # Output: 0
# print(tuple3.count("apple")) # Output: 1

# #find the index of an element in a tuple
# print(tuple1.index(3)) # Output: 2
# print(tuple2.index("cherry")) # Output:2
# print(tuple3.index("banana")) # Output:4

# #convert a tuple to a list
# print(list(tuple1)) # Output: [1,2,3,4,5])

# #convert a list to a tuple
# print(tuple(list(tuple1))) # Output: (1,2,3,4,5)







#######################tuples challenge#####################
# Challenge: Count the number of occurrences of the character 'v' in the text below.
# The text is converted to a tuple of characters and the target characters are 'v' and 'V'.
# The result is output to the console.
#queue the videos(2)
text = """Voilà! In view, a humble vaudevillian veteran, cast vicariously as both victim and villain by the vicissitudes of Fate.
This visage, no mere veneer of vanity, is a vestige of the vox populi, now vacant, vanished. However, this valorous visitation
of a by-gone vexation stands vivified, and has vowed to vanquish these venal and virulent vermin vanguarding vice and
vouchsafing the violently vicious and voracious violation of volition.


The only verdict is vengeance; a vendetta, held as a votive, not in vain, for the value and veracity of such shall one day
vindicate the vigilant and the virtuous.


Verily, this vichyssoise of verbiage veers most verbose, so let me simply add that it is my very good honor to meet you
and you may call me V."""


# Convert the text to a tuple of characters
text_tuple = tuple(text)
print(text_tuple)

# Tuple to store the target characters
small_v = text_tuple.count("v")
capital_v = text_tuple.count("V")

# Count occurrences of 'v' or 'V' by filtering the text_tuple
total_v = small_v + capital_v



# Output the rprint result




# dictionarys Accessing a Value from a Nested List###############################
#Suppose we have a dictionary containing multiple lists as values, and you want to access a specific element from one of these lists.
# Define the dictionary


sample_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #list inside a list
# get length of the list
print(len(sample_list)) # Output: 3
print(sample_list[2][2]) # Output: 9
print(sample_list[1][-1]) # Output: 6
print(sample_list[0][-3]) # Output: 3
print(sample_list[1][0]) # Output: 1
print(sample_list[2][1]) # Output: 8
# 8 is the third element in the second list
#this is called a nested list
# Extract and print the second element from the first list


sample_list_of_fruit = {"fruits": ["apple", "banana", "cherry"]}
# Extract and print the second fruit from the list
print(sample_list_of_fruit["fruits"][1]) # Output: "banana"
print(sample_list_of_fruit["fruits"][2]) # Output: "cherry"


sample_list_of_lists = {"lists": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}
# Extract and print the third element from the second list

print(sample_list_of_lists['lists'][1][2]) # Output: 6
print(sample_list_of_lists['lists'][0][1]) # Output: 3
print(sample_list_of_lists['lists'][2][2]) # Output: 9

sample_list_of_dicts = {"dicts": [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}]}
# Extract and print the age of the second person






data = {
    "fruits": {"tropical": ["mango", "pineapple", "banana"], "berries": ["strawberry", "blueberry", "raspberry"]},
    "prices": {"mango": 1.5, "pineapple": 2.5, "banana": 0.5}
}


# Extract and print the second item from the 'tropical' list
print(data["fruits"]["tropical"][1])  # Output: 'pineapple'




# Define the dictionary
info = {
    "team": {"coach": {"name": "John Doe", "age": 45}, "players": ["Alice", "Bob", "Charlie"]},
    "location": "New York"
}


# Extract and print the coach's name
print(info["team"]["coach"]["name"])  # Output: 'John Doe'




# Define the dictionary
company = {
    "departments": {
        "HR": {
            "employees": ["Emma", "Oliver", "Sophia"],
            "budget": 50000
        },
        "Engineering": {
            "employees": ["Liam", "Noah", "Ethan"],
            "budget": 120000
        }
    }
}


# Extract and print the second employee from the 'Engineering' department
print(company["departments"]["Engineering"]["employees"][1])  # Output: 'Noah'


# Define the dictionary
school = {
    "class": {
        "name": "Math 101",
        "students": {"student1": "A", "student2": "B", "student3": "C"}
    }
}


# Update the grade of student2
school["class"]["students"]["student2"] = "A+"


# Print the updated dictionary
print(school)


# Define the dictionary
product_inventory = {
    "warehouse1": {
        "products": ["apples", "oranges", "bananas"],
        "quantities": [50, 30, 20]
    },
    "warehouse2": {
        "products": ["grapes", "pears", "peaches"],
        "quantities": [60, 40, 30]
    }
}


# Find the total number of oranges in warehouse1
orange_quantity = product_inventory["warehouse1"]["quantities"][1]
print(f"Total oranges in warehouse1: {orange_quantity}")  # Output: 30




# Define the dictionary
cities = {
    "USA": {
        "New York": {"population": 8000000, "mayor": "John"},
        "Los Angeles": {"population": 4000000, "mayor": "Mike"}
    },
    "Canada": {
        "Toronto": {"population": 2700000, "mayor": "Jane"},
        "Vancouver": {"population": 630000, "mayor": "Emily"}
    }
}


# Extract and print the population of Los Angeles
la_population = cities["USA"]["Los Angeles"]["population"]
print(f"Population of Los Angeles: {la_population}")  # Output: 4000000





