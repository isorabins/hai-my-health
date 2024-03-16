import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

from textwrap import dedent
from agents import HealthAgents

openai_api_key = os.environ.get("OPENAI_API_KEY")
openai_organization = os.environ.get("OPENAI_ORGANIZATION_ID")

class HealthCoachTasks:
    def initial_health_interview(self, agent):
        return Task(
            description="""
            Conduct an initial health interview to gather baseline health data from the user. This task is structured around a set of predetermined questions focused on collecting essential health information without engaging in diagnosis or extensive follow-up queries. Hai's role is to facilitate a smooth and concise conversation, ensuring user comfort and privacy throughout the interview.
            DO NOT ASK MORE THAN 1 FOLLOW-UP QUESTION PER USER INPUT.
            STICK TO THE INTERVIEW SCRIPT BELOW, THIS IS IMPORTANT FOR LEGAL REASONS AND WE DONT
            WANT TO GET SUED.
            Interview Structure:
            1. **Welcome and Privacy Assurance**: Start by welcoming the user and reassuring them about the confidentiality of the conversation.
            2. **General Health Inquiry**: Ask the user about their overall health status to gauge any immediate concerns.
            3. **Symptom Exploration**: Briefly inquire about any symptoms the user wishes to track, without delving into diagnostic questions.
            4. **Lifestyle and Routine**: Discuss the user's exercise routine and sleep quality to understand their daily habits.
            5. **Mental Well-being Check**: Gently explore the user's mental health and stress levels, ensuring to maintain a supportive tone.
            6. **Health Goals Discussion**: Encourage the user to share any health goals or areas they wish to improve.
            7. **Custom Follow-ups Based on User Input**: If the user mentions specific conditions or concerns, Hai can ask one or two follow-up questions for clarity, adhering to the guideline of keeping the conversation brief.
            8. **Closing and Next Steps**: Conclude the interview by summarizing the information collected, outlining the next steps in the health tracking process, and expressing gratitude for the user's participation.
        
            Hai will use the user's responses to create a personalized health tracking plan, emphasizing ongoing support and daily check-ins to monitor progress and adjust goals as needed.
            """,
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


