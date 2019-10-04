# calculate the square root of the area
import numpy as np
dfValues['square'] = np.sqrt(dfValues['area'])
display(dfValues)

# calculate the difference between the square root of the area and the height
dfValues['difference'] = dfValues['square'] - dfValues['height']
display(dfValues)

# display the difference column of each buildings
display(dfValues['difference'].plot(kind='bar', figsize=(20,32)))

# add labels to the dataset
dfLabels = pd.read_csv("labels.csv")
df = dfValues.set_index('building_id').join(dfLabels.set_index('building_id'))

# calculate correlation
df['damage_grade'].corr(df['difference'])

# write out data
df.to_csv("new_values.csv",index=False,sep=',')