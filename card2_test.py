import subprocess
import sys
from pathlib import Path


def test_sample_input_6_outputs_4():
    script_path = Path(__file__).with_name("card2.py")

    completed = subprocess.run(
        [sys.executable, str(script_path)],
        input="6\n",
        text=True,
        capture_output=True,
        check=True,
    )

    assert completed.stdout.strip() == "4"