fileIn = open('data/qp_train_2019_11_05_100k.csv', 'r')
fileOut = open('data/train_100k.csv', 'w')

query = ""
tag = ""

fileOut.write("query,tags\n")

head = True

while True:


    line = fileIn.readline()

    if head:
        head=False
        continue

    if not line:
        break

    print(line)
    line = line.rstrip()

    segs = line.split(",")

    query = segs[0]
    tag = segs[1]
    row = query + "," + tag

    print (row)

    fileOut.write(row + "\n")

fileOut.close()