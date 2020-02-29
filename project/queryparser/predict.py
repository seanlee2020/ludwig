from ludwig.api import LudwigModel
import pandas as pd
import sys, getopt
import numpy as np

#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))

def gen_tag_labels(input_dataframe):
    tag_labels = []
    for index, row in input_dataframe.iterrows():
        print(row['query'], row['tags'])
        tag_labels.append(row['tags'])
    return tag_labels

def count_correct_predicts( output, tag_labels):

    count = 0
    for i in range(len(output)):
       tag_seq = " ".join( output[i][0])


       tag_label = tag_labels[i]

       if tag_seq == tag_label:
            count += 1


    return count



model_path = ""
input_file = ""

try:
    opts, args = getopt.getopt(sys.argv[1:],"hm:i:",["model_path=","input_file="])
except getopt.GetoptError:
    print ( 'predict.py -m <model_path> -i <input_file>' )
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
         print('predict.py -m <model_path> -i <input_file>')
         sys.exit(2)
    elif opt in ("-m", "--model_path"):
         model_path = arg
    elif opt in ("-i", "--input_file"):
         input_file = arg

print('model_path: ', model_path)
print('input_file: ', input_file)

#sys.exit(2)

#model_path = "results/experiment_run_0/model"



model = LudwigModel.load(model_path)

#input_file = "data/test_2019_11_05_head10.csv"

input_dataframe = pd.read_csv(input_file)

trunk_size = 10
num_trunks = int((input_dataframe.size + 1) / (trunk_size * 2))

print (num_trunks)


trunk_dataframes = np.array_split(input_dataframe, num_trunks)


total_count = input_dataframe.size/2

total_correct_count = 0

total_count = 0
for i in range(num_trunks):

    print( "\n\npredict trunk " + str(i))
    trunk_dataframe = trunk_dataframes[i]
    total_count += trunk_dataframe.size/2
    #predictions = model.predict(data_df = input_dataframe)

    predictions = model.predict(data_df = trunk_dataframe)

    #predictions = model.predict(data_csv=input_file)

    values = predictions.values


    tags_predictions = predictions.tags_predictions

    tags_probability = predictions.tags_probability

    tag_seq = values[0][0]
    last_tag = values[0][1]
    prob = values[0][2]

    print(values[0])
    print(values[0][0])

    print(values[0][0][0])
    print(predictions)

    #tag_labels = gen_tag_labels(input_dataframe)
    tag_labels = gen_tag_labels(trunk_dataframe)

    print(tag_labels)

    num_correct_predicts =  count_correct_predicts(values, tag_labels)

    print("num_correct_predicts " + str(num_correct_predicts))

    total_correct_count += num_correct_predicts

    print("total_correct_count: " + str(total_correct_count))
    print("total_count: " + str(total_count))
    print("accuracy =" + str(total_correct_count / total_count))


print("total_correct_count: " + str(total_correct_count))
print("accuracy =" + str(total_correct_count/total_count))