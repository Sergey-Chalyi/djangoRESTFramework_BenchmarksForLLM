import json
import os

def load_test_data(json_file='test_database.json'):
    """
    Load and process benchmarking results from a JSON file, and store them in the database.

    Parameters:
    json_file (str): The path to the JSON file containing benchmarking results.
                      Defaults to 'test_database.json' if not provided.

    Returns:
    None

    Raises:
    FileNotFoundError: If the specified JSON file is not found.

    The function reads the JSON file, extracts the benchmarking results, and updates or creates
    corresponding records in the Benchmark model.
    """
    from .models import Benchmark # to avoid cycle imports

    if not os.path.exists(json_file):
        raise FileNotFoundError(f"{json_file} not found.")

    with open(json_file, 'r') as file:
        data = json.load(file)

    results = data.get('benchmarking_results', [])
    for result in results:
        Benchmark.objects.update_or_create(
            request_id=result["request_id"],
            defaults={
                "prompt_text": result["prompt_text"],
                "generated_text": result["generated_text"],
                "token_count": result["token_count"],
                "time_to_first_token": result["time_to_first_token"],
                "time_per_output_token": result["time_per_output_token"],
                "total_generation_time": result["total_generation_time"],
                "timestamp": result["timestamp"],
            }
        )
