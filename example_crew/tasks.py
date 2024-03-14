import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

from textwrap import dedent
from agents import HealthAgents

openai_api_key = os.environ.get("OPENAI_API_KEY")
openai_organization = os.environ.get("OPENAI_ORGANIZATION_ID")

class HealthCoachTasks:
    def initial_health_interview(self, agent):
        return Task(description=dedent("""\
            As 'Hai', the Health Coach, your first task is to conduct an initial health interview.
            Engage the user in a conversation that feels natural and caring.
            Collect baseline health data without making any diagnoses.
            The goal is to make the user comfortable while gathering essential information
            to track their symptoms and health trends over time.
            Remember, privacy and empathy are key in these interactions."""),
            agent=agent
        )
    def daily_symptom_checkin(self, agent):
        return Task(description=dedent("""\
            Each day, 'Hai' will check in with the user to log their current symptoms.
            Ask about their well-being and any new or changing symptoms since the last check-in.
            Ensure that the conversation is supportive and that the user feels heard.
            Document the symptoms accurately to maintain a reliable health log."""),
            agent=agent
        )
    def weekly_health_insight(self, agent):
        return Task(description=dedent("""\
            At the end of each week, 'Hai' will analyze the health data collected.
            Identify any patterns or trends in the user's symptoms and well-being.
            Generate a weekly health insight report that is informative and easy to understand.
            Offer suggestions for lifestyle adjustments or reminders for follow-up if necessary."""),
            agent=agent
        )

    def user_feedback_collection(self, agent):
        return Task(description=dedent("""\
            Regularly, 'Hai' will seek feedback from the user about their health tracking experience.
            Inquire about the usefulness of the insights provided and any improvements they suggest.
            This information is crucial to enhance 'Hai's functionality and the user's experience."""),
            agent=agent
        )


