# ' or " can be used but use ' of you're going to use " in the strings
print('Today is a good day to learn Python')
print("Python is fun")
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
name = "Tim"
print(greeting + name)

# comment
print(greeting + ' ' + name)


age = 30
print(age)

print(type(greeting))
print(type(age))

# f string can be used instead of replacement fields

age_in_words = "2 years"
print(name + f" is {age}  years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
