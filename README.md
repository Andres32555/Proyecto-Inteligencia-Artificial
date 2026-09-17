Sesión 1 — Introducción a Sistemas Expertos y repaso de Python

Taller Analítico 1: Lógica Proposicional (20 min)

Enunciado: traducir a Reglas de Producción (SI... Y/O... ENTONCES...) el siguiente texto de un manual de otorgamiento de créditos:

> "Un cliente es elegible para el crédito Hipotecario Plus si sus ingresos anuales superan los 50,000 USD y tiene un historial crediticio 'Excelente'. Sin embargo, si el cliente tiene deudas activas superiores a 10,000 USD, no será elegible bajo ninguna circunstancia, a menos que presente un avalista."


Paso 1 — Identificar las variables Hechos que el sistema debe pedir al usuario

- `ingresos_anuales` (numérico)
- `historial_crediticio` (texto, ej. "Excelente")
- `deuda_activa` (numérico)
- `tiene_avalista` (booleano)

Paso 2 — Formalizar las reglas de producción

- R1 (Rechazo — máxima precedencia):**
  `SI deuda_activa > 10000 Y NO tiene_avalista ENTONCES elegible = RECHAZADO`
- R2 (Aprobación):**
  `SI ingresos_anuales > 50000 Y historial_crediticio == "Excelente" ENTONCES elegible = APROBADO`
- R3 (Fallback):**
  `SI ninguna de las anteriores se cumple ENTONCES elegible = EN REVISIÓN MANUAL`

Paso 3 — Justificar el orden

La cláusula de la deuda activa es una excepción que anula la aprobación ("no será elegible bajo ninguna circunstancia"), por lo tanto R1 debe evaluarse antes que R2: aunque el cliente cumpla ingresos e historial, si tiene deuda alta y no tiene avalista, el sistema debe rechazar. Esta es exactamente la lógica que implementa `motor_evaluacion_credito` en el material de la clase (regla de rechazo absoluto primero, regla de aprobación después, y un `return` por defecto al final).



Taller de Laboratorio: Sistema de Diagnóstico IT (40 min)

Reto: prototipo de Sistema Experto para el HelpDesk de una empresa tecnológica.

1. Diccionario `servidor_estado` con al menos 4 métricas técnicas (`cpu_uso`, `memoria_libre`, `ping_respuesta`, `temperatura`, `ventilador_activo`).
2. Función `diagnosticar_servidor(hechos)` con al menos 3 reglas anidadas (`if`/`elif` + `and`/`or`).
3. Una regla identifica un estado crítico (temperatura > 80 y ventilador apagado) y otra un estado de advertencia.
4. Se imprime el diagnóstico y se cambian los valores del diccionario para forzar que el motor tome caminos distintos (cobertura de ramas).


