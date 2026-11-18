
from typing import TypedDict
import time

from langgraph.graph import StateGraph, START, END

from agents.research_agent import research_agent
from agents.developer_agent import developer_agent
from agents.marketing_agent import marketing_agent
from agents.finance_agent import finance_agent
from agents.validation_agent import validation_agent
from agents.ceo_agent import ceo_agent


# ============================================================
# 1. WORKFLOW STATE
# ============================================================

class StartupState(TypedDict, total=False):
    startup_idea: str

    research_report: str
    developer_report: str
    marketing_report: str
    finance_report: str
    validation_report: str
    final_report: str

    agent_metrics: dict
    agent_errors: dict
    agent_statuses: dict
    total_execution_time: float


# ============================================================
# 2. RESPONSE NORMALIZATION
# ============================================================

def extract_text(response):

    if isinstance(response, str):
        return response

    if isinstance(response, list):
        text_parts = []

        for block in response:
            if isinstance(block, dict):
                text_parts.append(block.get("text", ""))
            elif isinstance(block, str):
                text_parts.append(block)

        return "\n".join(text_parts)

    return str(response)


# ============================================================
# 3. AGENT NODES
# ============================================================

def research_node(state: StartupState):

    print("\n[1/6] Running Research Agent...")

    response = research_agent(state["startup_idea"])

    return {
        "research_report": extract_text(response)
    }


def developer_node(state: StartupState):

    print("\n[2/6] Running Developer Agent...")

    response = developer_agent(
        state["startup_idea"],
        state["research_report"]
    )

    return {
        "developer_report": extract_text(response)
    }


def marketing_node(state: StartupState):

    print("\n[3/6] Running Marketing Agent...")

    response = marketing_agent(
        state["startup_idea"],
        state["research_report"],
        state["developer_report"]
    )

    return {
        "marketing_report": extract_text(response)
    }


def finance_node(state: StartupState):

    print("\n[4/6] Running Finance Agent...")

    response = finance_agent(
        state["startup_idea"],
        state["research_report"],
        state["developer_report"],
        state["marketing_report"]
    )

    return {
        "finance_report": extract_text(response)
    }


def validation_node(state: StartupState):

    print("\n[5/6] Running Validation Agent...")

    response = validation_agent(
        state["startup_idea"],
        state["research_report"],
        state["developer_report"],
        state["marketing_report"],
        state["finance_report"]
    )

    return {
        "validation_report": extract_text(response)
    }


def ceo_node(state: StartupState):

    print("\n[6/6] Running CEO Agent...")

    response = ceo_agent(
        state["startup_idea"],
        state["research_report"],
        state["developer_report"],
        state["marketing_report"],
        state["finance_report"],
        state["validation_report"]
    )

    return {
        "final_report": extract_text(response)
    }


# ============================================================
# 4. AGENT CONFIGURATION
# ============================================================

AGENT_CONFIG = {

    "research": {
        "output_key": "research_report",
        "dependencies": []
    },

    "developer": {
        "output_key": "developer_report",
        "dependencies": ["research"]
    },

    "marketing": {
        "output_key": "marketing_report",
        "dependencies": ["developer"]
    },

    "finance": {
        "output_key": "finance_report",
        "dependencies": ["marketing"]
    },

    "validation": {
        "output_key": "validation_report",
        "dependencies": ["finance"]
    },

    "ceo": {
        "output_key": "final_report",
        "dependencies": ["validation"]
    }
}


# ============================================================
# 5. SAFE PROGRESS CALLBACK
# ============================================================

def notify_progress(
    progress_callback,
    node_name,
    agent_name,
    completed_count,
    status
):

    if not progress_callback:
        return

    try:

        progress_callback(
            node_name,
            agent_name,
            completed_count,
            status
        )

    except Exception as error:

        print(
            f"Progress callback warning for {agent_name}: "
            f"{error}"
        )


# ============================================================
# 6. TIMED AGENT EXECUTION WITH ERROR HANDLING
# ============================================================

def timed_node(
    node_name,
    node_function,
    agent_metrics,
    progress_callback,
    agent_names,
    execution_tracker
):

    config = AGENT_CONFIG[node_name]

    output_key = config["output_key"]
    dependencies = config["dependencies"]

    def execute_node(state):

        start_time = time.perf_counter()

        agent_name = agent_names[node_name]

        current_statuses = dict(
            state.get("agent_statuses", {})
        )

        current_errors = dict(
            state.get("agent_errors", {})
        )

        # ----------------------------------------------------
        # CHECK WHETHER A REQUIRED AGENT FAILED OR WAS SKIPPED
        # ----------------------------------------------------

        failed_dependencies = [
            dependency
            for dependency in dependencies
            if current_statuses.get(dependency) != "Completed"
        ]

        if failed_dependencies:

            elapsed_time = 0.0

            agent_metrics[node_name] = elapsed_time

            reason = ", ".join(
                agent_names[dependency]
                for dependency in failed_dependencies
            )

            skip_message = (
                f"{agent_name} was skipped because "
                f"the required dependency did not complete: "
                f"{reason}."
            )

            current_statuses[node_name] = "Skipped"

            current_errors[node_name] = skip_message

            print(f"\n{skip_message}")

            notify_progress(
                progress_callback,
                node_name,
                agent_name,
                execution_tracker["completed"],
                "Skipped"
            )

            return {
                output_key: skip_message,
                "agent_statuses": current_statuses,
                "agent_errors": current_errors
            }

        # ----------------------------------------------------
        # START AGENT
        # ----------------------------------------------------

        notify_progress(
            progress_callback,
            node_name,
            agent_name,
            execution_tracker["completed"],
            "Running"
        )

        print(f"\n{agent_name} is running...")

        try:

            result = node_function(state)

            if not isinstance(result, dict):
                raise ValueError(
                    "Agent returned an invalid result."
                )

            report = extract_text(
                result.get(output_key, "")
            )

            if not report.strip():
                raise ValueError(
                    "Agent returned an empty report."
                )

            elapsed_time = round(
                time.perf_counter() - start_time,
                2
            )

            agent_metrics[node_name] = elapsed_time

            execution_tracker["completed"] += 1

            current_statuses[node_name] = "Completed"

            print(
                f"{agent_name} completed successfully "
                f"in {elapsed_time:.2f} seconds."
            )

            notify_progress(
                progress_callback,
                node_name,
                agent_name,
                execution_tracker["completed"],
                "Completed"
            )

            return {
                output_key: report,
                "agent_statuses": current_statuses,
                "agent_errors": current_errors
            }

        except Exception as error:

            elapsed_time = round(
                time.perf_counter() - start_time,
                2
            )

            agent_metrics[node_name] = elapsed_time

            error_message = (
                f"{type(error).__name__}: {str(error)}"
            )

            failure_message = (
                f"{agent_name} could not complete its task. "
                f"Error: {error_message}"
            )

            current_statuses[node_name] = "Failed"

            current_errors[node_name] = failure_message

            print(
                f"\n{agent_name} FAILED "
                f"after {elapsed_time:.2f} seconds."
            )

            print("Failure reason:", error_message)

            notify_progress(
                progress_callback,
                node_name,
                agent_name,
                execution_tracker["completed"],
                "Failed"
            )

            # Return a failure result instead of crashing
            # the complete LangGraph workflow.

            return {
                output_key: failure_message,
                "agent_statuses": current_statuses,
                "agent_errors": current_errors
            }

    return execute_node


