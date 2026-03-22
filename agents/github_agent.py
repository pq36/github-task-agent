import requests
from config.settings import BASE_URL, HEADERS


class GitHubAgent:

    def __init__(self, owner):
        self.owner = owner

    def get_repositories(self):
        url = f"{BASE_URL}/users/{self.owner}/repos"
        return requests.get(url, headers=HEADERS).json()

    def get_issues(self, repo):
        url = f"{BASE_URL}/repos/{self.owner}/{repo}/issues"
        return requests.get(url, headers=HEADERS).json()

    def create_issue(self, repo, title, body="", labels=None):
        url = f"{BASE_URL}/repos/{self.owner}/{repo}/issues"

        payload = {
            "title": title,
            "body": body,
            "labels": labels or []
        }

        return requests.post(url, json=payload, headers=HEADERS).json()

    def close_issue(self, repo, issue_number):
        url = f"{BASE_URL}/repos/{self.owner}/{repo}/issues/{issue_number}"
        payload = {"state": "closed"}
        return requests.patch(url, json=payload, headers=HEADERS).json()