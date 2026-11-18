
import os

from workflow import run_startup_workflow


# ==========================================
# 1. SAVE AGENT REPORTS
# ==========================================

def save_report(filename, content):

    os.makedirs("outputs", exist_ok=True)

    file_path = os.path.join("outputs", filename)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Report saved successfully: {file_path}")


# ==========================================
# 2. MAIN STARTUP BUILDER
# ==========================================

def run_startup_builder():

    print("\n======================================")
    print("       MULTI-AGENT STARTUP BUILDER")
    print("======================================")

    startup_idea = input("\nEnter your startup idea: ").strip()

    if not startup_idea:
        print("Please enter a valid startup idea.")
        return

    try:

        # Execute all five agents through LangGraph
        print("\nStarting LangGraph workflow...")

        final_state = run_startup_workflow(startup_idea)

        # Extract individual reports
        research_report = final_state["research_report"]
        developer_report = final_state["developer_report"]
        marketing_report = final_state["marketing_report"]
        finance_report = final_state["finance_report"]
        validation_report = final_state["validation_report"]
        final_report = final_state["final_report"]

        # Save all five reports
        print("\nSaving generated reports...")

        save_report("research_report.md", research_report)
        save_report("developer_report.md", developer_report)
        save_report("marketing_report.md", marketing_report)
        save_report("finance_report.md", finance_report)
        save_report("validation_report.md", validation_report)
        save_report("final_startup_blueprint.md", final_report)

        # Display final startup blueprint
        print("\n======================================")
        print("       FINAL STARTUP BLUEPRINT")
        print("======================================\n")

        print(final_report)

        print("\n======================================")
        print("       STARTUP BUILDER COMPLETED")
        print("======================================")

        print("\nAll five reports have been saved successfully.")

    except Exception as error:

        print("\nAn error occurred while running the Startup Builder:")
        print(error)


# ==========================================
# 3. RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    run_startup_builder()
