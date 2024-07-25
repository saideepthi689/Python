data=[1,8,'carrot','mango','apple']
fruits=['apple','mango','orange','watermelon']
for i in data:
    if i in fruits:
        print(i)
#not in
veggies=['tomato','carrot','beans']
for i in data:
    if i in veggies and i not in fruits:
        print(i)