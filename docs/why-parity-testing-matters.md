# Why Parity Testing Matters

Modern system migrations often focus on API compatibility:
- same endpoints
- same schemas
- same response structures

But identical responses do not guarantee identical behavior.

Two systems may appear contract-compatible while behaving differently internally.

This is where parity validation becomes critical.

## Common Migration Risks

A migrated system may introduce hidden behavioral differences such as:
- incomplete persistence
- silent data corruption
- missing operational logs
- inconsistent tracing
- stricter null handling
- unexpected retries
- partial writes

These issues are often invisible at the API layer.

## Response Validation Is Not Enough

Traditional API testing usually validates:
- status codes
- response bodies
- schemas

Parity validation goes further by validating:
- persistence behavior
- operational observability
- log consistency
- tracing integrity
- system side effects
- cross-layer correctness

## Real-World Example

A migrated service may:
- return `200 OK`
- produce the expected JSON response
- pass contract validation

...while persisting incorrect data internally.

From the outside, both systems appear equivalent.

Operationally, they are not.

## Purpose of This Project

This project demonstrates controlled divergence scenarios where:
- responses appear correct
- contracts remain valid
- failures exist internally

The goal is to show how deeper validation strategies can detect:
- hidden regressions
- behavioral drift
- observability gaps
- silent failures

before they reach production systems.
