---
name: general-guidelines
description: "General guidelines and best practices for all development activities across the team."
applyTo: "**/*"
---

# General Development Guidelines

## Overview
These guidelines apply to all developers, reviewers, and QA engineers working on this project. They establish common practices and expectations.

## Code Standards

### 1. Naming Conventions
Follow language-specific conventions:

| Language | Convention | Example |
|----------|-----------|---------|
| Python | snake_case | `calculate_total_price`, `user_service.py` |
| JavaScript/TypeScript | camelCase | `calculateTotalPrice`, `userService.ts` |
| Java | PascalCase | `CalculateTotalPrice`, `UserService.java` |
| C# | PascalCase | `CalculateTotalPrice`, `UserService.cs` |
| Go | camelCase | `calculateTotalPrice`, `userService.go` |
| Rust | snake_case | `calculate_total_price`, `user_service.rs` |

### 2. File Organization
```
project/
├── src/                 # Source code
│   ├── domain/         # Business logic (entities, rules)
│   ├── services/       # Service layer (orchestration)
│   ├── controllers/    # Request handlers / API routes
│   ├── repositories/   # Data access layer
│   ├── utils/          # Utility functions
│   ├── middleware/     # Middleware (logging, auth, etc.)
│   └── config/         # Configuration
├── tests/              # Test files
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/               # Documentation
├── scripts/            # Build and utility scripts
└── README.md          # Project documentation
```

### 3. Code Comments
Write comments that explain **why**, not **what**:

```python
# Bad: Comment explains what the code does (redundant)
# Increment counter
counter += 1

# Good: Comment explains why
# Increment counter to track the number of retry attempts
# Reset on successful operation to prevent exponential backoff
counter += 1
```

### 4. Function/Method Guidelines

**Keep functions small and focused:**
```python
# Good: Single responsibility
def validate_email(email):
    """Validate email format."""
    return re.match(r'^[^@]+@[^@]+\.[^@]+$', email)

def send_confirmation_email(user):
    """Send confirmation email to user."""
    if validate_email(user.email):
        # send logic
        pass

# Bad: Multiple responsibilities
def create_user(data):
    # validation
    # database insert
    # email sending
    # logging
    # response formatting
    pass
```

**Use clear parameter names:**
```python
# Bad: Unclear parameters
def process_data(d, x, y, z):
    pass

# Good: Clear parameter names
def calculate_discount(price, quantity, discount_rate):
    pass
```

## Documentation

### 1. README.md
Every project/module should have a README with:
- [ ] Project description
- [ ] Features
- [ ] Prerequisites
- [ ] Installation instructions
- [ ] Usage examples
- [ ] Configuration guide
- [ ] Contributing guidelines
- [ ] License information

### 2. Code Documentation

**Python (Docstrings)**
```python
def calculate_discount(price: float, quantity: int) -> float:
    """
    Calculate discount based on price and quantity.
    
    Args:
        price: Product price in dollars
        quantity: Number of items purchased
        
    Returns:
        Discount amount in dollars
        
    Raises:
        ValueError: If price or quantity is negative
        
    Example:
        >>> calculate_discount(100, 5)
        10.0
    """
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative")
    
    discount_rate = 0.1 if quantity >= 5 else 0
    return price * discount_rate
```

**JavaScript (JSDoc)**
```javascript
/**
 * Calculate discount based on price and quantity.
 *
 * @param {number} price - Product price in dollars
 * @param {number} quantity - Number of items purchased
 * @returns {number} Discount amount in dollars
 * @throws {Error} If price or quantity is negative
 * 
 * @example
 * calculateDiscount(100, 5);
 * // returns 10
 */
function calculateDiscount(price, quantity) {
  if (price < 0 || quantity < 0) {
    throw new Error('Price and quantity must be non-negative');
  }
  
  const discountRate = quantity >= 5 ? 0.1 : 0;
  return price * discountRate;
}
```

### 3. API Documentation

Document all API endpoints:
```markdown
### POST /api/users

Creates a new user.

**Request Body:**
```json
{
  "email": "user@example.com",
  "firstName": "John",
  "lastName": "Doe"
}
```

**Response:**
- Status: 201 Created
```json
{
  "id": "usr_123",
  "email": "user@example.com",
  "firstName": "John",
  "createdAt": "2024-03-28T10:30:00Z"
}
```

**Error Responses:**
- 400 Bad Request: Invalid input
- 409 Conflict: Email already exists
```

## Version Control

### 1. Commit Messages
Use clear, descriptive commit messages:

