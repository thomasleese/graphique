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

cairo = gayplot.CairoRenderer(chart)
cairo.draw()
cairo.save('chart.png')
