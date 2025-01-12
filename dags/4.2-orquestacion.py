from airflow import DAG
from datetime import datetime

from airflow.operators.empty import EmptyOperator

with DAG(dag_id="4.2-orquestacion",
         description="",
         schedule_interval="0 7 * * 1",
         start_date=datetime(2024,1,1),
         end_date=datetime(2025,6,1),
         catchup=True) as dag:


    t1 = EmptyOperator(task_id="tarea1")

    t2 = EmptyOperator(task_id="tarea2")

    t3 = EmptyOperator(task_id="tarea3")

    t4 = EmptyOperator(task_id="tarea4")


    t1 >> t2 >> [t3,t4]
