import pandas as pd
import matplotlib.pyplot as plt

def test_run():
  df=pd.read_csv("Curs_valutar1.csv", index_col="Data", parse_dates=True)
  # convert the 'Date' column to datetime format 
  df['Data']= pd.to_datetime(df['Data']) 
  print(df.head())
  ###df['CHF'].plot()
  df[['CHF','EUR']].plot()
  plt.show()
  
if __name__=="__main__":
  test_run()
