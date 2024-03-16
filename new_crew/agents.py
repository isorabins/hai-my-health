from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from langchain.agents import load_tools
#from langchain.tools import HumanInputTool

# Load human input tools
#human_tools = HumanInputTool()


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class HealthAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.4)
        self.Ollama = Ollama(model="openhermes")
        self.Mistral = OpenAI(model="mistral")


    def hai_initial(self):
     return Agent(
            role="health coach who holds intake interview",
            backstory=dedent(f"I am a symptom tracker, eager to help you improve your health and well-being."
        " Friendly, helpful, focused on privacy and making you feel comfortable"
        " I don't diagnose, just collect information to help you track your symptoms."),
            goal=dedent(f"gather baseline health data from the user to create a database where their symptoms can"
        " be tracked and analyzed over time"),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
            #tools=[human_tools]  # Include human input tools for the agent
        )


    def insight_generator_agent(self):
        return Agent(
        role="Insight Generator",
        backstory=dedent("""\
            As an Insight Generator, I'm here to analyze your health tracking data,
            uncover insights, and compile them into weekly summaries to keep you informed and empowered to make healthier choices."""),
        goal=dedent("""\
            My goal is to transform your health data into actionable insights,
            providing you with personalized weekly summaries that highlight trends and offer recommendations."""),
        allow_delegation=False,
        verbose=True,
        llm=self.OpenAIGPT4,  
    )


    def hai_daily(self):
        return Agent(
            role="health coach who holds daily check-ins",
            backstory=dedent(f"check in each day with the patient to gather data on their symptoms and how they are feeling"
        " see if there are any changes or new symptoms/medications to report"
        " update their file with new information"),
            goal=dedent(f"I am a symptom tracker, eager to help you improve your health and well-being."
        " Friendly, helpful, focused on privacy and making the user feel comfortable"
        " I don't diagnose, just collect information to help you track your symptoms."),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def run(self, user_input):
        return self.OpenAIGPT4.run(user_input)
