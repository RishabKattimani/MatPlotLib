# ------------------------------------------------------------------------------
# Imports

import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# Data

x = [1, 2, 3, 4, 5, 6, 7]

first_y = [70, 89, 58, 99, 92, 78, 75]
second_y = [70, 80, 82, 86, 90, 92, 99]

# ------------------------------------------------------------------------------
# Extras

plt.xlabel('Time Studied (Hours)')
plt.ylabel('Test Scores')

plt.title('Time Studied Vs. Test Scores of Different Schools')

# ------------------------------------------------------------------------------
# Plotting Data

plt.plot(x, first_y)
plt.plot(x, second_y)
plt.show()
