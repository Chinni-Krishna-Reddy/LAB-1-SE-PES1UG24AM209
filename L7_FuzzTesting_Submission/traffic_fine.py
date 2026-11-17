"""Traffic ticket input processor.

Invalid input is handled defensively:
- parse_ticket_id returns None for malformed ticket IDs.
- total_fines returns 0 for malformed CSV input.
- speed_excess returns 0 for malformed readings or an invalid speed limit.
"""

def parse_ticket_id(ticket_id):
    """Parse IDs such as TF-2024-0456 into (prefix, year, serial).

    Returns None when the supplied value is missing or malformed.
    """
    if not isinstance(ticket_id, str):
        return None

    parts = ticket_id.strip().split("-")
    if len(parts) != 3:
        return None

    prefix, year_text, serial_text = parts
    if not prefix or not prefix.isalpha():
        return None
    if len(year_text) != 4 or not year_text.isdigit():
        return None
    if not serial_text or not serial_text.isdigit():
        return None

    return prefix.upper(), int(year_text), int(serial_text)


def total_fines(amounts_csv):
    """Sum comma-separated non-negative integer fines, capped at 10,000.

    Returns 0 for missing, empty, malformed, or negative input.
    """
    if not isinstance(amounts_csv, str):
        return 0

    value = amounts_csv.strip()
    if not value:
        return 0

    try:
        pieces = [piece.strip() for piece in value.split(",")]
        if any(piece == "" for piece in pieces):
            return 0
        amounts = [int(piece) for piece in pieces]
    except (TypeError, ValueError):
        return 0

    if any(amount < 0 for amount in amounts):
        return 0

    return min(sum(amounts), 10000)


def speed_excess(reading):
    """Return percentage over the speed limit using integer arithmetic.

    Returns 0 for malformed input, negative speeds, or a non-positive limit.
    """
    if not isinstance(reading, str):
        return 0

    parts = reading.strip().split("/")
    if len(parts) != 2:
        return 0

    speed_text, limit_text = (part.strip() for part in parts)
    try:
        speed = int(speed_text)
        limit = int(limit_text)
    except (TypeError, ValueError):
        return 0

    if speed < 0 or limit <= 0:
        return 0

    return (speed - limit) * 100 // limit


def main():
    print("==== Running parse_ticket_id ====")
    user_input = input("Enter a ticket ID (e.g. TF-2024-0456): ")
    result = parse_ticket_id(user_input)
    print("Ticket Prefix, Year and Serial:", result)

    print("\n==== Running total_fines ====")
    user_input = input("Enter fine amounts as CSV (e.g. 500,1200,300): ")
    result = total_fines(user_input)
    print("Total Fines:", result)

    print("\n==== Running speed_excess ====")
    user_input = input("Enter speed/limit (e.g. 72/60): ")
    result = speed_excess(user_input)
    print("Percent Over Limit:", result)


if __name__ == "__main__":
    main()
