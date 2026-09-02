# AAC GitHub Testbed

A small, **public, read-only** demo repository used by the *Agentic Access Control*
GitHub-Agent to run benchmark prompts through the OBOT gateway. It mirrors a minimal
MCP GitHub-agent project so prompts like "read the README", "list the open issues",
or "summarize run_query.py" have real targets.

## Contents
- `github_agent.py` - agent entry point (connects to the GitHub MCP, runs a ReAct agent)
- `run_query.py` - small CLI to run one prompt
- `shared_utils.py` - auth helpers for the OBOT gateway
- `requirements.txt` - Python dependencies
- `docs/` - overview, roadmap, tagline

Nothing here is secret; it exists purely so read-only demo prompts have something to read.
