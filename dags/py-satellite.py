from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime


def _generate_platzi_data(**kwargs):
    import pandas as pd
    data = pd.DataFrame({"student": ["Maria Cruz", "Daniel Crema",
                                     "Elon Musk", "Karol Castrejon", "Freddy Vega"],
                         "timestamp": [kwargs['logical_date'],
                                       kwargs['logical_date'], kwargs['logical_date'], kwargs['logical_date'],
                                       kwargs['logical_date']]})
    data.to_csv(f"/tmp/platzi_data_{kwargs['ds_nodash']}.csv", header=True)



with DAG('satellitedata',
         start_date=datetime(2021, 1, 1),
         end_date=datetime(2021, 1, 10),
         schedule_interval='@once') as dag:

    #Tasks

    t1 = BashOperator(
        task_id='NASA_auth',
        bash_command='sleep 20 && echo "OK" > /tmp/response_{{ds_nodash}}.txt',
    )

    t2 = FileSensor(
        task_id='WaitingForData',
        filepath='/tmp/response_{{ds_nodash}}.txt',
        poke_interval=5
    )

    t3 = BashOperator(
        task_id='DataCollection',
        bash_command="curl -o /tmp/history.json -L 'https://api.spacexdata.com/v5/launches/latest'",
    )

    t4 = PythonOperator(
        task_id='SatelliteDataGenerated',
        python_callable=_generate_platzi_data
    )

    t5 = BashOperator(
        task_id='ShowDataCollected',
        bash_command='ls /tmp && head /tmp/platzi_data_{{ds_nodash}}.csv'
    )

    t1 >> t2 >> t3 >> t4 >> t5



