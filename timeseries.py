import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import os
import pandas as pd


def timeseriesplot(df):
    yleg = df.columns.tolist()
    # xaxis = [x[:3] for x in df.index.values.tolist()]
    yleg = df.columns.tolist()[1:]
    xaxis = [x[:3] for x in df['Month/Year'].values.tolist()]
    fig, ax = plt.subplots(figsize=(10, 6),  facecolor='white')
    for i in yleg:
        points = savgol_filter(df[i],window_length = 7, polyorder = 3 , mode = 'constant' )
        ax.plot(xaxis, points, 'o-', label = i, linewidth = 3 )
        plt.ylim(0, 1)
        ax.legend()
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    
    print(f'{param} graph generated')


if __name__ == "__main__":

    dirname = os.path.dirname(os.path.abspath(__file__))
    os.chdir(dirname)

    data = pd.read_csv('data/1058.csv')

    
    
    
