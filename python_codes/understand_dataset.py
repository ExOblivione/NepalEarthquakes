# Read in features (values.csv)
import pandas as pd

dfValues = pd.read_csv("values.csv")

display(dfValues)

# Get statistical info
dfValues.describe()

# Different types in the dataset
dfValues.dtypes

# Investigate has_ columns
dfValues.has_superstructure_adobe_mud.unique()

# Plot of age column
display(dfValues.boxplot(column='age'))

# Investigate non-numerical columns
dfValues.land_surface_condition.value_counts()