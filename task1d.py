def character_word_count(string):
 	 my_string = string.lower().split()
 	 my_dict = {}
 	 for item in my_string:
   	  my_dict[item] = item.count(item)
 	 print(my_dict)

word_count("I am that I am")



