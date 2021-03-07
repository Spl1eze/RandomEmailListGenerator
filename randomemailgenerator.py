from pyperclip import copy
import random
import os

while True:
    try:
        file = input('Enter the name of the txt file: \n')
        file_dir = os.getcwd() + "/" + file
        file = open(file_dir).read()
        divider = input("Type in what the emails are divided by default= \" \":\n")
        if divider == "":
            divider = " "
        txt_file_data = file.split(divider)
        break
    except:
        print("That was not a valid file or incorrect name")
    

email_ending = input("Enter what the email ending is if there is extra text in file:\n")    
emails = []
for item in txt_file_data:
    if email_ending in item:
        emails.append(item)

while True:
    try:
        num_of_emails = int(input("Enter the number of random emails you want: \n"))
        break
    except:
        print("That wasn't a valid number")

email_string = ""
used_nums = []
for i in range(num_of_emails):
    while True:
        number = random.randint(0,len(emails))
        if number in used_nums:
            continue
        else:
            used_nums.append(number)
            email_string = email_string + emails[number] + "\n"
            break

copy(email_string)