def number_of_words(text):
    count = 0
    string_list = text.split()
    for i in string_list:
        count += 1
    return count

def get_characters(text):
    lower_case = text.lower()
    char_dict = {}
    for char in lower_case:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]
def sorted_count(char_dict):
    list_chars =[]
    for char in char_dict:
        new_char_dict = {}
        new_char_dict["char"] = char
        new_char_dict["num"] = char_dict[char]
        list_chars.append(new_char_dict)
    
    list_chars.sort(reverse=True,key=sort_on)
    return list_chars




   
    
   

    


