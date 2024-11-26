from django.db import models


class Benchmark(models.Model):
    request_id = models.CharField(max_length=255, primary_key=True)
    prompt_text = models.TextField()
    generated_text = models.TextField()
    token_count = models.IntegerField()
    time_to_first_token = models.IntegerField()
    time_per_output_token = models.IntegerField()
    total_generation_time = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return f'Benchmark id {self.request_id}'
    