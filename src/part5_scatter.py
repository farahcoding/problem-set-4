'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
def scatterplot_hue(pred_universe):
    '''
    Produces scatter plots using the given dataset

    Parameters:
    - pred_universe dataframe

    Returns:
    - Scatterplot with hue by felony
    '''

    sns.lmplot(data=pred_universe, 
               x='prediction_felony', 
               y='prediction_nonfelony',
               fit_reg=False,
               hue='y_felony'
               )
    plt.savefig('./data/part5_plots/scatterplot_hue_felony.png', bbox_inches='tight')
    

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
def scatterplot(pred_universe):
    '''
    Produces scatter plots using the given dataset

    Parameters:
    - pred_universe dataframe

    Returns:
    - Scatterplot with hue by felony
    '''
    sns.lmplot(data=pred_universe, 
               x='prediction_felony', 
               y='y_felony',
               fit_reg=False
               )
    plt.savefig('./data/part5_plots/scatterplot.png', bbox_inches='tight')
    print('This model is not calibrated.')
