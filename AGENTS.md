# Agent Registry

## Overview
This repository contains three specialized agents for different aspects of software development and quality assurance. Each agent is language-agnostic and works across all programming languages and frameworks.

All agents follow the principles defined in [CONSTITUTION.md](CONSTITUTION.md).

---

## Agents

### 1. Code Reviewer Agent (`/code-reviewer`)

**Purpose:** Comprehensive code analysis and quality assurance

**Use Cases:**
- Pull request reviews
- Code quality audits
- Security vulnerability identification
- Performance optimization suggestions
- Architecture evaluation
- Test coverage assessment

**Expertise:**
- Security review (vulnerabilities, best practices)
- Code correctness (logic errors, edge cases)
- Performance analysis (complexity, optimization)
- Code quality (readability, maintainability)
- Testing & coverage (adequacy, effectiveness)
- Architecture & design patterns

**Output:**
- Categorized findings by severity (Critical → Low)
- Detailed explanations with examples
- Actionable recommendations
- References to best practices

**Documentation:**
- [Agent Details](.github/agents/code-reviewer.agent.md)
- [Review Instructions](.github/instructions/code-review.instructions.md)
- [Issue Template](.github/issue-templates/code-review.md)

**Example Invocation:**
```
/code-reviewer Please review this pull request for security issues and performance concerns
```

---

### 2. QA Tester Agent (`/qa-tester`)

**Purpose:** Quality assurance, testing strategy, and validation

**Use Cases:**
- Test planning and strategy
- Test coverage gap analysis
- Test implementation guidance
- Edge case identification
- Quality metric assessment
- Test quality evaluation

**Expertise:**
- Test coverage analysis
- Edge case & boundary testing
- Test quality assessment
- Functional validation
- Non-functional testing (performance, security)
- Test architecture & design

**Output:**
- Test gap reports
- Edge case suggestions
- Quality recommendations
- Test scenario guidance
- Coverage metrics

**Documentation:**
- [Agent Details](.github/agents/qa-tester.agent.md)
- [QA Instructions](.github/instructions/qa-testing.instructions.md)
- [Issue Template](.github/issue-templates/qa-issue.md)

**Example Invocation:**
```
/qa-tester Help me identify test coverage gaps for the payment module
```

---

### 3. Developer Agent (`/developer`)

**Purpose:** Feature implementation, debugging, and technical problem-solving

**Use Cases:**
- Feature implementation guidance
- Bug diagnosis and troubleshooting
- Code refactoring
- Performance optimization
- Architecture & design decisions
- Technical mentoring

**Expertise:**
- Feature implementation (design, architecture, coding)
- Debugging & troubleshooting (root cause analysis)
- Code refactoring (safe, incremental improvements)
- Performance optimization (profiling, analysis)
- Architecture & design (patterns, principles)
- Problem-solving (algorithms, data structures)

**Output:**
- Implementation guidance with code examples
- Bug analysis and reproduction steps
- Refactoring suggestions
- Performance optimization recommendations
- Architecture consultation

**Documentation:**
- [Agent Details](.github/agents/developer.agent.md)
- [Development Instructions](.github/instructions/development.instructions.md)
- [Issue Template](.github/issue-templates/dev-task.md)

**Example Invocation:**
```
/developer Help me implement user authentication with OAuth
```

---

## Language Support

All agents work with any programming language and framework:

### Programming Languages
- **Dynamic:** Python, JavaScript, Ruby, PHP, Perl
- **Compiled:** Java, C#, C++, Go, Rust, D, Kotlin
- **Functional:** Scala, Haskell, Clojure, F#, Elixir

### Frameworks & Platforms
- **Web:** Django, Flask, Express, Spring, ASP.NET, FastAPI
- **Frontend:** React, Vue, Angular, Svelte
- **Mobile:** React Native, Flutter, Swift, Kotlin
- **Data:** SQL, NoSQL, Graph Databases, Data Pipelines
- **Cloud:** AWS, Azure, GCP, Kubernetes
- **Infrastructure:** Docker, Terraform, CloudFormation

---

## How to Use Agents

### 1. Using Slash Commands
Type `/` in your chat to see available agents and skills:

```
/code-reviewer [your request]
/qa-tester [your request]
/developer [your request]
```

### 2. In Pull Requests
Request specific agent reviews:

```markdown
@code-reviewer Please review for security issues
@qa-tester Suggest test scenarios for this feature
@developer Is my implementation approach sound?
```

### 3. Creating Agent-Based Issues
Use the issue templates to create structured tasks:

