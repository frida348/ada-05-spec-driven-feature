"""Comprehensive automated tests covering SPEC.md acceptance criteria and test scenarios.

Covers:
- Acceptance Criteria: AC-01 through AC-12
- Test Scenarios: TS-01 through TS-13
- Functional Requirements: FR-01 through FR-06
- Non-Functional Requirements: NFR-01 through NFR-03
"""

from unittest.mock import MagicMock
import pytest
from customer_search.exceptions import InvalidSearchQueryError
from customer_search.interface import CustomerSearchInterface
from customer_search.models import Customer
from customer_search.repository import InMemoryCustomerRepository
from customer_search.service import CustomerSearchService


@pytest.fixture
def spec_customers() -> list[Customer]:
    """Standard customer dataset matching examples from SPEC.md."""
    return [
        Customer(id="1", name="Ana López", email="ana@example.com"),
        Customer(id="2", name="Anabel García", email="agarcia@gmail.com"),
        Customer(id="3", name="Mariana Torres", email="mariana@empresa.com"),
        Customer(id="4", name="Carlos Ruiz", email="carlos@gmail.com"),
        Customer(id="5", name="Beatriz Ramos", email="beatriz@example.org"),
    ]


@pytest.fixture
def search_system(spec_customers: list[Customer]):
    """Provides wired search service and interface with test customer data."""
    repo = InMemoryCustomerRepository(spec_customers)
    service = CustomerSearchService(repository=repo)
    interface = CustomerSearchInterface(service=service)
    return repo, service, interface


# ============================================================================
# SPEC.md Acceptance Criteria & Test Scenarios
# ============================================================================


def test_ts01_exact_name_search(search_system) -> None:
    """TS-01 / AC-01: Exact name search 'Ana López' returns matching customer (FR-01)."""
    _, _, interface = search_system
    results = interface.search("Ana López")
    assert len(results) == 1
    assert results[0].name == "Ana López"
    assert results[0].email == "ana@example.com"


def test_ts02_exact_email_search(search_system) -> None:
    """TS-02 / AC-02: Exact email search 'ana@example.com' returns matching customer (FR-02)."""
    _, _, interface = search_system
    results = interface.search("ana@example.com")
    assert len(results) == 1
    assert results[0].name == "Ana López"
    assert results[0].email == "ana@example.com"


def test_ts03_partial_name_search(search_system) -> None:
    """TS-03 / AC-03: Partial name search 'Ana' returns customers whose names contain 'Ana' (FR-03)."""
    _, _, interface = search_system
    results = interface.search("Ana")
    names = [c.name for c in results]
    assert "Ana López" in names
    assert "Anabel García" in names
    assert "Mariana Torres" in names
    assert len(results) == 3


def test_ts04_partial_email_search(search_system) -> None:
    """TS-04 / AC-04: Partial email search 'example' returns customers whose emails contain 'example' (FR-03)."""
    _, _, interface = search_system
    results = interface.search("example")
    emails = [c.email for c in results]
    assert "ana@example.com" in emails
    assert "beatriz@example.org" in emails
    assert len(results) == 2


def test_ts05_and_ts06_case_insensitive_search(search_system) -> None:
    """TS-05, TS-06 / AC-05: 'ana', 'Ana', 'ANA' return equivalent matching customers (FR-04)."""
    _, _, interface = search_system
    results_lower = interface.search("ana")
    results_mixed = interface.search("Ana")
    results_upper = interface.search("ANA")

    assert results_lower == results_mixed == results_upper
    assert len(results_lower) == 3
    assert {c.name for c in results_lower} == {"Ana López", "Anabel García", "Mariana Torres"}


def test_ts07_empty_query_validation(search_system) -> None:
    """TS-07 / AC-06: Empty query '' fails validation and search is not executed (FR-05)."""
    repo, _, interface = search_system
    spy_repo_find = MagicMock(wraps=repo.find_by_name_or_email)
    repo.find_by_name_or_email = spy_repo_find

    with pytest.raises(InvalidSearchQueryError) as exc_info:
        interface.search("")

    assert "cannot be empty" in str(exc_info.value)
    spy_repo_find.assert_not_called()


def test_ts08_whitespace_only_query_validation(search_system) -> None:
    """TS-08 / AC-07: Whitespace query '   ' fails validation and search is not executed (FR-05)."""
    repo, _, interface = search_system
    spy_repo_find = MagicMock(wraps=repo.find_by_name_or_email)
    repo.find_by_name_or_email = spy_repo_find

    with pytest.raises(InvalidSearchQueryError) as exc_info:
        interface.search("   ")

    assert "whitespace-only" in str(exc_info.value)
    spy_repo_find.assert_not_called()


def test_ts09_no_matching_customer(search_system) -> None:
    """TS-09 / AC-08: Valid query with no matches returns empty collection without error (FR-06)."""
    _, _, interface = search_system
    results = interface.search("nonexistent")
    assert results == []


def test_ts10_multiple_matches(search_system) -> None:
    """TS-10 / AC-09: Query 'ana' returns all matching customers (FR-06)."""
    _, _, interface = search_system
    results = interface.search("ana")
    assert len(results) == 3
    assert [c.name for c in results] == ["Ana López", "Anabel García", "Mariana Torres"]


def test_ts11_name_and_email_both_match(search_system) -> None:
    """TS-11 / AC-10: Customer matching both name and email appears only once (FR-06)."""
    single_customer = Customer(id="1", name="Ana López", email="ana@example.com")
    repo = InMemoryCustomerRepository([single_customer])
    service = CustomerSearchService(repository=repo)
    interface = CustomerSearchInterface(service=service)

    results = interface.search("ana")
    assert len(results) == 1
    assert results[0] == single_customer


def test_ts12_search_does_not_modify_data(search_system, spec_customers: list[Customer]) -> None:
    """TS-12 / AC-11 / NFR-02: Executing search does not create, update, or delete customer records."""
    repo, _, interface = search_system

    initial_snapshot = [(c.id, c.name, c.email) for c in spec_customers]

    # Perform multiple different searches (exact, partial, no match, multiple matches)
    interface.search("Ana López")
    interface.search("gmail")
    interface.search("nonexistent")

    final_snapshot = [(c.id, c.name, c.email) for c in repo.get_all()]

    assert initial_snapshot == final_snapshot
    assert len(repo.get_all()) == len(spec_customers)


def test_ts13_deterministic_behavior(search_system) -> None:
    """TS-13 / AC-12 / NFR-03: Repeated identical searches return identical matching customer records."""
    _, _, interface = search_system

    run_1 = interface.search("ana")
    run_2 = interface.search("ana")
    run_3 = interface.search("ana")

    assert run_1 == run_2 == run_3
