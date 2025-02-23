from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource
from .output_schemas.route_identifier_output import RouteIdentifierOutput



@CrewBase
class TalTripPlanner():
	"""TalTripPlanner crew"""

	
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'


	text_source = TextFileKnowledgeSource(
    	file_paths=["policy.txt" ]
	)

	csv_source = CSVKnowledgeSource(
   		file_paths=["users.csv"]
	)

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
			#tools=[self.search_tool, self.web_rag_tool]
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
			output_json=RouteIdentifierOutput
		)
	

	@crew
	def crew(self) -> Crew:
		"""Creates the TalTripPlanner crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			memory=False,
    		respect_context_window=True,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
