# 🤖 Agent System Configuration (.agents)

Este directorio está diseñado para organizar y centralizar las instrucciones, reglas pasivas y flujos de trabajo de los agentes de IA (como **Antigravity**) que interactúan con este repositorio.

## 📂 Estructura de Directorios

El sistema está organizado en tres niveles para facilitar la lectura, el contexto modular y la automatización del agente:

```text
.agents/
├── README.md               # Este archivo explicativo.
├── rules/
│   └── global.md           # Restricciones pasivas, reglas globales de seguridad, TDD y DevSecOps.
├── workflows/              # Secuencias de pasos o comandos automatizados que el agente ejecuta.
└── skills/                 # Habilidades dinámicas empaquetadas en archivos SKILL.md.
```

### 1. ⚙️ Rules (Reglas)
Ubicadas en `.agents/rules/`. Son restricciones pasivas y principios inquebrantables que rigen la conducta y calidad del agente (por ejemplo, directrices de seguridad de pnpm, políticas de protección de ramas, límites de líneas de código por archivo, TDD y firmas obligatorias).

* El archivo principal es [global.md](file:///Users/ropa/Develop/english-coach-app/.agents/rules/global.md).

### 2. 🔄 Workflows (Flujos de Trabajo)
Ubicados en `.agents/workflows/`. Son secuencias estructuradas de pasos que se pueden invocar. Guían al agente a través de flujos específicos como despliegues, migraciones de base de datos o pipelines de testing complejos.

### 3. 🧠 Skills (Habilidades)
Ubicadas en `.agents/skills/`. Son carpetas o archivos `SKILL.md` que detallan cómo resolver problemas específicos paso a paso. El agente puede leerlos bajo demanda cuando el contexto de la tarea lo requiera.

---

## 🧭 Instrucción para el Agente de IA

> [!IMPORTANT]
> **Antes de realizar cualquier acción o escribir código en este repositorio:**
> 1. Lee y asimila las reglas de comportamiento y desarrollo en [global.md](file:///Users/ropa/Develop/english-coach-app/.agents/rules/global.md).
> 2. Aplica estrictamente los estándares de seguridad de dependencias (`pnpm`), el flujo de desarrollo guiado por pruebas (TDD) y los límites de arquitectura del proyecto.
> 3. **Nunca olvides firmar al final de tus respuestas** según lo especificado en la primera sección de las reglas.
