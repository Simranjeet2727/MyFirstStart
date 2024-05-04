# email validation using RegEx
# a-z
# 0-9
# . _ time/count 1
# @ count 1
# . 2,3 position from last

import re # regex module
email_condition="^[a-z] + [\._]?[a-z 0-9] +[@]\w + [.]\w{2,3}$"
user_email=input('Enter your email: ')

if re.search(email_condition, user_email):
    print("Right email")
else:
    print("Wrong email")    


# ^ used to check string/characters from starting
# in regex + used to concatinate string
# when we search any character in regex we use \
# ? works for 0 and 1(binary type) means it tells that the character is used 1 time or not 
# \w used to search in string
# {} used to search character at particular position like '.' should be at position 2 or 3 we will use {}
# $ used to search string characters from last
# to check condition in regex we use search fnction i.e.; re.search()
