# Control Structures: for loops and if statements

# Python "for" Loops (Definite Iteration):  https://realpython.com/python-for-loop/
# Conditional Statements in Python:  https://realpython.com/python-conditional-statements/

# >>> d = {'foo': 1, 'bar': 2, 'baz': 3}
# >>> for k in d:
# ...     print(k)

# You can make a dictionary reference using the key as usual
# >>> for k in d:
# ...     print(d[k])

# You can also iterate through a dictionary’s values directly by using .values():
# >>> for v in d.values():
# ...     print(v)

# -------------------
# the Pythonic way to iterate through a dictionary accessing both the keys and values looks like this:
# >>> d = {'foo': 1, 'bar': 2, 'baz': 3}
# >>> for k, v in d.items():
# ...     print('k =', k, ', v =', v)
# ...
# k = foo , v = 1
# k = bar , v = 2
# k = baz , v = 3


# Challenge
# Dot wants to visit all the London landmarks where the wait time is less than 15 minutes. We have a dictionary called landmarks, within which landmark names are keys and wait times are their respective values.

# Using Python, develop a list of the landmarks where the wait time is less than 15 minutes. What will be the length of the list?

# dictionary where 
landmarks = {
    "Big Ben": 12,
    "Tower Bridge": 25,
    "Buckingham Palace": 15,
    "Madame Tussauds": 25,
    "London Eye": 40,
    "Tower of London": 25,
    "Emirates Air Line cable car": 16,
    "London Transport Museum": 7,
    "Wembley Stadium": 8,
    "Hyde Park": 0,
    "The View from The Shard": 14
}

keys = list(landmarks.keys())
values = list(landmarks.values())
# print(keys, values)
# print(keys)

landmark = []
for i in keys:
    if landmarks[i] < 15:
        landmark.append(i)
print(landmark, len(landmark))

# ['Big Ben', 'London Transport Museum', 'Wembley Stadium', 'Hyde Park', 'The View from The Shard'] 5

# SOLUTION

keys = list(landmarks.keys())
values = list(landmarks.values())


res = []
for i in range(len(keys)):
    if values[i] < 15:
        res.append(keys[i])
res
len(res)

