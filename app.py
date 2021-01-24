import pandas as pd 
  
# to read csv file named "samplee" 
a = pd.read_csv("./Resources/cities.csv") 
  
# to save as html file 
# named as "Table" 
a.to_html("output.html")