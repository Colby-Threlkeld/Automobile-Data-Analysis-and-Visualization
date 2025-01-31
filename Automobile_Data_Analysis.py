import pandas as pd
from matplotlib import pyplot as plt

car_info = pd.read_csv('car_info.csv')
print(car_info)

#GOAL 2 -- Print names of Japanese cars with V6 engines
def jap_v6_cars(car_info):
    car_names = car_info[(car_info['origin'] == 'japan') & (car_info['cylinders'] == 6)]
    return car_names['name']

#GOAL 3 -- Print names of cars with a missing value for horsepower
def hp_missing(car_info):
    null_hp = car_info[car_info['horsepower'].isnull()]
    return null_hp['name']

#GOAL 4 -- Print number of cars with a mpg >= 20
def mpg_filter(car_info):
    num_of_cars = car_info[car_info['mpg'] >= 20]
    return num_of_cars['mpg'].count()

#GOAL 5 -- Print name of most efficient car
def best_mpg(car_info):
    max_mpg_idx = car_info['mpg'].idxmax()
    return car_info.loc[max_mpg_idx, 'name']

#GOAL 6 -- Prints the max, min, and mean for weight
def max_min_mean(car_info):
    max = car_info['weight'].max()
    min = car_info['weight'].min()
    mean = car_info['weight'].mean()
    return print(f'\nTASK --> 6:\nMinimum weight: {min}, Maximum weight: {max}, Average weight: {mean:.2f}')

#GOAL 7 -- Prints the shape of the dataframe after altering it | .dropna() method for dropping rows with missing values
def drop_null_rows(car_info):
    new_car_info = car_info.dropna(inplace = False)
    return new_car_info.shape


#TASK 1 -- Shape of DF
print('TASK --> 1:\nShape of the DataFrame:\n',car_info.shape)
print('\nTASK --> 2:\nJapanese cars with V6:\n',jap_v6_cars(car_info))
print('\nTASK --> 3:\nCars with missing horsepower data:\n',hp_missing(car_info))
print('\nTASK --> 4:\nNumber of cars with MPG >= 20:\n',mpg_filter(car_info))
print('\nTASK --> 5:\nMost fuel-efficient car:\n',best_mpg(car_info))
max_min_mean(car_info)
print('\nTASK --> 7:\nNew DataFrame Shape:\n', drop_null_rows(car_info))

#GOAL 8 -- using .value_counts method to count how many cars belong to each origin
origin_data = car_info['origin'].value_counts()

#GOAL 8 -- using the data gathered we implement it into the pie chart | converted the numbers to a percentage using 'autopct'
plt.pie(origin_data, labels = origin_data.index, autopct='%1.1f%%')

#GOAL 9 -- Create subplots with 2 rows and 1 column | figsize to fit everything on screen
fig, ax = plt.subplots(2, 1, figsize = (15, 10))

#sorting the data by the x values only (for line plot)
sorted_car_info = car_info.sort_values(by='displacement')

#Line plot for -- GOAL 9
ax[0].plot(sorted_car_info['displacement'], sorted_car_info['mpg'], label='MPG vs Displacement')
ax[0].set_xlabel('Displacement')
ax[0].set_ylabel('MPG')
ax[0].set_title('Line Plot: MPG vs Displacement')
ax[0].legend()

#Scatter plot for -- GOAL 9
ax[1].scatter(car_info['weight'], car_info['mpg'], label='MPG Vs. Weight')
ax[1].set_xlabel('Weight')
ax[1].set_ylabel('MPG')
ax[1].set_title('Scatter Plot: MPG Vs. Weight')
ax[1].legend()

plt.show()