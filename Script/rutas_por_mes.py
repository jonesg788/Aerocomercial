# Autor: Glorianna Alfonzo 
#Fecha de creación: 9/9/2024
import matplotlib.pyplot as plt

# Convert the 'indice_tiempo' column to datetime format
df['indice_tiempo'] = pd.to_datetime(df['indice_tiempo'])

# Plotting the data
plt.figure(figsize=(12, 6))

# Plot each classification separately
for flight_type in df['clasificacion_vuelo'].unique():
    subset = df[df['clasificacion_vuelo'] == flight_type]
    plt.plot(subset['indice_tiempo'], subset['total_rutas'], label=flight_type)

# Customizing the plot
plt.title('Cantidad de Rutas por Clasificación de Vuelo')
plt.xlabel('Fecha')
plt.ylabel('Total de Rutas')
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig("/mnt/data/cantidad_rutas.png")

# Display the plot
plt.show()
