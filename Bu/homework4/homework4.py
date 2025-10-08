favoritefoods = ["pizza", "sushi", "pasta", "ice cream", "tacos"]
print(favoritefoods[1])
print(favoritefoods[-1])
favoritefoods.append("burger")
favoritefoods.insert(0, "apple")
del favoritefoods[2]
print(len(favoritefoods))
for food in favoritefoods:
    print(food.upper())
first_last_foods = favoritefoods[::len(favoritefoods)-1]
print(first_last_foods)
if "potato" in favoritefoods:
    print("A potato!")
else:
    print("No potato!")


numbers = list(range(0, 21))
def get15(numbers):
    return numbers[:15]
def get5th(lst):
    return lst[::5]
def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]
step1 = get15(numbers)
step2 = get5th(step1)
step3 = reverse_and_stride(step2)

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(numbers[2])
print(numbers[1][1])
numbers.append([10, 11, 12])
def sum_nested(nested_list):
    total = 0
    for row in nested_list:
        for number in row:
            total += number
    return total
print(sum_nested(numbers))

def create_5x5():
    list = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        list.append(row)
    return list

five_by_five = create_5x5()

def replace_multiples_of_3(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] % 3 == 0:
                list[i][j] = "?"
    return list

updated_list = replace_multiples_of_3(five_by_five)

def sum_non_question(list):
    total = 0
    for row in list:
        for element in row:
            if element != "?":
                total += element
    return total

result_sum = sum_non_question(updated_list)

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
for name, age in ages.items():
    print(name, age)
print(create_5x5())
