#!/usr/bin/python3

#Each set of lines should be ran in the main.pynb file using jupiter notebook. 
#In this way you can view the visualizations 

#
#
#
#
#
#
#

#imports from path to find any datasets inside of your data folder
from pathlib import Path
data_dir_path = Path('data')
file_names = [x.name for x in data_dir_path.glob('*') if x.is_file()]


#prints the sizes of both datasets
import os
print('---Size of each dataset---\n')
print('Super Bowl History:')
print(os.path.getsize('data/datasets_superbowl.csv'))
print('\nSuper Bowl Ads:')
print(os.path.getsize('data/datasets_superbowl-ads.csv'))

#prints the amount of rows that are in each dataset
from utils import line_count
print("---Number of rows from each dataset---\n")
print("Super Bowl History:")
line_num = line_count('data/datasets_superbowl.csv')
print(line_num)
print("\nSuper Bowl Ads:")
line_num = line_count('data/datasets_superbowl-ads.csv')
print(line_num)










