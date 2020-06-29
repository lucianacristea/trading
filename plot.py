import pandas as pd
import matplotlib.pyplot as plt

def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # TODO: Your code here
    # Note: DO NOT modify anything else!
    df=df.loc[start_index:end_index, columns]
    return df

def plot_data(df, title, fontsize, xlabel, ylabel):
  ax=df.plot(title=title, fontsize=fontsize)
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  plt.show()
    
def normalize_data(df):
    return df/df.iloc[0,:]

def test_run():
  df=pd.read_csv("Curs_valutar.csv", index_col="Dates", parse_dates=True)
  # convert the 'Date' column to datetime format 
  print(df.head())
  print (df.dtypes)
  print(df.loc['03.01.2020':'29.06.2020',['CHF','EUR','GBP','USD']])
  ###df.index = pd.to_datetime(df.index)
  ###df['CHF'].plot()
  ###df[['CHF','EUR']].plot()
  ###df=df/df.loc[0]
  ###df.plot()
  # Slice and plot
  plot_selected(df, ['CHF','EUR','GBP','USD'], '03.01.2020', '29.06.2020')
  plot_data(normalize_data(df), "Curs valutar", 2, "Dates", "Price")
  
  
if __name__=="__main__":
  test_run()
