'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt


# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def barplots_fta(pred_universe):
    '''
    Produces various types of bar plots using the given datasets

    Parameters:
    - pred_universe dataframe

    Returns:
    - Vertical barplot
    '''
    #print (pred_universe.columns.values)
    #fta_df =pred_universe[['fta']]
    #print(fta_df.head(10))
    sns.countplot(data=pred_universe, x='fta')
    #sns.countplot(data=fta_df, x='fta')
    #sns.barplot(x=fta_df.fta.value_counts().index, y=fta_df.fta.value_counts())
    plt.savefig('./data/part3_plots/vertical_barplot.png', bbox_inches='tight')


# 2. Hue the previous barplot by sex
def barplots_hue_sex(pred_universe):
    #fta_df =pred_universe[['fta','sex']]
    sns.countplot(data=pred_universe, x='fta', hue='sex')
    #sns.countplot(data=fta_df, x='fta', hue='sex')
    #sns.barplot(x=fta_df.fta.value_counts().index, y=fta_df.fta.value_counts(),  hue='sex')
    plt.savefig('./data/part3_plots/vertical_barplot_with_hue.png', bbox_inches='tight')


# 3. Plot a histogram of age_at_arrest
def histograms_age(pred_universe):
    '''
    Produces different types of histograms using the given dataset

    Parameters:
    - pred_universe dataframe

    Returns:
    - Histogram without specifying bins for age_at_arrest
    '''
    sns.histplot(data=pred_universe, 
                 x='age_at_arrest')
    plt.savefig('./data/part3_plots/histogram.png', bbox_inches='tight')


# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def histograms_bin(pred_universe):
    '''
    Produces different types of histograms using the given dataset

    Parameters:
    - pred_universe dataframe

    Returns:
    - Histogram with a specified number of bins
    '''
    sns.histplot(data=pred_universe, 
                 x='age_at_arrest',
                 bins=[18, 21, 30, 40, 100])
    plt.savefig('./data/part3_plots/histogram_bin.png', bbox_inches='tight')

