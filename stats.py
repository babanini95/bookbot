def count_words(text):
    count = len(text.split())
    return count

def count_char(text: str) -> dict:
    char_dict = {}
    for character in text.lower():
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict :dict) -> list:
    charStats = []
    for k in dict:
        if not k.isalpha():
            continue
        charStats.append({"char": k, "num": dict[k]})
    charStats.sort(reverse=True, key=sort_on)
    return charStats