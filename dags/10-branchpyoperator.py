from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime, date

default_args = {
    'start_date': datetime(2024, 12 , 1),
    'end_date': datetime(2024, 12, 31)
}

def choose(**context):

    if context["logical_date"].date() < date(2024,12,15):
        return "finish_14"

    return "start_15"

with DAG("10-branching",
         schedule_interval="@daily",
         default_args=default_args) as dag:

    branching = BranchPythonOperator(task_id="branching", python_callable=choose)

    finish_14 = BashOperator(task_id="finish_14", bash_command="echo 14")

    start_15 = BashOperator(task_id="start_15", bash_command="echo 15")

    branching >> [finish_14, start_15]