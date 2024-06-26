import pandas as pd
import matplotlib.pyplot as plt
import calendar
import seaborn as sns

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

"""
def average_percentage_docks_available_per_month_year(df):
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
    avg_percentage = df.groupby('date')['percentage_docks_available'].mean()
    return avg_percentage

def average_percentage_docks_available_per_day_of_week(df):
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
    df['day_of_week'] = df['date'].dt.day_name()
    avg_percentage = df.groupby('day_of_week')['percentage_docks_available'].mean()
    return avg_percentage

def average_percentage_docks_available_per_month(df):
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
    avg_percentage = df.groupby(df['date'].dt.month)['percentage_docks_available'].mean()
    return avg_percentage

def average_percentage_docks_available_by_holiday(df):
    avg_percentage = df.groupby('festius')['percentage_docks_available'].mean()
    return avg_percentage


def average_percentage_docks_available_by_weekend(df):
    avg_percentage = df.groupby('is_weekend')['percentage_docks_available'].mean()
    return avg_percentage

df = load_data("../full_data.csv")

avg_percentage_per_month_year = average_percentage_docks_available_per_month_year(df)
avg_percentage_per_day_of_week = average_percentage_docks_available_per_day_of_week(df)
avg_percentage_per_month = average_percentage_docks_available_per_month(df)
avg_percentage_by_holiday = average_percentage_docks_available_by_holiday(df)
avg_percentage_by_weekend = average_percentage_docks_available_by_weekend(df)

# Svae path
results = 'data/results/images/'

# Plotting
#fig1, ax1 = plt.subplots(figsize=(8, 6))
#ax1.plot(avg_percentage_per_month_year.index, avg_percentage_per_month_year.values, marker='o', color='skyblue')
#ax1.set_xlabel('Date')
#ax1.set_ylabel('Average Percentage Docks Available')
#plt.xticks(rotation=45)
#fig1.savefig(results+"average_percentage_per_month_year.png")

#fig2, ax2 = plt.subplots(figsize=(8, 6))
#avg_percentage_per_day_of_week = avg_percentage_per_day_of_week.reindex(list(calendar.day_name))  # Convert to list
#ax2.bar(avg_percentage_per_day_of_week.index, avg_percentage_per_day_of_week.values, color='skyblue')
#ax2.set_xlabel('Day of the Week')
#ax2.set_ylabel('Average Percentage Docks Available')
#fig2.savefig(results+"average_percentage_per_day_of_week.png")

fig3, ax3 = plt.subplots(figsize=(8, 6))
ax3.bar(avg_percentage_per_month.index, avg_percentage_per_month.values, color='skyblue')
ax3.set_xlabel('Month')
ax3.set_ylabel('Average Percentage Docks Available')
ax3.set_xticks(range(1, 13))
ax3.set_xticklabels(calendar.month_name[1:], rotation=45)
fig3.tight_layout()  
fig3.savefig(results+"average_percentage_per_month.png", bbox_inches='tight')

# Plotting average percentage docks available by holiday
fig4, ax4 = plt.subplots(figsize=(8, 6))
colors = ['skyblue', 'lightcoral']
ax4.bar(avg_percentage_by_holiday.index, avg_percentage_by_holiday.values, color=colors)
ax4.set_xlabel('Holiday (0 = No, 1 = Yes)')
ax4.set_ylabel('Average Percentage Docks Available')
ax4.set_ylim(0.56, 0.64)
ax4.set_xticks([0, 1])
ax4.set_xticklabels(['No', 'Yes'])
plt.tight_layout()
plt.savefig(results+"average_percentage_by_holiday.png", bbox_inches='tight')


fig, ax = plt.subplots(figsize=(8, 6))
colors = ['skyblue', 'lightcoral']
ax.bar(avg_percentage_by_weekend.index, avg_percentage_by_weekend.values, color=colors)
ax.set_xlabel('Weekend (1) vs Weekday (0)')
ax.set_ylabel('Average Percentage Docks Available')
ax.set_ylim(0.56, 0.64)
ax.set_xticks([0, 1])
ax.set_xticklabels(['Weekday', 'Weekend'])
plt.tight_layout()
plt.savefig(results+"average_percentage_by_weekend.png", bbox_inches='tight')


## Pivot table to calculate average docks availability by hour and day
#pivot_table = df.pivot_table(index='hour', columns='day_of_week', values='percentage_docks_available', aggfunc='mean')
#
## Plotting heatmap
#fig, ax = plt.subplots(figsize=(10, 8))
#sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='.1f', cbar_kws={'label': 'Average Percentage Docks Available'}, ax=ax)
#ax.set_xlabel('Day of the Week')
#ax.set_ylabel('Hour of the Day')
#fig.savefig(results+"average_percentage_by_hour_and_day.png")

## Seasonal Trends
#df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
#df['season'] = df['date'].dt.month % 12 // 3 + 1
#seasonal_trends = df.groupby('season')['percentage_docks_available'].mean()
#
#fig, ax = plt.subplots()
#ax.bar(seasonal_trends.index, seasonal_trends.values, color='skyblue')
#ax.set_xlabel('Estació')
#ax.set_ylabel('Average Percentage Docks Available')
#ax.set_xticks([1, 2, 3, 4])
#ax.set_xticklabels(['Hivern', 'Primavera', 'Estiu', 'Tardor'])
#plt.savefig(results+"seasonal_trends.png")

# Weather Impact
#fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
#
#sns.scatterplot(x='mm_precip', y='percentage_docks_available', data=df, ax=ax1)
#ax1.set_xlabel('Precipitation (mm)')
#ax1.set_ylabel('Percentage Docks Available')
#
#sns.scatterplot(x='temperature', y='percentage_docks_available', data=df, ax=ax2)
#ax2.set_xlabel('Temperature')
#ax2.set_ylabel('Percentage Docks Available')
#
#plt.savefig(results+"weather_impact.png")
#
## Geospatial Analysis
#plt.figure(figsize=(10, 6))
#plt.scatter(df['lon'], df['lat'], c=df['percentage_docks_available'], cmap='coolwarm', alpha=0.5)
#plt.colorbar(label='Percentage Docks Available')
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
#plt.savefig(results+"geospatial_distribution.png")
#
# Correlation Matrix
# Calculate the correlation matrix
corr_matrix = df[['percentage_docks_available', 'capacity', 'mm_precip', 'temperature', 'rating']].corr()

plt.figure(figsize=(10, 8))  # Adjusted the figure size to give more room
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')

plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0) 

plt.tight_layout()  
plt.savefig(results+"correlation_matrix.png")


#Categorize precipitation into no rain (0 mm) and rain (> 0 mm)
df['precip_category'] = df['mm_precip'].apply(lambda x: 'No Rain' if x == 0 else 'Rain')

# Plot the impact of precipitation categories on dock availability
fig, ax1 = plt.subplots(figsize=(8, 6))

sns.boxplot(x='precip_category', y='percentage_docks_available', data=df, ax=ax1)
ax1.set_xlabel('Precipitation Category')
ax1.set_ylabel('Percentage Docks Available')

plt.tight_layout()
plt.savefig(results+"weather_impact_comparison.png") 
"""


