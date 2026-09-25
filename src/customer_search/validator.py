"""Input validation for customer search."""

from .exceptions import InvalidSearchQueryError


class SearchInputValidator:
    """Validates search queries according to SPEC.md validation rules."""

    def validate(self, query: str) -> None:
        """Validate the search query.

        Rules:
        - Query must be a string containing searchable text.
        - Empty string is invalid.
        - String containing only whitespace is invalid.

        Raises:
            InvalidSearchQueryError: If query is invalid.
        """
        if not isinstance(query, str):
            raise InvalidSearchQueryError("Search query must be a string.")

        if not query or query.isspace():
            raise InvalidSearchQueryError(
                "Search query must contain searchable text and cannot be empty or whitespace-only."
            )

    def is_valid(self, query: str) -> bool:
        """Return True if query is valid, False otherwise."""
        try:
            self.validate(query)
            return True
        except InvalidSearchQueryError:
            return False
