# 🤖 Global Agent Rules & Guidelines (Antigravity)

Este archivo define las directrices del sistema y las restricciones pasivas (Rules) de desarrollo para **Antigravity** y otros agentes de IA en este espacio de trabajo. Estas reglas deben ser seguidas estrictamente en todas las interacciones y modificaciones de código.

---

## 👑 Mandatory Rules (Reglas Mandatorias)

1. **La Firma ("ok, jefecito"):**
   Al final de **CADA RESPUESTA**, sin excepción, debes escribir exactamente en una línea limpia:
   ```text
   ok, jefecito
   ```
   > [!IMPORTANT]
   > Esta regla es de máxima prioridad. Si respondes sin esta frase al final, se considerará que has fallado la instrucción fundamental.

2. **Acuerdo Conceptual Previo:**
   No escribas código complejo ni generes archivos masivos de manera unilateral. Primero propón la idea conceptual en el chat, discútela con el usuario y, una vez que haya un acuerdo explícito, procede con la implementación.

3. **Control de Ramas (`main` Branch Protection):**
   Nunca realices o propongas fusiones (merges) o subidas directas a la rama `main` sin antes explicar detalladamente qué cambios se subirán y obtener la aprobación directa y explícita del usuario.

---

## 🛡️ Strict Security Guidelines (DevSecOps)

Para mitigar ataques de cadena de suministro y garantizar un entorno de desarrollo seguro, se aplican las siguientes directrices estrictas:

1. **Uso Exclusivo de `pnpm`:**
   * Está estrictamente prohibido usar o recomendar comandos basados en `npm` o `yarn` (como `npm install` o `yarn add`).
   * Toda la gestión de dependencias debe realizarse exclusivamente con **pnpm (versión 11 o superior)**.

2. **Políticas de Compilación Segura:**
   * **Quarantine Window:** Evita instalar paquetes publicados hace menos de 24 horas (`minimum-release-edge=1440`).
   * **Block Exotic Sub-dependencies:** Bloquea dependencias de terceros no confiables o exóticas (`block-exotic-sub-dependencies=true`).
   * **Ignore Scripts:** Evita la ejecución automática de scripts potencialmente maliciosos (`preinstall` / `postinstall`) durante la instalación usando siempre la bandera `--ignore-scripts`.

3. **Zero Hardcoded Credentials:**
   * Nunca expongas tokens de API, llaves secretas o credenciales de base de datos en el código fuente.
   * Toda la configuración debe realizarse a través de variables de entorno mediante un archivo seguro `.env`.

---

## 🏗️ Architecture & Clean Code

El backend actúa como un robusto BFF (Backend for Frontend), y el frontend es modular y dinámico.

### 🐍 Backend & Persistence (MySQL)
* Arquitectura Limpia / Patrones DDD con tipado estricto.
* ORM / Frameworks: TypeScript con Prisma ORM, o Python con FastAPI y esquemas Pydantic.
* **Esquema de Base de Datos MySQL:**
  * `Level`: id, name (A1-C2), description.
  * `Lesson`: id, level_id, type ('grammar' o 'phonetics'), title, explanation.
  * `Example`: id, lesson_id, english_phrase, spanish_translation, ipa_transcription (usando el Alfabeto Fonético Internacional).
  * `Exercise`: id, lesson_id, question, correct_answer.
* Mantén un directorio limpio y modular para futuras integraciones de IA en `services/ai/`.

### 🅰️ Frontend (Angular 17+ / Standalone)
* Enrutamiento dinámico y escalable con carga diferida (Lazy Loading) por nivel mediante parámetros de ruta (`/level/:levelId`). **No hardcodear** vistas por nivel.
* **Componentes Limpios:** Mantén los archivos de código fuente por debajo de **200–300 líneas de código**. Si un componente crece más allá de esto, modularízalo en componentes reutilizables o servicios de utilidad.
* **Preparación de UI:** Muestra la frase en inglés, su traducción e IPA en las tarjetas de ejemplos. Deja los botones visuales para "Listen" y "Record Audio" (preparados para futuras fases de audio), pero sin lógica activa o marcados como deshabilitados/placeholders para no romper el diseño.

---

## 🧪 Testing, QA & TDD (Quality Assurance)

La calidad del código es innegociable en este proyecto. Seguimos una filosofía de desarrollo orientada a pruebas (Test-First / TDD):

1. **Cobertura Mínima:** Todo código funcional nuevo debe tener o superar un **80% de cobertura de pruebas** (tanto cobertura de líneas como de ramas).
2. **Test-First Generation:** Antes de generar lógica de negocio o componentes complejos, debes escribir y proponer el archivo de prueba correspondiente (ej. `.spec.ts` o `test_*.py`).
3. **Verificación Continua:** Después de proponer cualquier cambio funcional, ejecuta o indica explícitamente el comando para correr las pruebas (`pnpm test`) y verificar que pasen.
4. **Protección contra Regresiones:** Ninguna propuesta de código debe romper pruebas existentes. Asegúrate de incluir pruebas tanto para flujos exitosos ("Happy Paths") como para manejo de errores (ej. límites o fallos de conexión).

---

## ✍️ Interaction Workflow

* **Idioma de Comunicación:** Aunque estas instrucciones y el backend puedan estar en inglés, la comunicación con el usuario y las explicaciones/comentarios de código deben ser redactados en **español**.
* **Language Protocol for UI vs Content:** Card titles and descriptions (description) are ALWAYS 100% English to maintain UI consistency. Deep theoretical explanations and grammar/phonetics rules should be handled inside the lesson's internal content or translation fields, NOT in the overview.
* **Precisión de Datos:** Al generar semillas (seeds) o datos de prueba, básate estrictamente en metodologías de referencia de Cambridge (Essential/Intermediate/Advanced Grammar and Vocabulary in Use) y estructuras fonéticas oficiales de la IPA.
* **Gestión de Librerías:** Si propones una nueva librería de terceros, debes validar su legitimidad y documentar exactamente su instalación usando `pnpm add --ignore-scripts`.
