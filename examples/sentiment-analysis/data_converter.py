import re

fileIn = open('data/train.tsv', 'r')
fileOut = open('data/train.csv', 'w')


fileOut.write("review,sentiment\n")

idx = 0
while True:

    line = fileIn.readline()
    # print(line)

    if not line:
        break

    line = line.rstrip()

    segs = re.split("\t", line)

    if len(segs) < 4 :
        continue

    if len(segs[3]) > 1 :
        continue

    curIdx = int(segs[1])

    if curIdx == idx:
        continue

    review =  re.sub(',', ' ',  segs[2])
    sentiment = segs[3]
    row = review + " , " + sentiment

    print(row)

    fileOut.write(row + "\n")

    idx = curIdx




fileIn.close()
fileOut.close()