# 23 July 2018 Miroslav Gasparek
# Caltech Data Analysis in the Biological sciences by Justin Bois

# Tutorial 1b: Data frames

import numpy as np
import pandas as pd 

import bokeh.io
import bokeh.plotting

# Read in data and store them in  a DataFrame
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Slice a column out of a DataFrame by using the column name
impf = df['impact force (mN)']

# Convert DataFrame to a NumPy float64 data type
df['impact force (mN)'] = df['impact force (mN)'].astype(float)

# Check that it worked
df['impact force (mN)'].dtype