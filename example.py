import gayplot


dataset = gayplot.Dataset(
    [(float, 'X'), (float, 'Y')],
    [(x * 3, x) for x in range(100)],
)

chart = gayplot.ScatterChart(dataset)
chart.title = 'Scatter Chart'
chart.size = gayplot.Vector(1000, 1000)
chart.layout()

renderer = gayplot.CairoRenderer(chart)
renderer.draw()
renderer.save('chart.png')
