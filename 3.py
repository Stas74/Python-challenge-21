# Challenge
# We need to find Dot an empty seat on the plane. We have logged the layout of the section of the plane as a Python list. This is formatted as a nested list, which means that elements of the list are lists as well. Listception.

# Note: Our plane section contains three sections of seats in each row, and three seats in each section. Here is what the values in the layout mean:

# e = empty seat
# o = occupied seat
# None = aisle (you can't sit here!)
# Capital letters = window seats

# layout = [
#     ["O","e","e",None, "e","o","e",None, "o","o","E"], # row 1
#     ["O","o","e",None, "e","o","e",None, "e","o","E"], # row 2
#     ["O","o","o",None, "o","o","e",None, "o","e","O"], # row 3
#     ["E","o","e",None, "e","o","e",None, "o","e","E"], # row 4 
#     ["E","e","o",None, "e","e","e",None, "o","o","E"], # row 5
#     ["O","e","e",None, "e","e","e",None, "e","e","E"]  # row 6
# ]

# Dot has two conditions for their sitting:

# It has to be window seat
# The next seat needs to be empty

# Identify the right place for Dot to sit. If there is more than one option that matches the conditions above, choose the seat that is closer to the front, i.e. has a lower row number. What is the list index of Dot's seat?

# Stretch Question
# Use python's pop() and insert() list functions to change Dot's seat from E to O.

# Stretch Questions are not required to be completed to finish the challenge but are recommended to further develop your skills.

# new_layout = ...


# SOLUTION
layout = [
    ["O","e","e",None, "e","o","e",None, "o","o","E"], # row 1
    ["O","o","e",None, "e","o","e",None, "e","o","E"], # row 2
    ["O","o","o",None, "o","o","e",None, "o","e","O"], # row 3
    ["E","o","e",None, "e","o","e",None, "o","e","E"], # row 4 
    ["E","e","o",None, "e","e","e",None, "o","o","E"], # row 5
    ["O","e","e",None, "e","e","e",None, "e","e","E"]  # row 6
]

print(str(len(layout)) + ' rows')
print('row: ' + str(layout[0]))
print('length of the row: ' + str(len(layout[0])))

print("Correct indexes for the Dot's seat: ")
layout[3][-1]

# 6 rows
# row: ['O', 'e', 'e', None, 'e', 'o', 'e', None, 'o', 'o', 'E']
# length of the row: 11
# Correct indexes for the Dot's seat: 
# 'E'

# STRETCH SOLUTION
new_layout = layout
new_layout[3].insert(-1,'O')
new_layout[3].pop(-1)
new_layout

# [['O', 'e', 'e', None, 'e', 'o', 'e', None, 'o', 'o', 'E'],
#  ['O', 'o', 'e', None, 'e', 'o', 'e', None, 'e', 'o', 'E'],
#  ['O', 'o', 'o', None, 'o', 'o', 'e', None, 'o', 'e', 'O'],
#  ['E', 'o', 'e', None, 'e', 'o', 'e', None, 'o', 'e', 'O'],
#  ['E', 'e', 'o', None, 'e', 'e', 'e', None, 'o', 'o', 'E'],
#  ['O', 'e', 'e', None, 'e', 'e', 'e', None, 'e', 'e', 'E']]
