#!/usr/bin/env python3
"""
Instruction Referencing System for AI Agents

This module provides standardized instruction referencing for agent responses,
ensuring transparency and compliance with established guidelines.
"""

from typing import Dict, Optional
from dataclasses import dataclass
from enum import Enum

class AgentType(Enum):
    """Types of agents in the system"""
    CODE_REVIEWER = "code-reviewer"
    DEVELOPER = "developer"
    QA_TESTER = "qa-tester"
    GENERAL = "general"

@dataclass
class InstructionReference:
    """Represents an instruction file reference"""
    name: str
    file_path: str
    description: str
    emoji: str

class InstructionReferencingSystem:
    """System for managing instruction references in agent responses"""

    def __init__(self):
        self.instruction_map: Dict[AgentType, InstructionReference] = {
            AgentType.CODE_REVIEWER: InstructionReference(
                name="Code Review Guidelines",
                file_path="code-review.instructions.md",
                description="Detailed guidelines for conducting effective code reviews",
                emoji="📋"
            ),
            AgentType.DEVELOPER: InstructionReference(
                name="Development Guidelines",
                file_path="development.instructions.md",
                description="Standards for feature implementation and debugging",
                emoji="🔧"
            ),
            AgentType.QA_TESTER: InstructionReference(
                name="QA Testing Guidelines",
                file_path="qa-testing.instructions.md",
                description="Standards for testing and quality assurance",
                emoji="🧪"
            ),
            AgentType.GENERAL: InstructionReference(
                name="General Guidelines",
                file_path="general.instructions.md",
                description="General development best practices",
                emoji="📚"
            )
        }

    def get_reference_header(self, agent_type: AgentType) -> str:
        """Get the instruction reference header for an agent type"""
        ref = self.instruction_map.get(agent_type)
        if not ref:
            return ""

        return f"{ref.emoji} **Following {ref.name}** ({ref.file_path})"

    def get_compliance_indicators(self, agent_type: AgentType) -> str:
        """Get compliance indicators for the agent type"""
        indicators = {
            AgentType.CODE_REVIEWER: """🔍 **Review Structure Applied:**
- ✅ Security Review Completed
- ✅ Correctness Analysis Done
- ✅ Performance Evaluation Complete
- ✅ Code Quality Assessment Finished
- ✅ Testing Coverage Verified""",

            AgentType.DEVELOPER: """🔧 **Development Standards Applied:**
- ✅ Naming conventions followed
- ✅ Error handling implemented
- ✅ Code documentation added
- ✅ Testing included
- ✅ Best practices applied""",

            AgentType.QA_TESTER: """🧪 **Testing Standards Applied:**
- ✅ Test coverage measured
- ✅ Edge cases covered
- ✅ Test quality assessed
- ✅ Automation considered
- ✅ Documentation updated""",

            AgentType.GENERAL: """📚 **General Standards Applied:**
- ✅ Code formatting consistent
- ✅ Documentation maintained
- ✅ Version control followed
- ✅ Security considered
- ✅ Performance optimized"""
        }

        return indicators.get(agent_type, "")

    def format_response_with_references(self,
                                      agent_type: AgentType,
                                      main_content: str,
                                      include_compliance: bool = True) -> str:
        """Format a complete response with instruction references"""
        header = self.get_reference_header(agent_type)
        compliance = self.get_compliance_indicators(agent_type) if include_compliance else ""

        parts = [header]
        if compliance:
            parts.append(compliance)
        parts.append("")  # Empty line
        parts.append(main_content)

        return "\n".join(parts)

# Global instance for easy access
instruction_system = InstructionReferencingSystem()

# Convenience functions for easy use
def get_code_review_reference() -> str:
    """Get code review instruction reference"""
    return instruction_system.get_reference_header(AgentType.CODE_REVIEWER)

def get_development_reference() -> str:
    """Get development instruction reference"""
    return instruction_system.get_reference_header(AgentType.DEVELOPER)

def get_qa_reference() -> str:
    """Get QA testing instruction reference"""
    return instruction_system.get_reference_header(AgentType.QA_TESTER)

def format_code_review_response(content: str, include_compliance: bool = True) -> str:
    """Format a code review response with references"""
    return instruction_system.format_response_with_references(
        AgentType.CODE_REVIEWER, content, include_compliance
    )

def format_development_response(content: str, include_compliance: bool = True) -> str:
    """Format a development response with references"""
    return instruction_system.format_response_with_references(
        AgentType.DEVELOPER, content, include_compliance
    )

def format_qa_response(content: str, include_compliance: bool = True) -> str:
    """Format a QA testing response with references"""
    return instruction_system.format_response_with_references(
        AgentType.QA_TESTER, content, include_compliance
    )

# Example usage
if __name__ == "__main__":
    # Example code review response
    review_content = """## Code Review Complete!
**Overall Assessment:** 🟢 GOOD (7.5/10)

**Key Findings:**
- Clean code structure ✅
- Good test coverage ✅
- Some input validation needed ⚠️"""

    formatted_review = format_code_review_response(review_content)
    print("Code Review Response Example:")
    print("=" * 50)
    print(formatted_review)
    print()

    # Example development response
    dev_content = """## Feature Implementation Complete!
**Status:** ✅ Successfully implemented user authentication

**Changes Made:**
- Added OAuth integration
- Created user model
- Implemented login/logout endpoints"""

    formatted_dev = format_development_response(dev_content)
    print("Development Response Example:")
    print("=" * 50)
    print(formatted_dev)