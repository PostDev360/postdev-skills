# PostDev Skills

Skills de código abierto para [Claude Code](https://claude.com/claude-code), pensados para quienes lanzan productos reales.

[![Licencia: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../LICENSE)
[![Skills](https://img.shields.io/badge/skills-1-green.svg)](#skills)
[![PRs bienvenidos](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](../../CONTRIBUTING.md)
[![ko-fi](https://img.shields.io/badge/support-ko--fi-ff5e5b.svg)](https://ko-fi.com/postdev360)

**Leer en otro idioma:** [English](../../README.md) · [Français](README.fr.md) · [中文](README.zh.md)

---

## Skills

| Skill | Qué hace |
| --- | --- |
| [**app-blueprint**](../../skills/app-blueprint/) | Realiza una breve entrevista de descubrimiento en lenguaje sencillo *antes* de proponer código o arquitectura para una nueva app, producto o funcionalidad — y luego escribe un `PROJECT_BRIEF.md` que tú confirmas. |

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

## Contribuir

Las contribuciones son bienvenidas — nuevos skills, mejoras a los existentes, traducciones e informes de errores. Empieza por [CONTRIBUTING.md](../../CONTRIBUTING.md), y consulta el [Código de Conducta](../../CODE_OF_CONDUCT.md).

## Licencia

[MIT](../../LICENSE) © PostDev360

## Apoya el proyecto

Si estos skills te ahorran tiempo, puedes apoyar su desarrollo en [Ko-fi](https://ko-fi.com/postdev360).
