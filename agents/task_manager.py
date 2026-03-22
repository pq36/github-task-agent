from tools.github_tool import GitHubTool


class TaskManager:

    def __init__(self):
        self.github = GitHubTool()

    def execute(self, action, data):
        return self.github.run(action, data)