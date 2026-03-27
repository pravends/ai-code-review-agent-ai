---
name: qa-testing-instructions
description: "Detailed guidelines for QA testing, test strategy, and quality assurance across all programming languages and platforms."
applyTo: "**/*test*.py,**/*test*.js,**/*test*.ts,**/*spec*.js,**/*spec*.ts,test/**,tests/**,__tests__/**"
---

# QA Testing Instructions

## Purpose
These instructions guide QA activities to ensure comprehensive test coverage, high test quality, and effective bug identification across all programming languages and platforms.

## Testing Strategy

### 1. Understand Requirements
- [ ] Read user stories and acceptance criteria
- [ ] Identify success scenarios (happy path)
- [ ] Identify failure scenarios (sad path)
- [ ] Determine non-functional requirements
- [ ] Map test cases to requirements
- [ ] Identify test environment needs

### 2. Design Test Strategy

#### Test Pyramid
```
        /\
       /  \  E2E Tests (10%)
      /----\
     /      \
    /--------\  Integration Tests (30%)
   /          \
  /            \
 /              \  Unit Tests (60%)
/________________\
```

- **Unit Tests (60%)**: Individual functions/methods
- **Integration Tests (30%)**: Component interactions
- **E2E Tests (10%)**: Full user workflows

### 3. Test Coverage Planning
- [ ] Identify coverage by percentage (target: >80% for critical code)
- [ ] Plan coverage by code path (branch coverage)
- [ ] Plan coverage by feature area
- [ ] Identify untestable or low-value areas
- [ ] Set incremental coverage goals

## Unit Testing Guidelines

### 1. Test Structure
Use the AAA (Arrange-Act-Assert) pattern:

```python
# Python (pytest)
def test_calculate_discount():
    # Arrange
    calculator = PriceCalculator()
    base_price = 100
    discount_rate = 0.1
    
    # Act
    result = calculator.calculate_discount(base_price, discount_rate)
    
    # Assert
    assert result == 10
```

```javascript
// JavaScript (Jest)
describe('PriceCalculator', () => {
  it('should calculate discount correctly', () => {
    // Arrange
    const calculator = new PriceCalculator();
    const basePrice = 100;
    const discountRate = 0.1;
    
    // Act
    const result = calculator.calculateDiscount(basePrice, discountRate);
    
    // Assert
    expect(result).toBe(10);
  });
});
```

### 2. Test Naming
Name tests to clearly describe what they test:

```
test_[method_name]_with_[condition]_returns_[expected_result]
test_calculate_discount_with_valid_inputs_returns_discount_amount
test_process_payment_with_insufficient_funds_throws_error
```

### 3. What to Test
- [ ] Happy path (normal operation)
- [ ] Edge cases (boundary values)
- [ ] Error cases (exceptions)
- [ ] State changes
- [ ] Return values
- [ ] Side effects
- [ ] Interactions with dependencies

### 4. Unit Testing Checklist
- [ ] One assertion per test (or logical grouping)
- [ ] Tests are independent (no shared state)
- [ ] Tests run in any order
- [ ] Tests are fast (<100ms each)
- [ ] No hardcoded test data with special meaning
- [ ] Mocks appropriate for external dependencies
- [ ] Spies used to verify interactions
- [ ] Stubs provide predictable data
- [ ] Test setup is minimal and clear
- [ ] Cleanup (teardown) is handled

## Integration Testing Guidelines

### 1. When to Use Integration Tests
- [ ] Testing multiple components together
- [ ] Database interactions
- [ ] API calls and integrations
- [ ] Event bus or message queue interactions
- [ ] File system operations
- [ ] Authentication/authorization flows

### 2. Integration Test Setup
```javascript
// Jest example with database
describe('UserService Integration', () => {
  let db;
  
  beforeAll(async () => {
    // Setup: Start test database
    db = await setupTestDatabase();
  });
  
  afterEach(async () => {
    // Cleanup: Clear test data
    await db.clearAllTables();
  });
  
  afterAll(async () => {
    // Teardown: Stop test database
    await db.close();
  });
  
  it('should save and retrieve user', async () => {
    const user = { id: 1, name: 'John' };
    await userService.saveUser(user);
    const retrieved = await userService.getUserById(1);
    expect(retrieved).toEqual(user);
  });
});
```

