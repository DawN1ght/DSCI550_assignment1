import pandas as pd

# read csv file
df = pd.read_csv('reports.csv')
#  save as tsv file
df.to_csv('converted_reports.tsv', sep='\t', index=False)  # set the seperator as '\t'






