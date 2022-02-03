# import modules
from sklearn import datasets, preprocessing
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#read in the pokemon dataset as a CSV
df = pd.read_csv('pokemon.csv')

#get rid of first 19 columns
df.drop(df.iloc[:, :19], inplace = True, axis = 1)

#factorize the pokemon types so that we can use them as class labels
df['type1'] = pd.factorize(df['type1'])[0].astype(np.uint16)

#set the factorized pokemon types as the class labels/targets
pk_targets = df['type1']

#create the dataset as a list with samples and targets
pokemon = []
for i in range(len(pk_targets)):
    pokemon.append([df.loc[i], pk_targets[i]])

#get all the features of the dataset.
all_features = []
for col in df.columns:
    all_features.append(col)
