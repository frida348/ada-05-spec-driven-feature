"""Customer Search package."""

from .exceptions import (
    CustomerSearchError,
    InvalidSearchQueryError,
    ValidationError,
)
from .interface import CustomerSearchInterface, SearchResponse
from .models import Customer
from .repository import CustomerRepository, InMemoryCustomerRepository
from .service import CustomerSearchService
from .validator import SearchInputValidator

__all__ = [
    "Customer",
    "CustomerSearchError",
    "ValidationError",
    "InvalidSearchQueryError",
    "SearchInputValidator",
    "CustomerRepository",
    "InMemoryCustomerRepository",
    "CustomerSearchService",
    "CustomerSearchInterface",
    "SearchResponse",
]
