import math

import graphique


sin_scatter = graphique.series.Scatter([(x, math.sin(x / 10) * 10 + 20) for x in range(100)])
cos_scatter = graphique.series.Scatter([(x, math.cos(x / 10) * 10 + 20) for x in range(100)])
tan_scatter = graphique.series.Scatter([(x, math.tan(x / 10) * 10 + 20) for x in range(100)])

chart = graphique.Chart([sin_scatter, cos_scatter, tan_scatter])
chart.title = 'Sine, Cosine & Tangent'
chart.size = graphique.Size(1000, 500)

renderer = graphique.renderer.Cairo(chart)
renderer.draw()
renderer.save('chart.png')
