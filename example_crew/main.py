from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Crew, Task



from tasks import HealthCoachTasks
from agents import HealthAgents



# Initialize the task and agent classes
tasks = HealthCoachTasks()
agents = HealthAgents()

print("## Welcome to 'Hai' the Health Coach Interface")
print('------------------------------------------------')

# For testing, we might want a simple command line interface
action = input("Please select an action:\n1. Start Initial Interview\n2. Generate Health Insight\n3. Daily Check-in\n> ")

# Create Agents
hai_initial_agent = agents.hai_initial()
insight_generator_agent = agents.insight_generator_agent()
hai_daily_agent = agents.hai_daily()

# Define Tasks for each agent (for illustration, let's assume each method is already defined in HealthCoachTasks)
initial_interview_task = tasks.initial_health_interview(hai_initial_agent)
health_insight_task = tasks.weekly_health_insight(insight_generator_agent)
daily_checkin_task = tasks.daily_symptom_checkin(hai_daily_agent)

# Decide on action based on user input
if action == "1":
    selected_task = initial_interview_task
    selected_agent = hai_initial_agent
elif action == "2":
    selected_task = health_insight_task
    selected_agent = insight_generator_agent
elif action == "3":
    selected_task = daily_checkin_task
    selected_agent = hai_daily_agent
else:
    print("Invalid selection. Exiting.")
    exit()

# Create a Crew with the selected agent and task
test_crew = Crew(
    agents=[selected_agent],
    tasks=[selected_task],
    verbose=True
)

# Kick off the selected task and print the result
result = test_crew.kickoff()

print("\n## 'Hai' the Health Coach responds:")
print(result)