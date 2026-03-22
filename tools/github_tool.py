from agents.github_agent import GitHubAgent
from config.settings import GITHUB_USERNAME, DEFAULT_REPO


class GitHubTool:

    def __init__(self):
        self.agent = GitHubAgent(owner=GITHUB_USERNAME)

    def run(self, action, data=None):
        repo = data.get("repo", DEFAULT_REPO) if data else DEFAULT_REPO

        if action == "get_tasks":
            return self.agent.get_issues(repo)

        elif action == "create_task":
            return self.agent.create_issue(
                repo=repo,
                title=data.get("title"),
                body=data.get("body", ""),
                labels=[data.get("priority", "medium")]
            )

        elif action == "complete_task":
            return self.agent.close_issue(
                repo=repo,
                issue_number=data.get("issue_number")
            )

        return {"error": "Invalid action"}