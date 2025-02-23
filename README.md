# TalTripPlanner

Welcome to the TalTripPlanner, Its a multi-agent AI system. The goal is to leverage AI agents to address Travel Planning related pain.

## Problems/Challenges
- Slow and Manual Process
  - Today, the admin team takes up to 2 weeks to arrange travel for 100 employees, leading to inefficiencies and delays.
- Lack of a Unified View
  - No single platform provides a comprehensive view of travel options from a small village (source) to Pune (destination). Employees and admins must check multiple sources manually.
- Budget and Policy Compliance Adherence
  - The travel options adhere to company budgets and policies, leading to cost overruns or non-compliant bookings.
- Respect User Preferences
  - Employees have individual travel preferences (e.g., comfort, timing, transport mode).
- Excessive Back-and-Forth Communication
  - Employees and the travel desk engage in repeated discussions due to missing information.
- Prone to Errors
  - Manual coordination increases the risk of incorrect bookings, miscommunication, or missing details, requiring last-minute corrections and added costs.

## Ideal Solution
- As an admin user I will provide a list of users with source and destination.
- The solution shall generate option which I shall approve.
- The Employee shall pick one option.
- System shall make the bookings. 

## WorkFlow

![Alt text](https://github.com/anupam-talentica/agent-hack/blob/main/workflow.png?raw=true)



## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/tal_trip_planner/config/agents.yaml` to define your agents
- Modify `src/tal_trip_planner/config/tasks.yaml` to define your tasks
- Modify `src/tal_trip_planner/crew.py` to add your own logic, tools and specific args
- Modify `src/tal_trip_planner/main.py` to add custom inputs for your agents and tasks

## Running the Open Source LLM Model Locally

Download the `Ollama` tool in your system to run large language models (LLMs) locally

Execute below command in your terminal to run `llama3.2:1b` Open Source LLM Model Locally

```bash
$ ollama run llama3.2:1b
```

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the tal-trip-planner Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The tal-trip-planner Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the TalTripPlanner Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
