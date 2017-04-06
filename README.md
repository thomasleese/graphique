![Graphique - Better charts for Python](logo.png)

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
chart.size = graphique.Vector(1000, 1000)

renderer = graphique.CairoRenderer(chart)
renderer.draw()
renderer.save('chart.png')
```
