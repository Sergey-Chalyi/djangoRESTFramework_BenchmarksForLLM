import json
import os

def load_test_data(json_file='test_database.json'):
    from .models import Benchmark

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