- [Code Review Template](.github/issue-templates/code-review.md)
- [QA Testing Template](.github/issue-templates/qa-issue.md)
- [Development Template](.github/issue-templates/dev-task.md)

---

## Governance & Standards

### Constitution
All agents operate under principles defined in [CONSTITUTION.md](CONSTITUTION.md):
- Language agnostic operation
- Non-intrusive, constructive feedback
- Quality over quantity
- Transparency in findings
- Collaborative workflow

### Review Standards
Each agent follows established standards:
- **Code Reviewer:** Focus on Critical → High → Medium → Low severity issues
- **QA Tester:** Coverage goals, test quality metrics, edge case identification
- **Developer:** SOLID principles, design patterns, performance-first analysis

### Communication Guidelines
- Use clear, concise language
- Provide examples and specific recommendations
- Reference documentation and standards
- Include reasoning behind suggestions

---

## Instructions & Guidelines

### General Guidelines
[General Development Guidelines](.github/instructions/general.instructions.md)
- Code standards (naming, organization, comments)
- Documentation (README, API docs, code docs)
- Version control (branches, commits)
- CI/CD pipeline
- Security best practices
- Performance guidelines
- Error handling
- Testing standards
- Code review guidelines

### Specific Instructions
1. [Code Review Instructions](.github/instructions/code-review.instructions.md)
   - Before/during/after review process
   - Structure and format
   - Language-specific focus areas
   - Common pitfalls

2. [QA Testing Instructions](.github/instructions/qa-testing.instructions.md)
   - Testing strategy & pyramid
   - Unit/integration/E2E testing
   - Edge case identification
   - Mocking & stubbing
   - Test quality metrics

3. [Development Instructions](.github/instructions/development.instructions.md)
   - Feature implementation process
   - Debugging methodology
   - Refactoring safely
   - Performance optimization
   - Architecture & design

---

## Quick Reference

| Need | Agent | Template | Instructions |
|------|-------|----------|---|
| Code quality review | Code Reviewer | [code-review.md](.github/issue-templates/code-review.md) | [code-review.instructions.md](.github/instructions/code-review.instructions.md) |
| Test planning | QA Tester | [qa-issue.md](.github/issue-templates/qa-issue.md) | [qa-testing.instructions.md](.github/instructions/qa-testing.instructions.md) |
| Feature implementation | Developer | [dev-task.md](.github/issue-templates/dev-task.md) | [development.instructions.md](.github/instructions/development.instructions.md) |
| General guidelines | All | - | [general.instructions.md](.github/instructions/general.instructions.md) |

---

## Creating Issues with Agents

### To create a Code Review issue:
```bash
gh issue create --template code-review --title "Code Review: [Component Name]"
```

### To create a QA Testing issue:
```bash
gh issue create --template qa-issue --title "QA: [Component Name] - Testing"
```

### To create a Development task:
```bash
gh issue create --template dev-task --title "Dev: [Feature/Task Name]"
```

---

## Integration with CI/CD

Agents can be integrated into your pipeline:

1. **Pre-commit hooks:** Run code quality checks
2. **PR validation:** Automatically request reviews
3. **Test execution:** Run test suites
4. **Coverage reporting:** Track test coverage trends
5. **Deployment gates:** Validate before production

---

## FAQ

**Q: Can I use multiple agents for one task?**  
A: Yes! You can work with multiple agents. For example:
- `/developer` to implement a feature
- `/qa-tester` to plan tests
- `/code-reviewer` to review the PR

**Q: How do agents handle language-specific code?**  
A: All agents automatically detect language and adapt their responses using language idioms and best practices.

**Q: What if I need specialized agents for my workflow?**  
A: You can create custom agents following the same patterns. See `.github/agents/` for examples.

**Q: How are agent decisions documented?**  
A: See [CONSTITUTION.md](CONSTITUTION.md) for governance, and individual `.instructions.md` files for detailed guidelines.

---

## Resources

- [Constitution](CONSTITUTION.md) - Governing principles
- [Workspace Instructions](copilot-instructions.md) - Overview of agents
- [.github/agents/](. github/agents/) - Agent specifications
- [.github/instructions/](.github/instructions/) - Detailed guidelines
- [.github/issue-templates/](.github/issue-templates/) - Issue templates

---

## Contact & Contribution

To update or improve agents:
1. Create an issue describing the change
2. Follow existing agent patterns
3. Update relevant documentation
4. Submit for review

For questions about agent usage, refer to the relevant instructions file or use an agent directly!

---

**Last Updated:** March 28, 2026  
**Version:** 1.0.0
