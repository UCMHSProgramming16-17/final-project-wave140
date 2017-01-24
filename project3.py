#import modules
import csv
import pandas as pd
import bokeh

# read csv dataframe
df = pd.read_csv('Pokemon.csv')

# import plotting imports
from bokeh.charts import Histogram, output_file, save
# create output file
output_file('Histogram.html')
# set up the graph components
poke = Histogram(df, 'Defense', 'Sp. Def', title = 'Comparison of Defenses')
# save the graph to file
save(poke)