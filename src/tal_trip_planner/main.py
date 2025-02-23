#!/usr/bin/env python
import sys
import warnings
import csv
import json

from datetime import datetime

from tal_trip_planner.crew import TalTripPlanner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(source, destination, travel_date=None, preferred_method='flight'):
    """
    Run the crew.
    
    Args:
        source (str): Starting location
        destination (str): Destination location
        travel_date (str, optional): Date of travel in YYYY-MM-DD format. Defaults to today's date.
        preferred_method (str, optional): Preferred method of travel. Defaults to 'flight'.
    """
    if travel_date is None:
        travel_date = datetime.now().strftime('%Y-%m-%d')

    inputs = []
    outputs = []

    with open('./knowledge/users.csv', encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        inputs = [row for row in csvReader]
        
    # Add travel parameters to each input
    for input_dict in inputs:
        input_dict.update({
            'source': source,
            'destination': destination,
            'travel_date': travel_date,
            'preferred_method': preferred_method
        })

    try:
        crew_outputs = TalTripPlanner().crew().kickoff_for_each(inputs=inputs)
        
        for output in crew_outputs:
            outputs.append(output.json_dict)

        return outputs
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        "source": "Atru",
        "destination": "Pune",
        "travel_date": "2025-02-28"
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
