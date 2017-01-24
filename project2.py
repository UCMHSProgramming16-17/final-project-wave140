# import modules
import csv
import pandas as pd
import bokeh

# read csv dataframe
df = pd.read_csv('Pokemon.csv')

# import necessary plotting imports
from bokeh.charts import Scatter, output_file, save
# create output file
output_file('Scatter.html')
# set up the bar graph components
poke = Scatter(df, 'HP', 'Attack', title = 'HP vs. Attack')
# save the pie graph to file
save(poke)