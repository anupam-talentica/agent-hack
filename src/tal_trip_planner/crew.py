from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource
from src.tal_trip_planner.tools.railways_agent import RailwaysAgent

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class TalTripPlanner():
	"""TalTripPlanner crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# docs_tool = DirectoryReadTool(directory='./blog-posts')
	# file_tool = FileReadTool()
	# search_tool = SerperDevTool()
	# web_rag_tool = WebsiteSearchTool()

	text_source = TextFileKnowledgeSource(
    	file_paths=["policy.txt" ]
	)

	csv_source = CSVKnowledgeSource(
   		file_paths=["users.csv"]
	)


	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools

	@agent
	def route_identifier(self) -> Agent:
		return Agent(
			config=self.agents_config['route_identifier'],
			#tools=[self.search_tool, self.web_rag_tool],
			verbose=True,
			knowledge_sources=[self.csv_source]
		)
	
	@agent
	def cost_calculator(self) -> Agent:
		return Agent(
			config=self.agents_config['cost_calculator'],
			#tools=[self.search_tool, self.web_rag_tool],
		)
	

	@agent
	def comfort_assessor(self) -> Agent:
		return Agent(
			config=self.agents_config['comfort_assessor'],
			#tools=[self.search_tool, self.web_rag_tool],
		)
	
	@agent
	def policy_enforcer(self) -> Agent:
		return Agent(
			config=self.agents_config['policy_enforcer'],
			#tools=[self.search_tool, self.web_rag_tool],
		)

	@agent
	def railways_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['railways_agent'],
			tools=[RailwaysAgent()],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def route_identification_task(self) -> Task:
		return Task(
			config=self.tasks_config['route_identification_task'],
		)
	
	@task
	def cost_calculator_task(self) -> Task:
		return Task(
			config=self.tasks_config['cost_calculation_task'],
		)
	
	@task
	def comfort_assessment_task(self) -> Task:
		return Task(
			config=self.tasks_config['comfort_assessment_task'],
		)
	
	@task
	def policy_enforcement_task(self) -> Task:
		return Task(
			config=self.tasks_config['policy_enforcement_task'],
		)
	
	@task
	def railway_booking_task(self) -> Task:
		return Task(
			config=self.tasks_config['railway_booking_task'],
			tools=[RailwaysAgent()]
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the TalTripPlanner crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=[self.railways_agent()], # Automatically created by the @agent decorator
			tasks=[self.railway_booking_task()], # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)