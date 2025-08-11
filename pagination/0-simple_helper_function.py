#!/usr/bin/env python3
"""
This module contains a helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: (start_index, end_index) for the page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
