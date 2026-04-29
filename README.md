🔐 Extractor de PINs con Python
Este es un proyecto desarrollado como parte de mi formación en Programación y Ciberseguridad. El script utiliza lógica de procesamiento de texto para extraer códigos secretos (PINs) basados en la estructura de diferentes poemas o textos.

🚀 ¿Cómo funciona?
El programa analiza una lista de poemas y genera un código numérico siguiendo estas reglas:

Divide el texto en líneas.

Identifica una palabra específica en cada línea basada en su índice dinámico.

Calcula la longitud de dicha palabra.

Manejo de Errores: Si una línea es más corta de lo esperado, el sistema asigna automáticamente un 0 para mantener la integridad del código final.

🛠️ Tecnologías utilizadas
Lenguaje: Python 3.x

Conceptos clave: Bucles anidados, validación de datos, manipulación de strings y listas, y lógica de escalabilidad.

📁 Estructura del Código
El núcleo del proyecto es la función pin_extractor(), la cual es capaz de procesar múltiples entradas simultáneamente, devolviendo una lista con todos los PINs generados.
