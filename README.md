![Graphique - Better charts for Python](logo.png)

[![Build Status](https://img.shields.io/travis/thomasleese/graphique.svg)](https://travis-ci.org/thomasleese/graphique) [![MIT Licence](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

## Installation

```bash
$ pip install graphique
```

## Example

```python
import graphique


dataset = graphique.Dataset(
    [(float, 'X'), (float, 'Y')],
    [(x * 3, x) for x in range(100)],
)

chart = graphique.ScatterChart(dataset)
chart.title = 'Scatter Chart'
chart.size = graphique.Size(1000, 1000)

renderer = graphique.CairoRenderer(chart)
renderer.draw()
renderer.save('chart.png')
```
