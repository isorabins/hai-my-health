from crewai import Task
from textwrap import dedent

class InitialHealthInterviewTasks:
    def __init__(self, hai_initial_agent):
        self.agent = hai_initial_agent

    def welcome_and_privacy_assurance(self):
        return Task(
            description=dedent("""\
                **Welcome and Privacy Assurance**
                Welcome the user and reassure them about the confidentiality of the conversation.
                This is crucial for building trust and comfort."""),
            agent=self.agent
        )

    def general_health_inquiry(self):
        return Task(
            description=dedent("""\
                **General Health Inquiry**
                Ask the user about their overall health status to gauge any immediate concerns.
                Remember to ask no more than one follow-up question before moving on."""),
            agent=self.agent
        )

    def symptom_exploration(self):
        return Task(
            description=dedent("""\
                **Symptom Exploration**
                Briefly inquire about any symptoms the user wishes to track.
                Avoid diagnostic questions and limit to one follow-up for clarity."""),
            agent=self.agent
        )

    def lifestyle_and_routine(self):
        return Task(
            description=dedent("""\
                **Lifestyle and Routine**
                Discuss the user's exercise routine and sleep quality.
                Understand their daily habits with minimal follow-up questions."""),
            agent=self.agent
        )

    def mental_wellbeing_check(self):
        return Task(
            description=dedent("""\
                **Mental Well-being Check**
                Gently explore the user's mental health and stress levels.
                Maintain a supportive tone and limit follow-up questions."""),
            agent=self.agent
        )

    def health_goals_discussion(self):
        return Task(
            description=dedent("""\
                **Health Goals Discussion**
                Encourage the user to share any health goals or areas they wish to improve.
                Engage with up to one follow-up question to understand their objectives better."""),
            agent=self.agent
        )

    def custom_follow_ups_based_on_user_input(self):
        return Task(
            description=dedent("""\
                **Custom Follow-ups Based on User Input**
                Based on the user's input, ask one or two follow-up questions for clarity.
                Adhere to the guideline of keeping the conversation brief and focused."""),
            agent=self.agent
        )

    def closing_and_next_steps(self):
        return Task(
            description=dedent("""\
                **Closing and Next Steps**
                Conclude the interview by summarizing the information collected.
                Outline the next steps in the health tracking process, expressing gratitude for the user's participation."""),
            agent=self.agent
        )
