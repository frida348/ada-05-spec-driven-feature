"""Customer search interface exposing search to clients."""

from dataclasses import dataclass
from typing import List, Optional
from .exceptions import CustomerSearchError, InvalidSearchQueryError
from .models import Customer
from .service import CustomerSearchService


@dataclass
class SearchResponse:
    """Response wrapper for search results or validation errors."""

    success: bool
    data: List[Customer]
    error_message: Optional[str] = None


class CustomerSearchInterface:
    """Interface entry point for Customer Search."""

    def __init__(self, service: CustomerSearchService) -> None:
        self.service = service

    def search(self, query: str) -> List[Customer]:
        """Execute customer search, returning matching customers or raising validation error."""
        return self.service.search(query)

    def search_customers(self, query: str) -> List[Customer]:
        """Alias for search(query) matching architectural specification."""
        return self.service.search(query)

    def execute_search(self, query: str) -> SearchResponse:
        """Execute search returning structured SearchResponse without unhandled exceptions."""
        try:
            results = self.service.search(query)
            return SearchResponse(success=True, data=results)
        except InvalidSearchQueryError as e:
            return SearchResponse(success=False, data=[], error_message=str(e))
        except CustomerSearchError as e:
            return SearchResponse(success=False, data=[], error_message=str(e))
