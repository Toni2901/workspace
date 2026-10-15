#Character Bookbot
def get_num_words(text):
    words = text.split()
    return len(words)

def convert(text):
    counts = {}
    text = text.lower()

    for char in text:
        if char in counts:
            counts[char] += 1  
        if char not in counts:
            counts[char] = 1
    return counts

def sort_dict(counts):
    new_list = []
    for key, value in counts.items():
        if key.isalpha():
            new_dict = {"char": key, "num": value}
            new_list.append(new_dict)
        new_list.sort(reverse=True, key=sort_on)
    return(new_list)


def sort_on(new_dict):
    return new_dict["num"]

#A dictionary isn't easy to sort hence why it was converted to a list
#convert the dict to a key, value form - for ease in sorting
#append the dictionary to the list
#sort the list using the key - num
#Transform into a list of only the value pairs