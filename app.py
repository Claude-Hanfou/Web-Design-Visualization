import pandas as pd

a = pd.read_csv('./Resources/cities.csv')

a.to_html("output.html")
