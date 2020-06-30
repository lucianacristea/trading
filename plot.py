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

def get_rolling_mean(values, window):
    """Return rolling mean of given values, using specified window size."""
    return values.rolling(window).mean()


def get_rolling_std(values, window):
    """Return rolling standard deviation of given values, using specified window size."""
    # TODO: Compute and return rolling standard deviation
    return values.rolling(window).std()

def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands."""
    # TODO: Compute upper_band and lower_band
    upper_band=rm+2*rstd
    lower_band=rm-2*rstd
    return upper_band, lower_band

def plot_bollinger_data(df, label, window, title, fontsize, xlabel, ylabel):
    # Compute Bollinger Bands
    # 1. Compute rolling mean
    rm_SPY = get_rolling_mean(df[label], window=window)

    # 2. Compute rolling standard deviation
    rstd_SPY = get_rolling_std(df[label], window=window)

    # 3. Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)
    
    # Plot raw SPY values, rolling mean and Bollinger Bands
    ax = df[label].plot(title=title, label=label)
    rm_SPY.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)  
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    plt.show()

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
  ###plot_data(normalize_data( plot_selected(df, ['CHF','EUR','GBP','USD'], '03.01.2020', '29.06.2020')), "Curs valutar", 2, "Dates", "Price")
  ###plot_data(plot_selected(df, ['CHF','EUR','GBP','USD'], '03.01.2020', '29.06.2020'), "Curs valutar", 2, "Dates", "Price")
  plot_bollinger_data(plot_selected(df,['CHF'], '03.01.2020', '29.06.2020'), 'CHF', 20, "Bollinger Bands", 2, "Dates", "Price")
  
if __name__=="__main__":
  test_run()