```
Format: [TYPE] Short description (50 chars max)

Body (if needed):
- More detailed explanation
- Multiple points if necessary

Footer:
Closes #123
Related-To: #456
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style (not logic changes)
- `refactor`: Code refactoring
- `perf`: Performance improvement
- `test`: Test additions/fixes
- `chore`: Build, deps, CI/CD

**Examples:**
```
feat: Add user authentication via OAuth
fix: Prevent race condition in database migration
docs: Update API documentation
perf: Optimize database query performance
```

### 2. Branching Strategy

**Branch naming:**
```
feature/feature-name          # New feature
bugfix/bug-description        # Bug fix
refactor/refactoring-name     # Refactoring
docs/documentation-update     # Documentation
perf/optimization-name        # Performance
```

**Branch protection:**
- All branches require code review before merge
- CI/CD must pass before merge
- No direct pushes to main/master branch

### 3. Pull Request Process

1. Create feature branch from `main`
2. Make commits with clear messages
3. Push to remote and create PR
4. Request reviewers (at least 2)
5. Address feedback and push updates
6. Squash commits if necessary
7. Merge after approval
8. Delete feature branch

## CI/CD Pipeline

### 1. Required Checks
Before merging, these must pass:
- [ ] Code linting (ESLint, Pylint, etc.)
- [ ] Type checking (TypeScript, mypy)
- [ ] Unit tests
- [ ] Integration tests
- [ ] Code coverage (>80% target)
- [ ] Security scan (SAST, dependency check)
- [ ] Build success

### 2. Deployment Process
```
main branch → Test environment → Staging → Production
```

## Security Best Practices

### 1. Secrets Management
```
✌️ Never commit secrets, passwords, API keys
✌️ Use environment variables
✌️ Use secrets management tools (AWS Secrets, HashiCorp Vault)
✌️ Rotate secrets regularly
```

### 2. Input Validation
```python
# Always validate and sanitize user input
def process_user_input(data):
    # Validate type
    if not isinstance(data, str):
        raise ValueError("Input must be a string")
    
    # Validate length
    if len(data) > 1000:
        raise ValueError("Input too long")
    
    # Validate pattern
    if not re.match(r'^[a-zA-Z0-9\s]+$', data):
        raise ValueError("Input contains invalid characters")
    
    return data.strip()
```

### 3. Dependency Management
- Use lock files (package-lock.json, poetry.lock, Cargo.lock)
- Regularly update dependencies
- Check for security vulnerabilities
- Review security advisories

## Performance Guidelines

### 1. Optimization Priority
1. Make it work (correctness)
2. Make it clear (readability)
3. Make it fast (performance)

### 2. Bottleneck Identification
```
✌️ Profile first, then optimize
✌️ Don't guess about performance
✌️ Use appropriate tools for your language
```

### 3. Resource Management
```
✌️ Close file handles and connections
✌️ Limit memory usage
✌️ Handle timeouts appropriately
✌️ Implement rate limiting where needed
```

## Error Handling

### 1. Principles
- Be specific about errors
- Provide context (what failed, why)
- Don't expose internal details
- Log errors appropriately
- Recover gracefully when possible

### 2. Error Logging
```python
import logging

logger = logging.getLogger(__name__)

try:
    perform_operation()
except SpecificException as e:
    # Log with context
    logger.error(
        "Operation failed",
        extra={
            "error": str(e),
            "operation": "perform_operation",
            "user_id": user_id,
            "timestamp": datetime.now()
        }
    )
    # Re-raise or handle
    raise
```

## Testing Standards

### 1. Test Coverage Goals
- Critical code: >85% coverage
- Important code: >75% coverage
- Overall target: >80% coverage

### 2. Test Organization
```
tests/
├── unit/                # Unit tests
│   ├── test_models.py
│   ├── test_services.py
│   └── test_utils.py
├── integration/         # Integration tests
│   ├── test_api.py
│   └── test_database.py
└── e2e/               # End-to-end tests
    └── test_workflows.py
```

### 3. Test Quality
- Each test has one assertion (or logical group)
- Tests are independent
- Tests have descriptive names
- No test interdependencies
- Fast execution (<100ms for unit tests)

## Code Review Guidelines

### 1. As a Reviewer
- [ ] Understand the change context
- [ ] Review for correctness
- [ ] Check security implications
- [ ] Verify test coverage
- [ ] Be constructive
- [ ] Provide examples when suggesting changes
- [ ] Acknowledge good work

### 2. As an Author
- [ ] Keep PRs reasonably sized
- [ ] Write clear PR description
- [ ] Respond to feedback promptly
- [ ] Ask for clarification if needed
- [ ] Be open to suggestions
- [ ] Test locally before requesting review

## Continuous Learning

### 1. Stay Updated
- Follow language/framework release notes
- Review security advisories
- Keep dependencies current
- Learn from code reviews

### 2. Share Knowledge
- Document solutions to problems
- Share useful tools or resources
- Mentor junior developers
- Discuss architectural decisions

## Resources

- [Google Style Guides](https://google.github.io/styleguide/)
- [OWASP Security Guidelines](https://owasp.org/)
- [Clean Code Principles](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
- [Refactoring Techniques](https://refactoring.guru/)
- See `CONSTITUTION.md` for project governance
