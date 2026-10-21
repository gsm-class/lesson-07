import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    ("stdin_data", "expected_output"),
    [
        ("10 3\n1 2 3\n", "0"),
        ("10 3\n2 9 5\n", "8"),
    ],
)
def test_rolling_queue_samples(stdin_data, expected_output):
    script_path = Path(__file__).with_name("rolling_queue.py")

    completed = subprocess.run(
        [sys.executable, str(script_path)],
        input=stdin_data,
        text=True,
        capture_output=True,
        check=True,
    )

    assert completed.stdout.strip() == expected_output