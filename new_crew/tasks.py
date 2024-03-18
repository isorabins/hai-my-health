import os
from crewai import Task
from textwrap import dedent

class HealthCoachTasks:
    def __init__(self, agent):
        self.agent = agent

    def welcome_and_privacy_assurance(self):
        return Task(
            description=dedent("""\
                **Welcome and Privacy Assurance**
                Start by welcoming the user and reassuring them about the confidentiality of the conversation."""),
            agent=self.agent
        )

    def general_health_inquiry(self):
        return Task(
            description=dedent("""\
                **General Health Inquiry**
                Ask the user about their overall health status to gauge any immediate concerns."""),
            agent=self.agent
        )

    def symptom_exploration(self):
        return Task(
            description=dedent("""\
                **Symptom Exploration**
                Briefly inquire about any symptoms the user wishes to track, without delving into diagnostic questions."""),
            agent=self.agent
        )

    def lifestyle_and_routine(self):
        return Task(
            description=dedent("""\
                **Lifestyle and Routine**
                Discuss the user's exercise routine and sleep quality to understand their daily habits."""),
            agent=self.agent
        )

    def mental_wellbeing_check(self):
        return Task(
            description=dedent("""\
                **Mental Well-being Check**
                Gently explore the user's mental health and stress levels, ensuring to maintain a supportive tone."""),
            agent=self.agent
        )

    def health_goals_discussion(self):
        return Task(
            description=dedent("""\
                **Health Goals Discussion**
                Encourage the user to share any health goals or areas they wish to improve."""),
            agent=self.agent
        )

    def custom_follow_ups_based_on_user_input(self):
        return Task(
            description=dedent("""\
                **Custom Follow-ups Based on User Input**
                If the user mentions specific conditions or concerns, ask one or two follow-up questions for clarity, adhering to the guideline of keeping the conversation brief."""),
            agent=self.agent
        )

    def closing_and_next_steps(self):
        return Task(
            description=dedent("""\
                **Closing and Next Steps**
                Conclude the interview by summarizing the information collected, outlining the next steps in the health tracking process, and expressing gratitude for the user's participation."""),
            agent=self.agent
        )
