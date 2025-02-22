#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from tal_trip_planner.crew import TalTripPlanner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year),
        "source": "Atru",
        "destination": "Pune",
        "url": "https://irctc1.p.rapidapi.com/api/v2/getFare",
        "headers": {
            "x-rapidapi-host": "irctc1.p.rapidapi.com",
            "x-rapidapi-key": "api_key"
        },
        "params": {
            "trainNo": "19038",
            "fromStationCode": "ST",
            "toStationCode": "BVI"
        }
    }
    
    try:
        TalTripPlanner().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year),
        "source": "Atru",
        "destination": "Pune",
        "url": "https://irctc1.p.rapidapi.com/api/v2/getFare",
        "headers": {
            "x-rapidapi-host": "irctc1.p.rapidapi.com",
            "x-rapidapi-key": "api_key"
        },
        "params": {
            "trainNo": "19038",
            "fromStationCode": "ST",
            "toStationCode": "BVI"
        }
    }
    try:
        TalTripPlanner().crew().train(n_iterations=1, filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TalTripPlanner().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        TalTripPlanner().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
