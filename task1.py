# -*- coding: utf-8 -*-

import csv

import sys

import datetime

import pycountry


#lists declarations

num_of_impr = []

ctr = []

clicks = []

date = []
date_conv = []

state = []

country_codes = []


#This function take a argument argv (namve of the csv file) and return coverter csv file acording to a guideliens

def put_file(argv):

 #converting argv to a string
 
 temp_file_name = str(argv)
 string_temp = temp_file_name[1:-1]
  
  
 file_name = string_temp[1:-1]

 #loading file data to a lists
 
 with open(file_name, 'r') as csvfile:
  
   csvreader = csv.reader(csvfile)
  
   for row in csvreader:
    
     date.append(row[0])
     
     state.append(row[1])
     
     num_of_impr.append(row[2])
     
     ctr.append(row[3])

 #calculating the clicks value
 
 for i in range(11):
  
   num_of_impr[i] = float(num_of_impr[i])
   
   ctr[i] = float(ctr[i])
  
   a = ctr[i]*num_of_impr[i]/100.
   
   clicks.append(round(a))

 #converting the date
 
 for i in range(len(date)):

     x = datetime.datetime.strptime(date[i], "%m/%d/%Y").strftime("%Y-%m-%d")
     
     date_conv.append(x)


 #checking the country code based on region name
 
 kip_value = {}

 for subd in pycountry.subdivisions:
   
   kip_value[subd.name] = subd.country_code

 for i in range(len(state)):
   
   y=state[i]

  
   if y in kip_value.keys():
     
     #print(kip_value[y])
    
     country_codes.append(kip_value[y])
  
   else:
     country_codes.append('XXX')
 
 #saving the data to a csv file

 rows = zip(date_conv, country_codes, num_of_impr, clicks)

 with open('output.csv', "w+") as f:
    
     writer = csv.writer(f)
    
     for row in rows:
        
        writer.writerow(row)
         
if __name__=="__main__":
  
  put_file(sys.argv[1:])        