#!/usr/bin/env python3
"""Contenido del curso: 15 lecciones sobre sistemas multi-agentes."""

LESSONS = [
    # ─────────────────────────────────────────────────────────────────────────
    # MÓDULO 1: FUNDAMENTOS DE AGENTES
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "m1s1",
        "module": 1,
        "module_title": "Fundamentos de Agentes",
        "step": 1,
        "title": "¿Qué es un Agente de IA?",
        "description": "Aprende la diferencia entre un chatbot simple y un agente de IA real. Construye tu primer agente con memoria y capacidad de acción.",
        "concept_html": """
<p>Un <strong>agente de IA</strong> es un sistema que percibe su entorno, razona sobre él y toma acciones para alcanzar objetivos. A diferencia de un chatbot (una sola llamada al LLM), un agente puede:</p>
<ul>
  <li>🧠 <strong>Razonar</strong> sobre qué hacer a continuación</li>
  <li>🔧 <strong>Usar herramientas</strong> para actuar en el mundo</li>
  <li>👁️ <strong>Observar</strong> los resultados de sus acciones</li>
  <li>🔁 <strong>Iterar</strong> hasta completar el objetivo</li>
</ul>
<p>El ciclo fundamental es: <code>Observar → Pensar → Actuar → repetir</code></p>
""",
        "diagram_type": "react",
        "starter_code": """class SimpleAgent:
    def __init__(self, nombre):
        self.nombre = nombre
        self.memoria = []

    def observar(self, observacion):
        self.memoria.append({"rol": "observacion", "contenido": observacion})
        print(f"[{self.nombre}] Observo: {observacion}")

    def pensar(self, pensamiento):
        self.memoria.append({"rol": "pensamiento", "contenido": pensamiento})
        print(f"[{self.nombre}] Pienso: {pensamiento}")
        return pensamiento

    def actuar(self, accion):
        self.memoria.append({"rol": "accion", "contenido": accion})
        resultado = f"Ejecutando: {accion}"
        print(f"[{self.nombre}] Acto: {accion}")
        return resultado


# TODO: Crea un agente llamado "investigador" y ejecuta un bucle de 3 pasos:
# Paso 1: observa "Se necesita buscar papers sobre agentes de IA"
# Paso 2: piensa "Debo buscar en PubMed y luego analizar los resultados"
# Paso 3: actúa "buscar_papers(query='AI agents')"
# Luego imprime el número total de items en memoria

agente = SimpleAgent("investigador")
# Tu código aquí...
""",
        "solution_code": """class SimpleAgent:
    def __init__(self, nombre):
        self.nombre = nombre
        self.memoria = []

    def observar(self, observacion):
        self.memoria.append({"rol": "observacion", "contenido": observacion})
        print(f"[{self.nombre}] Observo: {observacion}")

    def pensar(self, pensamiento):
        self.memoria.append({"rol": "pensamiento", "contenido": pensamiento})
        print(f"[{self.nombre}] Pienso: {pensamiento}")
        return pensamiento

    def actuar(self, accion):
        self.memoria.append({"rol": "accion", "contenido": accion})
        resultado = f"Ejecutando: {accion}"
        print(f"[{self.nombre}] Acto: {accion}")
        return resultado


agente = SimpleAgent("investigador")
agente.observar("Se necesita buscar papers sobre agentes de IA")
agente.pensar("Debo buscar en PubMed y luego analizar los resultados")
agente.actuar("buscar_papers(query='AI agents')")

print(f"\nMemoria total: {len(agente.memoria)} items")
for item in agente.memoria:
    print(f"  [{item['rol'].upper()}] {item['contenido']}")
""",
        "expected_output_contains": ["Observo", "Pienso", "Acto", "Memoria total"],
        "requires_api_key": False,
    },
    {
        "id": "m1s2",
        "module": 1,
        "module_title": "Fundamentos de Agentes",
        "step": 2,
        "title": "El Patrón ReAct (Reason + Act)",
        "description": "Implementa el patrón ReAct del paper de Yao et al. (2022): el ciclo Pensamiento→Acción→Observación que usa todo agente moderno.",
        "concept_html": """
<p><strong>ReAct</strong> (Reasoning + Acting) es el patrón fundamental de los agentes modernos. Publicado por Yao et al. en 2022, combina:</p>
<ul>
  <li>💡 <strong>Thought</strong>: el agente razona sobre qué debe hacer</li>
  <li>⚡ <strong>Action</strong>: el agente llama a una herramienta específica</li>
  <li>👁️ <strong>Observation</strong>: el agente ve el resultado de la herramienta</li>
</ul>
<p>Este ciclo se repite hasta que el agente responde con <code>Respuesta Final:</code>. Es la base de LangChain, AutoGen, CrewAI y Claude's tool use.</p>
""",
        "diagram_type": "react",
        "starter_code": """HERRAMIENTAS = {
    "calculadora": lambda expr: str(eval(expr)),
    "buscar": lambda q: f"Resultado para '{q}': encontrados 42 papers relevantes sobre {q}",
    "contar_palabras": lambda texto: str(len(texto.split())),
}


def react_agent(pregunta, herramientas, max_pasos=5):
    historial = []
    print(f"Pregunta: {pregunta}\n")

    for paso in range(max_pasos):
        print(f"--- Paso {paso + 1} ---")

        # TODO: Simula el 'pensamiento' del LLM basado en la pregunta y el historial
        # Hint: Si el historial está vacío, el pensamiento debería ser planificar la búsqueda
        # Si ya hay observaciones, el pensamiento debería evaluar si tenemos respuesta
        pensamiento = "(implementa la lógica de pensamiento aquí)"
        print(f"Pensamiento: {pensamiento}")

        # TODO: Decide qué herramienta usar (o si ya tenemos la respuesta final)
        # Si el pensamiento contiene 'Respuesta Final:', retorna esa respuesta
        # Si no, elige una herramienta y llama a herramientas[nombre](argumento)
        herramienta_nombre = None
        resultado = None

        if herramienta_nombre:
            print(f"Acción: {herramienta_nombre}")
            print(f"Observación: {resultado}")
            historial.append({"pensamiento": pensamiento, "accion": herramienta_nombre, "observacion": resultado})
        else:
            break

    return "Máximo de pasos alcanzado"


resultado = react_agent("Busca papers sobre sistemas multi-agente", HERRAMIENTAS)
print(f"\nResultado final: {resultado}")
""",
        "solution_code": """HERRAMIENTAS = {
    "calculadora": lambda expr: str(eval(expr)),
    "buscar": lambda q: f"Resultado para '{q}': encontrados 42 papers relevantes sobre {q}",
    "contar_palabras": lambda texto: str(len(texto.split())),
}


def react_agent(pregunta, herramientas, max_pasos=5):
    historial = []
    print(f"Pregunta: {pregunta}\n")

    for paso in range(max_pasos):
        print(f"--- Paso {paso + 1} ---")

        if not historial:
            pensamiento = f"Debo buscar información sobre: {pregunta}"
            accion = "buscar"
            argumento = pregunta
        elif len(historial) == 1:
            obs = historial[-1]["observacion"]
            pensamiento = f"Tengo la información: '{obs}'. Puedo dar una respuesta final."
            print(f"Pensamiento: {pensamiento}")
            respuesta = f"Respuesta Final: {obs}"
            print(respuesta)
            return respuesta
        else:
            pensamiento = "Ya tengo suficiente información."
            accion = None
            argumento = None

        print(f"Pensamiento: {pensamiento}")

        if accion and accion in herramientas:
            resultado = herramientas[accion](argumento)
            print(f"Acción: {accion}({argumento!r})")
            print(f"Observación: {resultado}")
            historial.append({"pensamiento": pensamiento, "accion": accion, "observacion": resultado})
        else:
            break

    return "Máximo de pasos alcanzado"


resultado = react_agent("Busca papers sobre sistemas multi-agente", HERRAMIENTAS)
print(f"\nResultado final: {resultado}")
""",
        "expected_output_contains": ["Pregunta", "Pensamiento", "Acción", "Observación", "Respuesta Final"],
        "requires_api_key": False,
    },
    {
        "id": "m1s3",
        "module": 1,
        "module_title": "Fundamentos de Agentes",
        "step": 3,
        "title": "Tool Calling: La Interface Agente-Mundo",
        "description": "Define herramientas con JSON Schema, el estándar que usan Claude, GPT-4 y Gemini. Implementa un dispatcher que ejecuta la herramienta correcta.",
        "concept_html": """
<p>El <strong>tool calling</strong> (o function calling) permite que el LLM solicite ejecutar funciones de forma estructurada. En vez de texto libre, el modelo retorna JSON con nombre y argumentos.</p>
<p>Cada herramienta se define con un <strong>JSON Schema</strong>:</p>
<ul>
  <li><code>name</code>: identificador único</li>
  <li><code>description</code>: para que el LLM sepa cuándo usarla</li>
  <li><code>input_schema</code>: tipos y campos esperados</li>
</ul>
<p>Este es exactamente el formato que usa la API de Anthropic (Claude).</p>
""",
        "diagram_type": "none",
        "starter_code": """# Herramienta 1 ya definida:
herramientas = [
    {
        "name": "buscar_papers",
        "description": "Busca artículos académicos en PubMed y Semantic Scholar",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Término de búsqueda"},
                "max_resultados": {"type": "integer", "description": "Máximo de resultados", "default": 10}
            },
            "required": ["query"]
        }
    },
    # TODO: Agrega herramienta "resumir_paper" con campos: doi (string, requerido), idioma (string, default "es")
    # TODO: Agrega herramienta "guardar_nota" con campos: titulo (string), contenido (string), etiquetas (array de strings)
]


# Implementación mock de las herramientas
def _buscar_papers(query, max_resultados=10):
    return [{"titulo": f"Paper sobre {query} #{i}", "doi": f"10.1000/xyz{i}"} for i in range(min(3, max_resultados))]

def _resumir_paper(doi, idioma="es"):
    return f"Resumen en {idioma} del paper {doi}: Este estudio analiza..."

def _guardar_nota(titulo, contenido, etiquetas=None):
    etiquetas = etiquetas or []
    return f"Nota guardada: '{titulo}' con etiquetas {etiquetas}"


def dispatch_tool(nombre_herramienta, argumentos):
    """Ejecuta la herramienta correcta dado su nombre y argumentos."""
    # TODO: implementa el dispatcher
    # Debe llamar a _buscar_papers, _resumir_paper o _guardar_nota según el nombre
    # Si el nombre no existe, retorna {"error": "Herramienta desconocida: <nombre>"}
    pass


# Prueba el dispatcher:
print(dispatch_tool("buscar_papers", {"query": "multi-agent systems"}))
print(dispatch_tool("resumir_paper", {"doi": "10.1000/abc123"}))
print(dispatch_tool("guardar_nota", {"titulo": "Nota 1", "contenido": "Contenido...", "etiquetas": ["IA", "agentes"]}))
print(dispatch_tool("herramienta_inexistente", {}))
""",
        "solution_code": """herramientas = [
    {
        "name": "buscar_papers",
        "description": "Busca artículos académicos en PubMed y Semantic Scholar",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Término de búsqueda"},
                "max_resultados": {"type": "integer", "description": "Máximo de resultados", "default": 10}
            },
            "required": ["query"]
        }
    },
    {
        "name": "resumir_paper",
        "description": "Genera un resumen de un paper dado su DOI",
        "input_schema": {
            "type": "object",
            "properties": {
                "doi": {"type": "string", "description": "DOI del paper"},
                "idioma": {"type": "string", "description": "Idioma del resumen", "default": "es"}
            },
            "required": ["doi"]
        }
    },
    {
        "name": "guardar_nota",
        "description": "Guarda una nota con contenido y etiquetas",
        "input_schema": {
            "type": "object",
            "properties": {
                "titulo": {"type": "string"},
                "contenido": {"type": "string"},
                "etiquetas": {"type": "array", "items": {"type": "string"}}
            },
            "required": ["titulo", "contenido"]
        }
    },
]

def _buscar_papers(query, max_resultados=10):
    return [{"titulo": f"Paper sobre {query} #{i}", "doi": f"10.1000/xyz{i}"} for i in range(min(3, max_resultados))]

def _resumir_paper(doi, idioma="es"):
    return f"Resumen en {idioma} del paper {doi}: Este estudio analiza..."

def _guardar_nota(titulo, contenido, etiquetas=None):
    etiquetas = etiquetas or []
    return f"Nota guardada: '{titulo}' con etiquetas {etiquetas}"


def dispatch_tool(nombre_herramienta, argumentos):
    if nombre_herramienta == "buscar_papers":
        return _buscar_papers(**argumentos)
    elif nombre_herramienta == "resumir_paper":
        return _resumir_paper(**argumentos)
    elif nombre_herramienta == "guardar_nota":
        return _guardar_nota(**argumentos)
    else:
        return {"error": f"Herramienta desconocida: {nombre_herramienta}"}


print(dispatch_tool("buscar_papers", {"query": "multi-agent systems"}))
print(dispatch_tool("resumir_paper", {"doi": "10.1000/abc123"}))
print(dispatch_tool("guardar_nota", {"titulo": "Nota 1", "contenido": "Contenido...", "etiquetas": ["IA", "agentes"]}))
print(dispatch_tool("herramienta_inexistente", {}))
""",
        "expected_output_contains": ["Paper sobre", "Resumen", "Nota guardada", "desconocida"],
        "requires_api_key": False,
    },

    # ─────────────────────────────────────────────────────────────────────────
    # MÓDULO 2: TU PRIMER AGENTE CON CLAUDE API
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "m2s1",
        "module": 2,
        "module_title": "Tu Primer Agente con Claude API",
        "step": 1,
        "title": "Configurando el Ambiente",
        "description": "Aprende la estructura exacta de la API de Anthropic: mensajes, roles y parámetros. Este código funciona en modo demo sin API key.",
        "concept_html": """
<p>La <strong>API de Anthropic</strong> recibe una lista de mensajes con roles <code>user</code> y <code>assistant</code> alternados. Los parámetros clave son:</p>
<ul>
  <li><code>model</code>: el modelo a usar (ej: <code>claude-3-5-haiku-20241022</code>)</li>
  <li><code>max_tokens</code>: límite de tokens en la respuesta</li>
  <li><code>system</code>: instrucciones del sistema (rol del agente)</li>
  <li><code>messages</code>: historial de la conversación</li>
</ul>
<p>En este ejercicio el código funciona en <strong>modo demo</strong> sin API key real.</p>
""",
        "diagram_type": "none",
        "starter_code": """# Simulamos la API de Anthropic en modo demo (sin API key real)
class AnthropicDemo:
    """Cliente demo que simula respuestas de Claude."""
    def __init__(self, api_key="demo"):
        self.api_key = api_key
        self.messages = type('obj', (object,), {'create': self._create})()

    def _create(self, model, max_tokens, system="", messages=None, **kwargs):
        # Simula una respuesta realista de Claude
        ultimo_mensaje = (messages or [{}])[-1].get("content", "")
        respuesta = f"[Demo Claude] Respuesta a: '{ultimo_mensaje[:50]}...' - En producción, Claude analizaría esto con el modelo {model}."
        return type('resp', (object,), {
            'content': [type('block', (object,), {'text': respuesta, 'type': 'text'})()],
            'stop_reason': 'end_turn',
            'usage': type('u', (object,), {'input_tokens': 50, 'output_tokens': 30})()
        })()


client = AnthropicDemo(api_key="demo")


def llamar_claude(prompt, sistema="Eres un asistente útil especializado en investigación científica"):
    """Hace una llamada simple a Claude (o demo) y retorna el texto de respuesta."""
    # TODO: usa client.messages.create() con:
    # - model="claude-3-5-haiku-20241022"
    # - max_tokens=1024
    # - system=sistema
    # - messages=[{"role": "user", "content": prompt}]
    # Retorna el .text del primer elemento de response.content
    pass


respuesta = llamar_claude("¿Qué es un agente de IA en una oración?")
print(f"Claude dice: {respuesta}")
print("\nEstructura de un mensaje de la API:")
print('{"role": "user", "content": "Tu pregunta aquí"}')
print('{"role": "assistant", "content": "Respuesta de Claude"}')
""",
        "solution_code": """class AnthropicDemo:
    def __init__(self, api_key="demo"):
        self.api_key = api_key
        self.messages = type('obj', (object,), {'create': self._create})()

    def _create(self, model, max_tokens, system="", messages=None, **kwargs):
        ultimo_mensaje = (messages or [{}])[-1].get("content", "")
        respuesta = f"[Demo Claude] Respuesta a: '{ultimo_mensaje[:50]}' - En producción, Claude usaría el modelo {model}."
        return type('resp', (object,), {
            'content': [type('block', (object,), {'text': respuesta, 'type': 'text'})()],
            'stop_reason': 'end_turn',
            'usage': type('u', (object,), {'input_tokens': 50, 'output_tokens': 30})()
        })()


client = AnthropicDemo(api_key="demo")


def llamar_claude(prompt, sistema="Eres un asistente útil especializado en investigación científica"):
    response = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=1024,
        system=sistema,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text


respuesta = llamar_claude("¿Qué es un agente de IA en una oración?")
print(f"Claude dice: {respuesta}")
print("\nEstructura de un mensaje de la API:")
print('{"role": "user", "content": "Tu pregunta aquí"}')
print('{"role": "assistant", "content": "Respuesta de Claude"}')
""",
        "expected_output_contains": ["Claude dice", "Estructura", "role"],
        "requires_api_key": False,
    },
    {
        "id": "m2s2",
        "module": 2,
        "module_title": "Tu Primer Agente con Claude API",
        "step": 2,
        "title": "El Bucle de Agente",
        "description": "Implementa el bucle central de cualquier agente: mantener el historial de mensajes y continuar hasta que Claude diga 'end_turn'.",
        "concept_html": """
<p>El <strong>bucle de agente</strong> es el corazón de cualquier sistema agente. El flujo es:</p>
<ol>
  <li>Llama a Claude con el historial completo</li>
  <li>Si <code>stop_reason == "end_turn"</code>: Claude terminó, retorna la respuesta</li>
  <li>Si <code>stop_reason == "tool_use"</code>: Claude quiere usar una herramienta, ejécutala</li>
  <li>Agrega el resultado al historial y repite</li>
</ol>
<p>La clave es mantener la <strong>alternancia de roles</strong>: siempre <code>user → assistant → user → ...</code></p>
""",
        "diagram_type": "none",
        "starter_code": """# Cliente demo
class DemoClient:
    def __init__(self):
        self.messages = type('obj', (object,), {'create': self._create})()
        self._llamadas = 0

    def _create(self, model, max_tokens, system, messages, tools=None, **kwargs):
        self._llamadas += 1
        contenido_usuario = messages[-1]["content"] if isinstance(messages[-1]["content"], str) else "..."
        # Simula que en la segunda llamada Claude termina
        if self._llamadas >= 2 or "Fin" in str(contenido_usuario):
            texto = f"Análisis completado. He revisado la información y puedo confirmar que el tema tiene 42 papers relevantes."
            return type('r', (), {'content': [type('b', (), {'type': 'text', 'text': texto})()], 'stop_reason': 'end_turn'})()
        else:
            texto = "Necesito buscar más información sobre este tema."
            return type('r', (), {'content': [type('b', (), {'type': 'text', 'text': texto})()], 'stop_reason': 'end_turn'})()

client = DemoClient()


def ejecutar_bucle_agente(mensaje_inicial, sistema="Eres un investigador científico", max_iter=10):
    """Bucle principal del agente: itera hasta que Claude termine."""
    mensajes = [{"role": "user", "content": mensaje_inicial}]
    print(f"Usuario: {mensaje_inicial}\n")

    for i in range(max_iter):
        print(f"[Iteración {i+1}] Llamando a Claude...")

        respuesta = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=1024,
            system=sistema,
            messages=mensajes,
        )

        # TODO: extrae el texto de respuesta.content[0].text
        texto_respuesta = None
        print(f"Claude: {texto_respuesta}")

        # TODO: si stop_reason == "end_turn", retorna texto_respuesta

        # TODO: si no, agrega la respuesta al historial y agrega un mensaje de usuario
        # con contenido "Continua con la investigación."

    return "Máximo de iteraciones alcanzado"


resultado = ejecutar_bucle_agente("Investiga sobre sistemas multi-agente de IA")
print(f"\nResultado final: {resultado}")
""",
        "solution_code": """class DemoClient:
    def __init__(self):
        self.messages = type('obj', (object,), {'create': self._create})()
        self._llamadas = 0

    def _create(self, model, max_tokens, system, messages, tools=None, **kwargs):
        self._llamadas += 1
        if self._llamadas >= 2:
            texto = "Análisis completado. He revisado la información y puedo confirmar que el tema tiene 42 papers relevantes."
        else:
            texto = "Necesito buscar más información sobre este tema."
        return type('r', (), {'content': [type('b', (), {'type': 'text', 'text': texto})()], 'stop_reason': 'end_turn'})()

client = DemoClient()


def ejecutar_bucle_agente(mensaje_inicial, sistema="Eres un investigador científico", max_iter=10):
    mensajes = [{"role": "user", "content": mensaje_inicial}]
    print(f"Usuario: {mensaje_inicial}\n")

    for i in range(max_iter):
        print(f"[Iteración {i+1}] Llamando a Claude...")

        respuesta = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=1024,
            system=sistema,
            messages=mensajes,
        )

        texto_respuesta = respuesta.content[0].text
        print(f"Claude: {texto_respuesta}")

        if respuesta.stop_reason == "end_turn":
            return texto_respuesta

        mensajes.append({"role": "assistant", "content": texto_respuesta})
        mensajes.append({"role": "user", "content": "Continua con la investigación."})

    return "Máximo de iteraciones alcanzado"


resultado = ejecutar_bucle_agente("Investiga sobre sistemas multi-agente de IA")
print(f"\nResultado final: {resultado}")
""",
        "expected_output_contains": ["Iteración", "Claude:", "Resultado final"],
        "requires_api_key": False,
    },
    {
        "id": "m2s3",
        "module": 2,
        "module_title": "Tu Primer Agente con Claude API",
        "step": 3,
        "title": "Agregando Herramientas Reales",
        "description": "Conecta el bucle de agente con herramientas reales. Claude decide cuándo usar cada herramienta y el agente la ejecuta automáticamente.",
        "concept_html": """
<p>Cuando Claude decide usar una herramienta, retorna un bloque <code>tool_use</code> con:</p>
<ul>
  <li><code>id</code>: identificador único de esta llamada a herramienta</li>
  <li><code>name</code>: nombre de la herramienta</li>
  <li><code>input</code>: argumentos en formato dict</li>
</ul>
<p>El agente debe ejecutar la herramienta y retornar un bloque <code>tool_result</code> con el mismo <code>tool_use_id</code>. La conversación continúa hasta <code>end_turn</code>.</p>
""",
        "diagram_type": "none",
        "starter_code": """import json

# Herramientas disponibles
def buscar_papers(query, max_resultados=5):
    return [{"titulo": f"{query} - Paper #{i+1}", "citas": (i+1)*10} for i in range(max_resultados)]

# TODO: Agrega la función resumir_paper(titulo, estilo="academico")
# Debe retornar: f"Resumen {estilo} de '{titulo}': Este paper analiza..."

HERRAMIENTAS_SCHEMA = [
    {
        "name": "buscar_papers",
        "description": "Busca papers académicos sobre un tema",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "max_resultados": {"type": "integer", "default": 5}
            },
            "required": ["query"]
        }
    },
    # TODO: Agrega el schema de resumir_paper aquí
    # Con campos: titulo (string, requerido), estilo (string, default "academico")
]

DISPATCH = {
    "buscar_papers": buscar_papers,
    # TODO: agrega resumir_paper al dispatcher
}


class DemoClientConTools:
    def __init__(self):
        self._llamadas = 0
        self.messages = type('obj', (object,), {'create': self._create})()

    def _create(self, model, max_tokens, system, messages, tools=None, **kwargs):
        self._llamadas += 1
        if self._llamadas == 1:
            # Simula que Claude quiere buscar
            bloque = type('b', (), {
                'type': 'tool_use', 'id': 'tool_001',
                'name': 'buscar_papers', 'input': {'query': 'multi-agent AI'}
            })()
            return type('r', (), {'content': [bloque], 'stop_reason': 'tool_use'})()
        elif self._llamadas == 2:
            # Simula que Claude quiere resumir el primer resultado
            bloque = type('b', (), {
                'type': 'tool_use', 'id': 'tool_002',
                'name': 'resumir_paper', 'input': {'titulo': 'multi-agent AI - Paper #1'}
            })()
            return type('r', (), {'content': [bloque], 'stop_reason': 'tool_use'})()
        else:
            texto = "Listo. Encontré varios papers y resumí el más relevante sobre multi-agent AI."
            return type('r', (), {'content': [type('b', (), {'type': 'text', 'text': texto})()], 'stop_reason': 'end_turn'})()

client = DemoClientConTools()


def agente_con_herramientas(pregunta):
    mensajes = [{"role": "user", "content": pregunta}]
    print(f"Usuario: {pregunta}\n")

    for i in range(10):
        resp = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=1024,
            system="Eres un investigador científico. Usa las herramientas disponibles.",
            messages=mensajes,
            tools=HERRAMIENTAS_SCHEMA,
        )

        if resp.stop_reason == "end_turn":
            texto = resp.content[0].text
            print(f"Claude (final): {texto}")
            return texto

        if resp.stop_reason == "tool_use":
            bloque = resp.content[0]
            print(f"Claude usa herramienta: {bloque.name}({bloque.input})")

            # Ejecuta la herramienta
            resultado = DISPATCH[bloque.name](**bloque.input)
            print(f"Resultado: {resultado}")

            # TODO: agrega al historial:
            # 1) el mensaje assistant con el bloque tool_use
            # 2) el mensaje user con el tool_result
            # El tool_result debe tener: type="tool_result", tool_use_id=bloque.id, content=str(resultado)

    return "Máximo de pasos alcanzado"


agente_con_herramientas("Investiga papers sobre multi-agent AI y resume el mejor")
""",
        "solution_code": """import json

def buscar_papers(query, max_resultados=5):
    return [{"titulo": f"{query} - Paper #{i+1}", "citas": (i+1)*10} for i in range(max_resultados)]

def resumir_paper(titulo, estilo="academico"):
    return f"Resumen {estilo} de '{titulo}': Este paper analiza sistemas multi-agente y sus aplicaciones."

HERRAMIENTAS_SCHEMA = [
    {
        "name": "buscar_papers",
        "description": "Busca papers académicos sobre un tema",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "max_resultados": {"type": "integer", "default": 5}
            },
            "required": ["query"]
        }
    },
    {
        "name": "resumir_paper",
        "description": "Resume un paper dado su título",
        "input_schema": {
            "type": "object",
            "properties": {
                "titulo": {"type": "string"},
                "estilo": {"type": "string", "default": "academico"}
            },
            "required": ["titulo"]
        }
    },
]

DISPATCH = {"buscar_papers": buscar_papers, "resumir_paper": resumir_paper}


class DemoClientConTools:
    def __init__(self):
        self._llamadas = 0
        self.messages = type('obj', (object,), {'create': self._create})()

    def _create(self, model, max_tokens, system, messages, tools=None, **kwargs):
        self._llamadas += 1
        if self._llamadas == 1:
            bloque = type('b', (), {'type': 'tool_use', 'id': 'tool_001', 'name': 'buscar_papers', 'input': {'query': 'multi-agent AI'}})()
            return type('r', (), {'content': [bloque], 'stop_reason': 'tool_use'})()
        elif self._llamadas == 2:
            bloque = type('b', (), {'type': 'tool_use', 'id': 'tool_002', 'name': 'resumir_paper', 'input': {'titulo': 'multi-agent AI - Paper #1'}})()
            return type('r', (), {'content': [bloque], 'stop_reason': 'tool_use'})()
        else:
            texto = "Listo. Encontré varios papers y resumí el más relevante sobre multi-agent AI."
            return type('r', (), {'content': [type('b', (), {'type': 'text', 'text': texto})()], 'stop_reason': 'end_turn'})()

client = DemoClientConTools()


def agente_con_herramientas(pregunta):
    mensajes = [{"role": "user", "content": pregunta}]
    print(f"Usuario: {pregunta}\n")

    for i in range(10):
        resp = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=1024,
            system="Eres un investigador científico.",
            messages=mensajes,
            tools=HERRAMIENTAS_SCHEMA,
        )

        if resp.stop_reason == "end_turn":
            texto = resp.content[0].text
            print(f"Claude (final): {texto}")
            return texto

        if resp.stop_reason == "tool_use":
            bloque = resp.content[0]
            print(f"Claude usa herramienta: {bloque.name}({bloque.input})")
            resultado = DISPATCH[bloque.name](**bloque.input)
            print(f"Resultado: {resultado}")

            mensajes.append({"role": "assistant", "content": [{"type": "tool_use", "id": bloque.id, "name": bloque.name, "input": bloque.input}]})
            mensajes.append({"role": "user", "content": [{"type": "tool_result", "tool_use_id": bloque.id, "content": str(resultado)}]})

    return "Máximo de pasos alcanzado"


agente_con_herramientas("Investiga papers sobre multi-agent AI y resume el mejor")
""",
        "expected_output_contains": ["usa herramienta", "buscar_papers", "Resultado", "Claude (final)"],
        "requires_api_key": False,
    },

    # ─────────────────────────────────────────────────────────────────────────
    # MÓDULO 3: ORQUESTACIÓN MULTI-AGENTE
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "m3s1",
        "module": 3,
        "module_title": "Orquestación Multi-Agente",
        "step": 1,
        "title": "El Patrón Orquestador",
        "description": "Un agente central delega tareas a agentes especializados. Este patrón es el corazón de sistemas como Bruno, CrewAI y AutoGen.",
        "concept_html": """
<p>El <strong>patrón orquestador</strong> tiene un agente principal (el orquestador) que:</p>
<ul>
  <li>Conoce el objetivo global</li>
  <li>Divide la tarea en subtareas</li>
  <li>Delega cada subtarea al agente especializado correcto</li>
  <li>Combina los resultados en una respuesta final</li>
</ul>
<p>Ventajas: cada agente tiene contexto enfocado, se pueden paralelizar tareas, y el sistema escala mejor que un solo agente monolítico.</p>
""",
        "diagram_type": "orchestrator",
        "starter_code": """class Orquestador:
    def __init__(self):
        self.agentes = {}
        self.resultados = {}

    def registrar(self, nombre, agente):
        """Registra un agente con un nombre."""
        self.agentes[nombre] = agente
        print(f"Agente registrado: {nombre}")

    def despachar(self, nombre_agente, tarea):
        """Envía una tarea a un agente y guarda el resultado."""
        # TODO: implementa esto:
        # 1. Verifica que el agente exista, si no lanza ValueError
        # 2. Imprime: f"[Orquestador] Despachando a {nombre_agente}: {tarea[:50]}"
        # 3. Llama a self.agentes[nombre_agente].ejecutar(tarea)
        # 4. Guarda el resultado en self.resultados[nombre_agente]
        # 5. Retorna el resultado
        pass

    def ejecutar_pipeline(self, tema):
        """Orquesta el pipeline completo: buscar -> analizar -> reportar."""
        # TODO: implementa el pipeline de 3 pasos
        pass


# Agentes especializados simples
class AgenteBuscador:
    def ejecutar(self, tarea):
        return {"papers": [f"Paper sobre {tarea} #{i}" for i in range(3)], "total": 3}

class AgenteAnalizador:
    def ejecutar(self, tarea):
        datos = eval(tarea) if isinstance(tarea, str) and tarea.startswith("{") else {"papers": []}
        return {"resumen": f"Analizados {len(datos.get('papers', []))} papers", "calidad": "alta"}

class AgenteReportero:
    def ejecutar(self, tarea):
        return f"Reporte generado basado en: {tarea[:80]}..."


orquestador = Orquestador()
orquestador.registrar("buscador", AgenteBuscador())
orquestador.registrar("analizador", AgenteAnalizador())
orquestador.registrar("reportero", AgenteReportero())

orquestador.ejecutar_pipeline("sistemas multi-agente")
""",
        "solution_code": """class Orquestador:
    def __init__(self):
        self.agentes = {}
        self.resultados = {}

    def registrar(self, nombre, agente):
        self.agentes[nombre] = agente
        print(f"Agente registrado: {nombre}")

    def despachar(self, nombre_agente, tarea):
        if nombre_agente not in self.agentes:
            raise ValueError(f"Agente desconocido: {nombre_agente}")
        print(f"[Orquestador] Despachando a {nombre_agente}: {str(tarea)[:50]}")
        resultado = self.agentes[nombre_agente].ejecutar(tarea)
        self.resultados[nombre_agente] = resultado
        return resultado

    def ejecutar_pipeline(self, tema):
        print(f"\nIniciando pipeline para: {tema}\n")
        papers = self.despachar("buscador", tema)
        print(f"  -> Encontrados: {papers}")
        analisis = self.despachar("analizador", str(papers))
        print(f"  -> Análisis: {analisis}")
        reporte = self.despachar("reportero", str(analisis))
        print(f"  -> Reporte: {reporte}")
        return reporte


class AgenteBuscador:
    def ejecutar(self, tarea):
        return {"papers": [f"Paper sobre {tarea} #{i}" for i in range(3)], "total": 3}

class AgenteAnalizador:
    def ejecutar(self, tarea):
        datos = eval(tarea) if isinstance(tarea, str) and tarea.startswith("{") else {"papers": []}
        return {"resumen": f"Analizados {len(datos.get('papers', []))} papers", "calidad": "alta"}

class AgenteReportero:
    def ejecutar(self, tarea):
        return f"Reporte generado basado en: {str(tarea)[:80]}"


orquestador = Orquestador()
orquestador.registrar("buscador", AgenteBuscador())
orquestador.registrar("analizador", AgenteAnalizador())
orquestador.registrar("reportero", AgenteReportero())

resultado_final = orquestador.ejecutar_pipeline("sistemas multi-agente")
print(f"\nPipeline completado. Resultado: {resultado_final}")
""",
        "expected_output_contains": ["Agente registrado", "Despachando", "Pipeline completado"],
        "requires_api_key": False,
    },
    {
        "id": "m3s2",
        "module": 3,
        "module_title": "Orquestación Multi-Agente",
        "step": 2,
        "title": "Delegación a Subagentes",
        "description": "Diseña una clase base para agentes reutilizables. Implementa SearchAgent y SummaryAgent que siguen el mismo contrato.",
        "concept_html": """
<p>En sistemas multi-agente robustos, cada agente hereda de una <strong>clase base</strong> común que define el contrato:</p>
<ul>
  <li><code>nombre</code> y <code>descripcion</code>: para que el orquestador sepa a quién llamar</li>
  <li><code>ejecutar(tarea)</code>: el método principal</li>
  <li><code>log(mensaje)</code>: para reportar progreso al orquestador</li>
</ul>
<p>Este patrón se usa en Bruno, CrewAI (<code>Agent</code> class) y LangGraph (<code>StateGraph</code> nodes).</p>
""",
        "diagram_type": "orchestrator",
        "starter_code": """from abc import ABC, abstractmethod
import time


class AgenteBase(ABC):
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self._logs = []

    def log(self, mensaje, nivel="info"):
        self._logs.append({"nivel": nivel, "mensaje": mensaje})
        emoji = {"info": "ℹ️", "exito": "✅", "error": "❌", "advertencia": "⚠️"}.get(nivel, "ℹ️")
        print(f"  [{self.nombre}] {emoji} {mensaje}")

    @abstractmethod
    def ejecutar(self, tarea: str) -> dict:
        """Ejecuta la tarea y retorna un dict con los resultados."""
        pass


class AgenteSearcher(AgenteBase):
    def __init__(self):
        super().__init__("Buscador", "Experto en búsqueda bibliográfica")

    def ejecutar(self, tarea: str) -> dict:
        self.log(f"Buscando: '{tarea}'")
        time.sleep(0.1)  # simula latencia de API
        papers = [{"titulo": f"{tarea} - Estudio #{i+1}", "ano": 2020+i, "citas": (i+1)*15} for i in range(4)]
        self.log(f"Encontrados {len(papers)} papers", "exito")
        return {"papers": papers, "total": len(papers), "query": tarea}


# TODO: Implementa AgenteSummarizer que herede de AgenteBase:
# - nombre: "Resumidor"
# - descripcion: "Experto en resumir y sintetizar papers"
# - ejecutar(tarea): espera que tarea sea un dict con 'papers'
#   - itera sobre los papers y genera un resumen para cada uno
#   - retorna {"resumenes": [...], "total": N, "tema": papers[0]['titulo']}


# Prueba
buscador = AgenteSearcher()
resultados = buscador.ejecutar("sistemas multi-agente con LLMs")
print(f"\nBuscador retornó: {resultados['total']} papers")

# TODO: instancia AgenteSummarizer y resume los papers del buscador
""",
        "solution_code": """from abc import ABC, abstractmethod
import time


class AgenteBase(ABC):
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self._logs = []

    def log(self, mensaje, nivel="info"):
        self._logs.append({"nivel": nivel, "mensaje": mensaje})
        emoji = {"info": "ℹ️", "exito": "✅", "error": "❌", "advertencia": "⚠️"}.get(nivel, "ℹ️")
        print(f"  [{self.nombre}] {emoji} {mensaje}")

    @abstractmethod
    def ejecutar(self, tarea) -> dict:
        pass


class AgenteSearcher(AgenteBase):
    def __init__(self):
        super().__init__("Buscador", "Experto en búsqueda bibliográfica")

    def ejecutar(self, tarea) -> dict:
        self.log(f"Buscando: '{tarea}'")
        time.sleep(0.1)
        papers = [{"titulo": f"{tarea} - Estudio #{i+1}", "ano": 2020+i, "citas": (i+1)*15} for i in range(4)]
        self.log(f"Encontrados {len(papers)} papers", "exito")
        return {"papers": papers, "total": len(papers), "query": tarea}


class AgenteSummarizer(AgenteBase):
    def __init__(self):
        super().__init__("Resumidor", "Experto en resumir y sintetizar papers")

    def ejecutar(self, tarea) -> dict:
        papers = tarea.get("papers", []) if isinstance(tarea, dict) else []
        self.log(f"Resumiendo {len(papers)} papers...")
        resumenes = []
        for p in papers:
            resumen = f"Resumen de '{p['titulo']}' ({p['ano']}): Estudio con {p['citas']} citas que analiza..."
            resumenes.append(resumen)
            self.log(f"Resumido: {p['titulo'][:40]}...", "exito")
        return {"resumenes": resumenes, "total": len(resumenes)}


buscador = AgenteSearcher()
resultados = buscador.ejecutar("sistemas multi-agente con LLMs")
print(f"\nBuscador retornó: {resultados['total']} papers")

resumidor = AgenteSummarizer()
resumenes = resumidor.ejecutar(resultados)
print(f"\nResumidor generó: {resumenes['total']} resúmenes")
for r in resumenes["resumenes"]:
    print(f"  - {r[:70]}...")
""",
        "expected_output_contains": ["Buscando", "Encontrados", "Resumiendo", "resúmenes"],
        "requires_api_key": False,
    },
    {
        "id": "m3s3",
        "module": 3,
        "module_title": "Orquestación Multi-Agente",
        "step": 3,
        "title": "Comunicación con MessageBus",
        "description": "Implementa un bus de mensajes desacoplado usando queue.Queue, el mismo patrón que usa el sistema Bruno para streaming en tiempo real.",
        "concept_html": """
<p>Un <strong>MessageBus</strong> desacopla a los agentes: en vez de llamarse directamente, publican mensajes en colas. Ventajas:</p>
<ul>
  <li>🔁 <strong>Asincronismo</strong>: el publicador no espera al receptor</li>
  <li>🔀 <strong>Desacoplamiento</strong>: los agentes no se conocen entre sí</li>
  <li>📡 <strong>Streaming</strong>: el frontend puede escuchar eventos en tiempo real</li>
</ul>
<p>El sistema Bruno usa exactamente esto: <code>queue.Queue</code> entre los agentes y el endpoint SSE de FastAPI.</p>
""",
        "diagram_type": "orchestrator",
        "starter_code": """import queue
import threading


class MessageBus:
    def __init__(self):
        self._colas = {}

    def suscribir(self, nombre_agente):
        """Crea una cola para un agente."""
        self._colas[nombre_agente] = queue.Queue()
        print(f"Bus: {nombre_agente} suscrito")

    def publicar(self, agente_destino, mensaje):
        """Envía un mensaje a la cola del agente destino."""
        # TODO: verifica que el agente esté suscrito, si no lanza KeyError
        # Luego pon el mensaje en la cola con .put()
        pass

    def recibir(self, nombre_agente, timeout=5):
        """Recibe el siguiente mensaje de la cola del agente."""
        # TODO: usa .get(timeout=timeout) de la cola del agente
        # Si Queue.Empty se lanza, retorna None
        pass

    def publicar_a_todos(self, mensaje):
        """Publica el mismo mensaje a todos los agentes suscritos."""
        # TODO: itera sobre todos los agentes y publica el mensaje
        pass


# Agente que escucha el bus en un hilo separado
class AgenteListener:
    def __init__(self, nombre, bus):
        self.nombre = nombre
        self.bus = bus
        self.mensajes_recibidos = []

    def escuchar(self, max_mensajes=3):
        for _ in range(max_mensajes):
            msg = self.bus.recibir(self.nombre)
            if msg:
                self.mensajes_recibidos.append(msg)
                print(f"  [{self.nombre}] Recibió: {msg}")


# Prueba del sistema
bus = MessageBus()
bus.suscribir("analista")
bus.suscribir("reportero")

analista = AgenteListener("analista", bus)
reportero = AgenteListener("reportero", bus)

# Publica mensajes
bus.publicar("analista", {"tipo": "tarea", "contenido": "Analiza 10 papers"})
bus.publicar("analista", {"tipo": "tarea", "contenido": "Evalua calidad metodologica"})
bus.publicar_a_todos({"tipo": "broadcast", "contenido": "Pipeline iniciado"})

# Los agentes leen sus mensajes
print("\nAnalista leyendo mensajes:")
analista.escuchar(3)

print("\nReportero leyendo mensajes:")
reportero.escuchar(1)
""",
        "solution_code": """import queue
import threading


class MessageBus:
    def __init__(self):
        self._colas = {}

    def suscribir(self, nombre_agente):
        self._colas[nombre_agente] = queue.Queue()
        print(f"Bus: {nombre_agente} suscrito")

    def publicar(self, agente_destino, mensaje):
        if agente_destino not in self._colas:
            raise KeyError(f"Agente no suscrito: {agente_destino}")
        self._colas[agente_destino].put(mensaje)

    def recibir(self, nombre_agente, timeout=5):
        try:
            return self._colas[nombre_agente].get(timeout=timeout)
        except queue.Empty:
            return None

    def publicar_a_todos(self, mensaje):
        for nombre in self._colas:
            self._colas[nombre].put(mensaje)


class AgenteListener:
    def __init__(self, nombre, bus):
        self.nombre = nombre
        self.bus = bus
        self.mensajes_recibidos = []

    def escuchar(self, max_mensajes=3):
        for _ in range(max_mensajes):
            msg = self.bus.recibir(self.nombre)
            if msg:
                self.mensajes_recibidos.append(msg)
                print(f"  [{self.nombre}] Recibió: {msg}")


bus = MessageBus()
bus.suscribir("analista")
bus.suscribir("reportero")

analista = AgenteListener("analista", bus)
reportero = AgenteListener("reportero", bus)

bus.publicar("analista", {"tipo": "tarea", "contenido": "Analiza 10 papers"})
bus.publicar("analista", {"tipo": "tarea", "contenido": "Evalua calidad metodologica"})
bus.publicar_a_todos({"tipo": "broadcast", "contenido": "Pipeline iniciado"})

print("\nAnalista leyendo mensajes:")
analista.escuchar(3)

print("\nReportero leyendo mensajes:")
reportero.escuchar(1)
""",
        "expected_output_contains": ["suscrito", "Recibió", "broadcast", "Pipeline iniciado"],
        "requires_api_key": False,
    },

    # ─────────────────────────────────────────────────────────────────────────
    # MÓDULO 4: PATRONES AVANZADOS
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "m4s1",
        "module": 4,
        "module_title": "Patrones Avanzados",
        "step": 1,
        "title": "Ejecución Paralela",
        "description": "Ejecuta múltiples agentes simultáneamente usando ThreadPoolExecutor. Bruno usa este patrón para buscar en PubMed, Semantic Scholar y CrossRef al mismo tiempo.",
        "concept_html": """
<p>La <strong>ejecución paralela</strong> reduce el tiempo total cuando las tareas son independientes. Si buscar en PubMed tarda 2s y en Semantic Scholar tarda 2s:</p>
<ul>
  <li>🕰️ <strong>Secuencial</strong>: 2 + 2 = 4 segundos</li>
  <li>⚡ <strong>Paralelo</strong>: max(2, 2) = 2 segundos</li>
</ul>
<p><code>ThreadPoolExecutor</code> del módulo <code>concurrent.futures</code> es la forma más simple de paralelizar en Python. Bruno lo usa con <code>max_workers=4</code>.</p>
""",
        "diagram_type": "parallel",
        "starter_code": """import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# Simula bases de datos con latencias distintas
BASES_DE_DATOS = {
    "pubmed": 0.3,
    "semantic_scholar": 0.2,
    "crossref": 0.25,
}


def buscar_en_db(nombre_db, query):
    """Simula búsqueda en una base de datos con latencia."""
    latencia = BASES_DE_DATOS[nombre_db]
    time.sleep(latencia)
    n_resultados = random.randint(5, 15)
    papers = [{"titulo": f"[{nombre_db}] {query} - Paper #{i}", "fuente": nombre_db} for i in range(n_resultados)]
    print(f"  {nombre_db}: {n_resultados} papers encontrados ({latencia}s)")
    return papers


def deduplicar(todos_los_papers):
    """Elimina duplicados por título."""
    vistos = set()
    unicos = []
    for p in todos_los_papers:
        if p["titulo"] not in vistos:
            vistos.add(p["titulo"])
            unicos.append(p)
    return unicos


def busqueda_paralela(query):
    """Busca en todas las bases de datos en paralelo."""
    print(f"\nBuscando '{query}' en paralelo...")
    inicio = time.time()
    todos = []

    # TODO: usa ThreadPoolExecutor(max_workers=3) para ejecutar buscar_en_db
    # en paralelo para cada base de datos en BASES_DE_DATOS.keys()
    # Recoge los resultados con as_completed() y extiende la lista `todos`

    duracion = time.time() - inicio
    unicos = deduplicar(todos)
    print(f"\nTotal: {len(todos)} papers en {duracion:.2f}s (paralelo)")
    print(f"Después de deduplicar: {len(unicos)} papers únicos")
    return unicos


# Compara paralelo vs secuencial
resultados = busqueda_paralela("sistemas multi-agente")
print(f"\n(Búsqueda secuencial habría tardado ~{sum(BASES_DE_DATOS.values()):.2f}s)")
""",
        "solution_code": """import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

BASES_DE_DATOS = {
    "pubmed": 0.3,
    "semantic_scholar": 0.2,
    "crossref": 0.25,
}


def buscar_en_db(nombre_db, query):
    latencia = BASES_DE_DATOS[nombre_db]
    time.sleep(latencia)
    n_resultados = random.randint(5, 15)
    papers = [{"titulo": f"[{nombre_db}] {query} - Paper #{i}", "fuente": nombre_db} for i in range(n_resultados)]
    print(f"  {nombre_db}: {n_resultados} papers encontrados ({latencia}s)")
    return papers


def deduplicar(todos_los_papers):
    vistos = set()
    unicos = []
    for p in todos_los_papers:
        if p["titulo"] not in vistos:
            vistos.add(p["titulo"])
            unicos.append(p)
    return unicos


def busqueda_paralela(query):
    print(f"\nBuscando '{query}' en paralelo...")
    inicio = time.time()
    todos = []

    with ThreadPoolExecutor(max_workers=3) as executor:
        futuros = {executor.submit(buscar_en_db, db, query): db for db in BASES_DE_DATOS.keys()}
        for futuro in as_completed(futuros):
            resultado = futuro.result()
            todos.extend(resultado)

    duracion = time.time() - inicio
    unicos = deduplicar(todos)
    print(f"\nTotal: {len(todos)} papers en {duracion:.2f}s (paralelo)")
    print(f"Después de deduplicar: {len(unicos)} papers únicos")
    return unicos


resultados = busqueda_paralela("sistemas multi-agente")
print(f"\n(Búsqueda secuencial habría tardado ~{sum(BASES_DE_DATOS.values()):.2f}s)")
""",
        "expected_output_contains": ["paralelo", "pubmed", "semantic_scholar", "deduplicar"],
        "requires_api_key": False,
    },
    {
        "id": "m4s2",
        "module": 4,
        "module_title": "Patrones Avanzados",
        "step": 2,
        "title": "Pipeline Secuencial con Contexto Acumulativo",
        "description": "Cada etapa del pipeline enriquece los datos para la siguiente. Este patrón garantiza que ningún agente pierda información importante.",
        "concept_html": """
<p>En un <strong>pipeline secuencial acumulativo</strong>, cada etapa recibe el output de la anterior y agrega más información en vez de reemplazarla. Ejemplo de Bruno:</p>
<ul>
  <li>Etapa 1 (Búsqueda): <code>{papers: [...]}</code></li>
  <li>Etapa 2 (Análisis): <code>{papers: [...], analysis: {pico: ..., evidencia: ...}}</code></li>
  <li>Etapa 3 (Síntesis): <code>{papers: [...], analysis: {...}, meta: {nivel_global: ...}}</code></li>
</ul>
<p>Clave: nunca sobrescribas datos anteriores, solo agrega nuevas claves al dict de contexto.</p>
""",
        "diagram_type": "pipeline",
        "starter_code": """# Pipeline de 3 etapas con contexto acumulativo

def etapa_busqueda(tema):
    """Etapa 1: Búsqueda de papers"""
    print(f"\n[Etapa 1] Buscando papers sobre: {tema}")
    papers = [
        {"titulo": f"{tema} - RCT multicenter", "tipo": "RCT", "ano": 2023, "n_pacientes": 500},
        {"titulo": f"{tema} - Systematic review", "tipo": "revision", "ano": 2022, "n_pacientes": None},
        {"titulo": f"{tema} - Cohort study", "tipo": "cohorte", "ano": 2021, "n_pacientes": 120},
    ]
    print(f"  Encontrados: {len(papers)} papers")
    # Retorna contexto inicial
    return {"tema": tema, "papers": papers}


def etapa_analisis(contexto):
    """Etapa 2: Análisis de cada paper — AGREGA al contexto, no reemplaza."""
    print(f"\n[Etapa 2] Analizando {len(contexto['papers'])} papers...")

    # TODO: itera sobre contexto['papers'] y agrega a cada paper un campo 'analisis'
    # con: nivel_evidencia ("1a" para RCT, "1b" para revision, "2b" para cohorte)
    # y calidad ("alta" si n_pacientes > 200 o None, "media" si <= 200)
    # Retorna el mismo contexto con papers enriquecidos Y agrega contexto['analisis_completado'] = True
    pass


def etapa_sintesis(contexto):
    """Etapa 3: Síntesis global — AGREGA al contexto, no reemplaza."""
    print(f"\n[Etapa 3] Sintetizando evidencia...")

    # TODO: calcula nivel_evidencia_global (el nivel más alto encontrado entre los papers)
    # y n_total_pacientes (suma de n_pacientes excluyendo None)
    # Agrega al contexto: {'meta': {'nivel_global': ..., 'n_total': ..., 'n_estudios': len(papers)}}
    # Imprime un resumen de la síntesis
    # Retorna el contexto completo
    pass


# Ejecuta el pipeline
resultado = etapa_busqueda("laparoscopic appendectomy in children")
resultado = etapa_analisis(resultado)
resultado = etapa_sintesis(resultado)

print("\n--- Contexto Final ---")
print(f"Tema: {resultado['tema']}")
print(f"Papers: {len(resultado['papers'])}")
print(f"Meta: {resultado.get('meta', 'No generado')}")
""",
        "solution_code": """def etapa_busqueda(tema):
    print(f"\n[Etapa 1] Buscando papers sobre: {tema}")
    papers = [
        {"titulo": f"{tema} - RCT multicenter", "tipo": "RCT", "ano": 2023, "n_pacientes": 500},
        {"titulo": f"{tema} - Systematic review", "tipo": "revision", "ano": 2022, "n_pacientes": None},
        {"titulo": f"{tema} - Cohort study", "tipo": "cohorte", "ano": 2021, "n_pacientes": 120},
    ]
    print(f"  Encontrados: {len(papers)} papers")
    return {"tema": tema, "papers": papers}


def etapa_analisis(contexto):
    print(f"\n[Etapa 2] Analizando {len(contexto['papers'])} papers...")
    niveles = {"RCT": "1a", "revision": "1b", "cohorte": "2b"}
    for paper in contexto["papers"]:
        n = paper.get("n_pacientes")
        paper["analisis"] = {
            "nivel_evidencia": niveles.get(paper["tipo"], "3"),
            "calidad": "alta" if (n is None or n > 200) else "media",
        }
        print(f"  {paper['titulo'][:45]}... -> Niv.{paper['analisis']['nivel_evidencia']} Cal.{paper['analisis']['calidad']}")
    contexto["analisis_completado"] = True
    return contexto


def etapa_sintesis(contexto):
    print(f"\n[Etapa 3] Sintetizando evidencia...")
    papers = contexto["papers"]
    niveles = [p["analisis"]["nivel_evidencia"] for p in papers if "analisis" in p]
    nivel_global = sorted(niveles)[0] if niveles else "ND"
    n_total = sum(p["n_pacientes"] for p in papers if p.get("n_pacientes") is not None)
    contexto["meta"] = {
        "nivel_global": nivel_global,
        "n_total": n_total,
        "n_estudios": len(papers),
    }
    print(f"  Nivel de evidencia global: {nivel_global}")
    print(f"  Pacientes totales: {n_total}")
    return contexto


resultado = etapa_busqueda("laparoscopic appendectomy in children")
resultado = etapa_analisis(resultado)
resultado = etapa_sintesis(resultado)

print("\n--- Contexto Final ---")
print(f"Tema: {resultado['tema']}")
print(f"Papers: {len(resultado['papers'])}")
print(f"Meta: {resultado.get('meta')}")
""",
        "expected_output_contains": ["Etapa 1", "Etapa 2", "Etapa 3", "Contexto Final", "nivel_global"],
        "requires_api_key": False,
    },
    {
        "id": "m4s3",
        "module": 4,
        "module_title": "Patrones Avanzados",
        "step": 3,
        "title": "Patrón Crítico/Evaluador",
        "description": "Un agente generador produce output; un agente evaluador lo puntaú. Si la puntuación es baja, el generador revisa. Este loop asegura calidad automáticamente.",
        "concept_html": """
<p>El <strong>patrón crítico/evaluador</strong> (o 'generator-critic') es un loop de calidad automática:</p>
<ol>
  <li>El <strong>Generador</strong> produce un borrador</li>
  <li>El <strong>Evaluador</strong> asigna una puntuación y da feedback</li>
  <li>Si la puntuación &lt; umbral, el Generador revisa usando el feedback</li>
  <li>Repite hasta alcanzar el umbral o el máximo de rondas</li>
</ol>
<p>Usado en Constitutional AI (Anthropic), AutoGen's GroupChat y sistemas de revisión de papers.</p>
""",
        "diagram_type": "none",
        "starter_code": """import random


class AgenteGenerador:
    def __init__(self):
        self.version = 0

    def generar(self, tarea, feedback=None):
        self.version += 1
        if feedback:
            print(f"\n[Generador v{self.version}] Revisando con feedback: '{feedback[:60]}...'")
            calidad = min(5, 2 + self.version)  # mejora con cada revisión
        else:
            print(f"\n[Generador v{self.version}] Generando primera versión para: '{tarea}'")
            calidad = 2  # primera versión siempre mediocre
        contenido = f"Versión {self.version}: Análisis de '{tarea}' " + "mejorado " * (self.version - 1)
        return {"contenido": contenido, "version": self.version, "calidad_interna": calidad}


class AgenteEvaluador:
    def evaluar(self, resultado):
        # Simula evaluación: mejora con cada versión
        puntuacion = min(5, resultado["calidad_interna"])
        if puntuacion < 4:
            feedback = f"Versión {resultado['version']} necesita más detalle, evidencia estadística y referencias."
        else:
            feedback = "Excelente. Incluye evidencia sólida y estructura clara."
        print(f"  [Evaluador] Puntuación: {puntuacion}/5 - {feedback[:60]}")
        return {"puntuacion": puntuacion, "feedback": feedback}


def bucle_critico(tarea, puntaje_minimo=4, max_rondas=4):
    """Ejecuta el loop generador-evaluador hasta alcanzar la calidad mínima."""
    generador = AgenteGenerador()
    evaluador = AgenteEvaluador()
    print(f"Iniciando bucle crítico para: '{tarea}'")
    print(f"Objetivo: puntuación >= {puntaje_minimo} en max {max_rondas} rondas\n")

    feedback_anterior = None
    for ronda in range(1, max_rondas + 1):
        print(f"=== Ronda {ronda}/{max_rondas} ===")

        # TODO: genera un resultado usando el generador (pasa feedback_anterior si no es None)
        resultado = None

        # TODO: evalúa el resultado con el evaluador
        evaluacion = None

        # TODO: si la puntuación >= puntaje_minimo, imprime "Calidad alcanzada" y retorna el resultado

        # TODO: si no, actualiza feedback_anterior con evaluacion['feedback']

    print(f"Máximo de rondas alcanzado. Última puntuación: {evaluacion['puntuacion'] if evaluacion else 'N/A'}")
    return resultado


bucle_critico("revisión sistemática de cirugía laparoscópica en niños")
""",
        "solution_code": """import random


class AgenteGenerador:
    def __init__(self):
        self.version = 0

    def generar(self, tarea, feedback=None):
        self.version += 1
        if feedback:
            print(f"\n[Generador v{self.version}] Revisando con feedback: '{feedback[:60]}...'")
            calidad = min(5, 2 + self.version)
        else:
            print(f"\n[Generador v{self.version}] Generando primera versión para: '{tarea}'")
            calidad = 2
        contenido = f"Versión {self.version}: Análisis de '{tarea}' " + "mejorado " * (self.version - 1)
        return {"contenido": contenido, "version": self.version, "calidad_interna": calidad}


class AgenteEvaluador:
    def evaluar(self, resultado):
        puntuacion = min(5, resultado["calidad_interna"])
        if puntuacion < 4:
            feedback = f"Versión {resultado['version']} necesita más detalle, evidencia estadística y referencias."
        else:
            feedback = "Excelente. Incluye evidencia sólida y estructura clara."
        print(f"  [Evaluador] Puntuación: {puntuacion}/5 - {feedback[:60]}")
        return {"puntuacion": puntuacion, "feedback": feedback}


def bucle_critico(tarea, puntaje_minimo=4, max_rondas=4):
    generador = AgenteGenerador()
    evaluador = AgenteEvaluador()
    print(f"Iniciando bucle crítico para: '{tarea}'")
    print(f"Objetivo: puntuación >= {puntaje_minimo} en max {max_rondas} rondas\n")

    feedback_anterior = None
    evaluacion = None
    for ronda in range(1, max_rondas + 1):
        print(f"=== Ronda {ronda}/{max_rondas} ===")
        resultado = generador.generar(tarea, feedback=feedback_anterior)
        evaluacion = evaluador.evaluar(resultado)

        if evaluacion["puntuacion"] >= puntaje_minimo:
            print(f"\n✅ Calidad alcanzada en ronda {ronda}! Puntuación: {evaluacion['puntuacion']}/5")
            return resultado

        feedback_anterior = evaluacion["feedback"]

    print(f"Máximo de rondas alcanzado. Última puntuación: {evaluacion['puntuacion'] if evaluacion else 'N/A'}")
    return resultado


bucle_critico("revisión sistemática de cirugía laparoscópica en niños")
""",
        "expected_output_contains": ["Ronda", "Evaluador", "Puntuación", "Calidad alcanzada"],
        "requires_api_key": False,
    },

    # ─────────────────────────────────────────────────────────────────────────
    # MÓDULO 5: PROYECTO FINAL — REPLICA EL SISTEMA BRUNO
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "m5s1",
        "module": 5,
        "module_title": "Proyecto Final: Replica el Sistema Bruno",
        "step": 1,
        "title": "Diseño: Sistema de 5 Agentes",
        "description": "Diseña la arquitectura completa de un sistema como Bruno: 5 agentes especializados con dependencias explícitas y configuración como código.",
        "concept_html": """
<p>El <strong>sistema Bruno</strong> tiene 5 agentes en secuencia:</p>
<ol>
  <li>🔍 <strong>Buscador</strong>: PubMed + Semantic Scholar + CrossRef en paralelo</li>
  <li>🔬 <strong>Analizador</strong>: PICO-S + nivel de evidencia CEBM por paper</li>
  <li>📊 <strong>Meta-Analista</strong>: síntesis global + grado de recomendación</li>
  <li>📝 <strong>Redactor</strong>: apunte clínico completo en Word</li>
  <li>🎨 <strong>Presentador</strong>: PowerPoint profesional 18+ slides</li>
</ol>
<p>La clave es definir las <strong>dependencias explícitas</strong>: qué agente necesita el output de cuál otro.</p>
""",
        "diagram_type": "full_system",
        "starter_code": """from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class AgentConfig:
    nombre: str
    icono: str
    color: str
    descripcion: str
    depende_de: List[str] = field(default_factory=list)
    timeout_segundos: int = 300
    reintentos: int = 1


# El primer agente ya está definido:
PIPELINE_CONFIG = [
    AgentConfig(
        nombre="Buscador",
        icono="🔍",
        color="#00b4d8",
        descripcion="Búsqueda bibliográfica en PubMed, Semantic Scholar y CrossRef",
        depende_de=[],  # es el primero, no depende de nadie
        timeout_segundos=60,
    ),
    # TODO: Agrega los otros 4 agentes en orden:
    # 2. Analizador (depende_de=["Buscador"], color="#9d4edd", timeout=300)
    # 3. Meta-Analista (depende_de=["Analizador"], color="#f77f00", timeout=120)
    # 4. Redactor (depende_de=["Meta-Analista", "Analizador"], color="#2dc653", timeout=300)
    # 5. Presentador (depende_de=["Meta-Analista"], color="#ff4d6d", timeout=300)
]


def validar_pipeline(config):
    """Verifica que las dependencias sean válidas (no hay ciclos ni dependencias inexistentes)."""
    nombres = {a.nombre for a in config}
    for agente in config:
        for dep in agente.depende_de:
            assert dep in nombres, f"{agente.nombre} depende de '{dep}' que no existe"
    print(f"Pipeline válido: {len(config)} agentes")
    for a in config:
        deps = f" <- {a.depende_de}" if a.depende_de else " (primero)"
        print(f"  {a.icono} {a.nombre}{deps}")
    return True


validar_pipeline(PIPELINE_CONFIG)
""",
        "solution_code": """from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class AgentConfig:
    nombre: str
    icono: str
    color: str
    descripcion: str
    depende_de: List[str] = field(default_factory=list)
    timeout_segundos: int = 300
    reintentos: int = 1


PIPELINE_CONFIG = [
    AgentConfig(
        nombre="Buscador", icono="🔍", color="#00b4d8",
        descripcion="Búsqueda bibliográfica en PubMed, Semantic Scholar y CrossRef",
        depende_de=[], timeout_segundos=60,
    ),
    AgentConfig(
        nombre="Analizador", icono="🔬", color="#9d4edd",
        descripcion="Análisis PICO-S y nivel de evidencia CEBM por paper",
        depende_de=["Buscador"], timeout_segundos=300,
    ),
    AgentConfig(
        nombre="Meta-Analista", icono="📊", color="#f77f00",
        descripcion="Síntesis global y grado de recomendación GRADE",
        depende_de=["Analizador"], timeout_segundos=120,
    ),
    AgentConfig(
        nombre="Redactor", icono="📝", color="#2dc653",
        descripcion="Apunte clínico completo en formato Word",
        depende_de=["Meta-Analista", "Analizador"], timeout_segundos=300,
    ),
    AgentConfig(
        nombre="Presentador", icono="🎨", color="#ff4d6d",
        descripcion="Presentación PowerPoint profesional con 18+ slides",
        depende_de=["Meta-Analista"], timeout_segundos=300,
    ),
]


def validar_pipeline(config):
    nombres = {a.nombre for a in config}
    for agente in config:
        for dep in agente.depende_de:
            assert dep in nombres, f"{agente.nombre} depende de '{dep}' que no existe"
    print(f"Pipeline válido: {len(config)} agentes")
    for a in config:
        deps = f" <- {a.depende_de}" if a.depende_de else " (primero)"
        print(f"  {a.icono} {a.nombre}{deps}")
    return True


validar_pipeline(PIPELINE_CONFIG)
""",
        "expected_output_contains": ["Pipeline válido", "Buscador", "Analizador", "Meta-Analista", "Presentador"],
        "requires_api_key": False,
    },
    {
        "id": "m5s2",
        "module": 5,
        "module_title": "Proyecto Final: Replica el Sistema Bruno",
        "step": 2,
        "title": "Implementando el Servidor FastAPI con SSE",
        "description": "Conecta todos los agentes en un servidor FastAPI con streaming en tiempo real. Este es el patrón exacto que usa Bruno en producción.",
        "concept_html": """
<p>El servidor FastAPI de Bruno usa <strong>Server-Sent Events (SSE)</strong> para transmitir el progreso de cada agente al frontend en tiempo real:</p>
<ol>
  <li>El frontend hace <code>POST /api/run</code> y recibe un <code>session_id</code></li>
  <li>Abre un stream con <code>GET /api/stream/{session_id}</code></li>
  <li>El pipeline corre en un hilo separado y emite eventos al <code>queue.Queue</code></li>
  <li>El endpoint SSE lee la cola y transmite cada evento como JSON</li>
</ol>
<p>Este patrón permite que el usuario vea cada paso del pipeline mientras ocurre.</p>
""",
        "diagram_type": "pipeline",
        "starter_code": """import asyncio
import json
import queue
import uuid
from concurrent.futures import ThreadPoolExecutor

# Simula el framework FastAPI en modo demo
class FakeSSEServer:
    def __init__(self):
        self.sesiones = {}  # session_id -> {"queue": Queue, "status": str}
        self.executor = ThreadPoolExecutor(max_workers=4)

    def iniciar_pipeline(self, tema, max_papers=10):
        """Equivalente a POST /api/run en FastAPI."""
        session_id = str(uuid.uuid4())[:8]
        q = queue.Queue()
        self.sesiones[session_id] = {"queue": q, "status": "corriendo"}

        # Inicia el pipeline en un hilo separado
        import threading
        hilo = threading.Thread(
            target=self._ejecutar_pipeline,
            args=(session_id, tema, max_papers, q),
            daemon=True
        )
        hilo.start()
        return session_id

    def _ejecutar_pipeline(self, session_id, tema, max_papers, q):
        """Corre el pipeline y emite eventos al queue."""
        try:
            # TODO: Emite evento agent_start para "Buscador"
            # Formato: q.put({"tipo": "agent_start", "agente": "Buscador", "icono": "🔍"})

            # TODO: Simula trabajo del Buscador (busca 'max_papers' papers)
            # Emite agent_log para cada paper encontrado
            # Emite agent_complete con summary f"{max_papers} papers encontrados"

            # TODO: Repite para Analizador, Meta-Analista (simplificado, sin output real)

            # TODO: Emite pipeline_complete al final
            pass

        except Exception as e:
            q.put({"tipo": "error", "mensaje": str(e)})
        finally:
            q.put(None)  # sentinel

    def leer_eventos(self, session_id):
        """Lee todos los eventos del queue (equivale a GET /api/stream/{id})."""
        q = self.sesiones[session_id]["queue"]
        print(f"\nEscuchando stream de sesión {session_id}...\n")
        while True:
            evento = q.get(timeout=10)
            if evento is None:
                print("\n[Stream terminado]")
                break
            print(f"data: {json.dumps(evento, ensure_ascii=False)}")


# Prueba el servidor
servidor = FakeSSEServer()
sid = servidor.iniciar_pipeline("cirugía laparoscópica pediátrica", max_papers=5)
import time; time.sleep(0.1)  # espera que el hilo inicie
servidor.leer_eventos(sid)
""",
        "solution_code": """import asyncio
import json
import queue
import uuid
import threading
import time
from concurrent.futures import ThreadPoolExecutor


class FakeSSEServer:
    def __init__(self):
        self.sesiones = {}
        self.executor = ThreadPoolExecutor(max_workers=4)

    def iniciar_pipeline(self, tema, max_papers=10):
        session_id = str(uuid.uuid4())[:8]
        q = queue.Queue()
        self.sesiones[session_id] = {"queue": q, "status": "corriendo"}
        hilo = threading.Thread(target=self._ejecutar_pipeline, args=(session_id, tema, max_papers, q), daemon=True)
        hilo.start()
        return session_id

    def _emit(self, q, tipo, **kw):
        q.put({"tipo": tipo, **kw})

    def _ejecutar_pipeline(self, session_id, tema, max_papers, q):
        try:
            # Buscador
            self._emit(q, "agent_start", agente="Buscador", icono="🔍", color="#00b4d8")
            papers = [{"titulo": f"{tema} - Paper #{i}"} for i in range(max_papers)]
            for p in papers:
                self._emit(q, "agent_log", agente="Buscador", mensaje=f"Encontrado: {p['titulo'][:50]}")
            self._emit(q, "agent_complete", agente="Buscador", resumen=f"{max_papers} papers encontrados")

            # Analizador
            self._emit(q, "agent_start", agente="Analizador", icono="🔬", color="#9d4edd")
            self._emit(q, "agent_log", agente="Analizador", mensaje=f"Analizando {max_papers} papers con PICO-S...")
            self._emit(q, "agent_complete", agente="Analizador", resumen=f"{max_papers} papers analizados")

            # Meta-Analista
            self._emit(q, "agent_start", agente="Meta-Analista", icono="📊", color="#f77f00")
            self._emit(q, "agent_log", agente="Meta-Analista", mensaje="Sintetizando evidencia global...")
            self._emit(q, "agent_complete", agente="Meta-Analista", resumen="Nivel evidencia: 1a | Grado: A")

            # Pipeline completo
            self._emit(q, "pipeline_complete", tema=tema, total_papers=max_papers)
            self.sesiones[session_id]["status"] = "completado"

        except Exception as e:
            q.put({"tipo": "error", "mensaje": str(e)})
        finally:
            q.put(None)

    def leer_eventos(self, session_id):
        q = self.sesiones[session_id]["queue"]
        print(f"\nEscuchando stream de sesión {session_id}...\n")
        while True:
            evento = q.get(timeout=10)
            if evento is None:
                print("\n[Stream terminado]")
                break
            print(f"data: {json.dumps(evento, ensure_ascii=False)}")


servidor = FakeSSEServer()
sid = servidor.iniciar_pipeline("cirugía laparoscópica pediátrica", max_papers=5)
time.sleep(0.1)
servidor.leer_eventos(sid)
""",
        "expected_output_contains": ["agent_start", "Buscador", "agent_complete", "pipeline_complete"],
        "requires_api_key": False,
    },
    {
        "id": "m5s3",
        "module": 5,
        "module_title": "Proyecto Final: Replica el Sistema Bruno",
        "step": 3,
        "title": "Testing y Despliegue",
        "description": "Último paso: aprende a testear sistemas multi-agente con mocks y guía de despliegue en Railway o Render (tier gratuito).",
        "concept_html": """
<p>Testear sistemas multi-agente requiere <strong>aislar</strong> el LLM con mocks. Principios clave:</p>
<ul>
  <li><code>unittest.mock.patch</code>: reemplaza funciones reales con fakes deterministas</li>
  <li>Prueba el <strong>flujo</strong>, no el output del LLM (que varía)</li>
  <li>Prueba los <strong>casos borde</strong>: API caída, timeout, papers duplicados</li>
</ul>
<p>Para despliegue: Railway y Render tienen tier gratuito compatible con FastAPI. Solo necesitas un <code>Procfile</code> o configuración de comando de inicio.</p>
""",
        "diagram_type": "none",
        "starter_code": """import unittest
from unittest.mock import patch, MagicMock


# Código a testear (simulado para este ejercicio)
class AgenteBuscador:
    def buscar(self, query, max_results=10):
        # En producción llamaría a PubMed API
        import requests
        r = requests.get(f"https://pubmed.ncbi.nlm.nih.gov/?query={query}")
        return r.json()

    def deduplicar(self, papers):
        vistos = set()
        unicos = []
        for p in papers:
            if p["titulo"] not in vistos:
                vistos.add(p["titulo"])
                unicos.append(p)
        return unicos


# Test 1: ya implementado como ejemplo
class TestDeduplicacion(unittest.TestCase):
    def test_elimina_duplicados(self):
        agente = AgenteBuscador()
        papers = [
            {"titulo": "Paper A", "fuente": "pubmed"},
            {"titulo": "Paper B", "fuente": "semantic"},
            {"titulo": "Paper A", "fuente": "crossref"},  # duplicado
        ]
        resultado = agente.deduplicar(papers)
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0]["titulo"], "Paper A")
        print("Test 1 PASADO: deduplicación funciona correctamente")


# TODO: Test 2 - TestBusquedaConMock
# Usa @patch('requests.get') para mockear la API de PubMed
# El mock debe retornar MagicMock con .json() = [{"titulo": "Paper Mock"}]
# Verifica que buscar() retorna la lista del mock SIN hacer HTTP real
class TestBusquedaConMock(unittest.TestCase):
    pass  # TODO: implementa test_busqueda_usa_requests


# TODO: Test 3 - TestPipelineConFallo
# Simula que requests.get lanza ConnectionError
# Verifica que el agente maneja el error gracefully (retorna lista vacía o lanza ValueError)
class TestPipelineConFallo(unittest.TestCase):
    pass  # TODO: implementa test_maneja_api_caida


if __name__ == "__main__":
    # Corre todos los tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestDeduplicacion))
    suite.addTests(loader.loadTestsFromTestCase(TestBusquedaConMock))
    suite.addTests(loader.loadTestsFromTestCase(TestPipelineConFallo))
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    print(f"\nTests pasados: {resultado.testsRun - len(resultado.failures) - len(resultado.errors)}/{resultado.testsRun}")
""",
        "solution_code": """import unittest
from unittest.mock import patch, MagicMock


class AgenteBuscador:
    def buscar(self, query, max_results=10):
        import requests
        r = requests.get(f"https://pubmed.ncbi.nlm.nih.gov/?query={query}")
        return r.json()

    def deduplicar(self, papers):
        vistos = set()
        unicos = []
        for p in papers:
            if p["titulo"] not in vistos:
                vistos.add(p["titulo"])
                unicos.append(p)
        return unicos


class TestDeduplicacion(unittest.TestCase):
    def test_elimina_duplicados(self):
        agente = AgenteBuscador()
        papers = [
            {"titulo": "Paper A", "fuente": "pubmed"},
            {"titulo": "Paper B", "fuente": "semantic"},
            {"titulo": "Paper A", "fuente": "crossref"},
        ]
        resultado = agente.deduplicar(papers)
        self.assertEqual(len(resultado), 2)
        print("Test 1 PASADO: deduplicación funciona correctamente")


class TestBusquedaConMock(unittest.TestCase):
    @patch('requests.get')
    def test_busqueda_usa_requests(self, mock_get):
        mock_get.return_value = MagicMock()
        mock_get.return_value.json.return_value = [{"titulo": "Paper Mock"}]

        agente = AgenteBuscador()
        resultado = agente.buscar("multi-agent AI")

        mock_get.assert_called_once()  # verifica que llamó a requests.get
        self.assertEqual(resultado, [{"titulo": "Paper Mock"}])
        print("Test 2 PASADO: busqueda llama a requests.get correctamente")


class TestPipelineConFallo(unittest.TestCase):
    @patch('requests.get', side_effect=ConnectionError("API caida"))
    def test_maneja_api_caida(self, mock_get):
        agente = AgenteBuscador()
        try:
            agente.buscar("cualquier query")
            # Si no lanza excepción, el agente debería retornar lista vacía
            self.fail("Debería haber lanzado excepción")
        except ConnectionError:
            print("Test 3 PASADO: ConnectionError propagada correctamente")
        except Exception as e:
            self.fail(f"Excepción inesperada: {e}")


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestDeduplicacion))
    suite.addTests(loader.loadTestsFromTestCase(TestBusquedaConMock))
    suite.addTests(loader.loadTestsFromTestCase(TestPipelineConFallo))
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    print(f"\nTests pasados: {resultado.testsRun - len(resultado.failures) - len(resultado.errors)}/{resultado.testsRun}")
""",
        "expected_output_contains": ["Test 1 PASADO", "Test 2 PASADO", "Test 3 PASADO", "Tests pasados"],
        "requires_api_key": False,
    },
]
