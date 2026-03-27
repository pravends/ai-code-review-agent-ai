---
name: development-instructions
description: "Detailed guidelines for feature implementation, debugging, architecture, and problem-solving across all languages."
applyTo: "src/**,lib/**,app/**,components/**"
---

# Development Instructions

## Purpose
These instructions guide the development process to ensure quality implementation, maintainable code, and effective problem-solving across all programming languages and frameworks.

## Feature Implementation

### 1. Requirements Analysis
Before implementing, understand:

```
✓ What problem does this solve?
✓ Who are the users?
✓ What are the acceptance criteria?
✓ What are the edge cases?
✓ What are the performance requirements?
✓ What are the security concerns?
✓ How does it integrate with existing code?
✓ What testing is required?
```

### 2. Design Phase

#### Architecture Decision Record (ADR)
For significant decisions, document:

```markdown
# ADR: [Title]

## Status
Proposed | Accepted | Superseded

## Context
[Why we need to make this decision]

## Decision
[What we decided and why]

## Consequences
Benefits: [...]
Tradeoffs: [...]
Risks: [...]
```

#### Design Review Checklist
- [ ] Architecture matches requirements
- [ ] Integration points identified
- [ ] Data model designed
- [ ] API contracts defined
- [ ] Error handling strategy
- [ ] Performance implications reviewed
- [ ] Security implications reviewed
- [ ] Scalability considered
- [ ] Backward compatibility ensured
- [ ] Monitoring and logging planned

### 3. Implementation

#### Code Structure Pattern
```
feature/
├── domain/          # Business logic
├── services/        # Service layer
├── controllers/     # Request handlers
├── models/          # Data models
├── utils/           # Helper functions
├── tests/           # Test files
└── README.md        # Feature documentation
```

#### Implementation Checklist
- [ ] Code follows language idioms
- [ ] Naming is clear and consistent
- [ ] Functions are single responsibility
- [ ] Error handling is comprehensive
- [ ] Edge cases are handled
- [ ] Code is DRY (Don't Repeat Yourself)
- [ ] Comments explain "why" not "what"
- [ ] No hardcoded values
- [ ] Logging is meaningful
- [ ] Configuration is externalized

### 4. Error Handling Strategy

#### Approach by Language

**Python**
```python
class APIError(Exception):
    """Base exception for API errors"""
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

try:
    # Operation that might fail
    result = external_api.call()
except requests.ConnectionError as e:
    logger.error(f"Connection failed: {e}")
    raise APIError("Service temporarily unavailable", 503)
except ValueError as e:
    logger.error(f"Invalid data: {e}")
    raise APIError("Invalid input provided", 400)
```

**JavaScript/TypeScript**
```typescript
class APIError extends Error {
  constructor(message: string, public statusCode: number = 400) {
    super(message);
    this.name = 'APIError';
  }
}

async function fetchUser(id: string): Promise<User> {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) {
      throw new APIError('User not found', response.status);
    }
    return response.json();
  } catch (error) {
    if (error instanceof APIError) throw error;
    logger.error('Unexpected error:', error);
    throw new APIError('Internal server error', 500);
  }
}
```

**Java**
```java
public class APIException extends Exception {
    private int statusCode;
    
    public APIException(String message, int statusCode) {
        super(message);
        this.statusCode = statusCode;
    }
    
    public int getStatusCode() {
        return statusCode;
    }
}

public User getUserById(String id) throws APIException {
    try {
        return userRepository.findById(id)
            .orElseThrow(() -> new APIException("User not found", 404));
    } catch (DatabaseException e) {
        logger.error("Database error: {}", e.getMessage());
        throw new APIException("Internal server error", 500);
    }
}
```

#### Error Handling Best Practices
- [ ] Specific exception types for different errors
- [ ] Meaningful error messages (not just "Error")
- [ ] Log errors with full context
- [ ] Don't swallow exceptions silently
- [ ] Provide user-friendly error messages
- [ ] Include error codes for programmatic handling
- [ ] Clean up resources (files, connections) in finally/finally
- [ ] Don't expose internal details to users
- [ ] Handle async errors appropriately
- [ ] Test error paths thoroughly

## Debugging & Troubleshooting

### 1. Systematic Debugging Approach

#### Step 1: Understand the Problem
```
What is the observed behavior?
What should happen instead?
When did this start?
What changed recently?
Can it be reproduced consistently?
```

#### Step 2: Gather Information
```
Error messages and stack traces
Log files and timestamps
Environment details (OS, version, config)
Code changes (git diff, recent commits)
External service status
Database state
```

#### Step 3: Form Hypotheses
```
Based on symptoms, what could cause this?
What are 3-5 most likely causes?
What evidence would prove/disprove each?
```

#### Step 4: Test Hypotheses
```
Run controlled tests
Check logs for timestamp correlation
Check for state-related issues
Verify assumptions about inputs
Test in isolation vs. full system
```

#### Step 5: Identify Root Cause
```
What is the actual cause?
Why wasn't it caught earlier?
How can we prevent recurrence?
```

#### Step 6: Implement Fix
```
Fix the root cause, not the symptom
Add tests to prevent recurrence
Update logging if needed
Document the issue and fix
```

### 2. Debugging Tools by Language

**Python**
```python
# Using pdb debugger
import pdb
pdb.set_trace()

# Or use breakpoint() in Python 3.7+
breakpoint()

# Print debugging with f-strings
print(f"Variable value: {var}, Type: {type(var)}")

# Logging configuration
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

**JavaScript/TypeScript**
```javascript
// VSCode debugging
// Add to .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/index.js"
    }
  ]
}

