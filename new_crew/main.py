from dotenv import load_dotenv
from crewai import Crew
from tasks import HealthCoachTasks
from agents import HealthAgents
from conversation import have_conversation_through_tasks  # Adjusted function name

load_dotenv()

# Initialize the agent classes
agents = HealthAgents()

# Instance of HealthCoachTasks no longer needed as tasks are called directly from agent methods
# Tasks are now more directly associated with agents in conversation flow

print("## Welcome to 'Hai' the Health Coach Interface")
print('------------------------------------------------')

# For testing, we might want a simple command line interface
action = input("Please select an action:\n1. Start Initial Interview\n2. Generate Health Insight\n3. Daily Check-in\n4. Have a Conversation\n> ")

# Define the selected agent based on user input
if action == "1":
    selected_agent = agents.hai_initial()
elif action == "2":
    selected_agent = agents.insight_generator_agent()
elif action == "3":
    selected_agent = agents.hai_daily()
elif action == "4":
    print("Starting a conversation with 'Hai'...")
    # Adjusted to start a conversation through tasks for a structured interview
    have_conversation_through_tasks(agents.hai_initial())
else:
    print("Invalid selection. Exiting.")
    exit()

# If action 1, 2, or 3 is selected, we execute the relevant task
if action in ["1", "2", "3"]:
    # For actions 1, 2, and 3, let's simulate the execution of a task
    # In practice, you might adapt this section to better fit how you intend to use tasks and agents
    print("\n## Simulating 'Hai' the Health Coach task execution for selected action...")
    # A placeholder to represent task execution since actual task execution logic will vary
    print(f"Task for action {action} executed with {selected_agent.role}.")
