# Instruction Referencing System - Usage Examples

## Overview
This system ensures that all agent responses explicitly reference the instructions they're following, providing transparency and accountability.

## How to Use

### 1. Import the System
```python
from instruction_referencing_system import (
    format_code_review_response,
    format_development_response,
    format_qa_response
)
```

### 2. Format Your Responses

#### Code Review Response
```python
review_content = """
## Code Review Complete!
**Overall Assessment:** 🟢 GOOD (7.5/10)

**Key Findings:**
- Clean code structure ✅
- Good test coverage ✅
- Some input validation needed ⚠️
"""

formatted_response = format_code_review_response(review_content)
print(formatted_response)
```

**Output:**
```
📋 **Following Code Review Guidelines** (code-review.instructions.md)
🔍 **Review Structure Applied:**
- ✅ Security Review Completed
- ✅ Correctness Analysis Done
- ✅ Performance Evaluation Complete
- ✅ Code Quality Assessment Finished
- ✅ Testing Coverage Verified

## Code Review Complete!
**Overall Assessment:** 🟢 GOOD (7.5/10)

**Key Findings:**
- Clean code structure ✅
- Good test coverage ✅
- Some input validation needed ⚠️
```

#### Development Response
```python
dev_content = """
## Feature Implementation Complete!
**Status:** ✅ Successfully implemented user authentication

**Changes Made:**
- Added OAuth integration
- Created user model
- Implemented login/logout endpoints
"""

formatted_response = format_development_response(dev_content)
```

**Output:**
```
🔧 **Following Development Guidelines** (development.instructions.md)
🔧 **Development Standards Applied:**
- ✅ Naming conventions followed
- ✅ Error handling implemented
- ✅ Code documentation added
- ✅ Testing included
- ✅ Best practices applied

## Feature Implementation Complete!
**Status:** ✅ Successfully implemented user authentication

**Changes Made:**
- Added OAuth integration
- Created user model
- Implemented login/logout endpoints
```

#### QA Testing Response
```python
qa_content = """
## Test Coverage Analysis Complete!
**Coverage:** 78% (Good)

**Recommendations:**
- Add tests for main() function
- Consider using pytest framework
- Add integration tests
"""

formatted_response = format_qa_response(qa_content)
```

## Benefits

### ✅ Transparency
Users can see exactly which guidelines are being followed.

### ✅ Consistency
All agents use the same referencing format.

### ✅ Accountability
Clear reference to standards ensures compliance.

### ✅ Education
Users learn about the guidelines being applied.

### ✅ Auditability
Easy to verify that proper procedures were followed.

## Integration with Agent System

### For Code Reviewer Agent
```python
class CodeReviewerAgent:
    def review_code(self, code):
        # Perform review logic
        findings = self.analyze_code(code)

        # Format response with references
        response_content = self.format_findings(findings)
        return format_code_review_response(response_content)
```

### For Developer Agent
```python
class DeveloperAgent:
    def implement_feature(self, requirements):
        # Implementation logic
        code = self.generate_code(requirements)

        # Format response with references
        response_content = self.format_implementation(code)
        return format_development_response(response_content)
```

### For QA Tester Agent
```python
class QATesterAgent:
    def analyze_coverage(self, tests):
        # Analysis logic
        coverage = self.measure_coverage(tests)

        # Format response with references
        response_content = self.format_coverage_report(coverage)
        return format_qa_response(response_content)
```

## Configuration

The system is configured in `instruction_referencing_system.py`:

```python
instruction_map = {
    AgentType.CODE_REVIEWER: InstructionReference(
        name="Code Review Guidelines",
        file_path="code-review.instructions.md",
        description="Detailed guidelines for conducting effective code reviews",
        emoji="📋"
    ),
    # ... other agent types
}
```

## Customization

### Adding New Agent Types
```python
# Add to AgentType enum
class AgentType(Enum):
    NEW_AGENT = "new-agent"

# Add to instruction_map
AgentType.NEW_AGENT: InstructionReference(
    name="New Agent Guidelines",
    file_path="new-agent.instructions.md",
    description="Guidelines for new agent type",
    emoji="🆕"
)
```

### Modifying Compliance Indicators
```python
def get_custom_compliance_indicators(agent_type: AgentType) -> str:
    """Custom compliance indicators for specific needs"""
    # Custom logic here
    pass
```

## Testing the System

```python
# Test the system
from instruction_referencing_system import format_code_review_response

def test_instruction_referencing():
    content = "Test content"
    result = format_code_review_response(content)

    assert "📋 **Following Code Review Guidelines**" in result
    assert "code-review.instructions.md" in result
    assert "Security Review Completed" in result
    print("✅ Instruction referencing system working correctly!")

if __name__ == "__main__":
    test_instruction_referencing()
```

## Migration Guide

### Before (Old Format)
```
## Code Review Complete!
- Found some issues
- Overall good
```

### After (New Format)
```
📋 **Following Code Review Guidelines** (code-review.instructions.md)
🔍 **Review Structure Applied:**
- ✅ Security Review Completed
- ✅ Correctness Analysis Done
- ✅ Performance Evaluation Complete
- ✅ Code Quality Assessment Finished
- ✅ Testing Coverage Verified

## Code Review Complete!
- Found some issues
- Overall good
```

## Best Practices

1. **Always include references** for agent responses
2. **Use appropriate agent type** for the context
3. **Keep compliance indicators** up to date
4. **Test the formatting** before deployment
5. **Document changes** in agent behavior

## Troubleshooting

### Issue: References not showing
**Solution:** Ensure the agent type is correctly specified

### Issue: Wrong guidelines referenced
**Solution:** Check that the correct AgentType is being used

### Issue: Compliance indicators outdated
**Solution:** Update the indicators in the system configuration

## Future Enhancements

- Add support for custom instruction sets
- Include version tracking for guidelines
- Add compliance validation
- Support for multiple instruction sets per agent
- Integration with automated compliance checking