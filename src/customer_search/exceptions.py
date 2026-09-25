"""Custom exceptions for customer search."""


class CustomerSearchError(Exception):
    """Base exception for all customer search errors."""

    pass


class ValidationError(CustomerSearchError, ValueError):
    """Base validation error for customer search input."""

    pass


class InvalidSearchQueryError(ValidationError):
    """Raised when search query is empty or contains only whitespace."""

    pass
