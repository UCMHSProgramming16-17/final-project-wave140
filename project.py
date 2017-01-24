# import modules
import csv
import pandas as pd
import bokeh

# read csv dataframe
df = pd.read_csv('Pokemon.csv')

# import needed plotting imports
from bokeh.charts import Bar, output_file, save
# create output file
output_file('Bar.html')
# set up the bar graph components
poke = Bar(df, 'Generation', '#', agg='count', title = 'Number of Pokemon per Generation')
# save the bar graph to file
save(poke)