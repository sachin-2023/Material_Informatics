#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# views.py
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt

def scatter_plot(request):
    # Load the dataset
    data = pd.read_csv('materials_data.csv')

    # Create a scatter plot
    plt.scatter(data['property1'], data['property2'])
    plt.xlabel('Property 1')
    plt.ylabel('Property 2')
    plt.title('Material Property Scatter Plot')
    plt.savefig('scatter_plot.png')

    return render(request, 'scatter_plot.html')

# scatter_plot.html
<img src="scatter_plot.png" alt="Scatter Plot">

