'''
pip install pandas
import pandas as pd; 

write csv to excel 
''' 
import pandas as pd  #import pandas

read_file = pd.read_csv (r'metadata.csv') #read csv file
read_file.to_excel (r'metadata.xlsx', index = None, header=True) #converts csv to excel document