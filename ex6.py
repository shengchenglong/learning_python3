types_of_people = 10
x = f"There are {types_of_people} type of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said : {x}")
# 引号见相互嵌套可当做变量,互不影响
print(f"I also said: '{y}'")
print(f'I also said: "{y}"')

hilarious= "False"
joke_evaluation = "Isn't that joke so funny?! {}"
# a.format(b),将b放进a的空处
print(joke_evaluation.format(hilarious))
print("Hello {}, I'm {}".format("shengchenglong", "dabao"))

w = "This is the left side of..."
a = "a string whth a righe side."
# +号,为字符串的拼接,且没有空格
print(w + a)
