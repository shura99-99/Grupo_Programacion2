import numpy as np


def cargar_experimentos():
    experimentos = {
        "exp1": {"politica": "PPO", "ambiente": "real", "ruta": "simple",
                 "ISE": 434.99, "IAE": 135.93, "ITSE": 6932.79, "ITAE": 2601.61,
                 "tiempo_s": None, "pasos": None, "reward_medio": None},

        "exp2": {"politica": "PPO-Mask", "ambiente": "real", "ruta": "simple",
                 "ISE": 362.85, "IAE": 128.92, "ITSE": 5869.30, "ITAE": 2669.86,
                 "tiempo_s": None, "pasos": None, "reward_medio": None},

        "exp3": {"politica": "PPO", "ambiente": "simulado", "ruta": "triangular",
                 "ISE": 200.0, "IAE": 90.0, "ITSE": 3000.0, "ITAE": 1500.0,
                 "tiempo_s": 40.0, "pasos": 1000, "reward_medio": -10.0},

        "exp4": {"politica": "PPO-Mask", "ambiente": "simulado", "ruta": "triangular",
                 "ISE": 170.0, "IAE": 85.0, "ITSE": 2800.0, "ITAE": 1400.0,
                 "tiempo_s": 38.0, "pasos": 950, "reward_medio": -8.0},

        "exp5": {"politica": "PPO", "ambiente": "simulado", "ruta": "cuadrada",
                 "ISE": 300.0, "IAE": 110.0, "ITSE": 4800.0, "ITAE": 2200.0,
                 "tiempo_s": 55.0, "pasos": 1400, "reward_medio": -18.0},

        "exp6": {"politica": "PPO-Mask", "ambiente": "simulado", "ruta": "cuadrada",
                 "ISE": 260.0, "IAE": 100.0, "ITSE": 4000.0, "ITAE": 2000.0,
                 "tiempo_s": 50.0, "pasos": 1300, "reward_medio": -15.0},

        "exp7": {"politica": "PPO", "ambiente": "real", "ruta": "triangular",
                 "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
                 "tiempo_s": 70.0, "pasos": 1600, "reward_medio": -22.0},

        "exp8": {"politica": "PPO-Mask", "ambiente": "real", "ruta": "triangular",
                 "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
                 "tiempo_s": 65.0, "pasos": 1500, "reward_medio": -19.0},

        "exp9": {"politica": "PPO", "ambiente": "simulado", "ruta": "simple",
                 "ISE": 150.0, "IAE": 70.0, "ITSE": 2000.0, "ITAE": 900.0,
                 "tiempo_s": 30.0, "pasos": 800, "reward_medio": -5.0},

        "exp10": {"politica": "PPO-Mask", "ambiente": "simulado", "ruta": "simple",
                  "ISE": 130.0, "IAE": 65.0, "ITSE": 1800.0, "ITAE": 850.0,
                  "tiempo_s": 28.0, "pasos": 780, "reward_medio": -4.0},

        "exp11": {"politica": "PPO", "ambiente": "real", "ruta": "cuadrada",
                  "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
                  "tiempo_s": 80.0, "pasos": 1800, "reward_medio": -25.0},

        "exp12": {"politica": "PPO-Mask", "ambiente": "real", "ruta": "cuadrada",
                  "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
                  "tiempo_s": 75.0, "pasos": 1700, "reward_medio": -22.0}
    }

    return experimentos


def generar_trayectoria_ideal(waypoints, puntos_por_segmento=100):
    x_ideal = []
    y_ideal = []

    for i in range(len(waypoints) - 1):
        x0, y0 = waypoints[i]
        x1, y1 = waypoints[i + 1]

        x_segmento = np.linspace(x0, x1, puntos_por_segmento)
        y_segmento = np.linspace(y0, y1, puntos_por_segmento)

        x_ideal.extend(x_segmento)
        y_ideal.extend(y_segmento)

    return np.array(x_ideal), np.array(y_ideal)


def simular_lidar(n_sectores=36, d_min=0.5, d_max=30.0):
    angulos_deg = np.linspace(0, 360, n_sectores)

    distancias = np.random.uniform(d_min, d_max, n_sectores)

    distancias[5:9] = np.random.uniform(0.5, 2.0, 4)

    distancias_norm = (distancias - d_min) / (d_max - d_min)

    return angulos_deg, distancias, distancias_norm
