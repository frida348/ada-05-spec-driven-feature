# Agent Instructions

## Project Rules

- Read `REQUIREMENTS.md` before implementing or modifying Customer Search.
- Read `SPEC.md` before implementing to understand the expected observable behavior, validation rules, acceptance criteria, and test scenarios.
- Read `ARCHITECTURE.md` before making architectural or structural changes.
- Follow the implementation order and scope defined in `TASKS.md`.
- Inspect the existing project structure and conventions before creating new files, classes, services, repositories, or abstractions.
- Prefer small, focused, and reversible changes.
- Reuse existing project patterns and abstractions whenever possible.
- Do not invent business requirements that are not defined in `REQUIREMENTS.md` or `SPEC.md`.
- Do not make assumptions for unresolved Open Questions.
- Do not modify `REQUIREMENTS.md` or `SPEC.md` simply to make an implementation or failing test pass.
- Do not delete, skip, disable, or weaken existing tests.
- Do not change unrelated functionality.
- Do not add external dependencies unless they are necessary and the reason is clearly justified.
- Preserve Customer Search as a read-only operation.
- Do not introduce customer creation, modification, or deletion behavior as part of this feature.
- Keep implementation details consistent with the boundaries described in `ARCHITECTURE.md`.
- If the existing project architecture differs from the conceptual structure in `ARCHITECTURE.md`, prefer integrating with the existing conventions while preserving the specified responsibilities and behavior.

## Validation

Before making changes:

1. Run the existing test suite with:

```bash
pytest
```

2. Record whether the baseline test suite passes or contains pre-existing failures.

After making changes:

1. Add or update automated tests for the new Customer Search behavior.
2. Run the relevant Customer Search tests.
3. Run the complete test suite with:

```bash
pytest
```

4. Verify that no existing behavior has regressed.
5. Verify that Customer Search satisfies the acceptance criteria and test scenarios defined in `SPEC.md`.
6. Verify that search operations do not modify customer data.

The implementation must include automated coverage for:

- Search by name.
- Search by email.
- Partial name matching.
- Partial email matching.
- Case-insensitive matching.
- Empty input validation.
- Whitespace-only input validation.
- No matching customers.
- Multiple matching customers.
- Duplicate prevention when both name and email match.
- Read-only behavior.
- Deterministic search behavior.

When completing a task, report:

- Files created.
- Files modified.
- Tests added or modified.
- Commands executed.
- Test results.
- Any assumptions or limitations encountered.

If requirements, specifications, architecture, existing implementation, or tests conflict, stop implementation and ask for clarification rather than choosing a behavior arbitrarily.

If an Open Question from `REQUIREMENTS.md` or `SPEC.md` blocks implementation, stop and request clarification.

## Definition of Done

A Customer Search task is considered complete only when:

- The implementation satisfies the relevant requirements from `REQUIREMENTS.md`.
- The observable behavior matches `SPEC.md`.
- Relevant acceptance criteria are covered by automated tests.
- Relevant test scenarios from `SPEC.md` are covered.
- All newly added tests pass.
- The complete `pytest` suite passes, excluding clearly documented pre-existing failures.
- No existing tests have been deleted, disabled, skipped, or weakened to accommodate the implementation.
- Customer Search remains read-only.
- No unrelated functionality has been modified.
- No unrelated files have been changed.
- No unnecessary dependencies have been introduced.
- The implementation follows the existing project conventions and the architectural responsibilities described in `ARCHITECTURE.md`.
- Documentation reflects the final implemented behavior.
- Changed files and final test results are reported.
