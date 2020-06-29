import pandas as pd
import matplotlib.pyplot as plt

def test_run():
  df=pd.read_csv("Curs_valutar1.csv")
  print(df.head())
  ###df['CHF'].plot()
  df[['CHF','EUR']].plot()
  plt.show()
  
if __name__=="__main__":
  test_run()
