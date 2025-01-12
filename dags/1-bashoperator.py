from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(dag_id="bash_operator",
         description="Ejemplo de operador bash",
         start_date=datetime(2025, 1, 10),
         schedule_interval="@once") as dag:

    #Tareas
    t1 = BashOperator(task_id="print_date",
                      bash_command="echo 'Jefecito Andy'")
