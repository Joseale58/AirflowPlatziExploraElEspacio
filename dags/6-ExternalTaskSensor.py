from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(dag_id="6-externalTaskSensor",
         description="",
         schedule_interval="@daily",
         start_date=datetime(2025, 1, 1),
         end_date=datetime(2025, 1, 10)) as dag:


    t1 = BashOperator(task_id="tarea1",
                      bash_command="sleep 10 && echo 'DAG finalizado'",
                      depends_on_past=True)
