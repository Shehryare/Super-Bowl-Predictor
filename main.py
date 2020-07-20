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

#prints all columns and one row from each dataset
from utils import head
print("All columns and one row from each dataset\n")
print("Super Bowl History:")
print(head('data/datasets_superbowl.csv', 2))
print("\nSuper Bowl Ads:")
print(head('data/datasets_superbowl-ads.csv', 2))
 
#-------------------------------------------------------#

# There are 10 columns in the Super Bowl History CSV:

# Date: date, Date of Super Bowl
# SB: string, Super Bowl name
# Winner: sting, Winning team
# Winner Pts: int, Points scored by winning team
# Loser: string, Losing team
# Loser Pts: int, Points scored by losing team
# MVP: string, Most Valuable Player award recepient
# Stadium: string, Stadium name of Super Bowl
# City: string, City of Super Bowl
# State: string, State of Super Bowl

# There are 4 columns in the Super Bowl Ads CSV:

# Year: string, Year of Super Bowl
# Product/Type: string, Indusrty of ad
# Product/Title: string, Name of product
# Plot/Notes: string, Description of commercial

#-----------------------------------------------------#

# There are two CSV files that are in this project. The datasets are structured by rows
# with headers as the attributes. Each have very different attritbutes, but the main and only attribute
# that is similar in both datasets is the Date in the History and the Year in the Ads. Since there is
# only 1 Super Bowl in a year, it will help comine and merge the two datasets together and analyze
# the data better and in more detail.

# After combining the two datasets, the dataset will have 13 columns. And the same number
# of columns. Another thing to do is to change all of the Product/Type into categories, they’re are
# similiraties like Soft Drink and Beer or Web hosting and Wireless. These will be assigned to Beverages
# and Technology, respectively.

#-----------------------------------------------------#

###NEED TO PARSE DATA BC SOME HAVE 5 FIELDS INSTEAD OF THE DEFAULT FIELD 4

#Read into textfile by readline method 
#read line into text file
#splitting by , into a list
# check if the the line is greater than 4 
#if it is then modify


import pandas as pd 
df = pd.read_csv('test-data/datasets_superbowl-ads.txt')




import pandas as pd
ads = pd.read_csv('data/datasets_superbowl-ads.csv')
history = pd.read_csv('data/datasets_superbowl.csv')












