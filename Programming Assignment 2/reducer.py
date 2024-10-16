#!/usr/bin/python3
import sys

# initializes an empty dictionary output to store word counts
output = {}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    # tries to convert count to an integer using the int() function. 
    # if it fails (e.g. count is not a valid integer), it skips to the next iteration of the loop using continue
    try:
        count = int(count)
    except ValueError:
        continue

    # increments count of word in the output dictionary
    # if word doesn't exist yet, it creates it and assigns value count
    try:
        output[word] = output[word]+count
    except:
        output[word] = count

# loops over the items in output, sorted in descending order of value. 
# prints the top 100 most frequent words and their counts. 
# loop stops after 100 words are printed
counter = 0
for k,v in sorted(output.items(), key = lambda kv:(kv[1], kv[0]), reverse=True):
    if counter == 100:
        break
    print(f"{k}\t{v}")
    counter+=1