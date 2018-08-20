import numpy as np
import pandas as pd

#dimiourgia pinakwn 
name = np.array(['Brand', 'Cunning', 'Allen'])
age = np.array([22, 38, 26])
fare = np.array([6.28, 7.25, 4.25])
survived = np.array([True, True, False])

#enwsi pinakwn
data = {'name': name, 'age': age, 'fare': fare, 'survived': survived}
data = pd.DataFrame(data, columns = ['name', 'age', 'fare', 'survived'])

#typwnei ta onomata
data['name']

#tupwnei ta onomata kai tis ilikies
data[['name', 'age']]

#tupwnei ola ta features tis deuteris seiras
data.loc[1]

#tupwnei tin deuteri kai triti grammi kai tin prwti, deuteri kai triti stili 
#(to 1:3 simainei oti tupwnei to col. 1 kai to col.2 kai oxi to col.3)
data.iloc[1:3, 0:3]

#tupwnei tis grammes pou exoun ilikia > 25
data[data['age'] > 25]

#tupwnei ta apotelesmata gia survived apo osous exoun age > 25
data['survived'][data['age'] > 25]

#gia na xrisimopoiisw sunartiseis (p.x. tou numpy):
data.apply(np.mean)
# alliws
data.mean()
