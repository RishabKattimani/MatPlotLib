# ------------------------------------------------------------------------------
# Imports

import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# Data

values = [200, 2530, 80, 540, 394]
labels = ['Cell Plone Bill', 'Mortgage', 'Electric', 'Water Bill', 'Others']

# ------------------------------------------------------------------------------
# Plotting Data

plt.pie(values, labels=labels, explode=[0.1, 0, 0, 0, 0,], shadow=True)
plt.show()
