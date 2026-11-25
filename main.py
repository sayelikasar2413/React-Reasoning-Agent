"""
ReAct Reasoning Agent
Goal: Prepare a college project presentation before 2:00 PM.

This is a beginner-friendly, rule-based simulation of the ReAct loop:
Thought -> Action -> Observation -> next Thought.

The tools are simulated Python functions, so no API key is required.
"""

from dataclasses import dataclass


@dataclass
class ToolResult:
    success: bool
    message: str


# -----------------------------
# Tools used by the agent
# -----------------------------

def collect_content() -> ToolResult:
    """Simulate collecting a teammate's project section."""
    # Intentional failure to demonstrate dynamic replanning.
    return ToolResult(
        success=False,
        message="Teammate's section is not available."
    )


def make_backup_content() -> ToolResult:
    """Create a temporary section from already available project notes."""
    return ToolResult(
        success=True,
        message=(
            "A temporary section was drafted from the project report "
            "and marked for verification."
        )
    )


def create_outline() -> ToolResult:
    return ToolResult(
        success=True,
        message="Presentation outline created from the available project notes."
    )


def create_slides() -> ToolResult:
    return ToolResult(
        success=True,
        message=(
            "Slides created with available content and a clearly marked "
            "placeholder for the missing section."
        )
    )


def review_slides() -> ToolResult:
    return ToolResult(
        success=True,
        message="Slides reviewed and speaking points prepared."
    )


TOOLS = {
    "collect_content": collect_content,
    "make_backup_content": make_backup_content,
    "create_outline": create_outline,
    "create_slides": create_slides,
    "review_slides": review_slides,
}


# -----------------------------
# ReAct agent
# -----------------------------

def log(step_type: str, message: str) -> None:
    print(f"{step_type.upper()}: {message}")


def run_agent() -> None:
    print("=" * 65)
    print("REACT REASONING AGENT")
    print("GOAL: Prepare a college project presentation before 2:00 PM.")
    print("=" * 65)

    log("Thought", "I should collect the project content before planning the slides.")
    log("Action", "Use tool: collect_content")
    result = TOOLS["collect_content"]()
    log("Observation", result.message)

    # Dynamic replanning: react to the failed content collection step.
    if not result.success:
        log(
            "Thought",
            "The teammate's section is missing. Waiting may affect the deadline."
        )
        log(
            "Thought",
            "I will prepare a temporary section from available notes and mark it for review."
        )
        log("Action", "Use tool: make_backup_content")
        backup_result = TOOLS["make_backup_content"]()
        log("Observation", backup_result.message)

        if not backup_result.success:
            log("Final status", "Could not recover from the missing content. Human help is needed.")
            return

        log(
            "Thought",
            "The backup is ready. I can continue, but the temporary section must be verified."
        )

    # Continue the original plan after recovery.
    for tool_name, thought in [
        ("create_outline", "The content is organised. I can now prepare the slide outline."),
        ("create_slides", "The outline is ready. I can now create the slides."),
        ("review_slides", "The slides are ready. I should review them before delivery."),
    ]:
        log("Thought", thought)
        log("Action", f"Use tool: {tool_name}")
        tool_result = TOOLS[tool_name]()
        log("Observation", tool_result.message)

        if not tool_result.success:
            log("Thought", f"The action {tool_name} failed, so I should stop and request human help.")
            log("Final status", "Task not completed.")
            return

    log(
        "Thought",
        "All planned steps are complete. The temporary section is marked for verification."
    )
    log("Final status", "Presentation draft is ready for human review before 2:00 PM.")
    print("=" * 65)


if __name__ == "__main__":
    run_agent()
