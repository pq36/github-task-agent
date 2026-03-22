import json
from utils.gemini_client import get_gemini_model


SYSTEM_PROMPT = """
You are an AI freelancer productivity assistant.

Convert user input into structured JSON.

Available actions:
1. create_task
2. get_tasks
3. complete_task

Format:
{
  "action": "create_task",
  "data": {
    "title": "...",
    "body": "...",
    "priority": "low/medium/high"
  }
}

Rules:
- add/create/remind → create_task
- show/list → get_tasks
- done/completed → complete_task
- Output ONLY JSON (no explanation)
"""


class PlannerAgent:

    def __init__(self):
        self.llm = get_gemini_model()

    def plan(self, user_input: str):
        prompt = f"{SYSTEM_PROMPT}\n\nUser Input: {user_input}"

        response = self.llm.invoke(prompt)
        output = response.content.strip()

        # 🔥 Clean Gemini output
        if "```" in output:
            output = output.split("```")[1]
            output = output.replace("json", "").strip()

        try:
            return json.loads(output)
        except:
            return {
                "error": "Invalid JSON",
                "raw_output": output
            }