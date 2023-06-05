#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt

# Load the dataset
X, y = load_material_data()

# Create a scatter plot of two properties
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.xlabel('Property 1')
plt.ylabel('Property 2')
plt.title('Material Property Visualization')
plt.colorbar(label='Material Class')
plt.show()

