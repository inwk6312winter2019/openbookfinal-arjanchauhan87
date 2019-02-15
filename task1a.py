def unique-words(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list
unique_words(file = open("Book1.txt","r")
