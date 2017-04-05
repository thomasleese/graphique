import gayplot


dataset = gayplot.Dataset(
    [(str, 'Fruit'), (int, 'Amount')],
    [
        ('Apples', 2),
        ('Bananaes', 4),
        ('Pears', 3),
        ('Peaches', 1)
    ]
)

chart = gayplot.PieChart(dataset)
chart.title = 'Different Fruits'
chart.size = gayplot.Vector(2000, 1200)
chart.layout()

renderer = gayplot.CairoRenderer(chart)
renderer.draw()
renderer.save('chart.png')
