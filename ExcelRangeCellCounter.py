"""
Excel Range Cell Counter
-----------------------
Given an Excel range (e.g., F26:H29), this script calculates the total number of cells in that range.
"""


def column_letter_to_number(col):
    """Convert Excel column letter(s) to a number (e.g., A=1, Z=26, AA=27)."""
    num = 0
    for c in col.upper():
        num = num * 26 + (ord(c) - ord("A") + 1)
    return num


def parse_range(range_str):
    """Parse a range like 'F26:H29' and return (start_col, start_row, end_col, end_row)."""
    import re

    match = re.match(r"([A-Z]+)(\d+):([A-Z]+)(\d+)", range_str.strip(), re.I)
    if not match:
        raise ValueError("Invalid range format. Use e.g. F26:H29")
    start_col, start_row, end_col, end_row = match.groups()
    return start_col, int(start_row), end_col, int(end_row)


def count_cells_in_range(range_str):
    start_col, start_row, end_col, end_row = parse_range(range_str)
    start_col_num = column_letter_to_number(start_col)
    end_col_num = column_letter_to_number(end_col)
    # Range validation
    if start_col_num > end_col_num:
        raise ValueError(
            f"Invalid range: start column '{start_col}' is after end column '{end_col}'."
        )
    if start_row > end_row:
        raise ValueError(
            f"Invalid range: start row {start_row} is after end row {end_row}."
        )
    col_count = end_col_num - start_col_num + 1
    row_count = end_row - start_row + 1
    total_cells = col_count * row_count
    return row_count, col_count, total_cells


def main():
    print("Excel Range Cell Counter")
    range_str = input("Enter Excel range (e.g., F26:H29): ").strip()
    try:
        rows, cols, total = count_cells_in_range(range_str)
        print(f"Rows: {rows}")
        print(f"Columns: {cols}")
        print(f"Total cells: {rows} × {cols} = {total}")
        print(f"✅ Answer: {total} cells are in the range {range_str}.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
