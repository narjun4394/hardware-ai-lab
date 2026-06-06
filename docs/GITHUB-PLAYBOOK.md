# GitHub Portfolio Playbook

## What Recruiters and Collaborators Should See

A useful hardware + AI portfolio makes judgment visible. A reader should be able
to answer:

- What real problem did this solve?
- What did you personally design and build?
- What measurements support the result?
- What tradeoffs did you make?
- What failed, and how did you respond?
- Can someone else reproduce it?

## Weekly Workflow

1. Create a GitHub issue for the next measurable milestone.
2. Create a branch named after the issue, such as
   `feature/stream-accelerometer-data`.
3. Commit each understandable step.
4. Open a pull request, even when working alone.
5. Include test evidence, photos, plots, or measurements in the pull request.
6. Merge only when the milestone is reproducible.
7. Write a short learning-log entry.

## Good Commit Examples

- `docs: define vibration monitor success metrics`
- `feat: stream timestamped accelerometer samples`
- `test: compare normal and imbalanced motor captures`
- `fix: prevent dropped samples at 3.2 kHz`

Avoid commits such as `updates`, `stuff`, or one giant commit for the entire
project.

## Repository Strategy

Use this repository as the portfolio home base and starting lab. When a project
becomes substantial, move it into its own public repository and link it from the
main README.

