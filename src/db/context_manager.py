from __future__ import annotations

import json


def build_query_part(key: str, values: str) -> str | None:
    """
    Build an individual query part based on key-value pairs.

    Args:
        key (str): The key of the JSON query.
        values (str): The value(s) associated with the key. Can be a string or a list of strings.

    Returns:
        str or None: The constructed query part as a string, or None if the values are ['na'].

    Example:
        >>> build_query_part('full_name', 'John')
        "full_name.str.lower().str.contains('John'.lower())"
    """

    # If the value is ['na'], skip this key
    if values == ["na"]:
        return None
    if not isinstance(values, list):
        return f"{key}.str.lower().str.contains('{values}'.lower())"
    if conditions := [
        f"{key}.str.lower().str.contains('{val}'.lower())"
        for val in values
        if val != "na"
    ]:
        return "(" + " or ".join(conditions) + ")"


def specific_context_query(query_json: json) -> str:
    """
    Generate a specific context query from a Python dictionary.

    Args:
        query_json (dict): Query in the form of a Python dictionary where keys represent
                           the fields to search and values represent the values to match.

    Returns:
        str: The final query part based on key-value pairs.

    Example:
        >>> query = {'full_name': ['John'], 'skill_name': 'Python'}
        >>> specific_context_query(query)
        "(full_name.str.lower().str.contains('John'.lower())) and (skill_name.str.lower().str.contains('Python'.lower()))"
    """

    query_parts = []
    skip_keys = []

    for key, value in query_json.items():
        # Skip if the value is 'na' and all other values for the keys are also 'na'
        if value == "na" and all(
            v == "na" for k, v in query_json.items() if k != key and k not in skip_keys
        ):
            skip_keys.append(key)
            continue
        # Include the key-value pair if it's not in the skip list and the value is not 'na'
        if key not in skip_keys and value != "na":
            if query_part := build_query_part(key, value):
                query_parts.append(query_part)
    return " and ".join(query_parts)


def build_query_condition(key: str, value: str) -> str | None:
    """
    Build an individual query part based on key-value pairs.

    Args:
        key (str): The key of the JSON query.
        value (str): The value associated with the key. Can be a string or a list of strings.

    Returns:
        str or None: The constructed query part as a string, or None if the values are ['na'].

    Example:
        >>> build_query_part('full_name', 'John')
        "full_name.str.lower().str.contains('John'.lower())"
    """

    # Check if the value is a list
    if isinstance(value, list):
        # If all values in the list are 'na'
        if all(val == "na" for val in value):
            return None
        else:
            # Join conditions for non-'na' values in the list
            return " or ".join(
                f"{key}.str.lower().str.contains('{val}'.lower())"
                for val in value
                if val != "na"
            )
    # If the value is not 'na'
    elif value != "na":
        return f"{key}.str.lower().str.contains('{value}'.lower())"
    return None


def all_context_query(query_json: json) -> str:
    """
    Generate query string from a Python dictionary.

    Args:
        query_json (dict): Query in the form of a Python dictionary where keys represent
                           the fields to search and values represent the values to match.

    Returns:
        str: The final query string based on key-value pairs.

    Example:
        >>> query = {'full_name': ['John'], 'skill_name': 'Python'}
        >>> specific_context_query(query)
        "full_name.str.lower().str.contains('John'.lower()) or skill_name.str.lower().str.contains('Python'.lower())"
    """

    query_conditions = []

    for key, value in query_json.items():
        if condition := build_query_condition(key, value):
            # Add condition to the list if not None
            query_conditions.append(condition)

    return " or ".join(query_conditions)