### 3. API Contract Testing
```javascript
describe('User API Contract', () => {
  it('should return user object with expected schema', async () => {
    const response = await api.get('/users/1');
    
    // Verify schema
    expect(response.body).toHaveProperty('id');
    expect(response.body).toHaveProperty('name');
    expect(response.body).toHaveProperty('email');
    
    // Verify types
    expect(typeof response.body.id).toBe('number');
    expect(typeof response.body.name).toBe('string');
  });
});
```

## End-to-End Testing Guidelines

### 1. E2E Test Scenarios
Identify complete user workflows:

```
Scenario: User Registration and Login
1. Navigate to signup page
2. Fill registration form
3. Submit form
4. Verify confirmation email
5. Click email link
6. Verify email confirmed
7. Login with new credentials
8. Verify dashboard loads
```

### 2. E2E Test Implementation
```javascript
// Using Cypress
describe('User Registration Flow', () => {
  it('should register and login successfully', () => {
    // Navigate
    cy.visit('/signup');
    
    // Fill form
    cy.get('[data-testid="email-input"]').type('test@example.com');
    cy.get('[data-testid="password-input"]').type('SecurePass123!');
    cy.get('[data-testid="confirm-input"]').type('SecurePass123!');
    
    // Submit
    cy.get('[data-testid="signup-button"]').click();
    
    // Verify
    cy.url().should('include', '/dashboard');
    cy.get('[data-testid="welcome-message"]').should('be.visible');
  });
});
```

### 3. E2E Best Practices
- [ ] Use data attributes for element selection (`data-testid`)
- [ ] Avoid testing implementation details
- [ ] Test complete user workflows
- [ ] Use real data or realistic test data
- [ ] Handle timing issues with proper waits
- [ ] Take screenshots on failure
- [ ] Keep E2E tests lean (only critical paths)
- [ ] Run E2E tests in CI/CD pipeline

## Edge Case Testing

### Common Edge Cases to Test

#### Null/Nil/Undefined
```javascript
test_function_with_null_input_handles_gracefully
test_function_with_undefined_parameter_returns_default
```

#### Boundary Values
```javascript
test_function_with_zero_input
test_function_with_negative_input
test_function_with_max_integer_input
test_function_with_empty_string_input
test_function_with_very_large_collection_input
```

#### Type Mismatches
```javascript
test_function_expecting_number_receives_string
test_function_expecting_array_receives_single_item
test_function_expecting_object_receives_null
```

#### Concurrent Access
```javascript
test_concurrent_writes_to_shared_resource
test_race_condition_between_read_and_write
```

#### Resource Exhaustion
```javascript
test_function_with_memory_pressure
test_function_with_many_simultaneous_connections
test_function_with_disk_full_scenario
```

## Test Data Management

### 1. Test Data Approaches

**Approach 1: Fixtures (Recommended)**
```javascript
// fixtures/user.json
{
  "id": 1,
  "name": "Test User",
  "email": "test@example.com"
}

// In test
const testUser = require('./fixtures/user.json');
```

**Approach 2: Builders**
```javascript
class UserBuilder {
  withName(name) { this.name = name; return this; }
  withEmail(email) { this.email = email; return this; }
  build() { return { id: 1, ...this }; }
}

const testUser = new UserBuilder()
  .withName('John')
  .withEmail('john@example.com')
  .build();
```

**Approach 3: Factories**
```javascript
const createTestUser = (overrides = {}) => ({
  id: 1,
  name: 'Test User',
  email: 'test@example.com',
  ...overrides
});
```

### 2. Test Data Best Practices
- [ ] Use builders or factories for test data
- [ ] Make test data realistic
- [ ] Avoid magic numbers without context
- [ ] Use descriptive variable names
- [ ] Keep test data simple and minimal
- [ ] Do not hardcode production-like secrets
- [ ] Use factories with sensible defaults

## Mocking & Stubbing

### 1. When to Mock
| Scenario | Mock? |
|----------|-------|
| External API calls | ✅ Yes |
| Database calls (unit tests) | ✅ Yes |
| File I/O operations | ✅ Yes |
| Time/Date functions | ✅ Yes |
| Random number generators | ✅ Yes |
| User input | ❌ No (use fixtures) |
| Business logic | ❌ No (test real logic) |

