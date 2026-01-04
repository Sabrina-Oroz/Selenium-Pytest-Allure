import pytest
import os

@pytest.mark.regression
def test_flaky_demo():
    """
    Test flaky controlado:
    - Falla la primera vez
    - Pasa en el retry
    """
    flag_file = "/tmp/flaky_flag.txt"

    if not os.path.exists(flag_file):
        # Primera ejecución → falla
        with open(flag_file, "w") as f:
            f.write("failed once")
        pytest.fail("Intentional flaky failure (first run)")

    # Segunda ejecución (retry) → pasa
    assert True