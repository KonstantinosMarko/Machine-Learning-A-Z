import numpy as np
import pandas as pd

# ftiaxnw pandas DataFrame
country = np.array(['Greece', 'Germany', 'France', 'Sweden' ])

salary = np.array([10000, 35000, 30000, 40000])

life_exp = np.array([82.5, 69, 72, 85])


data = {'country': country, 'salary': salary, 'life_exp': life_exp }
data_df = pd.DataFrame(data, columns = ['country', 'salary', 'life_exp'])



# prosthetw sto dataframe ena neo column me to onoma age
age = [12, 14 , 15 ,18]

age = pd.Series(age, name = 'age')

data_df = pd.concat([data_df, age], axis=1)


print(data_df[['country','salary']])

mean = data_df.mean()
#vriskw to age gia salary > 30000 kai sti sunexeia se ena neo Series vazw osa age > 15
k = data_df['age'][data_df['salary'] > 30000]


n =[]
for item in k:
    if item > 15:
        n.append(item)
