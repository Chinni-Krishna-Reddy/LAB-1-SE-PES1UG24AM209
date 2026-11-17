"""Property-based fuzz tests for traffic_fine.py."""

from hypothesis import given, strategies as st

from traffic_fine import parse_ticket_id, total_fines, speed_excess


@given(st.text() | st.none())
def test_parse_ticket_id_no_crash(value):
    """Arbitrary text and None must never crash the parser."""
    result = parse_ticket_id(value)
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 3
        and isinstance(result[0], str)
        and isinstance(result[1], int)
        and isinstance(result[2], int)
    )


@given(st.text() | st.none())
def test_total_fines_no_crash(value):
    """Arbitrary CSV-like text and None must never crash the total function."""
    result = total_fines(value)
    assert isinstance(result, int)
    assert 0 <= result <= 10000


@given(st.text() | st.none())
def test_speed_excess_no_crash(value):
    """Arbitrary speed readings and None must never crash the calculator."""
    result = speed_excess(value)
    assert isinstance(result, int)


@given(
    st.text(min_size=1).filter(str.isalpha),
    st.integers(min_value=0, max_value=9999),
    st.integers(min_value=0, max_value=999999),
)
def test_valid_ticket_id_round_trip(prefix, year, serial):
    ticket = f"{prefix}-{year:04d}-{serial}"
    result = parse_ticket_id(ticket)
    assert result == (prefix.upper(), year, serial)


@given(st.lists(st.integers(min_value=0, max_value=20000), min_size=1, max_size=20))
def test_total_fines_valid_nonnegative_amounts(amounts):
    csv_value = ",".join(map(str, amounts))
    assert total_fines(csv_value) == min(sum(amounts), 10000)


@given(
    st.integers(min_value=0, max_value=100000),
    st.integers(min_value=1, max_value=100000),
)
def test_speed_excess_valid_readings(speed, limit):
    reading = f"{speed}/{limit}"
    assert speed_excess(reading) == (speed - limit) * 100 // limit
