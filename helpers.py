def difference(string1, string2) -> bool:
    # Split both strings into list items
    string1 = string1.split()
    string2 = string2.split()

    A = set(string1)  # Store all string1 list items in set A
    B = set(string2)  # Store all string2 list items in set B

    str_diff = A.symmetric_difference(B)
    isEmpty = (len(str_diff) == 0)

    if isEmpty:
        return True
    else:
        return False
        # print("Test Failed!")
        # print("The Difference is: ")
        # print(str_diff)
