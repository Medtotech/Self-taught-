#Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

user_input = input("Enter a word: ")

if user_input[0: ] == user_input[ ::-1]:
    print ("The word " + user_input + " is a palindrome ")
else:
    print ("The word " + user_input + " is not a palindrome ")