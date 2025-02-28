# 1. print string in reverse , its lenght , in upppeer case lower
# case and copy into another string

# text = str("hello world")
# print(text.upper())
# print(text.lower())
# copy = text
# print(copy)
# print(len(text))

# b = ""
# for i in range(len(text)-1, -1, -1):
#     b = b + text[i]
#     # print(text[i], end=" ")

# print(b)

# 2. Arrenge string chracters suct thta lower case should com first

# text = "PyNaTive"
# lower = ""
# upper = ""
# for i in text:
#     if i.lower() == i:
#         lower = lower + i
#     if i.upper() == i:
#         upper = upper + i


# print(lower)
# print(upper)
# print(lower + upper)

# 3. Arrange string characters such that lowercase letters should come first

# text = "How Are You hOPe You Are Doing WElL"
# words = text.split()
# transformed_words = []

# for i in words:
#     lower_chars = []
#     upper_chars = []
#     for j in i:
#         if j.islower():
#             lower_chars.append(j)
#         else:
#             upper_chars.append(j)
#     transformed_word = "".join(lower_chars + upper_chars)
#     transformed_words.append(transformed_word)

# result = " ".join(transformed_words)
# print(result)


# 4. count and store  all letter digits and symbols in the givven string
# text = "P@#yn26at^&i5ve"
# letters = 0
# digits = 0
# symbols = 0
# Letters = ""
# Digits = ""
# Symbols = ""


# for i in text:
#     # print(i, end="")
#     if i.isalpha():
#         letters += 1
#         Letters = Letters + i

#     if i.isdigit():
#         digits += 1
#         Digits = Digits + i
#     if not i.isalpha() and not i.isdigit():
#         symbols += 1
#         Symbols = Symbols + i


# print(letters, digits, symbols)
# print(Letters, Digits, Symbols)

# 5. count vowvels from given strings and print the count

# text = "I am a student of BCA"
# print(text)
# for i in text:
#     if i in "aeiouAEIOU":
#         print(i)

# 6. check string is paillindrome or not
# def paillindrome(text):
#     rev = ""
#     for i in range(len(text)-1, -1, -1):
#         rev += text[i]

#     if (rev == text):
#         print(f"{text} is palindrome")
#     else:
#         print(f"{text} not palindrome")


# paillindrome("madam")
# paillindrome("sir")

# 7. accept list element and reprint it
# data = []

# n = int(input("Enter the number of elements: "))

# for i in range(n):
#     element = input("Enter an element: ")
#     data.append(element)

# print("Original list:", data)

# 8. list in reverse order

# list = [10, 20, 30, 40, 50]
# for i in range(len(list)-1, -1, -1):
#     print(list[i], end=" ")

# 9. print positive and negetive element of list in a sperated list
# list = [10, -21, 4, -45, 66, -93, 1]
# pos = []
# neg = []
# for i in list:
#     if i > 0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(pos)
# print(neg)

# 10. find greatest elemnt and its index
# list = [10, 100, 4, 45, 99]
# print(max(list).__index__)

# max = 0
# max2 = 0
# index = 0
# index2 = 0
# for i in range(len(list)):
#     if list[i] > max:
#         max2 = max
#         max = list[i]
#         index2 = index
#         index = i
#     elif list[i] > max2:
#         max2 = list[i]
#         index2 = i

# print(f"{max} is found at index : {index}")
# print(f"{max2} is second largest")

# 11. check list is shoorted or not
# list = [100, 2, 3, 4, 50]
# is_sorted = True
# for i in range(len(list)-1):
#     if list[i] > list[i+1]:
#         is_sorted = False
#         break
# print("List is sorted" if is_sorted else "List is not sorted")

# 12. check list if its paillindrome or not
# list = [10, 20, 30, 20, 10]
# rev = []
# for i in range(len(list)-1, -1, -1):
#     print(list[i], end=" ")
#     rev.append(list[i])
# if rev == list:
#     print("\nlist is paillindrome")
# else:
#     print("\nlist is not paillindrome")


# 13. remove repetion of a given element from list
# list = [1, 2, 2, 2, 2, 2, 222, 3, 3, 34, 4, 4, 4, 4, 4]

# list2 = set(list)

# print(list2)

# 14. write a python script to merge two dictorinary
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# dict1.update(dict2)
# print(dict1)

# 15. sum of all items in dict
# a = {'a': 100, 'b': 200, 'c': 300}

# sum = 0
# for i in a.values():
#     sum += i
# print(sum)

# 16. find frequency of element in list
list = [1, 2, 2, 2, 2, 2, 222, 3, 3, 34, 4, 4, 4, 4, 4]
dict = {}

for i in list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)
