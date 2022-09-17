# Using a dictionary for word count

def wordcount(fname):

    try:
        fhand = open(fname)
    except:
        print("File Cannot be opened")
        exit()

    count = dict()

    for line in fhand:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1     
    return(count) 

print(wordcount('word_count.txt'))

print("\n")

res_count = wordcount('freecodecamp.txt')

filtered = {k:v for k, v in res_count.items() if v > 1}

print(filtered)
            