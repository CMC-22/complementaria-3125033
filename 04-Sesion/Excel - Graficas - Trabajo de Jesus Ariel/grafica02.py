import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar todos los datos del archivo
datos = pd.read_csv('grafica02.csv', delimiter=';')

# Verificar las primeras filas del dataset
print("Primeras filas del dataset:")
print(datos.head())

# Convertir la columna 'Semana' al formato datetime
datos['Semana'] = pd.to_datetime(datos['Semana'], errors='coerce')

# Verificar si hay valores nulos en 'Semana' o 'Utilizados'
print("\nValores nulos en las columnas:")
print(datos[['Semana', 'Utilizados']].isnull().sum())

# Eliminar filas con valores nulos en 'Semana' o 'Utilizados'
datos = datos.dropna(subset=['Semana', 'Utilizados'])

# Confirmar que 'Utilizados' sea numérico
datos['Utilizados'] = pd.to_numeric(datos['Utilizados'], errors='coerce')

# Convertir la columna 'Semana' a valores numéricos (días ordinales)
datos['Semana_ordinal'] = datos['Semana'].map(lambda x: x.toordinal())

# Verificar los datos después de limpiar
print("\nDatos después de convertir 'Semana' a valores ordinales:")
print(datos[['Semana', 'Semana_ordinal', 'Utilizados']].head())

# Crear la gráfica de regresión lineal
plt.figure(figsize=(12, 6))
sns.regplot(x='Semana_ordinal', y='Utilizados', data=datos, line_kws={"color": "red"}, scatter_kws={"alpha": 0.5})

# Personalizar la gráfica
plt.title('Regresión lineal: Semana vs Utilizados')
plt.xlabel('Semana (ordinal)')
plt.ylabel('Cantidad de Utilizados')

# Mostrar la gráfica
plt.show()
