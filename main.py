"""
Upper and Lower
"""
# Provide your solution here
def count_upper_lower(my_string: str):
    for my_string.isupper() in range(my_string):
        number = 0 + my_string.isupper()
        print(("The number of upper case characters is:", number))
    for my_string.islower() in range(my_string):
       number2 = 0 + my_string.islower()
       print("The number of lower case characters ist:", number2)


count_upper_lower("the world is cool")


"""
Check 33
"""
# Provide your solution here
def has_33(my_list: [int]) -> bool:
    if print(3, 3 in my_list):
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

has_33([1,3,3])
has_33([2,5,7])
has_33([3,5,3])