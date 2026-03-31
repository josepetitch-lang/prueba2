#Guía de Prompts para Aprendizaje Guiado en Python
#Esta guía está diseñada para que utilices la IA como un tutor socrático, no como una máquina de respuestas. El objetivo es que desarrolles tu lógica de programación mientras aprendes a comunicarte con modelos de lenguaje.

# La Regla de Oro: El Método R-I-C
#Antes de preguntar, asegúrate de que tu prompt tenga estos tres elementos:

#Rol: Define quién es la IA (ej. "Actúa como un tutor experto").
#Intención: Qué quieres lograr (ej. "Ayúdame a entender este error").
#Constricción: Pon límites (ej. "No me des el código corregido, dame pistas").

# Ejemplos de Prompts Útiles
#1. Para entender errores (Debugging)
#"Actúa como un tutor de Python. He recibido un error de tipo [Nombre del Error, ej: IndexError] en el código que pego abajo. No me des la solución. Explícame qué significa este error en términos sencillos y hazme una pregunta que me ayude a encontrar el fallo por mi cuenta."

#2. Para diseñar la lógica (Algoritmos)
#"Estoy intentando escribir un programa que [describe tu objetivo, ej: encuentre el número más grande en una lista], pero no sé por dónde empezar. ¿Podrías ayudarme a diseñar un pseudocódigo o un paso a paso lógico sin escribir código de Python todavía?"

#3. Para conceptos difíciles
#"No entiendo bien el concepto de [Concepto, ej: diccionarios o bucles while]. ¿Podrías darme una analogía de la vida real para entender para qué sirve y en qué se diferencia de [Otro concepto, ej: listas]?"

#4. Para mejorar tu código (Refactorización)
#"Mi código para este ejercicio funciona, pero siento que es muy repetitivo. Revisa mi código y sugiéreme una forma más 'pythonic' (eficiente y limpia) de hacerlo, explicándome el porqué del cambio pero dejando que yo intente escribir la versión final."

# Consejos para ser un Pro
#Pega siempre tu código: Si tienes un problema, adjunta el fragmento de código relevante para que la IA tenga contexto.
#Pide explicaciones, no soluciones: Si la IA te da el código directamente, dile: "Gracias, pero prefiero que me expliques la lógica detrás de la línea X para poder hacerlo yo mismo".
#Itera: Si la primera explicación no es clara, pide: "Usa una analogía diferente" o "Explícamelo como si tuviera 10 años".