df = load_data("../full_data.csv")
# Svae path
results = 'data/results/images/'

average_docks_available = df.groupby('capacity')['percentage_docks_available'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='capacity', y='percentage_docks_available', data=average_docks_available, 
            hue = 'capacity', palette='viridis', legend =False)
plt.xlabel('Capacity', fontsize=14)
plt.ylabel('Average Percentage of Docks Available', fontsize=14)

# Save the plot
plt.savefig(results+'capacity.png') 


# Create a datetime column
df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])

# Group by date and calculate the average capacity
df['date'] = df['datetime'].dt.date
average_capacity_daily = df.groupby('date')['capacity'].mean().reset_index()

# Convert 'date' back to datetime for plotting
average_capacity_daily['date'] = pd.to_datetime(average_capacity_daily['date'])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(average_capacity_daily['date'], average_capacity_daily['capacity'], marker='o')
plt.xlabel('Time', fontsize=14)
plt.ylabel('Average Capacity', fontsize=14)

# Save the plot
plt.savefig(results+'average_capacity_daily.png')

average_percentage_docks_available = df.groupby('capacity')['percentage_docks_available'].mean().reset_index()

# Calculate the correlation
correlation_avg = average_percentage_docks_available['capacity'].corr(average_percentage_docks_available['percentage_docks_available'])

# Plotting
plt.figure(figsize=(10, 6))
sns.scatterplot(x='capacity', y='percentage_docks_available', data=average_percentage_docks_available)
plt.title(f'Correlation between Capacity and Average Percentage of Docks Available\nCorrelation Coefficient: {correlation_avg:.2f}', fontsize=16)
plt.xlabel('Capacity', fontsize=14)
plt.ylabel('Average Percentage of Docks Available', fontsize=14)

# Save the plot
plt.savefig(results+'capacity_utilization_correlation.png')