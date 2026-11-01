"""Tests focused on executing every application line at least once.

Run:
    coverage run -m pytest CodeCoverageTest_PES1UG24AM209_traffic_fine.py
    coverage report -m
"""
import pytest

from traffic_fine import speeding_fine, license_action, total_penalty


def test_speeding_fine_all_return_lines():
    assert speeding_fine(50, 60, "city") == 0
    assert speeding_fine(105, 60, "school") == 6000
    assert speeding_fine(85, 60, "highway") == 2000
    assert speeding_fine(70, 60, "city") == 500


def test_license_action_all_return_lines():
    assert license_action(12, True, False) == "revoke"
    assert license_action(12, False, False) == "suspend"
    assert license_action(8, False, False) == "warning"
    assert license_action(4, False, False) == "notice"
    assert license_action(0, False, False) == "none"


def test_total_penalty_normal_capped_and_negative():
    assert total_penalty([100, 200, 300]) == 600
    assert total_penalty([7000, 5000]) == 10000
    with pytest.raises(ValueError, match="negative fine"):
        total_penalty([100, -1])
