from datetime import datetime
from airflow import DAG
from airflow.example_dags.tutorial import templated_command
from airflow.operators.bash import BashOperator

templated_command = """
{% for file in params.filenames %}
    echo "Logical date: {{ ds }}"
    echo "{{ file }}"
{% endfor %}
"""


with DAG(dag_id="7-templating",
         description="Example using templates",
         schedule_interval="@daily",
         start_date=datetime(2025, 1, 1),
         end_date=datetime(2025, 1, 10)) as dag:


    t1 = BashOperator(task_id="tarea1",
                      bash_command=templated_command,
                      params={"filenames": ["file1.txt", "file2.txt"]},
                      depends_on_past=True)

    t1