"""Run a single GitHub-agent query from the command line."""
import asyncio
import sys
from github_agent import run_github_agent


def main() -> None:
    prompt = " ".join(sys.argv[1:]) or "List the open issues in this repository."
    print(asyncio.run(run_github_agent(prompt)))


if __name__ == "__main__":
    main()
