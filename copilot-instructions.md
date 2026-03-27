# AI Code Review Agent - Copilot Instructions

## Overview
This workspace is configured with specialized agents for code review workflows:
- **Code Reviewer Agent**: Analyzes code quality, security, and best practices
- **QA Tester Agent**: Identifies test coverage gaps and validation issues
- **Developer Agent**: Assists with implementation, debugging, and refactoring

All agents are language-agnostic and work across Python, JavaScript, TypeScript, Java, C#, Go, Rust, and other languages.

## How to Use Agents

### Invoke via Slash Commands
Type `/` to see available agents and skills:
- `/code-reviewer` - Start a code review session
- `/qa-tester` - Begin QA testing workflow
- `/developer` - Get development assistance

### Agent Capabilities
- **Code Reviewer**: Detects code smells, security vulnerabilities, performance issues
- **QA Tester**: Validates test coverage, identifies edge cases, suggests test scenarios
- **Developer**: Helps implement features, debug issues, refactor code

## Configuration
- Agents use consistent practices defined in `CONSTITUTION.md`
- Each agent has specific instructions in `.github/instructions/`
- Language detection is automatic; agents adapt to any language
- Issue templates in `.github/issue-templates/` match agent specialties

## Language Support
All agents work with:
- **Programming**: Python, JavaScript, TypeScript, Java, C#, Go, Rust, C++, PHP, Ruby
- **Markup**: HTML, CSS/SCSS/Less, XML, JSON, YAML
- **Infrastructure**: Terraform, CloudFormation, Docker, Kubernetes
- **Configuration**: dotenv, properties, INI files
- **Query Languages**: SQL, GraphQL

## Best Practices
1. Provide full context when asking agents for review
2. Use issue templates when creating tickets via agents
3. Reference `CONSTITUTION.md` for governance principles
4. Keep agent instructions updated in `.github/instructions/`

See `CONSTITUTION.md` for principles and guidelines.
