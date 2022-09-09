# import random
# computer_number = random.randint(1,100)
#
# print(computer_number)
# #guess the number game
#
# #1. Allow user to guess the number in 7 chance
# #2. If the number guessed by user is greater or smaller than the number generated notify user about it.
# #3. If the user is able to guess the number correctly you need to confratulate the user and you need to tell in how many attempt the user cracked it
# #Congratulation!!! You cracked the number in 4 attempts
# #4 If the user is not able to crack the number, you need to say all chances exhausted.
#
# count=0
# for i in range(7):
#     try:
#         user_number = int(input("Enter your number between 1 to 100\n"))
#     except Exception as e:
#         print("You entered an invalid number")
#         continue
#     if user_number > computer_number:
#         print("Guess lesser number")
#
#     elif user_number < computer_number:
#         print("Guess larger number")
#
#     elif user_number == computer_number:
#         print("Congratulation!!! You cracked the number in" + count + "attempts")
#         break
#     count = count + 1
# else:
#         print(f"All chances exhausted, number to be guessed {computer_number}")
# #print("All chances exhauster")
#
from passlib.hash import pbkdf2_sha256
password = "Hello"
hashed = pbkdf2_sha256.hash(password)
print(hashed)
if pbkdf2_sha256.verify("Hi", hashed):
    print("Password matched successfully")
else:
    print("Password not matched")

