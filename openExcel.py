import pandas as pd
import matplotlib as plt

# Load an ODS file into a Pandas dataframe
fig2013 = pd.read_excel('figures2013.ods', engine='odf')
fig2016 = pd.read_excel('figures2016.ods', engine='odf')
fig2019 = pd.read_excel('figures2019.ods', engine='odf')

def getMean(df):
    # Titles
    col1 = df[df.columns[0]]
    titles = col1.tolist()

    # Calculate the mean of each row
    row_means = df.mean(axis=1)
    df = pd.DataFrame({'mean_values': row_means})

    # Combine with titles
    df.index = titles
    return df

def visualise(df):
    df.plot(kind='bar', x=df.index, y='pm 2.5')
    plt.xlabel('Index')
    plt.ylabel('Column Name')
    plt.title('Bar Chart')
    plt.show()#

df = getMean(fig2013)
visualise(df)