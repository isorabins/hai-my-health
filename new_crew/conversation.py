from agents import HealthAgents


def get_user_input() -> str:
    """Get input from the user."""
    return input("Enter your message: ")

def display_agent_response(response: str):
    """Display the agent's response."""
    print(f"Agent: {response}")

def have_conversation(agent):
    """Initiate a conversation between the user and the agent."""
    while True:
        user_input = get_user_input()
        if user_input.lower() == "exit":
            break
        agent_response = agent.execute_task(user_input)
        display_agent_response(agent_response)