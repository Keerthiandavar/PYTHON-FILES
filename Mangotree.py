rows = int(input())
columns = int(input())
tree_num = int(input())
if tree_num % columns == 2 or tree_num % columns == columns - 2 :
    print("It is a mango tree")
else:
    print("It is not a mango tree")