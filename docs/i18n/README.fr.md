# PostDev Skills

Skills open-source pour [Claude Code](https://claude.com/claude-code), conçus pour celles et ceux qui livrent de vrais produits.

[![Licence : MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../LICENSE)
[![Skills](https://img.shields.io/badge/skills-1-green.svg)](#skills)
[![PRs bienvenues](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](../../CONTRIBUTING.md)
[![ko-fi](https://img.shields.io/badge/support-ko--fi-ff5e5b.svg)](https://ko-fi.com/postdev360)

**Lire dans une autre langue :** [English](../../README.md) · [中文](README.zh.md) · [Español](README.es.md)

---

## Skills

| Skill | Rôle |
| --- | --- |
| [**app-blueprint**](../../skills/app-blueprint/) | Mène une courte interview de découverte en langage simple *avant* toute proposition de code ou d'architecture pour une nouvelle app, un produit ou une fonctionnalité — puis rédige un `PROJECT_BRIEF.md` que vous validez. |

## Installation

Chaque skill est un dossier autonome. Copiez ceux que vous voulez dans votre répertoire de skills.

**Pour un seul projet** — le skill n'est disponible que dans ce projet, et peut être versionné avec lui :

```bash
mkdir -p .claude/skills
git clone --depth 1 https://github.com/PostDev360/postdev-skills.git /tmp/postdev-skills
cp -r /tmp/postdev-skills/skills/app-blueprint .claude/skills/
rm -rf /tmp/postdev-skills
```

**Pour tous vos projets** — le skill est disponible partout :

```bash
mkdir -p ~/.claude/skills
git clone --depth 1 https://github.com/PostDev360/postdev-skills.git /tmp/postdev-skills
cp -r /tmp/postdev-skills/skills/app-blueprint ~/.claude/skills/
rm -rf /tmp/postdev-skills
```

Lancez ensuite Claude Code et tapez `/skills` pour vérifier qu'il est bien chargé. Les skills se déclenchent automatiquement quand votre demande correspond à leur description — vous pouvez aussi en invoquer un par son nom.

## app-blueprint

### Pourquoi ce skill existe

Les porteurs de projet non-techniques demandent souvent à un assistant IA de « construire leur app » sans réaliser combien de décisions sont prises silencieusement en chemin : faut-il des comptes utilisateurs, les données doivent-elles persister, quelles plateformes cibler, quel est le vrai périmètre de la v1. App Blueprint force ces décisions à être posées explicitement, sous forme de conversation, afin que ce soit le porteur du produit — et non l'IA — qui arbitre ces choix.

### Quand il se déclenche

Automatiquement, dès que vous voulez démarrer une nouvelle app/produit/fonctionnalité dont les besoins ne sont pas encore clairs (« je veux créer une app », « aide-moi à créer un projet », « j'ai une idée d'outil »), ou lorsque vous demandez directement du code sans périmètre défini. Le skill s'efface si vous avez déjà fourni un cahier des charges clair, ou demandez explicitement à sauter cette étape.

### Comment il fonctionne

1. Pose des questions en langage simple, en traduisant les choix techniques en conséquences concrètes — par ex. *« si la personne ferme l'app et revient demain, ses informations doivent-elles toujours être là ? »* au lieu de *« avez-vous besoin d'un stockage persistant ? »*
2. Pose les questions par petits groupes de 3-4, jamais un long questionnaire, avec des choix multiples quand les réponses sont concrètes.
3. Couvre sept catégories dans l'ordre : but & public, utilisateurs & accès, informations & mémoire, lieu/mode d'usage, périmètre & priorités, contraintes pratiques, intégrations & identité visuelle — une catégorie n'est sautée que si elle a déjà été couverte sans ambiguïté.
4. Rédige un **Project Brief** dans `PROJECT_BRIEF.md` et vous demande de le confirmer ou de le corriger avant toute architecture ou tout code.
5. Fonctionne dans la langue dans laquelle vous écrivez.

### Après la validation du brief

Deux principes se poursuivent pendant la construction :

- **Rapports concis** — les points d'avancement et résumés restent courts tout au long du projet, afin de limiter la consommation de tokens sur un projet long.
- **Construction modulaire par blocs** — l'application est structurée en modules indépendants et faiblement couplés, de sorte qu'ajouter ou supprimer une fonctionnalité ne touche que son propre bloc, pas l'ensemble du code.

### Résultat

Un Project Brief validé et écrit, qui devient la référence pour tout le travail d'implémentation qui suit.

## Contribuer

Les contributions sont bienvenues — nouveaux skills, améliorations des skills existants, traductions et rapports de bugs. Commencez par [CONTRIBUTING.md](../../CONTRIBUTING.md), et consultez le [Code de conduite](../../CODE_OF_CONDUCT.md).

## Licence

[MIT](../../LICENSE) © PostDev360

## Soutenir le projet

Si ces skills vous font gagner du temps, vous pouvez soutenir leur développement sur [Ko-fi](https://ko-fi.com/postdev360).
