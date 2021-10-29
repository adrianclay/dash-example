import pytest
import main
from pandas.testing import assert_frame_equal
from io import StringIO
import pandas as pd

def test_convert_from_CSV_to_DF():
	# create dummy csv data
	dummy_csv = StringIO("""\
col1
1,2,3
""")
	expected_df = pd.DataFrame({
		'column: 1': ['1', '2', '3']
	})

	#errors as this isn't a file path. Need to mock file paths.
	actual_df = main.convert_from_CSV_to_DF(dummy_csv)

	#assert that both dataframes are equal
	assert_frame_equal(expected_df, actual_df)


# test date formatting function 

