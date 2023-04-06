import numpy as np
import matplotlib.pyplot as plt

nan_data = '/Users/cgcouto/Downloads/data_release_baysor_merfish_gut/assignment_6_boundaries/nan_distribution.npy'

data = np.load(nan_data)

print(data)

filter = [val for val in data if val[0] == 0]

counts = [(val[1]) for val in filter]

# percent_with_nans = (len([val for val in data if val != 0])/len(data))*100

# percent_under_1 = (len([val for val in data if val != 0 and val < 1])/len([val for val in data if val != 0]))*100
# percent_under_2 = (len([val for val in data if val != 0 and val < 2])/len([val for val in data if val != 0]))*100

# print(percent_under_1)
# print(percent_under_2)
# print(len([val for val in data if val != 0 and val > 10]))
# print(len([val for val in data if val != 0 and val > 3]))
# print(len([val for val in data if val != 0]))

# # print(len([val for val in data if val > 1])/len([val for val in data if val != 0])*100)

# print(np.sort(data)[::-1])

plt.hist(counts, bins=100)
plt.title('Boundary size for normal boundaries',fontname="Helvetica")
plt.xlabel('Number of points in non NaN-containing boundaries',fontname="Helvetica")
plt.ylabel('Number of boundaries',fontname="Helvetica")
plt.show()

# print(np.sort(test)[::-1])
