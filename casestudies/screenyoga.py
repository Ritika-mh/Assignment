import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import figure,show
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory


# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
data = pd.read_csv("Screen Time Data.csv")

data.head()

data.info()

data.isnull()

df=data.copy()
df.head(27)

# Group the data by "Week Day" and sum the values for each activity
activity_totals = df.groupby('Week Day').sum()

# Select the columns to include in the plot
plot_columns = ['Social Networking', 'Reading and Reference', 'Other', 'Productivity', 'Health and Fitness', 'Entertainment', 'Creativity', 'Yoga']
# Plot the results as a stacked bar chart
activity_totals[plot_columns].plot(kind='bar', stacked=True)
print("plot1")
plt.show()

# Group the data by "Week Day" and sum the values for each activity
activity_totals = df.groupby('Week Day').sum()

# Select the columns to plot
plot_columns = ['Social Networking', 'Reading and Reference', 'Other', 'Productivity', 'Health and Fitness', 'Entertainment', 'Creativity', 'Yoga']

# Iterate over the columns and create a plot for each one
for column in plot_columns:
    # Set the size of the figure
    plt.figure(figsize=(10, 6))

    # Plot the column as a bar chart
    activity_totals[column].plot(kind='bar')

    # Set the title and labels
    plt.title(column)
    plt.xlabel('Week Day')
    plt.ylabel('Time (minutes)')

    # Show the plot
    plt.show()
df.set_index('Date', inplace=True)
# Create a line plot of the screen time data with a larger figure size
df.plot(y=['Social Networking', 'Reading and Reference', 'Other', 'Productivity', 'Health and Fitness', 'Entertainment', 'Creativity'], figsize=(10,5))
# Add a title and axis labels
plt.title('Screen Time by Activity')
plt.xlabel('Date')
plt.ylabel('Minutes')
# Show the plot
plt.show()
# Create a scatter plot of the data
df.plot(kind='scatter', x='Total Screen Time ', y='Yoga', figsize=(5,5))
# Add a title and axis labels
plt.title('Screen Time vs. Yoga')
plt.xlabel('Total Screen Time (minutes)')
plt.ylabel('Yoga (0=No, 1=Yes)')
# Show the plot
plt.show()
import scipy.stats as stats
# Perform a t-test to determine the statistical significance of the relationship
t, p = stats.ttest_ind(df['Total Screen Time '], df['Yoga'])
print(f't-statistic: {t:.3f}, p-value: {p:.3f}')
df[['Social Networking', 'Reading and Reference', 'Other', 'Productivity', 'Health and Fitness', 'Entertainment', 'Creativity']].plot(kind='bar', figsize=(20,10),linewidth=10)

# Add a title and axis labels
plt.title('Screen Time by Activity')
plt.xlabel('Date')
plt.ylabel('Minutes')

# Show the plot
plt.show()


df.plot(kind='bar', x='Week Day', y='Total Screen Time ')
plt.title('Total Screen Time by Week Day')
plt.xlabel('Week Day')
plt.ylabel('Total Screen Time')
plt.show()

df.columns = df.columns.str.strip()


df_yoga = df[df['Yoga'] > 0]
df_no_yoga = df[df['Yoga'] == 0]


mean_total_screen_time_yoga = df_yoga['Total Screen Time'].mean()
mean_total_screen_time_no_yoga = df_no_yoga['Total Screen Time'].mean()

print(f'Mean total screen time on days with yoga: {mean_total_screen_time_yoga:.2f}')
print(f'Mean total screen time on days without yoga: {mean_total_screen_time_no_yoga:.2f}')


df_yoga_by_category = df_yoga.groupby('Social Networking')
df_no_yoga_by_category = df_no_yoga.groupby('Social Networking')

mean_screen_time_yoga_by_category = df_yoga_by_category['Total Screen Time'].mean()
mean_screen_time_no_yoga_by_category = df_no_yoga_by_category['Total Screen Time'].mean()

print(f'Mean total screen time on days with yoga: {mean_total_screen_time_yoga:.2f}')
print(f'Mean total screen time on days without yoga: {mean_total_screen_time_no_yoga:.2f}')

print('Mean screen time by category on days with yoga:')
print(mean_screen_time_yoga_by_category)

print('Mean screen time by category on days without yoga:')
print(mean_screen_time_no_yoga_by_category)


mean_total_screen_time = pd.DataFrame({'Yoga': mean_total_screen_time_yoga, 'No Yoga': mean_total_screen_time_no_yoga}, index=['Total Screen Time'])
mean_total_screen_time.plot.bar()

df['Week Day'] = df['Week Day'].astype('category')
mean_total_screen_time_by_weekday = df.groupby('Week Day')['Total Screen Time'].mean()
mean_total_screen_time_by_weekday.plot.bar()

plt.title('Total Screen Time by Day of the Week')

df['Week Day'] = df['Week Day'].astype('category')
df_by_weekday_social_networking = df.groupby(['Week Day', 'Social Networking'])
mean_screen_time_by_weekday_social_networking = df_by_weekday_social_networking['Total Screen Time'].mean()
mean_screen_time_by_weekday_social_networking = mean_screen_time_by_weekday_social_networking.unstack()


