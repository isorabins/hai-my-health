Project Overview & Guidelines

Welcome, and a heartfelt thank you for joining this impactful project. I'm Iso, an entrepreneur driven by the vision to democratize health tracking, making it accessible and beneficial for all. Together, we're on a mission to develop an app that enables individuals to monitor their health symptoms, thereby fostering a healthier community.

Technical Setup:

Operating System: macOS
IDE: Visual Studio Code
Programming Language: Python, with which I have basic familiarity
While I can navigate the creation of .py files and execute them through the terminal in VSCode, my grasp of deeper programming concepts is still developing. Clear, straightforward explanations and step-by-step guidance will be incredibly valuable to me. See the end of this document for a project overiview.

Expectations for Assistance:
Efficiency and effectiveness are key to our progress. With this in mind, I have a specific request to streamline our collaboration:

Direct Solutions: Fully functional code snippets are essential. I seek to avoid the pitfalls of pseudocode, aiming for solutions that work right out of the gate. This approach will help maintain our momentum and ensure we meet our objectives without delay.
The work we are embarking on has the profound potential to positively impact lives. Your expertise, patience, and dedication are not only appreciated but essential as we undertake this journey together. Let’s join forces to make a meaningful difference!

-------------
TO WORK ON/SOLVE:

create loop for questions in initial interview
setup DB correctly to store data

# Project Status Report - Hai the Health Coach

**Date:** 3/27/24
working on getting the DB setup
Running into an issue importing the compiled_conditions.csv into the DB
heres an example of the error:
/Users/isorabins/Desktop/GPT_AI/HAI_MY_HEALTH/new_hai/new_crew/DB/compiled_conditions.csv:196: unescaped " character
/Users/isorabins/Desktop/GPT_AI/HAI_MY_HEALTH/new_hai/new_crew/DB/compiled_conditions.csv:193: expected 2 columns but found 5 - extras ignored
-converted the file and re-formatted it
-have tried formatting the file with "" etc
this is an example of a line in the .csv: "Iron Deficiency Anemia","For anemia caused by lack of iron."
and getting this error: 
/Users/isorabins/Desktop/GPT_AI/HAI_MY_HEALTH/new_hai/new_crew/DB/compiled_conditions.csv:197: INSERT failed: datatype mismatch
sqlite> 

NEXT 

Below is an overview of the DB I've created. Been testing a bit, and seems some of the data isnt coming up correctly. Specifically
that the health conditions didnt import
Database Overview:
The primary goal of your SQLite database is to support a health coaching application that can dynamically adapt to user inputs through initial and daily health interviews. The database is designed to store user accounts, their health conditions, daily check-ins, and related information to provide personalized health coaching. Key to this setup is the ability for the application to match user-described conditions to known health conditions stored in the database, leveraging natural language descriptions for effective mapping.

Tables and Their Structure:
Users Table (users):

Stores information about users.
Columns: user_id (INTEGER PRIMARY KEY AUTOINCREMENT), username (TEXT NOT NULL UNIQUE).
User Emails Table (user_emails):

Separates emails from the main user accounts for privacy.
Columns: email_id (INTEGER PRIMARY KEY AUTOINCREMENT), user_id (INTEGER NOT NULL UNIQUE, FOREIGN KEY REFERENCES users(user_id)), email (TEXT NOT NULL UNIQUE).
Initial Interviews Table (initial_interviews):

Captures responses from the initial health interview with users.
Columns include interview_id (INTEGER PRIMARY KEY AUTOINCREMENT), user_id (INTEGER, FOREIGN KEY REFERENCES users(user_id)), various TEXT columns for different interview questions like overall_feeling, sleep_quality, exercise_routine, mental_health, stress_level, health_goals, custom_condition, and interview_date (DATE NOT NULL).
Daily Check-Ins Table (daily_check_ins):

For recording daily health check-ins from users.
Columns: check_in_id (INTEGER PRIMARY KEY AUTOINCREMENT), user_id (INTEGER, FOREIGN KEY REFERENCES users(user_id)), date (DATE NOT NULL), sleep_duration (REAL), exercise_duration (REAL), mood (TEXT), stress_level (INTEGER), additional_notes (TEXT).
Health Conditions Table (health_conditions):

Contains a list of known health conditions with descriptions.
Columns: condition_id (INTEGER PRIMARY KEY AUTOINCREMENT), condition_name (TEXT NOT NULL), description (TEXT).
Common Foods Table (common_foods):

