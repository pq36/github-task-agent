from agents.planner_agent import PlannerAgent
from agents.task_manager import TaskManager


def main():
    planner = PlannerAgent()
    manager = TaskManager()

    print("\n🤖 Freelancer Productivity Agent (Gemini Powered)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("👋 Exiting...")
            break

        # 🧠 LLM Planning
        plan = planner.plan(user_input)
        print("\n🧠 Plan:", plan)

        if "error" in plan:
            print("❌ Error:", plan["raw_output"])
            continue

        # ⚙️ Execute Action
        result = manager.execute(
            action=plan["action"],
            data=plan.get("data", {})
        )

        print("\n✅ Result:", result)


if __name__ == "__main__":
    main()