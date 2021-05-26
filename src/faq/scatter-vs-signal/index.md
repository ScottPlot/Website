---
title: ScatterPlot vs SignalPlot - ScottPlot FAQ
description: Scatter and signal plots are the most commonly used plot types, so ensure you understand the pros and cons of each
---

# Scatter Plot vs. Signal Plot

💡 ***Favor SignalPlot over ScatterPlot***

Scatter and signal plots are the most commonly used plot types, so ensure you understand the pros and cons of each:

* **Scatter plots have paired X/Y data points.** Scatter plots are designed to display ***hundreds*** of points, but performance rapidly drops as the number of points increases, so scatter plots are not appropriate for large datasets.

* **Signal plots have Y data and a sample rate.** Signal plots are optimized for performance and can render datasets with ***millions*** of points at a high framerate.

* **SignalConst** plots uses an algorithm optimized for constant data values, allowing interactive rendering of ***hundreds of millions*** of data points at a high framerate.