A reference table for common foods.
Columns: food_id (INTEGER PRIMARY KEY AUTOINCREMENT), food_name (TEXT NOT NULL), category (TEXT), nutritional_info (TEXT).
User Conditions Table (user_conditions):

Links users to health conditions they've mentioned or been diagnosed with.
Columns: user_condition_id (INTEGER PRIMARY KEY AUTOINCREMENT), user_id (INTEGER, FOREIGN KEY REFERENCES users(user_id)), condition_id (INTEGER, FOREIGN KEY REFERENCES health_conditions(condition_id)), notes (TEXT), date_noted (DATE).
User Food Intake Table (user_food_intake):

Records food intake by users, referencing the common foods table.
Columns: food_intake_id (INTEGER PRIMARY KEY AUTOINCREMENT), user_id (INTEGER, FOREIGN KEY REFERENCES users(user_id)), food_id (INTEGER, FOREIGN KEY REFERENCES common_foods(food_id)), meal_type (TEXT), intake_date (DATE NOT NULL).


**Date:** 3/24/2
-working on creating the DB
   -creating a csv of 200 common health conditions
   -working on sourcing a DB of common foods
   -details of how Im thinking of the db
      -Idea would be to link the list of conditions and foods to the main DB, so it would
      fill in that cataogry when a user mentions a certain item. This would reduce the need
      for the AI to create its own catagories and increase normalization across the DB
      -want to seperate email address from health data asd much as possible for privacy
         -creating a seperate table for email and linked to userid with a foreign key

   Starting to create the DB
   -created all the tables
   -having trouble importing the conditions CSV, getting an error that there is a column mismatch, expecting 3 but getting 2
   -GPT says that it looks fine though, and that the 3rd is the condition_id so is supposed to be missing and auto filled
   in later...need to troubleshoot. 
**Date:** 3/24/24
Created a flow chart of the app user journey and considerations
-file saved in "docs" folder

Started work on the database
-using sqlite in VSCode

Considerations:
-going to try to find a pre-existing db of food items, to lessen the number of dynamic catagories AI needs to create, and lessen errors
   -need normalization using AI in case user mentions something similar that isnt on the list

-created a structure to seperate userID from email address, to improve privacy for users
-AI will need to dynamically create catagories for specific health concerns that users list
   -although I wonder if we could find a pre-existing DB with health issues that can be referenced?

-want AI to be able to dynamically create catagories as needed
   -not sure how this actually works


**Date:** 3/23/24


DO FIRST:
Create flow diagram of application
-what is the user journey
-how does it incorporate AI


-created many different functions for each question
   -solution isnt working

Next steps:
1.create a function that loops through a txt file of questions
2.setup DB to store data
3.setup daily interview that stores data
   -use sequel lite db - its an easy way to startup/practice
   -use first interview to set up catagories
   -catagory answers need to be consistent across users
      -can have dynamic catagories, but in each catagory value needs to be consistent
      -use AI to normalize the catagory input
      -create a rule for AI - write a function to normalize values
      -our DB structure is in drive: "Hai health db idea"

For me to learn:
   -general database design/function
Issue:
   -how would we deal with diet. Since every person will have different diets, would we need to create a whole different catagory for each food they eat? Otherwise, how would we cross reference when trying to make correlations in the data for the user?
   -can it be created dynamically when the user resonds?
   -is there an existing DB that mentions all foods that we can use
   -can DB be created/edited dynamically as user is answering questions, or does it need to be hard coded?


looping over text file:
FIRST STEP:
-to do: edit questions to be final 
-/n for line break after question
-remove all other question functions
SECOND STEP - once initial structure is complete:
-what if person answers incorrectly, how can AI followu to clarify and normalize the catagory
   -would create another function that takes task/question to check if answer is correct then if/else, ask a clarifying question

TO DO:
create a diagram of how I want the task/app to function
-start with the initial interview
   -ask the question
   -give it to AI
   -ask a followup question to clarify and normalize the data
   in conversation.py:
      -for tasks in task_file
         -is function for the loop



**Date:** 3/17/24
-tried changing the flow to split the initial interview into a task for each question, to improve the flow
-was successful, but now the tasks run right after eachother without taking real use input or having a conversation

Next steps:
-work on the logic for agent to have a full conversation, but not followup more than once on each question, and make sure they ask the specific questions that are needed. 



**Date:** 3/11/24

## Accomplishments to Date:

1. **Project Initialization**
   - Created a new Python virtual environment named `new_hai`.
   - Set up a new GitHub repository and synced it with local development using Git CLI.
   - Initialized the project directory structure with folders for `docs`, `src`, and `tests`.

