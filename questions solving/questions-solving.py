# # 1. Accept two number and print greatest between them
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# if num1 > num2:
#     print(num1, "is greater than", num2)
# else:
#     print(num2, "is greater than", num1)

# 2. Accept the gender from user and display msg accordingly

# G = input("Enter your gender (M/F): ")
# if G == "M" or G == "m":
#     print("You are male")
# elif G == "F" or G == "f":
#     print("You are female")
# else:
#     print("please enter your gender correctly")

# 3. Accept a number adn check if its even or odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(num, "is even")
# else:
#     print(num, "is odd")

# 4. Accept a name and age from user and check if its valid or not
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# if age >= 18:
#     print(name, "is eligible to vote")
# else:
#     print(name, "is not eligible to vote")

# 5. Accept a number and check if its leap year or not

# year = int(input("Enter a year: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")

# 6. Accept a alphabet and tell either its vowel or not

# alphabet = input("Enter an alphabet: ")
# if alphabet in "aeiouAEIOU":
#     print(alphabet, "is a vowel")
# else:

#     print(alphabet, "is not a vowel")

# 7. print natural number upto nth

# num = int(input("please enter a number "))
# for i in range(1,num+1):
#     print(i)

# 8. reverse loop now
# num = int(input("enter your number: "))

# for i in range(num, -1, -1):
#     print(i)

# 9. take a number as input and write it table
# num = int(input("enter a num: "))
# for i in range(1, 11):
#     print(f"{num} *  {i} = {num*i}")

# 10. sum upto n term
# num = int(input("enter a num:"))
# sum = 0
# for i in range(1, num):
#     # print(num+i)
#     sum = sum + i

# print(sum)

# 11. factorial of a number?
# num = int(input("enter a num: "))
# fact = 1
# for i in range(num, 0, -1):
#     fact = fact*i

# print(fact)

# 12. what are factors of a number

# num = int(input("enter a num: "))
# print("all factors are ")
# for i in range(1, num+1):
#     if num % i == 0:
#         print(i, end=" ")

# 13. enter a number and check if its a perfect number or not
# num = int(input("enter a num "))
# sum = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum = sum + i


# if sum == num:
#     print(f"{num} is a perfect number")
# else:
#     print(f"{num} is not a perfect number")
# 14. find prime number and composite number
# num = int(input("enter a num "))
# count = 0
# for i in range(1, num+1):
#     if num % i == 0:
#         count = count + 1
#         print(i)

# print(count)
# if (count == 2):
#     print("prime number")
# else:
#     print("composite number")

# 15. sperate each digit of a number and check if its pallindroic number 

num = int(input("enter a number: "))


