from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator

with DAG(dag_id="4.3-orquestacion",
    description="",
    schedule_interval="@monthly",
    start_date=datetime(2024,10,1),
    end_date=datetime(2025,1,30),
    default_args={"depends_on_past": True},
         max_active_runs=1) as dag:


    t1 = EmptyOperator(task_id="tarea1")

    t2 = EmptyOperator(task_id="tarea2")

    t3 = EmptyOperator(task_id="tarea3")

    t4 = EmptyOperator(task_id="tarea4")

    t1 >> t2 >> [t3,t4]