2. **Telegram Bot Setup**
   - Registered a new bot on Telegram via BotFather and retrieved the API token.
   - Installed the `python-telegram-bot` library to interact with the Telegram API.
   - Installed `python-dotenv` for environment variable management.

3. **Basic Bot Functionality**
   - Created `main.py` within the `src` directory as the entry point for the bot.
   - Implemented a basic `/start` command for the bot to greet users.
   - Set up an environment variable `TELEGRAM_TOKEN` to securely store the API token.
   - Ensured sensitive files like `.env` are listed in `.gitignore` to prevent them from being pushed to GitHub.

4. **Docker Integration**
   - Integrated Docker to ensure consistency across development, testing, and production environments.
   - Added `Dockerfile` and `docker-compose.yaml` for containerization and easy deployment.

5. **Bot Functional Enhancements**
   - Updated the bot to interact with OpenAI's GPT-4 for natural language processing, enhancing conversational capabilities.
   - Implemented functionality to handle both text and audio messages.

6. **GitHub Version Control**
   - Pushed updates to GitHub, ensuring all changes are version-controlled.
   - Created a new branch `feature_initial_interview` for developing the initial interview feature without affecting the main codebase.

## Next Steps:

1. **Expand Bot Commands**
   - Implement additional bot commands (`/help`, `/checkin`, etc.).
   - Develop a system for the bot to handle more complex interactions, possibly with `ConversationHandler`.

2. **Initial Interview Implementation**
   - Incorporate the initial interview questions into the bot's conversation flow, leveraging GPT-4 for dynamic question generation and follow-ups.

3. **Data Storage**
   - Decide on a database system (e.g., SQLite for simplicity, PostgreSQL for robustness) for storing user data and conversation states.
   - Create models and schemas for the required data.
   - Implement data persistence for bot conversations and user data.

4. **Periodic Notifications and Reporting**
   - Set up a job queue to send periodic reminders and health reports to users.

5. **Testing and Quality Assurance**
   - Write unit tests for individual bot functionalities.
   - Create integration tests to simulate user interactions with the bot.

6. **Documentation**
   - Document the bot's features, usage instructions, setup process, and contribution guidelines in the `docs` folder.

7. **User Feedback**
   - Deploy a minimum viable product (MVP) to a small group of test users.
   - Collect feedback and iterate on the bot features based on user input.

8. **Deployment**
   - Prepare for deployment to a cloud platform for continuous uptime.
   - Set up a CI/CD pipeline if necessary for automated testing and deployment.

9. **Continuous Development**
   - Continue developing features, refining the bot based on user feedback.
   - Keep the documentation updated as the project evolves.

## Additional Considerations:

- **Security:** Ensure all user data is handled securely and complies with privacy laws.
- **Scalability:** Design the bot's architecture to handle an increasing number of users as the project grows.
- **Monitoring and Maintenance:** Establish a system for monitoring the bot's health and uptime and for performing regular maintenance.

# Project Status Report - Hai the Health Coach

**Date:** 3/12/24

## Accomplishments to Date:

### March 11, 2024
- Project Initialization, Telegram Bot Setup, Basic Bot Functionality, Docker Integration, Bot Functional Enhancements, and GitHub Version Control as previously described.

### March 12, 2024
- **Conda Environment Setup**: Utilized a Conda environment for local development, avoiding Docker rebuilds for faster testing cycles.
- **Bot Behavior Modification**: Improved the bot's conversational state management to handle the interview process more smoothly.
- **Local Testing**: Addressed issues with local environment setup to facilitate rapid development and testing outside of Docker.
- **Git Operations**: Explored methods for pulling specific file versions from GitHub to revert changes or analyze previous states of the bot.
## Integration with CrewAI
- Implemented CrewAI to structure user interactions for health tracking within the Telegram bot. This allows for a more sophisticated management of tasks and agent interactions, enhancing the bot's functionality in health data collection and analysis.

## Code Optimization
- Corrected and optimized the bot's code for improved functionality and syntax. This ensures smoother operation and a more intuitive user interaction flow.

Pip installed all dependecies into conda env so I dont need to build the docker image on each test

## Troubleshooting
- Addressed and resolved issues related to the CrewAI library installation, ensuring compatibility and seamless operation in the development environment.
-the "working_code.py" file will run outside of docker image. 
-the bot.py code is not working...


## Next Steps:

