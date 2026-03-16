#Importar los datos
import pandas as pd
from prophet import Prophet

#Cargar los datos
df = pd.read_csv("example_wp_log_peyton_manning.csv")
df.head