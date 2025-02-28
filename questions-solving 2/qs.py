# 1. print string in reverse , its lenght , in upppeer case lower case and copy into another string

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

text = "How Are You hOPe You Are Doing WElL"
words = text.split()
transformed_words = []

for i in words:
    lower_chars = []
    upper_chars = []
    for j in i:
        if j.islower():
            lower_chars.append(j)
        else:
            upper_chars.append(j)
    transformed_word = "".join(lower_chars + upper_chars)
    transformed_words.append(transformed_word)

result = " ".join(transformed_words)
print(result)
