import pandas as pd
import matplotlib.pyplot as plt

def test_run():
  df=pd.read_csv("Curs_valutar.csv")
  print(df.head())
  print df[['CHF']]
  df.plot()
  plt.show()
  
if __name__=="__main__":
  test_run()
