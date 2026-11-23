"""
Name: Michael Ko
File Name: cosine_wave.py
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 11/22/2026
Purpose: Generating data and visualizing it using the matplotlib library 
- Imported the matplotlib.pyploy and math
Starter Code: Based on Chapter 15 of the Textbook but mostly from the Weekly Lecture recording on November 19th and the instructions on Blackboard
"""

import math
import matplotlib.pyplot as plt

x_values = []
y_values = []

for degree in range(0, 721):
    x_values.append(degree)
    y_values.append(math.cos(math.radians(degree)))

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

"""Part of the Optional Challenge: Plotting with a custom color, line style, and thickness"""
ax.plot(x_values, y_values, color="black", linestyle="-", linewidth=2.5)

"""Setting chart title and labeling the axes"""
ax.set_title("Cosine Wave: y = cos(x)", fontsize=24)
ax.set_xlabel("x (degrees)", fontsize=14)
ax.set_ylabel("cos(x)", fontsize=14)

"""Setting tick marks every 90 degrees and the size of tick labels"""
ax.set_xticks(range(0, 721, 90))
ax.tick_params(labelsize=14)

"""Showing the Image"""
plt.savefig("cosine.png", bbox_inches="tight")
plt.show()