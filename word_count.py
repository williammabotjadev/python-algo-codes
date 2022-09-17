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

print(wordcount('freecodecamp.txt'))
            