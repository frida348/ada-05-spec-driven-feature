"""Customer repository layer."""

from abc import ABC, abstractmethod
from typing import Iterable, List, Optional
from .models import Customer


class CustomerRepository(ABC):
    """Abstract base repository for customer data access."""

    @abstractmethod
    def find_by_name_or_email(self, query: str) -> List[Customer]:
        """Find customers whose name or email contains the search query.

        Must be case-insensitive, partial matching, deterministic, and read-only.
        A customer matching both name and email must appear only once.
        """
        raise NotImplementedError


class InMemoryCustomerRepository(CustomerRepository):
    """In-memory implementation of CustomerRepository."""

    def __init__(self, customers: Optional[Iterable[Customer]] = None) -> None:
        self._customers: List[Customer] = list(customers) if customers is not None else []

    def find_by_name_or_email(self, query: str) -> List[Customer]:
        """Find customers matching query in name or email.

        Rules:
        - Search is case-insensitive.
        - Partial matches are supported.
        - All matching customers are returned in deterministic order.
        - If both name and email match, the customer appears only once.
        - Returns an empty list if no customer matches.
        - Read-only operation: internal customer data is not modified.
        """
        query_lower = query.lower()
        results: List[Customer] = []
        seen = set()

        for customer in self._customers:
            customer_key = customer.id if customer.id is not None else id(customer)
            if customer_key in seen:
                continue

            name_matches = query_lower in customer.name.lower()
            email_matches = query_lower in customer.email.lower()

            if name_matches or email_matches:
                seen.add(customer_key)
                results.append(customer)

        return results

    def get_all(self) -> List[Customer]:
        """Return a copy of all customer records (read-only snapshot)."""
        return list(self._customers)

    def add_customer(self, customer: Customer) -> None:
        """Add a customer record to repository (for data initialization)."""
        self._customers.append(customer)
