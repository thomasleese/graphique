from collections import namedtuple


Column = namedtuple('Column', ['name', 'type'])
Row = namedtuple('Row', ['values'])


class Dataset:
    """Data for a chart."""

    def __init__(self, columns=None, rows=None):
        self.columns = []
        self.rows = []

        if columns is not None:
            self.add_columns(*columns)

        if rows is not None:
            self.add_rows(*rows)

    def __str__(self) -> str:
        return f'{self.columns} {self.rows}'

    def add_column(self, kind, name: str = None):
        """
        Add a column to the dataset.

        Parameters
        ----------
        kind
            The type of the column.

        name
            The name of the column.
        """

        if name is None:
            name = 'Column #{n}'.format(n=len(self.columns) + 1)

        self.columns.append(Column(name, kind))

    def add_columns(self, *columns):
        """Add multiple columns to the dataset."""

        for column in columns:
            self.add_column(*column)

    def add_row(self, *row):
        """
        Add a row to the dataset. The values in the dataset are converted into
        the type specified in the column.
        """

        if len(row) > len(self.columns):
            raise ValueError('Row has more values than number of columns.')

        row = list(row) + [None] * (len(self.columns) - len(row))

        values = [
            self.columns[i].type(value)
            for i, value in enumerate(row)
        ]

        self.rows.append(Row(values))

    def add_rows(self, *rows):
        """Add multiple rows to the dataset."""

        for row in rows:
            self.add_row(*row)
