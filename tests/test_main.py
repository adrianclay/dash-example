import pytest
import main
from pandas.testing import assert_frame_equal
from io import StringIO
import pandas as pd


def test_convert_from_CSV_to_DF():
    # create dummy csv data
    dummy_csv = 'data/dft-road-casualty-statistics-accident-2020.csv'

    actual_df = main.convert_from_CSV_to_DF(dummy_csv)

    assert isinstance(actual_df, pd.DataFrame)
    assert len(actual_df) == 91199

# test date formatting function
