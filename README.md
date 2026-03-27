# AI Code Review Agent

A comprehensive agentic AI system for code review, quality assurance, and development assistance. This repository demonstrates how to set up specialized agents for different aspects of software development.

## 🚀 Features

### Specialized Agents
- **Code Reviewer Agent** - Comprehensive code analysis, security review, performance assessment
- **QA Tester Agent** - Testing strategy, coverage analysis, edge case identification
- **Developer Agent** - Feature implementation, debugging, refactoring, architecture guidance

### Key Capabilities
- Language-agnostic analysis (Python, JavaScript, Java, C#, Go, Rust, and more)
- Scans repository for issues and opportunities
- Provides constructive, educational feedback
- Suggests improvements with code examples
- Integrates with PR and issue workflows
- Automatic issue and PR creation

## 📋 Quick Start

### Using Slash Commands
```
/code-reviewer [request]      # Request code review
/qa-tester [request]           # Get QA testing assistance
/developer [request]           # Get development help
```

### Creating Issues
Use built-in templates in `.github/issue-templates/`:
- `code-review.md` - Code review requests
- `qa-issue.md` - QA testing tasks
- `dev-task.md` - Development tasks

## 📚 Documentation

### Core Files
- **[CONSTITUTION.md](CONSTITUTION.md)** - Governing principles and standards
- **[AGENTS.md](AGENTS.md)** - Agent registry and usage guide
- **[copilot-instructions.md](copilot-instructions.md)** - Workspace instructions

### Agent Details
- **[Code Reviewer Agent](.github/agents/code-reviewer.agent.md)** - Detailed agent specification
- **[QA Tester Agent](.github/agents/qa-tester.agent.md)** - Detailed agent specification
- **[Developer Agent](.github/agents/developer.agent.md)** - Detailed agent specification

### Instructions & Guidelines
- **[General Guidelines](.github/instructions/general.instructions.md)** - Code standards, documentation, version control
- **[Code Review Instructions](.github/instructions/code-review.instructions.md)** - Review process and best practices
- **[QA Testing Instructions](.github/instructions/qa-testing.instructions.md)** - Testing strategy and patterns
- **[Development Instructions](.github/instructions/development.instructions.md)** - Implementation and debugging

### Issue Templates
- [Code Review Template](.github/issue-templates/code-review.md)
- [QA Testing Template](.github/issue-templates/qa-issue.md)
- [Development Template](.github/issue-templates/dev-task.md)

## 🔧 Setup

### Installation
```bash
git clone https://github.com/pravends/ai-code-review-agent.git
cd ai-code-review-agent
pip install -r requirements.txt
```

### Configuration
1. Review [CONSTITUTION.md](CONSTITUTION.md) for project principles
2. Review [AGENTS.md](AGENTS.md) for agent setup
3. Customize agent behavior in [.github/agents/](.github/agents/)
4. Update team standards in [.github/instructions/](.github/instructions/)

## 💡 Usage Examples

### Code Review
```
/code-reviewer Review this PR for security vulnerabilities 
and suggest performance optimizations
```

Response includes:
- Security findings with severity levels
- Performance analysis
- Code quality observations
- Actionable recommendations

### QA Testing
```
/qa-tester Help me identify test coverage gaps for the payment module
```

Response includes:
- Coverage analysis
- Edge case suggestions
- Test scenario recommendations
- Coverage metrics

### Development Help
```
/developer How should I implement user authentication with OAuth2?
```

Response includes:
- Implementation approach
- Architecture recommendations
- Code examples
- Best practices
- Error handling strategies

## 🏗️ Project Structure

```
.
├── CONSTITUTION.md              # Project principles & governance
├── AGENTS.md                    # Agent registry & usage guide
├── copilot-instructions.md      # Workspace instructions
├── README.md                    # This file
│
└── .github/
    ├── agents/                  # Agent specifications
    │   ├── code-reviewer.agent.md
    │   ├── qa-tester.agent.md
    │   └── developer.agent.md
    │
    ├── instructions/            # Detailed guidelines
    │   ├── general.instructions.md
    │   ├── code-review.instructions.md
    │   ├── qa-testing.instructions.md
    │   └── development.instructions.md
    │
    └── issue-templates/         # GitHub issue templates
        ├── code-review.md
        ├── qa-issue.md
        └── dev-task.md
```

## 🎯 Agent Capabilities Matrix

| Capability | Code Reviewer | QA Tester | Developer |
|-----------|---|---|---|
| Code Analysis | ✅ Advanced | ✅ Test-focused | ✅ Logic-focused |
| Security Review | ✅ Comprehensive | ⚠️ Limited | ✅ Basic |
| Performance Analysis | ✅ Advanced | ⚠️ Basic | ✅ Intermediate |
| Test Strategy | ⚠️ Basic | ✅ Comprehensive | ✅ Intermediate |
| Implementation Guidance | ⚠️ Limited | ❌ None | ✅ Comprehensive |
| Debugging Support | ⚠️ Limited | ⚠️ Limited | ✅ Comprehensive |
| Refactoring | ⚠️ Suggestions | ❌ None | ✅ Comprehensive |
| Architecture Design | ✅ Evaluation | ⚠️ Limited | ✅ Design |

## 📖 Language Support

All agents work with any programming language:

**Programming Languages:** Python, JavaScript, TypeScript, Java, C#, Go, Rust, C++, PHP, Ruby, Scala, Kotlin, and more

**Frameworks:** Django, Flask, Express, Spring, React, Vue, Angular, ASP.NET, FastAPI, and others

**Databases:** SQL, NoSQL, Graph, Time-series databases

**Cloud:** AWS, Azure, GCP, Kubernetes, Docker

**Infrastructure:** Terraform, CloudFormation, Docker, Ansible

## 🔐 Security & Governance

### Principles
1. **Language Agnostic** - Work with any language or framework
2. **Non-intrusive** - Constructive, educational feedback
3. **Quality-focused** - Critical issues first, then important, then nice-to-have
4. **Transparent** - Clear reasoning and references
5. **Collaborative** - Support human decision-making

See [CONSTITUTION.md](CONSTITUTION.md) for full governance details.

## 🚦 Workflow Integration

### GitHub Actions
Agents can be triggered in CI/CD pipelines:

```yaml
- name: Request code review
  uses: copilot/agents/code-reviewer@v1
  with:
    scope: "pr"
    focus: ["security", "performance"]
```

### Pull Request Integration
```markdown
Request code review with:
@code-reviewer Review these changes
```

### Issue-Based Workflow
Create issues using templates:
```bash
gh issue create --template code-review --title "Review: [Component]"
gh issue create --template qa-issue --title "QA: [Feature]"
gh issue create --template dev-task --title "Dev: [Task]"
```

## 📊 Metrics & Reporting

### Code Review Metrics
- Number of issues identified by severity
- Coverage of different code areas
- Review time and turnaround

### QA Metrics
- Test coverage percentage
- Test gap identification
- Edge case coverage

### Development Metrics
- Feature implementation time
- Bug fix time
- Refactoring impact

## 🤝 Contributing

### Adding New Agents
1. Create agent file in `.github/agents/`
2. Follow existing agent patterns
3. Create corresponding instructions in `.github/instructions/`
4. Add issue template in `.github/issue-templates/`
5. Update AGENTS.md and CONSTITUTION.md
6. Submit for review

### Updating Guidelines
1. Edit relevant instruction file
2. Ensure consistency across agents
3. Document changes
4. Update this README if needed

## 📚 Additional Resources

- [Google Engineering Practices](https://google.github.io/eng-practices/)
- [OWASP Security Guidelines](https://owasp.org/)
- [Clean Code Principles](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
- [Testing on the Toilet](https://testing.googleblog.com/)
- [System Design Primer](https://github.com/donnemartin/system-design-primer)

## 📝 Changelog

### Version 1.0.0 (March 28, 2026)
- Initial release with three specialized agents
- Code Reviewer Agent for comprehensive code analysis
- QA Tester Agent for testing strategy and coverage
- Developer Agent for implementation and debugging
- Complete agent documentation and instructions
- GitHub issue templates
- Constitutional governance framework

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see LICENSE file for details.

## 🙏 Acknowledgments

Built with principles from:
- Google Engineering Practices
- Clean Code and SOLID principles
- Modern software architecture patterns
- Community best practices

## 📞 Support

For questions or issues:
1. Review relevant instruction file in `.github/instructions/`
2. Check AGENTS.md for agent capabilities
3. Consult CONSTITUTION.md for governance
4. Create an issue with appropriate template
5. Use `/developer` agent for help with setup

---

**Last Updated:** March 28, 2026  
**Version:** 1.0.0  
**Maintainers:** [Your Team]
