import pytest
import main
import pandas as pd
from datetime import date

csv = 'data/dft-road-casualty-statistics-accident-2020.csv'
df = main.extract_road_casualty_statistics(csv)


def test_convert_from_CSV_to_DF():
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 91199


def test_date_column_is_converted_to_datetime():
    assert df.at[0, 'date'] == date(2020, 2, 4)
