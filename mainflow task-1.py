my_list = [1,2,3,4,5,6]
print(my_list);
my_list.append(7)
print(my_list)
my_list.remove(3)
popped_element = my_list.pop()
print("After popping the last element (", popped_element, "):",my_list)
# create a dictionary
my_dict = {"name": "SIDRA", "age" : 18, "city": "Hyderabad"}
print(my_dict)
my_dict["job"] = "Engineer"
print(my_dict)
my_dict["age"] = 19
print("After updating age: ", my_dict)
del my_dict["city"]
print("After removing city: ",my_dict)
#create  a set
my_set = { 1,5,6,8,9}
print(my_set)
my_set.add(2)
print(my_set)
my_set.remove(9)
print(my_set)