### 2. Mocking Examples

```javascript
// Jest mocking
jest.mock('./api/userService');

describe('UserController', () => {
  it('should fetch user from service', async () => {
    // Setup mock
    userService.getUser.mockResolvedValue({
      id: 1, name: 'John'
    });
    
    // Call controller
    const result = await controller.getUserById(1);
    
    // Verify interaction
    expect(userService.getUser).toHaveBeenCalledWith(1);
    expect(result).toEqual({ id: 1, name: 'John' });
  });
});
```

### 3. Avoid Mock Over-use
- ❌ Don't mock the thing you're testing
- ❌ Don't mock to avoid testing real logic
- ❌ Don't create overly complex mocks
- ✅ Do mock external dependencies
- ✅ Do verify mock interactions
- ✅ Do keep mocks simple and readable

## Test Quality Metrics

### 1. Coverage Metrics
```
Statement Coverage: % of statements executed
Branch Coverage: % of if/else branches tested
Function Coverage: % of functions called
Line Coverage: % of lines executed
```

### 2. Healthy Metrics
- Critical code: >85% coverage
- Important code: >75% coverage
- Less critical: >60% coverage
- Overall target: >80%

### 3. Beyond Coverage
- Code coverage != good tests
- Focus on critical paths
- Test behavior, not implementation
- High coverage with bad tests is worse than lower coverage with good tests

## Continuous Testing

### 1. Test Automation in CI/CD
```yaml
# GitHub Actions example
- name: Run unit tests
  run: npm test -- --coverage

- name: Run integration tests
  run: npm run test:integration

- name: Run E2E tests
  run: npm run test:e2e
```

### 2. Test Reporting
- Generate coverage reports
- Track coverage trends
- Alert on coverage drops
- Publish test results
- Track flaky tests

### 3. Performance Testing
```javascript
// Detecting performance regressions
it('should complete in under 100ms', () => {
  const start = performance.now();
  expensiveOperation();
  const duration = performance.now() - start;
  expect(duration).toBeLessThan(100);
});
```

## Debugging Tests

### 1. Test Failure Analysis
- [ ] Read the full error message
- [ ] Examine stack trace
- [ ] Check actual vs expected values
- [ ] Review test setup code
- [ ] Verify test isolation
- [ ] Check for timing issues

### 2. Tools and Techniques
- Use debugger breakpoints
- Add console.log for variable inspection
- Use test reporters with detailed output
- Enable verbose test output
- Run single test to isolate
- Check test order dependency

## Common Testing Pitfalls

### ❌ Don't
- Write tests that test the test framework
- Test implementation details instead of behavior
- Create non-deterministic tests (flaky)
- Share state between tests
- Test multiple concerns in one test
- Hardcode test data
- Overuse mocks
- Ignore test warnings

### ✅ Do
- Test behavior and outcomes
- Keep tests isolated and independent
- Name tests clearly
- Use descriptive assertions
- Maintain test code like production code
- Review and refactor tests
- Keep tests fast
- Document complex test setups

## Checklists

### Before Submitting Tests
- [ ] All tests pass locally
- [ ] Tests have descriptive names
- [ ] One concern per test
- [ ] Edge cases covered
- [ ] Error cases handled
- [ ] Test data reasonable
- [ ] Mocks appropriate
- [ ] No hardcoded delays/waits
- [ ] Code coverage >80% for new code
- [ ] Tests documented if complex

### QA Review Checklist
- [ ] Requirements mapped to test cases
- [ ] Happy path covered
- [ ] Error paths covered
- [ ] Edge cases identified
- [ ] Test data realistic
- [ ] Acceptance criteria validable
- [ ] Environment dependencies clear
- [ ] Regression impact assessed
- [ ] Performance baselines set
- [ ] Security tested

## Resources
- [Testing Pyramid](https://martinfowler.com/bliki/TestPyramid.html)
- [Test Naming Best Practices](https://osherove.com/blog)
- [Jest Documentation](https://jestjs.io/)
- [Cypress Documentation](https://docs.cypress.io/)
- See `CONSTITUTION.md` for governance principles
