---
name: code-review-instructions
description: "Detailed guidelines for conducting effective code reviews across all programming languages and frameworks."
applyTo: "**/*.py,**/*.js,**/*.ts,**/*.java,**/*.cs,**/*.go,**/*.rs,**/*.cpp,**/*.c,**/*.php,**/*.rb,**/*.scala,**/*.kt"
---

# Code Review Instructions

## Purpose
These instructions guide the code review process to ensure consistent, high-quality reviews that are constructive, educational, and actionable.

## Before the Review

### 1. Understand the Context
- [ ] Read the PR description and linked issues
- [ ] Understand the business context and requirements
- [ ] Check the branch strategy and release notes
- [ ] Review previous discussions if applicable
- [ ] Identify the target audience for code changes

### 2. Prepare Your Environment
- [ ] Checkout the branch locally (if possible)
- [ ] Review the diff visually
- [ ] Run tests locally to validate changes
- [ ] Check for obvious errors using linting/static analysis
- [ ] Note the change size and complexity

## During the Review

### 3. Structure Your Review

Start with **high-level observations** before diving into details:

```
### Overview
- [Brief summary of changes]
- [Positive observations]
- [Overall impression - looks good / has concerns / needs discussion]
```

Then organize by category:

#### Security
```
**Security Review** ✅/⚠️
- [Findings]
```

#### Correctness
```
**Correctness** ✅/⚠️
- [Logic errors or concerns]
- [Error handling gaps]
```

#### Performance
```
**Performance** ✅/⚠️
- [Optimization opportunities]
- [Resource concerns]
```

#### Code Quality
```
**Code Quality** ✅/⚠️
- [Maintainability issues]
- [Design concerns]
```

#### Testing
```
**Testing** ✅/⚠️
- [Coverage gaps]
- [Test quality observations]
```

### 4. Comment Best Practices

**For Issues Found:**

```
### 🔴 CRITICAL: [Issue]
**File**: `path/to/file.js` (line 42)
**Problem**: [Specific explanation]
**Impact**: [Why this matters]
**Example**:
```js
// Current
problematic_code();

// Suggested
fixed_code();
```

**Reference**: [Link to documentation/standard]
```

**For Questions:**

```
### 🤔 Question
**File**: `path/to/file.js`
Can you explain the logic here? I want to understand...
```

**For Suggestions:**

```
### 💡 Suggestion
Consider using [approach] because [benefit]. This would...
```

**For Positive Feedback:**

```
### ✅ Good catch!
I like how you handled [situation]. This pattern...
```

### 5. Focus Areas by Language

#### Python
- PEP 8 compliance and naming conventions
- Type hints for clarity
- Context managers for resource cleanup
- Exception specificity
- List comprehensions vs loops
- Import organization

#### JavaScript/TypeScript
- Type safety and typing
- Async/await vs promise chains
- Closure and scope issues
- Event listener cleanup
- Module exports and imports
- Null/undefined handling with optional chaining

#### Java
- Checked vs unchecked exceptions
- Resource management (try-with-resources)
- Generics type safety
- Access modifiers appropriateness
- Immutability where appropriate
- Annotation usage

#### C#
- LINQ usage and deferred execution
- Async/await patterns
- IDisposable and using patterns
- Null handling (null-coalescing, nullable reference types)
- Access modifiers
- Property vs field usage

#### Go
- Error handling (if err != nil pattern)
- Goroutine leaks
- Channel usage and deadlocks
- Interface design
- Defer usage for cleanup
- Pointer vs value receiver selection

#### Rust
- Ownership and borrowing correctness
- Lifetime annotations
- Error handling (Result vs panic)
- Unsafe block justification
- Iterator usage
- Memory safety

### 6. When to Approve/Request Changes

**Approve** ✅
- No critical issues
- Minor suggestions can be addressed later
- Tests are adequate
- Code quality is acceptable

**Request Changes** 🔴
- Critical security or correctness issues found
- Significant architectural concerns
- Test coverage is inadequate
- Multiple high-priority issues

**Comment** 💬
- Suggestions for improvement
- Questions for clarification
- Positive feedback
- Informational notes

## After the Review

### 7. Engage in Discussion
- Respond promptly to author questions
- Be open to pushback on your suggestions
- Acknowledge if author has better context
- Discuss trade-offs constructively
- Learn from disagreements

### 8. Verify Changes
- Review the updated code after changes
- Check that concerns were addressed
- Ensure tests were added as suggested
- Confirm no new issues were introduced

### 9. Document Learnings
- Note patterns to watch for in future reviews
- Share knowledge with team if applicable
- Update team standards if needed

## Common Pitfalls to Avoid

### ❌ Don't
- Be pedantic about style without reasoning
- Make assumptions about code intent
- Request perfect code (pragmatism matters)
- Ignore context and business requirements
- Block on subjective preferences
- Leave vague comments
- Ignore positive contributions

### ✅ Do
- Explain the "why" behind feedback
- Provide specific examples
- Consider team productivity
- Focus on impact and risk
- Be specific and actionable
- Acknowledge good work
- Accept trade-offs gracefully

## Review Severity Levels

| Level | When to Use | Action |
|-------|------------|--------|
| 🔴 Critical | Security risk, logic error, crash | Request changes |
| 🟠 High | Important issue affecting reliability | Request changes or discuss |
| 🟡 Medium | Code quality, maintainability | Suggestion, can approve with note |
| 🔵 Low | Minor improvements, style | Nice to have, informational |

## Checklists

### Security Review Checklist
- [ ] No hardcoded secrets or credentials
- [ ] Input validation implemented
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] Authentication/authorization proper
- [ ] Token expiration handled
- [ ] HTTPS used for sensitive data
- [ ] CORS properly configured
- [ ] Dependencies are secure (check advisories)

### Performance Review Checklist
- [ ] No obvious N+1 queries detected
- [ ] Appropriate data structures used
- [ ] Caching leveraged where beneficial
- [ ] No memory leaks on long-running
- [ ] Async used for I/O operations
- [ ] No blocking operations in loops
- [ ] Regex compiled, not in loops
- [ ] Large payloads paginated
- [ ] Indexes considered for queries

### Code Quality Checklist
- [ ] Naming is clear and descriptive
- [ ] Functions have single responsibility
- [ ] Complexity is manageable (< 10 nested levels)
- [ ] No code duplication (DRY)
- [ ] Constants used instead of magic numbers
- [ ] Comments explain "why", not "what"
- [ ] Documentation is clear
- [ ] No dead code
- [ ] Error cases handled

### Testing Checklist
- [ ] Tests added for new code
- [ ] Edge cases tested
- [ ] Error paths tested
- [ ] Tests are independent
- [ ] Assertions are specific
- [ ] No test duplication
- [ ] Coverage adequate (>80% for critical)
- [ ] CI/CD jobs pass
- [ ] No flaky tests

## Resources

- [Code Review Best Practices](https://google.github.io/eng-practices/review/)
- [Cognitive Complexity](https://www.sonarsource.com/docs/owasp/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- See `CONSTITUTION.md` for governance principles
