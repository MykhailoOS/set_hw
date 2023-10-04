# task2
def get_elements(text: str):
    new_list = list(text)
    check = len(set(new_list))
    print(check)


get_elements(input(">>>"))


# task4
friendships = {
    "user1": {"user2", "user3", "user4"},
    "user2": {"user1", "user3"},
    "user3": {"user1", "user2", "user4"},
    "user4": {"user1", "user3"}
}
name1 = input(">>> ")
name2 = input(">>> ")
set_name1 = set(friendships[name1])
set_name2 = set(friendships[name2])
if set_name1.isdisjoint(set_name2):
    print("Нема спільних друзів")
else:
    print(f"{name1} and {name2} мають спільних друзів:")
    print('\t', *set_name1 & set_name2)

# Task 5
word1 = input("")
word2 = input("")
if len(word1) > len(word2):
    score = word1.count(word1)
    print(f"{word1} більше ніж {word2} на {score}")
else:
    score2 = word2.count(word2)
    print(f"{word2} більше ніж {word1} на {score2}")

# дз на функції
# Task1
def count(x, y, text):
    int_sum = x + y
    new_sum = str(int_sum)
    count_text = text + new_sum
    return count_text


count_func = int(input("num1= ")), int(input("num2 = ")), input("text= ")
print(count_func)




# Task3
# Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел.
# Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».
def check_num(num: list, search_num):
    for i in num:
        if i == search_num:
            return num.index(i)
    else:
        return "-1"


check_num_func = check_num([1, 2, 10, 4, 5], 5)
print(check_num_func)


# Task4
def returner(text: str):
    scale = text.split()
    check_words = len(scale)
    return check_words


func = returner(input(">>> "))
print(func)
