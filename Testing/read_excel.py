import pandas as pd
import matplotlib.pyplot as plt
import time

# read the Excel file
df = pd.read_excel('../Files/Test_Excel.xlsx')

# create a plot
plt.ion()  # turn on interactive mode
fig, ax = plt.subplots()
line, = ax.plot(df.index, df['data'])

# plot live data
while True:
    new_df = pd.read_excel('../Files/Test_Excel.xlsx')
    if not new_df.equals(df):
        df = new_df
        line.set_xdata(df.index)
        line.set_ydata(df['data'])
        ax.relim()
        ax.autoscale_view()
        plt.draw()
    time.sleep(1)