

# Paso 1: diccionario con al menos 4 metricas tecnicas (Memoria de Trabajo)
servidor_estado = {
    "cpu_uso": 92,             # % de uso de CPU
    "memoria_libre": 15,       # % de memoria libre
    "ping_respuesta": 320,     # ms
    "temperatura": 85,         # grados C
    "ventilador_activo": False,
}


# Paso 2 y 3: funcion diagnosticar_servidor con >=3 reglas anidadas (if/elif + and/or)
def diagnosticar_servidor(hechos):
    # Regla 1 (maxima prioridad): estado CRITICO
    if hechos["temperatura"] > 80 and not hechos["ventilador_activo"]:
        return "CRITICO: Sobrecalentamiento sin refrigeracion. Apagar servidor de inmediato."

    # Regla 2: estado de ADVERTENCIA por combinacion de metricas
    elif hechos["cpu_uso"] > 85 or hechos["memoria_libre"] < 20:
        if hechos["ping_respuesta"] > 300:
            return "ADVERTENCIA: Servidor saturado y con latencia alta. Revisar procesos."
        else:
            return "ADVERTENCIA: Uso de recursos elevado. Monitorear de cerca."

    # Regla 3: recursos normales pero con red lenta
    elif hechos["ping_respuesta"] > 300:
        return "AVISO: Recursos normales pero red lenta. Revisar conectividad."

    # Regla por defecto (fallback)
    else:
        return "OK: Servidor operando dentro de parametros normales."


# Paso 4: ejecucion + cambio de valores para forzar distintas ramas (cobertura)
if __name__ == "__main__":
    print("Diagnostico 1 (critico esperado):", diagnosticar_servidor(servidor_estado))

    servidor_estado["temperatura"] = 60
    servidor_estado["ventilador_activo"] = True
    print("Diagnostico 2 (advertencia esperada):", diagnosticar_servidor(servidor_estado))

    servidor_estado["cpu_uso"] = 40
    servidor_estado["memoria_libre"] = 70
    servidor_estado["ping_respuesta"] = 50
    print("Diagnostico 3 (OK esperado):", diagnosticar_servidor(servidor_estado))

    servidor_estado["ping_respuesta"] = 450
    print("Diagnostico 4 (aviso red lenta esperado):", diagnosticar_servidor(servidor_estado))