// Console debugging
console.log('value:', value);
console.table(data);
console.error('Error:', error);
console.time('operation');
// ... operation ...
console.timeEnd('operation');

// Debugger keyword
debugger; // Execution stops here when DevTools open
```

**Java**
```java
// Using IDE debugger
// Set breakpoints and use Step Over/Into/Out

// Logging
import java.util.logging.*;
Logger logger = Logger.getLogger(ClassName.class.getName());
logger.fine("Detailed info");
logger.info("General info");
logger.warning("Warning");
logger.severe("Error");

// Exception printing
try {
    // operation
} catch (Exception e) {
    e.printStackTrace();
    logger.log(Level.SEVERE, "Error occurred", e);
}
```

### 3. Common Debugging Patterns

| Issue | Investigation Steps |
|-------|---------------------|
| NullPointerException | Check assignments, null checks, API responses |
| Memory leak | Profile heap, check event listeners, verify cleanup |
| Race condition | Add logging with timestamps, use mutex/locks |
| Infinite loop | Add loop counter, check exit condition |
| Wrong output | Verify input data, trace logic, check assumptions |
| Timeout | Check resource limits, verify I/O operations, profile |
| Intermittent failure | Capture system state, check for timing issues |

## Code Refactoring

### 1. Refactoring Safely

#### Before Refactoring
```
✓ Ensure comprehensive tests exist
✓ Establish baseline metrics
✓ Plan changes incrementally
✓ Get team agreement on approach
```

#### During Refactoring
```
✓ Make one small change at a time
✓ Run tests after each change
✓ Verify no new issues introduced
✓ Keep commits small and logical
✓ Don't combine refactoring with feature changes
```

#### After Refactoring
```
✓ Verify all tests pass
✓ Measure improvements
✓ Code review for quality
✓ Document significant changes
```

### 2. Common Refactoring Patterns

#### Extract Method
```python
# Before
def process_order(order):
    total = 0
    for item in order.items:
        total += item.price * item.quantity
    
    if total > 100:
        total *= 0.9  # 10% discount
    
    tax = total * 0.1
    return total + tax

# After
def process_order(order):
    subtotal = calculate_subtotal(order)
    discounted = apply_discount(subtotal)
    return apply_tax(discounted)

def calculate_subtotal(order):
    return sum(item.price * item.quantity for item in order.items)

def apply_discount(amount):
    return amount * 0.9 if amount > 100 else amount

def apply_tax(amount):
    return amount * 1.1
```

#### Extract Class
```javascript
// Before
class User {
  constructor(firstName, lastName, email, phone, street, city, zip) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.email = email;
    this.phone = phone;
    this.street = street;
    this.city = city;
    this.zip = zip;
  }
}

// After
class Address {
  constructor(street, city, zip) {
    this.street = street;
    this.city = city;
    this.zip = zip;
  }
}

