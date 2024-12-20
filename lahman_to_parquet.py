import marimo

__generated_with = "0.10.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pathlib
    import polars as pl

    input_dir = pathlib.Path('lahman_1871-2023_csv')
    output_dir = pathlib.Path('lahman_1871-2023_parquet')
    output_dir.mkdir(exist_ok=True)

    for csv_file in input_dir.glob('*.csv'):
        df = pl.read_csv(csv_file, encoding="latin1", truncate_ragged_lines=True)
        parquet_file = output_dir / (csv_file.stem + '.parquet')
        df.write_parquet(parquet_file)
    return csv_file, df, input_dir, output_dir, parquet_file, pathlib, pl


@app.cell
def _():
    import os

    def get_directory_size(directory):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size

    csv_directory = 'lahman_1871-2023_csv'
    parquet_directory = 'lahman_1871-2023_parquet'

    csv_size = get_directory_size(csv_directory)
    parquet_size = get_directory_size(parquet_directory)

    csv_size, parquet_size, csv_size/parquet_size
    return (
        csv_directory,
        csv_size,
        get_directory_size,
        os,
        parquet_directory,
        parquet_size,
    )


@app.cell
def _(mo):
    mo.md(r"""parquetに変換すると約5分の1に小さくできる！""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