XXXXX - use this example as a template for my file structure and code: https://github.com/joaomdmoura/crewAI-examples/blob/main/starter_template/tasks.py
- Continue refining the conversation logic to ensure the bot conducts the health interview seamlessly.
-edit code to create functional code for crewai to work
-troubleshoot issue with crewai module not loading when docker package is built
- Implement the remaining handlers for each state of the interview process.
- Expand the bot's command set as planned.
- Create a database structure for storing user responses.
- Develop and execute a comprehensive testing strategy, including unit and integration tests.
- Formalize the documentation in the `docs` folder.

## Additional Considerations:

- Security, scalability, and monitoring remain as ongoing concerns to address as development progresses.

3/14
conda env is new_hai
got the test interface to work
-chose the agent/task
-had correct output

need to figure out a way for it to take human input
-trying to add the human tool

try incorporating langraph
-that may be the solution

3/16
added converations.py file with functions to continue the conversations
added execute_task method to fix main.py crashing
got code working having a conversation with the user successully! 

next steps:

-work on functionality to get conversations going correctly with the user
-take it off test organization
-add to telegram bot





# Project Status Report - Hai the Health Coach

**Date:** 3/11/24

## Accomplishments to Date:

1. **Project Initialization**
   - Created a new Python virtual environment named `new_hai`.
   - Set up a new GitHub repository and synced it with local development using Git CLI.
   - Initialized the project directory structure with folders for `docs`, `src`, and `tests`.

2. **Telegram Bot Setup**
   - Registered a new bot on Telegram via BotFather and retrieved the API token.
   - Installed the `python-telegram-bot` library to interact with the Telegram API.
   - Installed `python-dotenv` for environment variable management.

3. **Basic Bot Functionality**
   - Created `main.py` within the `src` directory as the entry point for the bot.
   - Implemented a basic `/start` command for the bot to greet users.
   - Set up an environment variable `TELEGRAM_TOKEN` to securely store the API token.
   - Ensured sensitive files like `.env` are listed in `.gitignore` to prevent them from being pushed to GitHub.

4. **Docker Integration**
   - Integrated Docker to ensure consistency across development, testing, and production environments.
   - Added `Dockerfile` and `docker-compose.yaml` for containerization and easy deployment.

5. **Bot Functional Enhancements**
   - Updated the bot to interact with OpenAI's GPT-4 for natural language processing, enhancing conversational capabilities.
   - Implemented functionality to handle both text and audio messages.
   - **New**: The bot now starts asking initial health questions as part of the conversation flow.

6. **GitHub Version Control**
   - Pushed updates to GitHub, ensuring all changes are version-controlled.
   - Created a new branch `feature_initial_interview` for developing the initial interview feature without affecting the main codebase.

## Next Steps:

1. **Expand Bot Commands**
   - Implement additional bot commands (`/help`, `/checkin`, etc.).
   - Develop a system for the bot to handle more complex interactions, possibly with `ConversationHandler`.
   - edit bot commands so interview continues
	-currently only asking "how's your health overall" and then asking "is there anything else youd like to add?"

2. **Initial Interview Implementation**
   - Incorporate the initial interview questions into the bot's conversation flow, leveraging GPT-4 for dynamic question generation and follow-ups.

3. **Data Storage**
   - Decide on a database system (e.g., SQLite for simplicity, PostgreSQL for robustness) for storing user data and conversation states.
   - Create models and schemas for the required data.
   - Implement data persistence for bot conversations and user data.

4. **Periodic Notifications and Reporting**
   - Set up a job queue to send periodic reminders and health reports to users.

5. **Testing and Quality Assurance**
   - Write unit tests for individual bot functionalities.
   - Create integration tests to simulate user interactions with the bot.

6. **Documentation**
   - Document the bot's features, usage instructions, setup process, and contribution guidelines in the `docs` folder.

7. **User Feedback**
   - Deploy a minimum viable product (MVP) to a small group of test users.
   - Collect feedback and iterate on the bot features based on user input.

8. **Deployment**
   - Prepare for deployment to a cloud platform for continuous uptime.
   - Set up a CI/CD pipeline if necessary for automated testing and deployment.

9. **Continuous Development**
   - Continue developing features, refining the bot based on user feedback.
   - Keep the documentation updated as the project evolves.

## Additional Considerations:

- **Security:** Ensure all user data is handled securely and complies with privacy laws.
- **Scalability:** Design the bot's architecture to handle an increasing number of users as the project grows.
- **Monitoring and Maintenance:** Establish a system for monitoring the bot's health and uptime and for performing regular maintenance.