class User {
  constructor(firstName, lastName, email, phone, address) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.email = email;
    this.phone = phone;
    this.address = address;
  }
}
```

#### Replace Magic Numbers with Constants
```java
// Before
if (age >= 18 && age < 65) {
    // working age
}

// After
private static final int WORKING_AGE_MIN = 18;
private static final int WORKING_AGE_MAX = 65;

if (age >= WORKING_AGE_MIN && age < WORKING_AGE_MAX) {
    // working age
}
```

## Performance Optimization

### 1. Optimization Methodology

#### Step 1: Measure
```
✓ Identify actual bottlenecks (don't guess)
✓ Use profiling tools
✓ Establish baseline metrics
✓ Measure before and after
```

#### Step 2: Analyze Algorithms
```
✓ Check Big O complexity
✓ Consider space-time tradeoffs
✓ Look for algorithmic improvements
✓ Verify you're solving the real problem
```

#### Step 3: Optimize Iteratively
```
✓ Make one change at a time
✓ Measure each change
✓ Keep it if it improves performance
✓ Revert if no improvement or side effects
```

#### Step 4: Document
```
✓ Why was this optimization needed?
✓ What was the before/after measurement?
✓ What was the trade-off?
✓ Why is this better than alternatives?
```

### 2. Common Performance Issues

| Issue | Solution |
|-------|----------|
| N+1 queries | Use batch queries or JOINs |
| Missing indexes | Add database indexes for queries |
| Full table scans | Use WHERE clauses, optimize queries |
| Memory leaks | Clear event listeners, break circular refs |
| Blocking I/O | Use async/await, non-blocking I/O |
| Inefficient loops | Use streaming, pagination, caching |
| Large objects in memory | Use generators, pagination |
| Repeated computation | Memoization, caching |

### 3. Caching Strategy

```javascript
// Memoization for expensive computations
const memoize = (fn) => {
  const cache = new Map();
  return (...args) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
};

const expensiveOperation = memoize((x, y) => {
  // Expensive computation
  return x + y; // (simplified)
});
```

## Architecture & Design

### 1. SOLID Principles

| Principle | Description | Example |
|-----------|-------------|---------|
| **S**ingle Responsibility | One reason to change | UserRepository handles user data only |
| **O**pen/Closed | Open for extension, closed for modification | Use interfaces/inheritance |
| **L**iskov Substitution | Subtypes must be substitutable | Dog extends Animal correctly |
| **I**nterface Segregation | Many client-specific interfaces | Don't force unused methods |
| **D**ependency Inversion | Depend on abstractions | Use interfaces, not concrete classes |

### 2. Design Patterns

#### Factory Pattern
```python
class DatabaseFactory:
    @staticmethod
    def create(db_type: str):
        if db_type == 'postgres':
            return PostgresConnection()
        elif db_type == 'mysql':
            return MysqlConnection()
        else:
            raise ValueError(f"Unknown db type: {db_type}")

db = DatabaseFactory.create('postgres')
```

#### Observer Pattern
```javascript
class EventEmitter {
  constructor() {
    this.events = {};
  }
  
  on(event, listener) {
    if (!this.events[event]) {
      this.events[event] = [];
    }
    this.events[event].push(listener);
  }
  
  emit(event, data) {
    if (this.events[event]) {
      this.events[event].forEach(listener => listener(data));
    }
  }
}

const emitter = new EventEmitter();
emitter.on('user-created', (user) => {
  console.log('New user:', user);
});
emitter.emit('user-created', { id: 1, name: 'John' });
```

## Development Checklist

### Before Commit
- [ ] Code compiles/runs without errors
- [ ] Tests pass locally
- [ ] Code is properly formatted
- [ ] No debug statements left
- [ ] Comments are meaningful
- [ ] Error handling is comprehensive
- [ ] No security issues identified
- [ ] Documentation updated
- [ ] Commit message is clear

### Before Push
- [ ] Branch is up to date with main
- [ ] All CI/CD checks pass
- [ ] Code review checklist complete
- [ ] No merge conflicts
- [ ] Related tests included

## Resources
- [Design Patterns](https://refactoring.guru/design-patterns)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Code Complete](https://www.oreilly.com/library/view/code-complete-2nd/0735619670/)
- See `CONSTITUTION.md` for governance principles