# ============================================================
# 7. BUILD WORKFLOW
# ============================================================

def build_workflow(
    agent_metrics,
    progress_callback,
    agent_names,
    execution_tracker
):

    workflow = StateGraph(StartupState)

    nodes = {

        "research": research_node,
        "developer": developer_node,
        "marketing": marketing_node,
        "finance": finance_node,
        "validation": validation_node,
        "ceo": ceo_node

    }

    for node_name, node_function in nodes.items():

        workflow.add_node(
            node_name,

            timed_node(
                node_name,
                node_function,
                agent_metrics,
                progress_callback,
                agent_names,
                execution_tracker
            )
        )

    # Sequential execution

    workflow.add_edge(START, "research")

    workflow.add_edge("research", "developer")

    workflow.add_edge("developer", "marketing")

    workflow.add_edge("marketing", "finance")

    workflow.add_edge("finance", "validation")

    workflow.add_edge("validation", "ceo")

    workflow.add_edge("ceo", END)

    return workflow.compile()


# ============================================================
# 8. RUN WORKFLOW WITH LIVE PROGRESS AND ANALYTICS
# ============================================================

def run_startup_workflow_with_progress(
    startup_idea,
    progress_callback=None
):

    agent_metrics = {}

    agent_names = {

        "research": "Research Agent",
        "developer": "Developer Agent",
        "marketing": "Marketing Agent",
        "finance": "Finance Agent",
        "validation": "Validation Agent",
        "ceo": "CEO Agent"

    }

    execution_tracker = {
        "completed": 0
    }

    startup_workflow = build_workflow(
        agent_metrics,
        progress_callback,
        agent_names,
        execution_tracker
    )

    initial_state = {

        "startup_idea": startup_idea,

        "agent_errors": {},

        "agent_statuses": {}

    }

    final_state = initial_state.copy()

    workflow_start = time.perf_counter()

    try:

        for update in startup_workflow.stream(
            initial_state,
            stream_mode="updates"
        ):

            for node_output in update.values():

                final_state.update(node_output)

    except Exception as error:

        # Catch unexpected workflow-level errors.

        print("\nWORKFLOW-LEVEL ERROR:", error)

        final_state["workflow_error"] = (
            f"{type(error).__name__}: {str(error)}"
        )

    total_execution_time = round(
        time.perf_counter() - workflow_start,
        2
    )

    # --------------------------------------------------------
    # ATTACH EXECUTION ANALYTICS
    # --------------------------------------------------------

    final_state["agent_metrics"] = agent_metrics.copy()

    final_state["total_execution_time"] = (
        total_execution_time
    )

    final_state["agent_errors"] = dict(
        final_state.get("agent_errors", {})
    )

    final_state["agent_statuses"] = dict(
        final_state.get("agent_statuses", {})
    )

    # --------------------------------------------------------
    # EXECUTION SUMMARY
    # --------------------------------------------------------

    completed_count = execution_tracker["completed"]

    failed_count = sum(
        1
        for status in final_state["agent_statuses"].values()
        if status == "Failed"
    )

    skipped_count = sum(
        1
        for status in final_state["agent_statuses"].values()
        if status == "Skipped"
    )

    print("\n======================================")
    print("STARTUP WORKFLOW EXECUTION SUMMARY")
    print("======================================")

    print(f"Completed Agents: {completed_count}/6")
    print(f"Failed Agents: {failed_count}")
    print(f"Skipped Agents: {skipped_count}")

    print("Agent Metrics:", agent_metrics)

    print(
        "Total Execution Time:",
        total_execution_time,
        "seconds"
    )

    if failed_count == 0 and skipped_count == 0:

        print("Workflow Status: SUCCESS")

    else:

        print("Workflow Status: PARTIAL FAILURE")

    print("======================================")

    return final_state


# ============================================================
# 9. SIMPLE WORKFLOW EXECUTION
# ============================================================

def run_startup_workflow(startup_idea):

    return run_startup_workflow_with_progress(
        startup_idea
    )
