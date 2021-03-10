def Reformat_List_Byron(txt_file_data, categories):
    category_list = []
    category_sizes = {}
    for item in txt_file_data:
        for category in categories:
            try:
                if int(item) == category:
                    category_list.append(item)
                    category_sizes.setdefault(category, 0)
                    category_sizes[category] += 1
            except:
                continue
    
    grades = 0
    while grades < 4:
        category_list.pop(8+grades)
        grades += 1
    for category in category_sizes:
        category_sizes[category] -= 1
    category_data = category_list, category_sizes
    return category_data