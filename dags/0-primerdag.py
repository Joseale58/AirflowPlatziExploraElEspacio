from airflow import DAG
from airflow.operators.dummy_operator import EmptyOperator
from datetime import datetime

with DAG(dag_id="primerdag",
         description="Nuestro primer flujo que emociooon",
         start_date=datetime(2025, 1, 10),
         schedule_interval="@once") as dag:

    #Tareas
    t1 = EmptyOperator(task_id="dummy")