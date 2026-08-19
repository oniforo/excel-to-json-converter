# Contributing

Thanks for considering a contribution.

## Getting set up

```bash
git clone https://github.com/oniforo/excel-to-json-converter.git
cd excel-to-json-converter
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Making a change

1. Create a branch off `main`: `git checkout -b feat/short-description`
2. Make your change
3. Run `pylint main.py` locally before opening a PR (see `.pylintrc` for
   the project's rule overrides)
4. Commit with a clear message (Conventional Commits preferred:
   `feat: ...`, `fix: ...`, `docs: ...`, `chore: ...`, `ci: ...`)
5. Open a pull request against `main` and fill in the PR template

## Reporting bugs / requesting features

Use the issue templates — they ask for the details that make an issue
actionable (repro steps, expected vs. actual behavior, environment).

## Questions

Open an issue if you're not sure something counts as a bug.
