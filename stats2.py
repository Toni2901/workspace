# Word Bookbot
def get_num_words(text):
    words = text.split()
    return len(words)

def convert(text):
    counts = {}
    text = text.lower()
    words = text.split()

    for word in words:
        # if word in counts:
        #     counts[word] += 1  
        # else:
        #     counts[word] = 1
        counts[word] = counts.get(word, 0) + 1
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