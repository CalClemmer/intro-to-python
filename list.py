colors = ['purple', 'red', 'blue']
print(colors)

colors = ["red", "yellow", "green"]
my_class = ["James", "Zoe", "Steve", "Nhu", "Paulo"]

# Strings
colors = ["red", "yellow", "green"]

# Numbers
my_nums = [4, 7, 9, 1, 4]

#Both! 
loosy_goosy= ["red", 7, "yellow", 1, 4]

num_students = len(my_class)
print("There are", num_students, "students in the class")

my_class.append("Sonyl")
print(my_class)

my_class.insert(1, "Kelly")
print(my_class)

my_class = ["James", "Kelly", "Zoe", "Steve", "Nhu", "Paulo", "Sonyl"]

student_that_left = my_class.pop()
print(student_that_left, "has left the class.")
# => "Sonyl has left the class"
print(my_class)
# => ["James", "Kelly", "Zoe", "Steve", "Nhu", "Paulo"]

second_student_to_leave = my_class.pop(1)
print(student_that_left, "has left the class.")
# => "Kelly has left the class"
print(my_class)

# sum(numeric_list)

batting_avgs = [.328, .299, .208, .301, .275, .226, .253, .232, .287]
sum_avgs = sum(batting_avgs)
print("The total of all the batting averages is", sum_avgs)
# => 2.409

# max(numeric_list)
# min(numeric_list)

batting_avgs = [.328, .299, .208, .301, .275, .226, .253, .232, .287]
print("The highest batting average is", max(batting_avgs))
# => 0.328
print("The lowest batting average is", min(batting_avgs))
# => 0.208

x = range(1000000)

print("largest diff", max(x) - min(x))
print("avg", sum(x) / len(x))