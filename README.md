# ReAct Reasoning Agent

A beginner-friendly Python project for **Unit II: Reasoning, Planning and Decision-Making (CO-2)**.

## Problem statement

Build a reasoning agent using the ReAct (Reason + Act) framework. The agent should divide a multi-step goal into smaller tasks, execute them using tools, observe the results, and dynamically replan when a step fails.

## Goal selected

Prepare a college project presentation and make it ready for review before 2:00 PM.

## Sub-tasks

1. Collect project content from teammates and available notes.
2. Prepare a slide outline.
3. Create the presentation slides.
4. Review the slides and prepare speaking points.

## ReAct cycle

The agent follows this loop:

1. **Thought:** Decide what should happen next.
2. **Action:** Call a Python tool.
3. **Observation:** Read the tool's result.
4. **Replan:** If an action fails, choose a recovery action.

## Dynamic replanning example

The `collect_content()` tool intentionally returns a failure because a teammate's section is unavailable. The agent detects the failed result and changes its plan:

- It calls `make_backup_content()`.
- It creates a temporary section from available project notes.
- It marks the temporary section for verification.
- It continues with the outline, slide creation, and review.

The agent does not claim that the missing teammate content was received.

## Project structure

```text
react_reasoning_agent/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.9 or later
- No external Python packages are required.

## Run the project

Open a terminal in this folder and run:

```bash
python main.py
```

On some Windows installations, use:

```bash
py main.py
```

The terminal prints the Thought / Action / Observation trace for one complete run.

## Important note

This is an educational simulation. The tools are Python functions that return sample results; they do not actually access teammates' files or create PowerPoint slides. The purpose is to demonstrate the ReAct reasoning cycle and dynamic replanning. A real implementation would connect these tools to file storage and presentation software, with human approval before final delivery.
