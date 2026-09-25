# Requirements — Customer Search

## User Story

As a user, I want to search customers by name or email, so that I can quickly find the customer record I need.

## Functional Requirements

**FR-01:** The system shall allow the user to search for customers by **name**.

**FR-02:** The system shall allow the user to search for customers by **email address**.

**FR-03:** The search shall support **partial matches**. For example, searching for `Ana` may return customers such as `Ana López`, `Anabel García`, or `Mariana Torres`.

**FR-04:** The search shall be **case-insensitive**, so searches such as `ANA`, `Ana`, and `ana` produce equivalent results.

**FR-05:** The system shall validate the search input. Empty input or input containing only whitespace shall not trigger a customer search and shall return an appropriate validation response.

**FR-06:** The system shall return all customers whose name or email matches the search criteria. If no customers match, the system shall return an empty result without producing an error.

## Non-Functional Requirements

**NFR-01:** Customer Search shall include automated tests covering searches by name, searches by email, partial matches, case-insensitive searches, invalid input, and searches with no results.

**NFR-02:** The search functionality shall not modify, delete, or otherwise alter existing customer records.

**NFR-03:** Search results shall be deterministic: given the same customer data and the same search query, the search shall return the same matching customer records.

## Open Questions

**Q-01:** Should the search ignore leading and trailing whitespace in the search query?

**Q-02:** Should there be a minimum number of characters required before performing a search?

## Constraints / Assumptions

**C-01:** Customer Search shall operate only on existing customer records and shall search only the customer's name and email fields.

**A-01:** Each customer record is assumed to contain the necessary name and email information required by the existing customer data model.
