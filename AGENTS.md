# AGENTS.md

This file provides operational guidance for AI assistants working in this repository.

## Project overview

MoyshaBot is a Telegram bot project focused on text conversation, meme-like command responses, and utility features (Markov-based generation, wiki lookups, profanity-style roast responses, voice transcription + translation, and table-driven static commands).

Primary entrypoint and runtime flow:
1. `main.py` creates a `telebot.TeleBot`, loads secrets from environment variables, and wires message handlers.
2. Text messages are routed to `src/converse.py::converse`.
3. Voice messages are routed to `src/transcribe.py::transcribe`, then translated in `src/translate.py::translate`.

## Repository structure

- `main.py`
  - Application entrypoint for Telegram polling and top-level handlers.
- `src/`
  - `converse.py`: central command router for text inputs.
  - `transcribe.py`: Hugging Face Whisper request handling.
  - `translate.py`: Hugging Face translation request handling.
  - `utils.py`: shared API retry helper.
  - `modules/`: feature and utility modules (see below).
- `src/modules/`
  - `otherTools.py`: command helpers (`/roll`, wiki, emoji conversion, static command dispatch, etc.).
  - `markov.py`: Markov chain generator used by conversation commands.
  - `xlsxTools.py`: reads `commands.xlsx` and resolves table-driven responses.
  - `dict_reader.py`: dictionary word loaders for different difficulty/name categories.
  - `aboba.py`: Selenium-based Yandex YaLM integration.
  - `boyan.py`: image hash duplicate detection helper.
  - `zhirik.py`: image+text composition helpers.
  - `face_swap.py`, `faceSwap.py`, `face_detection.py`, `main_video.py`: face-swap/video processing pipeline.
  - `vkTools.py`, `gpt3.py`, `text_gen.py`, `soyjak.py`: legacy/experimental integrations and helpers.
- `dict/`
  - Local datasets and dictionaries used by Markov and helper modules.
  - Also includes `chromedriver` expected by Selenium module.
- `photos/`
  - Static image assets that may be returned by bot commands.
- `commands.xlsx`
  - Spreadsheet-based command/response database read by `xlsxTools.py`.
- `requirements.txt`
  - Python dependency pinning.

## Environment and secrets

Expected env vars:
- `TELEGRAM_TOKEN`: Telegram bot token.
- `HF_TOKEN`: Hugging Face API token for transcription/translation endpoints.

Local files and models expected by specific modules:
- `dict/messages.txt` for Markov generation.
- `dict/chromedriver` for Selenium-based modules.
- `models/shape_predictor_68_face_landmarks.dat` for face-detection/swap pipeline.

## Development workflow

### Setup
1. Create a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Create a `.env` file (or otherwise export required tokens).
4. Run `python main.py`.

### Suggested command checks
- Syntax check: `python -m py_compile main.py src/*.py src/modules/*.py`
- Optional formatting/linting (not currently enforced in repo): run formatter/linter before merge.

### Editing guidance
- Keep command-routing logic in `src/converse.py` concise; move heavy logic into `src/modules/*`.
- Prefer pure helper functions in modules over adding complexity to handler closures in `main.py`.
- Reuse `src/utils.py::send_request` for resilient Hugging Face calls.
- Preserve existing relative file paths unless you also update all call sites.

## Key code conventions and caveats

- This codebase mixes active Telegram logic with legacy/experimental modules. Do not remove legacy files unless explicitly requested.
- Some modules use older APIs (e.g., Selenium calls). When refactoring, prioritize backward-compatible changes unless a migration is requested.
- Most user-facing command handling is Russian-language and string-based; preserve behavior when changing command parsing.
- `commands.xlsx` is a runtime dependency for static command responses.
- Keep imports straightforward (no try/except around imports).

## Testing and validation expectations for agents

When making changes:
1. Run at least syntax validation (`py_compile`) on touched Python files.
2. If logic is modified, run focused functional checks where possible.
3. Report any limitations (missing credentials, unavailable external APIs, unavailable model files).

## Important agent instructions on documentation

- Each new module should have its own DOCUMENTATION.md file, explaining how it works.
- All the core elements and project content should be described in WIKI.md. Both the user and the agent after careful reading of this file should understand ALL the features of the codebase. See this as a through executive summary.
- All the progress should be documented in the file PROGRESS.md. After finishing each feature, the PROGRESS.md file should be updated, so if a user or an agent reads through this file, he should understand what this file is about.
- If the file PROGRESS.md is not created, but the code is already there, the file PROGRESS.md should be created with all the features explained and marked as working/planned, in accordance to the existing documentation.

## Important agent instructions about git usage

- Each feature that should be added, should be added in a separate git branch.
- The naming of the branch should have the following schema: <type_of_branch>/<feature_name>. For example: feature/async_judging
- Types of branches can be: feature, refactor, bugfix and methodology. feature branches add completely new features, refactor branches refactor and/or simplify the code, bugfix are for fixing bugs and methodology branches are for changing methodology of the experiments.
- Each meaningful code change should be formalized into a commit. This change may span multiple files and functions, but it should contain only one TODO item.
- Commit names follow the schema: <type_of_commit>: <description_of_commit>. For example: feat: Added asynchronous querying of the API for the judging
- Types of commits can be: feat, refactor, fix. feat commits are the commits that add new features, refactor are for refactoring of the code without any changes, fix are for bugfixes.
- Unit tests should be added after each branch merge.
- After the feature is finished and tested, the agent should ask whether the branch should be merged into main. If the user agrees, the agent should merge.
- Branches should never break main -- if feature A breaks the main branch, it should not be merged.

## Most important agent instructions on general productivity

- Each TODO list item MUST be committed right after it was checked as completed. Refer to the git usage instructions for commit message format.
- NEVER commit the changes from TODOs in bulk -- only commit them RIGHT AFTER the TODO is checked as completed. This is needed to have TODO lists appear in the commit history, so be sure to strictly follow this rule
- Before merging, the code should be ran through linter and formatter. If any problems arise, they should be fixed before merging.
