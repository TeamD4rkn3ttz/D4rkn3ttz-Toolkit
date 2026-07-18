# Contributing to TEAM_D4rkn3ttz Toolkit

Thank you for helping improve this defensive threat intelligence toolkit.

## Before you begin

- Use the issue tracker for reproducible defects, focused enhancements, and proposed skills.
- Do not include personal data, credentials, malware, stolen datasets, confidential evidence, or links that grant unauthorized access.
- Report security vulnerabilities privately as described in [SECURITY.md](SECURITY.md).
- Keep the Korean and English skill packages independently usable.

## Development workflow

1. Fork the repository and create a focused branch from `main`.
2. Make the smallest coherent change.
3. Update the relevant language package. If the behavior should match in both packages, update and review both without requiring literal translation.
4. Use relative links for repository files and pin external claims to authoritative sources.
5. Run:

   ```sh
   python3 scripts/validate_skills.py
   ```

6. Open a pull request using the repository template.

## Skill requirements

Each language package must contain:

- a `SKILL.md` with YAML frontmatter containing only `name` and `description`;
- a unique lowercase, hyphenated skill name;
- a concise trigger-oriented description;
- imperative instructions that distinguish claims, observations, assessments, and unknowns; and
- the required files in `references/`.

Do not add package-level README, changelog, or installation files. Repository-level documentation belongs at the repository root.

## Pull requests

Pull requests should explain the problem, the chosen approach, the affected language packages, and validation performed. Keep unrelated changes separate. By submitting a contribution, you agree that it is licensed under the repository's [Apache License 2.0](LICENSE).
