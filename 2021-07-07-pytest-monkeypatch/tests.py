import pytest
import pandas as pd
from requests import Response

import main
from main import check_resource_availability, save_some_data

# def test_check_resource_availability(monkeypatch):
#
#     monkeypatch.delattr(Response, "status_code")
#
#     assert False


def test_save_some_data(tmpdir, monkeypatch):

    monkeypatch.setitem(main.CONSTANTS, "RESULTS_DIR", tmpdir)
    save_some_data()
    df_ref = pd.DataFrame([[1, 3], [2, 4], [3, 5]])
    df_res = pd.read_csv(tmpdir / "output.csv")
    pd.testing.assert_frame_equal(df_res, df_ref)
