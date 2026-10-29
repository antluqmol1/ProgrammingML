import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("datasets/lab1/housing.csv")

# 1 How many geographical units are there in the dataset?
print("\nExercise 1: How many geographical units are there in the dataset?")

print("longtitude and lattitude would be the geographical units, ocean_proximity is a geographic variable\n and population is a socio-demographic variable but not a unit")

# 2. What is the mean house value among all “Ocean_proximity” categories?
print("\nExercise 2: What is the mean house value among all “Ocean_proximity” categories?")

def mean(list):
    sum = 0.
    for i in list:
        sum += i
    sum = sum / len(list)
    return sum

lhouses = data["median_house_value"].tolist()

print(mean(lhouses))

# 3. What is the mean house value in each “Ocean_proximity” category?
print("\nExercise 3: What is the mean house value in each “Ocean_proximity” category?")

def mean_house_value_by_proximity(data):
    l_ocean_proximities = []

    for value in data["ocean_proximity"]:
        if value not in l_ocean_proximities:
            l_ocean_proximities.append(value)
    print(l_ocean_proximities)

    dicc = {}
    for proximity, value in zip(data["ocean_proximity"], data["median_house_value"]):
        if proximity not in dicc:
            dicc[proximity] = [value]
        else:
            dicc[proximity].append(value)

    for proximity, values in dicc.items():
        dicc[proximity] = mean(values)
    return dicc

print(mean_house_value_by_proximity(data))

# dict.items() produces:
# proximity = "NEAR BAY"
# values = [452600, 358500]
# if was not with items() would try to unpack key in 2 variables


# 4. What can you tell about the differences between the mean and median values
# “Ocean_proximity” categories?
print("\nExercise 4: What can you tell about the differences between the mean and median values “Ocean_proximity” categories?")

