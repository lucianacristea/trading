import pandas as pd
import matplotlib.pyplot as plt

def test_run():
  df=pd.read_csv("Curs_valutar.csv", index_col="Dates", parse_dates=True)
  # convert the 'Date' column to datetime format 
  print(df.head())
  print (df.dtypes)
  print(df.loc['03.01.2020':'29.06.2020',['CHF','EUR','GBP','USD']])
  ###df.index = pd.to_datetime(df.index)
  ###df['CHF'].plot()
  ###df[['CHF','EUR']].plot()
  df=df/df[0]
  df.plot()
  plt.show()
  
if __name__=="__main__":
  test_run()
