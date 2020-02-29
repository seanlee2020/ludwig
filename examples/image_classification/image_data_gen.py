import os

input_dir = "/Users/seanl/data/intel-image-classification/seg_train/seg_train"

output_file = open("data/image_meta.csv", "w")
output_file.write("image_path,class\n")

for child in os.scandir(input_dir):
    if  child.is_dir():
        print (child.name)

        count = 0
        for cc in os.scandir(child):
            if  count >100:
                break

            print(cc.name)
            image_path = input_dir + "/" + child.name + "/" + cc.name
            row = image_path + "," + child.name
            print (row)
            output_file.write(row + "\n")





output_file.close()