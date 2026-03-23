def linear(list0, value, index):
    if index >= len(list0):
        return "Not in"

    if list0[index] == value:
        return index
    return linear(list0, value, index + 1)

list1 = []
inputVal = int(input("Enter the range of the list: "))
for a in range(1, inputVal + 1):
    val = int(input(f"value-{a}: "))
    list1.append(val)
    
print(f"The list value is {list1}") 
x = int(input("Enter the search Element: ")) 
i = 0
print(f"{x} value is present in index: {linear(list1, x, i)}")

