# Project Status Report - Hai the Health Coach

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
