# ------------------------------------------------------------------------------
# Imports

import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# Data

x = [1, 2, 3, 4, 5, 6, 7]
y = [70, 89, 58, 99, 92, 78, 75]

# ------------------------------------------------------------------------------
# Extras

plt.xlabel('Time Studied (Hours)')
plt.ylabel('Test Scores')

plt.title('Time Studied Vs. Test Scores of Students')

# ------------------------------------------------------------------------------
# Plotting Data


plt.plot(x, y, color='green', linewidth=5, linestyle='dotted', marker='H', markersize=20)
plt.show()
