# Project guidance

## Overview

- This is a small Flask login and registration application.
- Application code lives under `src/`: routes and startup in `app.py` and `index.py`, business rules in `services/`, in-memory persistence in `repositories/`, and Jinja templates in `templates/`.
- Browser acceptance tests use Robot Framework and live in `src/tests/`. Shared browser settings and keywords are in `src/tests/resource.robot`.
- Dependencies are managed with `uv` through `pyproject.toml` and `uv.lock`.

## Development

- Install dependencies with `uv sync`.
- Start the app from the repository root with `uv run python src/index.py`. It listens on port 5001.
- Robot browser tests expect the app to be running at `http://localhost:5001` and use the Browser library. Run a suite from the repository root with `uv run robot src/tests/<suite>.robot`.
- Test setup resets the in-memory user repository through `/tests/reset`; do not rely on users persisting between test cases or app restarts.

## Implementation conventions

- Keep credential and registration validation in `UserService` (`src/services/user_service.py`), especially `validate` for registration rules.
- Keep persistence operations in `UserRepository`; route handlers should delegate business logic to `UserService`.
- When adding routes or changing form behavior, update the relevant Jinja template and Robot acceptance coverage.
- Put shared Robot Framework keywords and configuration in `resource.robot`; keep suite-specific setup and checks in the relevant suite.
- Preserve the existing simple Flask/Jinja and Robot Framework style. Avoid adding dependencies unless needed.
