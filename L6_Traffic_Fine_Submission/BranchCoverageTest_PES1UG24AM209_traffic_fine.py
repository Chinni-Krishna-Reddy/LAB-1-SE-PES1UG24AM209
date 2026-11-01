"""Tests covering both outcomes of every decision in traffic_fine.py.

Run:
    coverage run --branch -m pytest BranchCoverageTest_PES1UG24AM209_traffic_fine.py
    coverage report -m
"""
import pytest

from traffic_fine import speeding_fine, license_action, total_penalty


# speeding_fine: speed limit, all zone choices, and all excess-speed bands
def test_speeding_fine_no_speeding_and_zone_bases():
    assert speeding_fine(60, 60, "city") == 0
    assert speeding_fine(61, 60, "school") == 2000
    assert speeding_fine(61, 60, "highway") == 1000
    assert speeding_fine(61, 60, "city") == 500


def test_speeding_fine_excess_speed_boundaries():
    assert speeding_fine(80, 60, "city") == 500       # excess == 20
    assert speeding_fine(81, 60, "city") == 1000      # excess > 20
    assert speeding_fine(100, 60, "city") == 1000    # excess == 40
    assert speeding_fine(101, 60, "city") == 1500    # excess > 40


# license_action: both outcomes of each nested and outer decision
def test_license_action_all_branches():
    assert license_action(12, True, False) == "revoke"
    assert license_action(12, False, False) == "suspend"
    assert license_action(8, False, True) == "suspend"
    assert license_action(8, False, False) == "warning"
    assert license_action(4, False, False) == "notice"
    assert license_action(3, False, False) == "none"


# total_penalty: empty/non-empty loop, negative/non-negative fine, cap/no cap
def test_total_penalty_all_branches():
    assert total_penalty([]) == 0
    assert total_penalty([100, 200]) == 300
    assert total_penalty([7000, 5000]) == 10000
    with pytest.raises(ValueError, match="negative fine"):
        total_penalty([100, -1])
