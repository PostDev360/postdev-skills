# PostDev Skills

Skills de código abierto para [Claude Code](https://claude.com/claude-code), pensados para quienes lanzan productos reales.

[![Licencia: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../LICENSE)
[![Skills](https://img.shields.io/badge/skills-2-green.svg)](#skills)
[![PRs bienvenidos](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](../../CONTRIBUTING.md)
[![ko-fi](https://img.shields.io/badge/support-ko--fi-ff5e5b.svg)](https://ko-fi.com/postdev360)

**Leer en otro idioma:** [English](../../README.md) · [Français](README.fr.md) · [中文](README.zh.md)

---

## Skills

| Skill | Qué hace |
| --- | --- |
| [**app-blueprint**](../../skills/app-blueprint/) | Realiza una breve entrevista de descubrimiento en lenguaje sencillo *antes* de proponer código o arquitectura para una nueva app, producto o funcionalidad — y luego escribe un `PROJECT_BRIEF.md` que tú confirmas. |
| [**openplaces**](../../skills/openplaces/) | Responde preguntas sobre lugares, direcciones y trayectos a partir de datos abiertos — búsqueda, geocodificación, rutas, isócronas — sin clave de API de pago y sin que las direcciones salgan de la UE. |

## Instalación

Cada skill es una carpeta autónoma. Copia las que quieras a tu directorio de skills.

**Para un solo proyecto** — el skill solo está disponible en ese proyecto, y puede versionarse junto a él:

```bash
mkdir -p .claude/skills
git clone --depth 1 https://github.com/PostDev360/postdev-skills.git /tmp/postdev-skills
cp -r /tmp/postdev-skills/skills/app-blueprint .claude/skills/
rm -rf /tmp/postdev-skills
```

**Para todos tus proyectos** — el skill está disponible en cualquier lugar:

```bash
mkdir -p ~/.claude/skills
git clone --depth 1 https://github.com/PostDev360/postdev-skills.git /tmp/postdev-skills
cp -r /tmp/postdev-skills/skills/app-blueprint ~/.claude/skills/
rm -rf /tmp/postdev-skills
```

Luego inicia Claude Code y ejecuta `/skills` para confirmar que está cargado. Los skills se activan automáticamente cuando tu petición coincide con su descripción — también puedes invocar uno por su nombre.

## app-blueprint

### Por qué existe

Los fundadores no técnicos y creadores en etapa temprana suelen pedirle a un asistente de IA que «construya su app» sin darse cuenta de cuántas decisiones se toman silenciosamente en el camino: si hacen falta cuentas de usuario, si los datos deben persistir, qué plataformas cubrir, cuál es el verdadero alcance de la v1. App Blueprint obliga a que estas decisiones se hagan explícitas primero, como una conversación, para que sea la persona dueña del producto —y no la IA— quien decida sobre esos compromisos.

### Cuándo se activa

Automáticamente, cuando quieres iniciar una nueva app/producto/funcionalidad y los requisitos aún no están claros («quiero crear una app», «ayúdame a crear un proyecto», «tengo una idea para una herramienta»), o cuando pides directamente código sin un alcance definido. El skill se aparta si ya proporcionaste una especificación clara, o pides explícitamente omitir esta etapa.

### Cómo funciona

1. Formula preguntas en lenguaje sencillo, traduciendo las decisiones técnicas en consecuencias reales — p. ej. *«si alguien cierra la app y vuelve mañana, ¿su información debería seguir ahí?»* en lugar de *«¿necesitas almacenamiento persistente?»*
2. Pregunta en tandas pequeñas de 3-4 preguntas relacionadas, nunca un cuestionario largo, usando opciones múltiples cuando las respuestas son concretas.
3. Cubre siete categorías en orden: propósito y público, personas y acceso, información y memoria, dónde y cómo se usa, alcance y prioridades, restricciones prácticas, integraciones y aspecto visual — saltando una categoría solo si ya fue respondida sin ambigüedad.
4. Escribe un **Project Brief** en `PROJECT_BRIEF.md` y te pide que lo confirmes o corrijas antes de escribir cualquier arquitectura o código.
5. Funciona en el idioma en el que escribes.

### Después de confirmar el brief

Dos principios continúan aplicándose durante la construcción:

- **Informes concisos** — las actualizaciones de estado y los resúmenes se mantienen breves durante todo el proyecto, para mantener bajo el consumo de tokens en proyectos largos.
- **Construcción modular por bloques** — la app se estructura en módulos independientes y poco acoplados, de modo que añadir o quitar una funcionalidad más adelante afecte solo a su propio bloque, no a todo el código base.

### Resultado

Un Project Brief confirmado y por escrito, que se convierte en la fuente de verdad para todo el trabajo de implementación posterior.

## openplaces

### Por qué existe

Preguntarle a un asistente «¿dónde está la farmacia más cercana?» o «¿cuáles son las coordenadas de esta dirección?» normalmente implica o bien una clave de Google Places de pago, o bien una respuesta inventada de memoria. Ambas son malas: una cuesta dinero en cada petición, la otra produce direcciones plausibles pero equivocadas, imposibles de distinguir de las correctas. Y para quien maneja direcciones de clientes o pacientes, enviarlas a una API alojada en Estados Unidos es un problema de RGPD, no una preferencia.

Este skill maneja [`openplaces`](https://github.com/PostDev360/openplaces), una CLI que responde a partir de OpenStreetMap, la Base Adresse Nationale francesa y OpenRouteService — gratis, y alojada en Francia y Alemania.

### Requisitos

El comando `openplaces`. El skill comprueba que esté instalado e indica cómo hacerlo:

```bash
uv tool install openplaces-cli    # o: pipx install openplaces-cli
```

### Cuándo se activa

Siempre que una petición involucre un lugar real, una dirección o un trayecto — «dónde está el X más cercano», «geocodifica esta dirección», «qué hay en estas coordenadas», «qué distancia hay entre A y B», «qué puedo alcanzar en 20 minutos», «busca panaderías abiertas cerca de Y» — o cuando pides explícitamente una alternativa a Google Maps.

### Cómo funciona

1. Verifica que la CLI esté instalada y se niega a inventar coordenadas si no lo está — la regla central es que una dirección plausible pero equivocada es peor que ninguna respuesta.
2. Elige el subcomando adecuado (`search`, `resolve`, `reverse`, `details`, `route`, `isochrone`) y lee los resultados en JSON.
3. Trata `open_now` como un valor de tres estados — `true`, `false` o **desconocido** — y comunica lo desconocido como tal, sin redondearlo a «cerrado».
4. Actúa según los códigos de salida por familia de error en lugar de reintentar a ciegas, y se niega a hacer bucles contra las instancias públicas de Overpass.
5. Conoce las particularidades de la Base Adresse Nationale: pondera débilmente el nombre del municipio en texto libre, así que el skill comprueba la puntuación de confianza y recurre a `--postcode` cuando un resultado contradice la ciudad que has nombrado.

### Límites que te comunicará

Sin valoraciones ni reseñas — OpenStreetMap no las alberga, y el skill lo dice en lugar de sustituirlas por sus impresiones sobre negocios concretos. La cobertura es excelente en la Europa urbana y más desigual fuera de ella. `route` da distancia y duración, no navegación paso a paso.

### Resultado

Fichas de lugares, coordenadas o datos de trayecto extraídos de datos abiertos en vivo, señalando la atribución `© colaboradores de OpenStreetMap` siempre que los resultados vayan a difundirse públicamente.

## Contribuir

Las contribuciones son bienvenidas — nuevos skills, mejoras a los existentes, traducciones e informes de errores. Empieza por [CONTRIBUTING.md](../../CONTRIBUTING.md), y consulta el [Código de Conducta](../../CODE_OF_CONDUCT.md).

## Licencia

[MIT](../../LICENSE) © PostDev360

## Apoya el proyecto

Si estos skills te ahorran tiempo, puedes apoyar su desarrollo en [Ko-fi](https://ko-fi.com/postdev360).
