def get_num_words(text):
    words = text.split() 
    return len(words)

def convert(text):
    counts = {}
    text =text.lower()

    for char in text:
        if char in counts:
            counts[char] += 1
        if char not in counts:
            counts[char] = 1
    return counts

def calibrate(counts):
    new_counts = []

    for key, value in counts.items():
        if key.isalpha():
            new_dict = {"char": key, "num": value}
            new_counts.append(new_dict)
            new_counts.sort(reverse=True, key = lambda d: d["num"])
    return new_counts


def sort_on(d):
    return d["num"]











































# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def convert(text):
#     counts = {}
#     text = text.lower()


#     for char in text:
#         if char in counts:
#             counts[char] += 1

#         if char not in counts:
#             counts[char] = 1
#     return counts

# def calibrate(counts):
#     new_counts = []

#     for key, value in counts.items():
#         if key.isalpha():
#             new_dict = {"char": key, "num":value}
#             new_counts.append(new_dict)
#         new_counts.sort(reverse=True, key=sort_on)
#     return new_counts

# def sort_on(new_dict):
#     return new_dict["num"]

