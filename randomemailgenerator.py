from pyperclip import copy
import random
import os
import categoryformatterbyron


def Split_File(file):
    divider = input("Type in what the emails are divided by default= \" \":\n") or " "
    txt_file_data = file.split(divider)
    return txt_file_data



def Open_File():
    file = input('Enter the name of the txt file: \n')
    # file_dir = os.getcwd() + "/" + file
    file_dir = file
    return open(file_dir).read()



def Extract_File_Data():
    while True:
        try:
            return Split_File(Open_File())
        except:
            print("That was not a valid file or incorrect name")
    


def Create_Email_List(txt_file_data):
    email_ending = input("Enter what the email ending is if there is extra text in file:\n")    
    emails = []
    for item in txt_file_data:
        if email_ending in item:
            emails.append(item)
    return emails



def Get_Number_Of_Random_Emails(emails):
    while True:
        try:
            num_of_emails = int(input("Enter the number of random emails you want: \n"))
            if Number_Checker(num_of_emails, len(emails)):
                continue
            else:
                break
        except:
            print("That wasn't a valid number")
    return num_of_emails

def Number_Checker(num_of_emails, len_emails):
    if num_of_emails > len_emails:
        print("That number was too large")
        return True
    elif num_of_emails < 0:
        print("No negatives")
        return True
    return False



def Get_Random_Emails(num_of_emails, emails):
    used_nums = []
    email_string = ""
    while len(used_nums) < num_of_emails:
        while True:
            number = random.randint(0,len(emails))
            if number in used_nums:
                continue
            else:
                used_nums.append(number)
                email_string = email_string + emails[number] + "\n"
                break
    email_string = email_string[0:-1]
    return email_string



def get_categories():
    entering_categories = True
    catergories = []
    first_input = True
    print("Don't type anything for default to grades otherwise type in the categories you want")
    print("Enter nothing anytime after the first input to stop inputing categories")
    while entering_categories:
        catergories.append(input("Type your categories: \n"))
        if first_input and catergories[0] == "":
            catergories = [9,10,11,12, "Byron"]
            first_input = False
            entering_categories = False
        elif catergories[len(catergories)-1] == "":
            catergories.pop(len(catergories)-1)
            entering_categories = False
    return catergories



def get_category_data(txt_file_data, categories):
    category_list = []
    category_sizes = {}
    for item in txt_file_data:
        for category in categories:
            if item in category:
                category_list.append(item)
                category_sizes.setdefault(category, 0)+1
    category_data = category_list, category_sizes
    return category_data
        


def get_category_num_of_emails(category_sizes, num_of_emails, len_of_emails):
    for category in category_sizes:
        category_number = round(category_sizes[category] * num_of_emails / len_of_emails, 0)
        if Number_Checker(category_number, len_of_emails):
            print("Can't complete a valid stratified sample doing SRS instead")
            return 0
        category_sizes[category] = category_number
    return category_sizes



def get_stratified_sample_group(category_list, emails):
    email_categories = {}
    for i in range(len(category_list)):
        email_categories.setdefault(category_list[i], []).append(emails[i])
    return email_categories



def main():
    print("Random Sample Email Finder\n" + "*"*50)
    print("Default if mispelled type will be SRS")
    sample_type = input("Enter the sample type (\"SRS\" or \"STRAT\"): \n")
    txt_file_data = Extract_File_Data()
    emails = Create_Email_List(txt_file_data)
    num_of_emails = Get_Number_Of_Random_Emails(emails)
    if sample_type == "STRAT":
        categories = get_categories()
        if len(categories) == 5 and categories[4] == "Byron":
            categories.pop(4)
            category_data = categoryformatterbyron.Reformat_List_Byron(txt_file_data, categories)
        else:
            category_data = get_category_data(txt_file_data, categories)
        category_sizes = get_category_num_of_emails(category_data[1],num_of_emails,len(emails))
        if category_sizes == 0:
            copy(Get_Random_Emails(num_of_emails, emails))
            return 0
        email_categories = get_stratified_sample_group(category_data[0], emails)
        
        email_string = ""
        for category in email_categories:
            email_string = email_string + "\n" + Get_Random_Emails(category_sizes[int(category)], email_categories[category])      
        print(email_string)
    else:
        copy(Get_Random_Emails(num_of_emails, emails))

if __name__ == "__main__":
    main()