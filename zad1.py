input_string = input("Enter numbers with ',' : ")

numbers = input_string.split(", ")[::-1]
print(*numbers,sep=" ") 


 