#fileIn = open('engtrain.bio', 'r')
#fileOut = open('train.csv', 'w')

fileIn = open('engtest.bio', 'r')
fileOut = open('test.csv', 'w')

bio = ""
tag = ""
while True:
    line = fileIn.readline()
    if not line:
        break

    line = line.rstrip()

    if ( len(line) > 0):

        segs = line.split("\t")

        if ( len(tag) == 0):
            tag = segs[0]
        else:
            tag += " " + segs[0]

        if ( len(bio) == 0):
            bio = segs[1]
        else:
            bio += " " + segs[1]

    else:
        newLine = bio + ", " +  tag
        print( newLine)
        fileOut.write(newLine + "\n")
        bio = ""
        tag = ""

fileIn.close()
fileOut.close()