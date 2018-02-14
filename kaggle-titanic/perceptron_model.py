"""
This uses a simple Perceptron model to make survival predictions 
using the Titanic data set provided by Kaggle.  It achieved a 70% accuracy
scoring.
"""

import pandas as pd
from sklearn.linear_model import Perceptron

training_data_filename = "train.csv"
gradeable_test_name = "train.csv"
test_name = "test.csv"
outfile_name = "out.csv"

#cabin_section_map = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6}
#print(cabin_section_map, end)

def read_training_data():
    df = pd.read_csv("train.csv")
    return df

def read_testing_data():
    return pd.read_csv(test_name)


def clean_Sex_col(dfa):
    dfb = dfa.replace('female',2)
    dfb = dfb.replace('male', 1)
    return dfb

def clean_Age_col(dfa):
    dfb = dfa.replace(float('NaN'), 1.0)
    return dfb

def clean_Embarked_col(dfa):
    uniques = []
    for a in dfa.Embarked:
        if a not in uniques:
            uniques.append(a)
    dfb = dfa
    for i in range(len(uniques)):
        dfb = dfb.Embarked.replace(uniques[i],i+1)
    return dfb



# def item_follows_cabin_patt(it):
#     try:
#         ret = it[:1].isalpha() and it[1:].isnumeric()
#         return ret
#     except:
#         return False

# def new_section(it):
#     keylist = list(cabin_section_map.keys())
#     keylist.sort()
#     last_key = keylist[-1]
#     cabin_section_map[it] = cabin_section_map[last_key] + 1

# def new_section_cabin_no_dict():
#     return {'section':0,'cabin_no':0}

# def split_cabin_no(cabin_no):
#     ret = new_section_cabin_no_dict()
#     if type(cabin_no) == type("string"):
#         cabin_list = cabin_no.split()
#         sec_list = []
#         cab_list = []
#         for it in cabin_list:
#             if item_follows_cabin_patt(it):
#                 sec = it[:1]
#                 cab = it[1:]
#                 if sec not in cabin_section_map.keys():
#                     new_section(sec)
#                 sec = cabin_section_map[sec]
#                 cab = int(cab)
#                 sec_list.append(sec)
#                 cab_list.append(cab)
#         sec = sum(sec_list) / len(sec_list)
#         cab = sum(cab_list) / len(cab_list)
#         ret['section'] = sec
#         ret['cabin_no'] = cab
#     return ret



def clean_train_data(dfa):
    surv = dfa.Survived
    dfb = dfa.drop(labels=None, axis=1, index=None, columns=['Name', 'Ticket', 'Cabin', 'Embarked', 'Survived'])
    dfb = clean_Sex_col(dfb) #Sex
    dfb = clean_Age_col(dfb) #Age
    return dfb, surv

def clean_test_data(dfa):
    dfb = dfa.drop(labels=None, axis=1, index=None, columns=['Name', 'Ticket', 'Cabin', 'Embarked'])
    dfb = clean_Sex_col(dfb) #Sex
    dfb = clean_Age_col(dfb) #Age
    return dfb



def main():
    df = read_training_data()
    td = read_testing_data()
    td = clean_test_data(td)
    df, train_against = clean_train_data(df)
    pc = Perceptron()
    pc.max_iter = 25000
    pc.fit(df, train_against)
    res = pc.predict(td)
    fp = open(outfile_name, mode='w')
    fp.write('PassengerId,Survived\n')
    for i in range(len(res)):
        fp.write(str(td.PassengerId[i]) + ',' + str(res[i]) + '\n')
    fp.close()
main()
