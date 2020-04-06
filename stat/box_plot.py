import seaborn as sns
import pandas as pd


def box_plot(groups=None, names=None):
    if not groups:
        raise Exception('No groups provided')
    if not names:
        names = list(range(len(groups)))
        names = list(map(str, names))
    if len(names) != len(groups):
        raise Exception('Different number of groups and names provided')
        
    df = pd.DataFrame(columns=['value', 'group'])
    
    for idx in range(len(groups)):
        df = pd.concat([df, pd.DataFrame({'value' :groups[idx], 'group' :names[idx]})])
        
    sns.boxplot(x='group', y='value', data=df)
   
if __name__ == '__main__':
    x, y, z = np.random.normal(20, 5, 100), np.random.normal(12, 4, 100), np.random.normal(35, 9, 100)
    box_plot(groups=[x, y, z])
