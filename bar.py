# ------------------------------------------------------------------------------
# Imports

import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------------
# Data

people = ['Rishab', 'John', 'Hitesh', 'Jimmy', 'Rony']
scores = [100, 89, 58, 99, 20]

ypos = np.arange(len(people))

# ------------------------------------------------------------------------------
# Extras

plt.xticks(ypos, people)

plt.xlabel('People')
plt.ylabel('Test Scores')

plt.title('People Vs. Test Scores of Students')

# ------------------------------------------------------------------------------
# Plotting Data

plt.bar(ypos, scores)
plt.show()
