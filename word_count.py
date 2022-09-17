# Using a dictionary for word count

def wordcount(fname):

    try:
        f = open(fname)
    except:
        print("File Cannot be opened")
        exit()

    count = dict()

    for line in f:
        words = line.split()
        for word in words:
            if word not in words:
                count[word] = 1
            else:
                count[word] += 1     
    return count 

print(wordcount("word_count.txt"))
            