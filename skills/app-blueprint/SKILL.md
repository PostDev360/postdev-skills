---
name: app-blueprint
description: Use this skill when a user wants to start building a new app, product, or feature and the requirements are not yet clear — phrases like "I want to build an app", "help me create a project", "let's start a new app", "I have an idea for a tool", or when a user jumps straight to asking for code/architecture for a project that has no defined scope yet. It runs a short, plain-language interview to pin down the essential product decisions BEFORE any code or architecture is proposed, so the assistant never silently guesses scope, data model, users, or trade-offs on the user's behalf. Skip this skill if the user already provided a clear written spec, or explicitly asks to skip discovery.
---

# App Blueprint

## Purpose

Non-technical founders and early-stage builders often ask an AI assistant to "build my app" without realizing how many architectural decisions get made — silently — on their behalf along the way. This skill forces those decisions into the open first, as a short conversation in plain language, so the person making the product owns the trade-offs instead of the AI guessing them.

The output is a written brief the user can read and correct, which then becomes the foundation for any architecture or implementation work.

## Core rule

**Never let a technical decision get made by default.** If a question below would normally be answered by a developer's judgment call (e.g. "does this need user accounts?", "should data survive a restart?", "one platform or several?"), it must be answered by the user in this interview — not inferred silently, even when the "obvious" answer seems obvious.

If the user's answer to a question doesn't resolve a downstream decision, ask a follow-up. Do not fill the gap with an assumption.

## Communication style

Keep every report, status update, and summary short and to the point, both during the interview and throughout any implementation work that follows the confirmed brief. Skip restating context the user already knows, and avoid padding explanations — this keeps token usage low across a long build. Brevity applies to the assistant's own commentary, not to the substance of the questions asked or the brief itself.

Run the interview and write the brief in **the language the user is writing in**. Match their language for the questions, the answer options, and the brief itself.

## Implementation principle: build in independent blocks

Once the brief is confirmed and implementation begins, structure the application as independent, loosely-coupled blocks (modules/components/files scoped to one feature or responsibility each), instead of a single tangled codebase. The goal: adding or removing a feature later should require touching only its own block, not rewriting shared code across the app. Apply this principle to all follow-up work under the brief, not just the initial build.

## How to run the interview

1. Ask questions in plain language a non-developer would understand. Translate technical concepts into their real-world consequence instead of using jargon.
   - Bad: "Do you need persistent storage?"
   - Good: "If someone closes the app and comes back tomorrow, should their information still be there?"
2. Ask in small batches (3–4 related questions at a time), not one long questionnaire.
   - When a question has a small set of concrete answers, use the `AskUserQuestion` tool so the user can pick instead of type. Give every option a short label plus a one-line description of what choosing it means in practice — e.g. label "Accounts required", description "People sign up, and each person only sees their own data."
   - When the answer is free-form ("what problem does this solve?"), ask it conversationally instead.
   - Never dump a batch of open questions as a wall of text; introduce them with one line of context.
3. Go through the categories below in order. Skip a category only if the user's own words already answered it unambiguously.
4. Keep track of the answers as you go. If a new answer contradicts an earlier one, say so in one sentence and ask which one holds — do not silently pick the more recent.
5. After all categories are covered, write the **Project Brief** (see below) and show it to the user for confirmation/correction before proposing any architecture or writing any code.

## Question categories

### 1. Purpose & audience
- In one or two sentences, what problem does this solve, and who is it for?
- Is there an existing app or tool this resembles or should improve on? ("kind of like X, but for Y")

### 2. People & access
- Will different people need to log in with their own account, or is this for one person / one internal team?
- Are there different kinds of users with different permissions (e.g. an admin vs. a regular visitor vs. a customer)?

### 3. Information & memory
- What information does the app need to remember from one visit to the next (e.g. profiles, history, uploaded files, settings)?
- Is any of that information sensitive (health, payment, government ID, private messages)?

### 4. Where and how it's used
- Where will people use this: a web browser, a phone app, a desktop program, or more than one?
- Does it need to work without an internet connection?

### 5. Scope & priority
- What are the 2–3 things this absolutely cannot ship without?
- What would be nice to have later, but isn't required for a first version?

### 6. Practical constraints
- Is there a budget, a required hosting provider, or an existing tool/company this must integrate with?
- Roughly how many people will use this, and how often (10 people once a week? 10,000 people daily)?
- Is there a deadline?

### 7. Integrations & look
- Does this need to connect to any other service (payments, email, calendar, another piece of software you already use)?
- Is there an existing visual identity (logo, colors, brand) to follow, or is that open?

## Writing the Project Brief

Read `references/brief-template.md` for the exact sections and formatting rules, then fill it in from the user's answers. Keep each bullet to one line, in the user's own words wherever possible.

**Write the brief to `PROJECT_BRIEF.md` at the root of the project directory** — not only into the chat. It is the source of truth for every later scope decision, so it has to outlive the conversation. If that file already exists, read it and update it rather than overwriting it from scratch.

End the brief with an **Open questions** section listing anything still unresolved. Do not proceed to architecture or code while that section is non-empty — ask the missing questions instead.

Present the brief to the user and ask them to confirm or correct it before moving on.

## When to stop using this skill

Once the user confirms the brief, this skill's job is done — proceed with normal architecture/implementation work, treating `PROJECT_BRIEF.md` as the source of truth for scope decisions. Don't re-run the interview for small follow-up features unless they introduce a new decision category above (e.g. adding payments later should trigger the relevant integration question); in that case ask only what that category raises and append the answers to the existing brief. The communication style and modular-blocks principles above still apply after this handoff.
