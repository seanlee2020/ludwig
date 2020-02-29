fileIn = open('data/qp_test_2019_11_05.csv', 'r')
fileOut = open('data/test_2019_11_05.csv', 'w')

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
