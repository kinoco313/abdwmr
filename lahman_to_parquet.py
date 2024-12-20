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
    return


if __name__ == "__main__":
    app.run()
