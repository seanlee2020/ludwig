import re

#fileIn = open('Data/atis.train.ctf', 'r')
#fileOut = open('Data/atis.train.csv', 'w')


fileIn = open('Data/atis.test.ctf', 'r')
fileOut = open('Data/atis.test.csv', 'w')

idx  = -1;

utterance = ""
slots = ""
intent = ""

fileOut.write("utterance,intent,slots\n")

while True:
    line = fileIn.readline()

    # print(line)
    if not line:
        break


    line = line.rstrip()

    segs = re.split("\s*\|\s*", line)

    curIdx = int(segs[0])
    token = re.split( "#\s*", segs[2])[1]

    slot = re.split( "#\s*", segs[4])[1]

    if (token == "BOS"):
        intent = slot
        continue
    if ( token == "EOS"):
        print(utterance)
        print(slots)
        print(intent)
        row = utterance + " , " + intent + " , " + slots
        fileOut.write(row + "\n")
        print(row)
        utterance = ""
        slots = ""
        idx = curIdx
        continue

    utterance = utterance + token + " "
    slots = slots + slot + " "

   # print (segs)

   # print (len(segs))