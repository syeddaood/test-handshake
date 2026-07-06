from pathlib import Path
import json



"""Verifier for the log-report task.

Each test corresponds 1:1 to a numbered success criterion in instruction.md.
Expected values are ground truth computed from environment/access.log and
independently verified by hand (line counts / distinct first fields / path
frequencies).
"""

REPORT = "/app/report.json"


def _load():
    with open(REPORT) as f:
        return json.load(f)


def test_report_is_valid_json_object():
    """/app/report.json exists and is a single valid JSON object."""
    report = _load()
    assert isinstance(report, dict)


def test_total_requests():
    """ "total_requests" is an integer equal to the number of non-empty lines in the log."""
    value = _load()["total_requests"]
    assert isinstance(value, int)
    assert value == 6


def test_unique_ips():
    """ "unique_ips" is an integer equal to the number of distinct client IPs (first whitespace-separated field of each line)."""
    value = _load()["unique_ips"]
    assert isinstance(value, int)
    assert value == 3


def test_top_path():
    """ "top_path" is a string equal to the most frequently requested path across GET/POST/PUT/DELETE/HEAD/PATCH requests."""
    value = _load()["top_path"]
    assert isinstance(value, str)
    assert value == "/index.html"
