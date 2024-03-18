from agents import HealthAgents
from tasks import HealthCoachTasks

def get_user_input(prompt):
    """Prompt the user for input."""
    print(prompt)  # Adjust this to match how you'd like to prompt the user
    return input("> ")

def display_agent_response(response):
    """Display the agent's response."""
    print(f"Agent: {response}")

def execute_task(task):
    """Simulate executing a task by displaying its description and capturing a simulated response."""
    print("\n[Task Description]")
    print(task.description)
    user_response = get_user_input("\n(Respond to the task, or type 'exit' to end the conversation)")
    if user_response.lower() == 'exit':
        return None  # Signal to exit the conversation
    return user_response  # In practice, this would involve processing the user's input related to the task.

def have_conversation_through_tasks(agents):
    """Initiate a conversation that sequentially goes through all the tasks."""
    # Initialize tasks
    task_manager = HealthCoachTasks(agents.hai_initial())
    
    # Define the sequence of tasks
    tasks_sequence = [
        task_manager.welcome_and_privacy_assurance(),
        task_manager.general_health_inquiry(),
        task_manager.symptom_exploration(),
        task_manager.lifestyle_and_routine(),
        task_manager.mental_wellbeing_check(),
        task_manager.health_goals_discussion(),
        task_manager.custom_follow_ups_based_on_user_input(),
        task_manager.closing_and_next_steps(),
    ]

    for task in tasks_sequence:
        user_response = execute_task(task)
        if user_response is None:  # User chose to exit
            print("Exiting conversation.")
            return
        display_agent_response(f"Simulated response to: {user_response}")
    
    print("\nThank you for participating in the health interview.")

# Assuming you've already defined your HealthAgents class elsewhere
agents = HealthAgents()
have_conversation_through_tasks(agents)
