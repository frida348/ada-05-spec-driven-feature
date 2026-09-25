"""Customer search service coordinating validation and search."""

from typing import List, Optional
from .models import Customer
from .repository import CustomerRepository
from .validator import SearchInputValidator


class CustomerSearchService:
    """Service orchestrating the customer search flow."""

    def __init__(
        self,
        repository: CustomerRepository,
        validator: Optional[SearchInputValidator] = None,
    ) -> None:
        self.repository = repository
        self.validator = validator or SearchInputValidator()

    def search(self, query: str) -> List[Customer]:
        """Perform customer search by name or email.

        1. Validates the query. If invalid, raises InvalidSearchQueryError
           and does not execute search on repository.
        2. Retrieves matching customers from repository.
        3. Returns the matching customers.
        """
        self.validator.validate(query)
        return self.repository.find_by_name_or_email(query)
