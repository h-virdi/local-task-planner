from datetime import datetime, timedelta
from typing import Dict, List
import logging

from clientai import ClientAI
from clientai.agent import create_agent, tool
from clientai.ollama import OllamaManager

logger = logging.getLogger(__name__)

class TaskPlanner:
	"""A local task planning system using Ollama."""

	def __init__(self):
		"""Initialise the task planner with Ollama."""
		self.manager = OllamaManager()
		self.client = None
		self.planner = None
	
	def stop(self):
		"""Stop the Ollama server if running."""
		if self.manager:
			self.manager.stop()

	def start(self):
		"""Start the Ollama server and initialise the client."""
		self.manager.start()
		self.client = ClientAI("ollama", host = "http://localhost:11434")

		self.planner = create_agent(
			client = self.client,
			role = "task planner",
			system_prompt = """You are a practical task planner. Break down goals into specific, actionable tasks with realistic time estimates and resource needs. Use the tools provided to validate timelines and format plans properly.""",
			model = "llama3",
			step = "think",
			tools = [self.validate_timeline, self.format_plan],
			tool_confidence = 0.8,
			stream = True,
		)
	@tool(name = "validate_timeline")
	def validate_timeline(tasks: Dict[str, int]) -> Dict[str, dict]:
		"""
		Validate time estimates and create a realistic timeline.

		Args:
			tasks: Dictionary of task names and estimated hours
		Returns:
			Dictionary with start dates and deadlines
		"""
		try:
			current_date = datetime.now()
			timeline = {}
			accumulated_hours = 0
			
			for task, hours in tasks.items():
				try:
					hours_int = int(float(str(hours)))
					if hours_int <= 0:
						logger.warning(f"Skipping task {task}: Invalid hours value {hours}")
						continue

					days_needed = hours_int / 6
					start_date = current_date + timedelta(hours = accumulated_hours)
					end_date = start_date + timedelta(days = days_needed)

					timeline[task] = {
						"start": start_date.strftime("%Y-%m-%d"),
						"end": end_date.strftime("%Y-%m-%d"),
						"hours": hours_int,
					}

					accumulated_hours += hours_int

				except (ValueError, TypeError) as e:
					logger.warning(f"Skipping task {task}: Invalid hours value {hours} - {e}")
					continue

			return timeline
		except Exception as e:
			logger.error(f"Error validating timeline: {str(e)}")
			return {}

	@tool(name = "format_plan")
	def format_plan(
		tasks: List[str],
		timeline: Dict[str, dict],
		resources: List[str]
	) -> str:
		"""
		Format the plan in a clear, structured way.

		Args:
			tasks: List of tasks
			timeline: Timeline from validate_timeline
			resources: List of required resources
		Returns:
			Formatted plan as a string
		"""
		try:
			plan = "== Project Plan ==\n\n"

			plan += "Tasks and Timeline:\n"
			for i, task in enumerate(tasks, 1):
				if task in timeline:
					t = timeline[task]
					plan += f"\n{i}. {task}\n"
					plan += f"	Start: {t['start']}\n"
					plan += f"	End: {t['end']}\n"
					plan += f"	Estimated Hours: {t['hours']}\n"

			plan += "\nRequired Resources:\n"
			for resource in resources:
				plan += f"- {resource}\n"

			return plan
		except Exception as e:
			logger.error(f"Error formatting plan: {str(e)}")
			return "Error: Unable to format plan"

	def get_plan(self, goal: str) -> str:
		"""
		Generate a plan for the given goal.

		Args:
			goal: The goal to plan for

		Returns:
			A formatted plan string
		"""
		if not self.planner:
			raise RuntimeError("Planner not initialised. Call start() first.")
		return self.planner.run(goal)
	

def main():
		planner = TaskPlanner()

		try:
			print("Task Planner (Local AI)")
			print("Enter your goal, and I'll create a practical, timeline-based plan.")
			print("Type 'quit' to exit.")

			planner.start()

			while True:
				print("\n" + "=" * 50 + "\n")
				goal = input("Enter your goal: ")

				if goal.lower() == "quit":
					break

				try:
					plan = planner.get_plan(goal)
					print("\nYour Plan:\n")
					for chunk in plan:
						print(chunk, end = "", flush = True)
				except Exception as e:
					print(f"Error: {str(e)}")
		finally:
			planner.stop()
	
	

if __name__ == "__main__":
	main()
