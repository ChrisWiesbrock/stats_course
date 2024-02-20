#converter

all_cities = pd.DataFrame()
for i in range(len(files)):
    city = pd.read_csv(files[i])
    city['Date'] = city['Date'].astype(str)
    city['Year'] = city['Date'].str[:4]
    city['Month'] = city['Date'].str[4:6]
    city['Day']=city['Date'].str[6:]
    city['ID']=i
    all_cities = pd.concat([all_cities, city], ignore_index=True)
    
all_cities.columns=city.columns

    


all_cities = all_cities.rename(columns={"Sunshine Duration" : "Sunshine_Duration"}) # make name pythonic
all_cities = all_cities.rename(columns={"Air Temperature" : "Air_Temperature"}) # make name pythonic
all_cities = all_cities.rename(columns={"Cloud Coverage" : "Cloud_Coverage"}) # make name pythonic

all_cities=all_cities[all_cities['Air_Temperature']>-50]

all_cities=all_cities.iloc[::200]

all_cities=all_cities[['Air_Temperature', 'Year','ID']]

print(all_cities)
      
sns.violinplot(data=all_cities, x='ID', y='Air_Temperature')

############TWo factor ANOVA##########

import statsmodels.api as sm
from statsmodels.formula.api import ols

model = ols('Air_Temperature ~ C(Year) + C(ID) + C(Year):C(ID)', data=all_cities).fit()
sm.stats.anova_lm(model, typ=2)
