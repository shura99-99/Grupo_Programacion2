import numpy as np


def calcular_IAE(errores, dt):
    errores = np.array(errores)
    return float(np.sum(np.abs(errores)) * dt)


def calcular_ISE(errores, dt):
    errores = np.array(errores)
    return float(np.sum(errores**2) * dt)


def calcular_ITAE(errores, dt):
    errores = np.array(errores)
    t = np.arange(len(errores)) * dt
    return float(np.sum(t * np.abs(errores)) * dt)


def calcular_ITSE(errores, dt):
    errores = np.array(errores)
    t = np.arange(len(errores)) * dt
    return float(np.sum(t * (errores**2)) * dt)


def calcular_todas_las_metricas(errores, dt):
    return {
        "ISE": round(calcular_ISE(errores, dt), 2),
        "IAE": round(calcular_IAE(errores, dt), 2),
        "ITSE": round(calcular_ITSE(errores, dt), 2),
        "ITAE": round(calcular_ITAE(errores, dt), 2),
    }


def calcular_mejora(valor_ppo, valor_mask):
    if valor_ppo == 0:
        return 0.0

    mejora = ((valor_ppo - valor_mask) / valor_ppo) * 100
    return round(mejora, 2)
