# 🏖️ Tarea 1 - Robot Beach

## 📌 Descripción
Este proyecto simula un robot autónomo en un entorno playero, integrando:
- Percepción mediante sensor LiDAR
- Modelo cinemático de movimiento
- Evaluación de desempeño con métricas de error
- Visualización de resultados

Se comparan dos enfoques de control:
- **PPO**
- **PPO-Mask**


## 🎯 Objetivos
- Simular la percepción del entorno con LiDAR
- Generar trayectorias ideales
- Evaluar el error de seguimiento
- Comparar desempeño entre algoritmos
- Automatizar la generación de gráficos


## 📂 Estructura del Proyecto
tarea1_robot_beach/
│── main.py
│
├── data/
│ └── robot_data.py
│
├── processing/
│ ├── cinematicas.py
│ └── metricas.py
│
├── visualization/
│ └── graficos.py
│
├── resultados_graficos/
│ ├── lidar.png
│ ├── trayectoria_triangulo.png
│ ├── trayectoria_cuadrada.png
│ └── reporte_metricas_real_simple.png


## ▶️ Ejecución

Desde la carpeta raíz del proyecto:

```bash
python main.py
