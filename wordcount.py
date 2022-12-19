"""Count words in file."""


# open file
all_text = open("test.txt")
# all_text = open("twain.txt")

# initiate empty dictionary
words_dict = {}

# go through each line of text
for line in all_text:
    
    # split line into list of words using space as delimiter
    words = line.rstrip().split(" ")
    # print(words)

    # for each word in dictionary
    for word in words:

        # increment count        
        words_dict[word] = words_dict.get(word, 0) + 1

# print count for each word
for word, count in words_dict.items():
    print(word, count)