def median(list):
    n = len(list)
    if n%2 == 1:
        mod = n // 2 - 1
        return list[mod]
    else:
        m1 = list[n // 2 - 1]
        m2 = list[n // 2]
        return (m1+m2)/2

def median_house_value_by_proximity(data):
    l_ocean_proximities = []

    for value in data["ocean_proximity"]:
        if value not in l_ocean_proximities:
            l_ocean_proximities.append(value)
    print(l_ocean_proximities)

    dicc = {}
    for proximity, value in zip(data["ocean_proximity"], data["median_house_value"]):
        if proximity not in dicc:
            dicc[proximity] = [value]
        else:
            dicc[proximity].append(value)

    for proximity, values in dicc.items():
        dicc[proximity] = median(values)
    return dicc

print(median_house_value_by_proximity(data))

# 5. Create a histogram for “households”, “median_income”, “housing_median_age” and
# “median_house_value”.
print("\nExercise 5: Create a histogram for “households”, “median_income”, “housing_median_age” and “median_house_value”. ")

'''
lhouseholds = data["households"].tolist()
lmedian_income = data["median_income"].tolist()
lhousing_median_age = data["housing_median_age"].tolist()
lmedian_house_value = data["median_house_value"].tolist()

plt.hist(lhouseholds)
plt.title("Households")
plt.xlabel("Households")
plt.ylabel("Frequency")
plt.show()

plt.hist(lmedian_income)
plt.title("Median Income")
plt.xlabel("Median Income")
plt.ylabel("Frequency")
plt.show()

plt.hist(lhousing_median_age)
plt.title("Housing Median Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.hist(lmedian_house_value)
plt.title("Median House Value")
plt.xlabel("House Value")
plt.ylabel("Frequency")
plt.show()

'''

# 6. What do you notice about the graphs? Specifically focus on end of “housing_median_age” and
# “median_house_value graphs”. What do you think about the magnitude of the values in
# “median_house_value”?

print("\nExercise 6: What do you notice about the graphs?")

print('''The graph of households shows that mosts of the districts have around 0-500 houses, then around 500-1000 houses (frecuency of 4000)
The graph of median income shows mosts of the houses have a median income of 2-3, then 3-4, then 4-5, then 0.8ish - 2...
The graph of median age shows that the house age of 32-36 are the most popular, followed by 16-21, 21-26, 26-32, 11-16, 47-52, 36-42, 42-47, 6-11, 1-6.
That could mean that most of the construction was around 32-36 years ago and looking at the end we can see that more construction happened 47-52 years ago than the following years until a good economic era 32-36 years ago.
If we look at the end of the graph we see that there is not more data after the age of 50, that could mean that they usually sell the house after kids move out or they rent it to other families while they go to more smaller places/ residences
The graph of median house value shows that the most popular house values are around 130k-160k, then 160k-220k, then 80k-130k, and then descending from 220k-260k...
The end shows that it ends the trend of the normal distribution that we could see, that probably means that the top 1% rich people make increasing heavily the price of houses in some districts''')

# 7. In which category are the most expensive and the largest houses typically located? In which
# category are the least expensive and smallest houses typically located?
print("\nExercise 7:  In which category are the most expensive and the largest houses typically located? In which category are the least expensive and smallest houses typically located?")

print('''
We have from before that the mean house values are:
{'NEAR BAY': 259212.31179039303, '<1H OCEAN': 240084.28546409807, 'INLAND': 124805.39200122119, 'NEAR OCEAN': 249433.97742663656, 'ISLAND': 380440.0}
So the most expensive houses are in 'ISLAND'
and the least expensive ones are in 'INLAND'
However, as we see in 8.), the largest houses are in 'ISLAND'
and the smallest ones are in 'INLAND'
''')

# 8. What can you tell about the quality of houses in each “Ocean_proximity” category? (e.g., the age
# of the houses, the number of rooms)
print("\nExercise 8: What can you tell about the quality of houses in each “Ocean_proximity” category?")

def mean_house_age_by_proximity(data):
    l_ocean_proximities = []

    for value in data["ocean_proximity"]:
        if value not in l_ocean_proximities:
            l_ocean_proximities.append(value)
    print(l_ocean_proximities)

    dicc = {}
    for proximity, value in zip(data["ocean_proximity"], data["housing_median_age"]):
        if proximity not in dicc:
            dicc[proximity] = [value]
        else:
            dicc[proximity].append(value)

    for proximity, values in dicc.items():
        dicc[proximity] = mean(values)
    return dicc

print(mean_house_age_by_proximity(data))

def mean_total_rooms_by_proximity(data):
    l_ocean_proximities = []

    for value in data["ocean_proximity"]:
        if value not in l_ocean_proximities:
            l_ocean_proximities.append(value)
    print(l_ocean_proximities)

    dicc = {}
    for proximity, value in zip(data["ocean_proximity"], data["total_rooms"]):
        if proximity not in dicc:
            dicc[proximity] = [value]
        else:
            dicc[proximity].append(value)

    for proximity, values in dicc.items():
        dicc[proximity] = mean(values)
    return dicc

print(mean_total_rooms_by_proximity(data))

print('''
We can observ that the quality of the houses in 'INLAND' are the best. Because the mean age house is less than the others and the number 
of rooms are bigger than the others, what is most surprising is that is the cheapest location, 
whereas in 'ISLAND', the most expensive location, we have the worst quality of houses with more age on the houses and less rooms.
''')

# 9. What can you tell about the demographic living in each “Ocean_proximity” category? (e.g.,
# population, households, median income)
print("\nExercise 9: What can you tell about the demographic living in each “Ocean_proximity” category?")

def mean_population_by_proximity(data):
    l_ocean_proximities = []
    print("Mean population by proximity:")

    for value in data["ocean_proximity"]:
        if value not in l_ocean_proximities:
            l_ocean_proximities.append(value)
    print(l_ocean_proximities)

    dicc = {}
    for proximity, value in zip(data["ocean_proximity"], data["population"]):
        if proximity not in dicc:
            dicc[proximity] = [value]
        else:
            dicc[proximity].append(value)

    for proximity, values in dicc.items():
        dicc[proximity] = mean(values)
    return dicc

print(mean_population_by_proximity(data))

def mean_households_by_proximity(data):
    l_ocean_proximities = []
    print("Mean households by proximity:")

    for value in data["ocean_proximity"]:
        if value not in l_ocean_proximities:
            l_ocean_proximities.append(value)
    print(l_ocean_proximities)

    dicc = {}
    for proximity, value in zip(data["ocean_proximity"], data["households"]):
        if proximity not in dicc:
            dicc[proximity] = [value]
        else:
            dicc[proximity].append(value)

    for proximity, values in dicc.items():
        dicc[proximity] = mean(values)
    return dicc

print(mean_households_by_proximity(data))

def mean_median_income_by_proximity(data):
    l_ocean_proximities = []
    print("Mean median income by proximity:")

    for value in data["ocean_proximity"]:
        if value not in l_ocean_proximities:
            l_ocean_proximities.append(value)
    print(l_ocean_proximities)

    dicc = {}
    for proximity, value in zip(data["ocean_proximity"], data["median_income"]):
        if proximity not in dicc:
            dicc[proximity] = [value]
        else:
            dicc[proximity].append(value)

    for proximity, values in dicc.items():
        dicc[proximity] = mean(values)
    return dicc

print(mean_median_income_by_proximity(data))

def median_house_income_by_proximity(data):
    l_ocean_proximities = []
    print("Median median income by proximity:")

    for value in data["ocean_proximity"]:
        if value not in l_ocean_proximities:
            l_ocean_proximities.append(value)
    print(l_ocean_proximities)

    dicc = {}
    for proximity, value in zip(data["ocean_proximity"], data["median_income"]):
        if proximity not in dicc:
            dicc[proximity] = [value]
        else:
            dicc[proximity].append(value)

    for proximity, values in dicc.items():
        dicc[proximity] = median(values)
    return dicc

print(median_house_income_by_proximity(data))

'''
The place with more population is in '<1H OCEAN' while the one with less is in 'ISLAND'
The place with more households is in '<1H OCEAN' while the one with less is in 'ISLAND'
The place with more average income is in '<1H OCEAN' while the one with less is in 'ISLAND'
The place with the best median income is in 'NEAR OCEAN' while the one with less is in 'ISLAND'
'''


# 10. Are there any other interesting observations and questions you can come up with regarding this
# dataset?

'''
Why the median income and median house value instad of mean, could it be more useful?
Observation: Actually, Median values are used for income and house value because these variables can be skewed by high-income households 
and expensive properties. The median is therefore more representative of a typical household/property than the mean.
'''