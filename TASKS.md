# Tasks

Tasks must be completed in order unless a task explicitly states otherwise.

Before starting any implementation task, read `REQUIREMENTS.md`, `SPEC.md`, `ARCHITECTURE.md`, and `AGENTS.md`.

---

## T-01 Project setup

- **Goal:**
  Inspect the existing project structure, identify the Customer model, data-access layer, application entry points, and testing conventions before implementing Customer Search. Establish the current test baseline.

- **Files:**
  - Existing project configuration files.
  - Existing customer-related modules.
  - Existing test configuration and test files.
  - No new production files should be created unless required by the existing project structure.

- **Acceptance:**
  - Existing Customer-related code has been identified.
  - Existing persistence/data-access mechanism has been identified.
  - Existing testing conventions have been identified.
  - The baseline test suite has been executed.
  - Any pre-existing test failures are documented.
  - No unrelated source code has been modified.

- **Verification:**

```bash
pytest
```

Record the number of passing, failing, and skipped tests before implementation.

---

## T-02 Domain model

- **Goal:**
  Verify that the existing Customer domain model provides the name and email information required by Customer Search. Reuse the existing model whenever possible.

- **Files:**
  - Existing Customer model file.
  - Existing Customer repository/data-access file, if applicable.
  - Related model tests only if changes are required.

- **Acceptance:**
  - The Customer model exposes the fields necessary to search by name and email.
  - No duplicate Customer model is introduced.
  - Existing Customer behavior remains unchanged.
  - No new fields are introduced unless they are necessary to satisfy existing requirements.
  - If the current Customer model already satisfies the feature requirements, no model modification is made.

- **Verification:**
  - Run existing Customer/domain tests.
  - Run:

```bash
pytest
```

  - Confirm that existing Customer tests continue to pass.

---

## T-03 Search logic

- **Goal:**
  Implement the core Customer Search behavior defined in `SPEC.md`.

- **Files:**
  - Existing Customer repository/data-access module.
  - Existing service/application module, if the project uses one.
  - Customer Search-specific module only if required by the existing architecture.
  - Relevant search tests.

- **Acceptance:**
  - Customers can be searched by name.
  - Customers can be searched by email.
  - Partial matches are supported.
  - Matching is case-insensitive.
  - All matching customers are returned.
  - A customer matching both name and email appears only once.
  - A valid query with no matches returns an empty collection.
  - Search operations do not modify customer records.
  - Repeated searches with the same query and unchanged data produce the same matching customer records.

- **Verification:**
  - Add focused automated tests for search behavior.
  - Run the Customer Search tests.
  - Run:

```bash
pytest
```

  - Verify that the complete suite continues to pass.

---

## T-04 Validation and errors

- **Goal:**
  Implement input validation and error behavior according to `SPEC.md`.

- **Files:**
  - Existing validation module, if applicable.
  - Customer Search interface/service module.
  - Relevant validation and error tests.

- **Acceptance:**
  - Empty search input is rejected.
  - Whitespace-only input is rejected.
  - Invalid input does not execute a customer search.
  - A valid query with no matches returns an empty collection and is not treated as an error.
  - Unexpected errors follow the application's existing error-handling conventions.
  - No behavior is introduced for unresolved Open Questions without clarification.

- **Verification:**
  - Test empty input.
  - Test whitespace-only input.
  - Test a valid query with zero matches.
  - Verify that invalid input does not reach the customer data-access operation.
  - Run:

```bash
pytest
```

---

## T-05 Tests

- **Goal:**
  Complete automated test coverage for the Customer Search feature and verify the acceptance criteria and test scenarios defined in `SPEC.md`.

- **Files:**
  - Existing Customer test files.
  - Customer Search test file(s), following existing project naming and directory conventions.

- **Acceptance:**
  Automated tests cover:

  - Search by exact name.
  - Search by exact email.
  - Partial name search.
  - Partial email search.
  - Case-insensitive search.
  - Empty query validation.
  - Whitespace-only query validation.
  - No matching customers.
  - Multiple matching customers.
  - Duplicate prevention when both name and email match.
  - Read-only search behavior.
  - Deterministic search behavior.

  Existing tests must not be deleted, skipped, disabled, or weakened.

- **Verification:**

Run the Customer Search tests independently using the appropriate test path for the existing project.

Then run:

```bash
pytest
```

Compare the final result with the baseline recorded in T-01.

No new unrelated test failures should be introduced.

---

## T-06 Documentation

- **Goal:**
  Verify that the project documentation accurately reflects the final Customer Search implementation and report the completed work.

- **Files:**
  - `REQUIREMENTS.md`
  - `SPEC.md`
  - `ARCHITECTURE.md`
  - `AGENTS.md`
  - `TASKS.md`
  - Existing project documentation only if the implemented feature requires an update.

- **Acceptance:**
  - Final implementation is consistent with `REQUIREMENTS.md`.
  - Final behavior is consistent with `SPEC.md`.
  - Implementation respects the responsibilities described in `ARCHITECTURE.md`.
  - `REQUIREMENTS.md` and `SPEC.md` have not been modified merely to accommodate implementation or test failures.
  - Documentation does not claim behavior that is not implemented.
  - Changed files are identified.
  - Added or modified tests are identified.
  - Final test results are documented.
  - Any unresolved Open Questions, assumptions, or limitations are reported.

- **Verification:**
  - Review the implementation against each applicable acceptance criterion in `SPEC.md`.
  - Review the final Git diff to ensure no unrelated files were changed.
  - Run the final test suite:

```bash
pytest
```

  - Report:
    - Files created.
    - Files modified.
    - Tests added or modified.
    - Final test results.
    - Remaining Open Questions or limitations.