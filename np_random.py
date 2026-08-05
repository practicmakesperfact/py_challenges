from numpy import random
import numpy as np
#generate random float numbers between 0 and 1
# x = random.rand(6)
# print(x)

#generate random numbers from array

# x = random.choice([3, 5, 7, 9],size=(3,4))
# print(x)


#probability distribution function(pdf)

# x = random.choice([4,7,3,9],p=[0.1,0.3,0.6,0.0],size=(3,4))
# print(x)

# import numpy as np
# arr = random.shuffle(np.array([3,4,6,7,8,9]))
# print(arr)  

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(np.array([0,1,2,3,4,5]), kind="kde")
plt.show()