
# my_set = set(a_list_to_convert)

unique_colors_list = ["red", "yellow", "red", "green", "red", "yellow"]
unique_colors_set = set(unique_colors_list)
# => {"green", "yellow", "red"}

# my_set_2 = (["enter", "list", "here"])

unique_colors_set_2 = set(["red", "yellow", "red", "green", "red", "yellow"])
# => {"green", "yellow", "red"}


clothing_set = {"sock", "shirt"}
clothing_list = ["sock", "pants"]

# In a list:
clothing_list.append("red")

# In a set
clothing_set.add("red")
