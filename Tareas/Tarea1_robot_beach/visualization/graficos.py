import os
import matplotlib.pyplot as plt
import numpy as np


# (a) Función de Métricas
def plot_metricas(diccionario_experimentos, ambiente, ruta):
    datos_filtrados = {}
    for nombre_experimento, info in diccionario_experimentos.items():
        if info['ambiente'] == ambiente and info['ruta'] == ruta:
            datos_filtrados[nombre_experimento] = info

    modelos_ia = ['PPO', 'PPO-Mask']
    metricas = ['ISE', 'IAE', 'ITSE', 'ITAE']
    colores = ['#3498db', '#2ecc71']

    fig, subplots = plt.subplots(1, 4, figsize=(18, 5))
    fig.suptitle(f'Comparación de Algoritmos - Ambiente: {ambiente} | Ruta: {ruta}')

    for i, metrica in enumerate(metricas):
        valores_grafica = []

        for modelo in modelos_ia:
            valor = 0
            for exp in datos_filtrados.values():
                if exp["politica"] == modelo:
                    valor = exp.get(metrica, 0)
            valores_grafica.append(valor)

        subplots[i].bar(modelos_ia, valores_grafica, color=colores)
        subplots[i].set_title(f'Indicador {metrica}', fontsize=12)
        subplots[i].set_ylabel('Magnitud del Error')
        subplots[i].grid(axis='y', alpha=0.3, linestyle='--')

    directorio_reportes = 'resultados_graficos'
    os.makedirs(directorio_reportes, exist_ok=True)

    nombre_final = f"reporte_metricas_{ambiente}_{ruta}.png"
    ruta_archivo = os.path.join(directorio_reportes, nombre_final)

    plt.savefig(ruta_archivo, dpi=300)
    print(f"✅ Gráfico de métricas guardado en: {ruta_archivo}")

    plt.show()


# (b) Función de percepción LiDAR
def plot_lidar(angulos, distancias, distancias_norm):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle('Percepción del Sensor LiDAR', fontsize=14)

    ax1.scatter(angulos, distancias, c=distancias, cmap='viridis_r', s=20)
    ax1.set_title('Vista del Operador (Metros)')
    ax1.set_xlabel('Ángulo (°)')
    ax1.set_ylabel('Distancia (m)')
    ax1.grid(True, alpha=0.3)

    ax2.plot(angulos, distancias_norm, color='orange', linewidth=1.5)
    ax2.fill_between(angulos, distancias_norm, color='orange', alpha=0.2)
    ax2.set_title('Lectura IA (Normalizada)')
    ax2.set_xlabel('Sector del Sensor')
    ax2.set_ylim(0, 1.1)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    os.makedirs('resultados_graficos', exist_ok=True)
    ruta_lidar = os.path.join('resultados_graficos', 'lidar.png')
    plt.savefig(ruta_lidar, dpi=300)
    print(f"📡 Mapa LiDAR guardado en: {ruta_lidar}")

    plt.show()


# (c) Función de Trayectorias Comparativas
def plot_trayectorias(x_ppo, y_ppo, x_mask, y_mask, waypoints, nombre):
    plt.figure(figsize=(8, 8))

    plt.plot(x_ppo, y_ppo, label='Trayectoria PPO', color='blue', alpha=0.6, linestyle='--')
    plt.plot(x_mask, y_mask, label='Trayectoria PPO-Mask', color='green', linewidth=2)

    wp_x, wp_y = zip(*waypoints)
    plt.scatter(wp_x, wp_y, color='black', marker='s', label='Waypoints (Metas)', s=60, zorder=5)

    plt.axis('equal')

    plt.title(f'Mapa de Navegación: Ruta {nombre.capitalize()}', fontsize=12)
    plt.xlabel('Eje X (metros)')
    plt.ylabel('Eje Y (metros)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)

    os.makedirs('resultados_graficos', exist_ok=True)
    ruta_mapa = os.path.join('resultados_graficos', f'trayectoria_{nombre}.png')
    plt.savefig(ruta_mapa, dpi=300)
    print(f"📍 Mapa de trayectoria guardado en: {ruta_mapa}")

    plt.show()
