"""
Authors: Gia Ky Huynh, Gaici Lin
"""

from unittest import mock
from unittest.mock import ANY

from main import main


@mock.patch('main.preprocess_data')
@mock.patch('main.analyze')
def test_main_invoke_preprocess_data_twice_and_invoke_analyze_twice(mock_preprocess_data, mock_analyze):
    main()

    mock_preprocess_data.assert_called_with(ANY)
    mock_analyze.assert_called_with(ANY)

    assert mock_preprocess_data.call_count == 2
    assert mock_analyze.call_count == 2
