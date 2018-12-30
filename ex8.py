formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, True, False))
# 报错:NameError: name 'true' is not defined
# print(formatter.format(True, False, true, false))
print(formatter.format(formatter, formatter, formatter, formatter))


