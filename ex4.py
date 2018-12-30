cars = 100
# 任何一个整数与浮点数运算后的结果是浮点数
print(3 + 4.0)
space_in_a_car = 4.0
drivers = 30
passengers = 90
cats_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")

print("We can transport", carpool_capacity, "people today.")

# 判断是否相等
print(drivers == passengers)
# 报错:TypeError: 'drivers' is an invalid keyword argument for this function
# print(drivers = passengers)

# 浮点数四舍五入
print("round(1.733)", round(1.733))
