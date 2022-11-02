"""Dictionary related utility functions."""

__author__ = "730334012"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []
   
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a new CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Tranform a row-oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], row_amount: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first 'row_amount' rows of data for each column."""
    result: dict[str, list[str]] = {}

    for column in column_table:
        column_values: list[str] = []
        i: int = 0
        if row_amount <= len(column_table[column]):
            result[column] = column_table[column]

        while i < row_amount:
            column_values.append(column_table[column][i])
            i += 1
        result[column] = column_values

    return result


def select(column_table: dict[str, list[str]], column_name: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for column_name in column_table:
        result[column_name] = column_table[column_name]
    return result


def concat(col_table1: dict[str, list[str]], col_table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    
    for column in col_table1:
        result[column] = col_table1[column]
    for column in col_table2:
        if column in col_table1:
            for item in col_table2[column]:
                result[column].append(item)
        else:
            result[column] = col_table2[column]
    return result
 

def count(cc: list[str]) -> dict[str, int]:
    """Function to count the number of times a value appears in the input list."""
    result: dict[str, int] = {}
    for item in cc:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
