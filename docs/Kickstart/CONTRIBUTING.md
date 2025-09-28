# Contributing to LangOne

Welcome! 🎉 Thanks for your interest in helping build LangOne.

## Code of Conduct
Be kind and respectful. We are building a welcoming, global community.  
(We’ll add a formal Code of Conduct file soon; for now, follow the spirit of the Contributor Covenant.)

## How Can I Help?
- **Specs & Design**: Discuss syntax, type system, runtime, and standard library.
- **Compiler/VM**: Tokenizer, parser, AST/IR, bytecode VM, AOT (LLVM) later.
- **Tooling**: VS Code LSP extension, CLI, package manager.
- **Cloud/IaC**: Terraform/Pulumi emitters, pipeline generators.
- **AI/ML**: ONNX runtime wrappers, training/deploy helpers.
- **Docs & Examples**: Tutorials, samples, guides.

## Development Setup
- Toolchain: Any modern environment (we’ll standardize soon).
- Editor: VS Code recommended.
- Language: Early prototypes may be in **Python/Rust/C#** (choose what you’re most productive in).
- Open an issue if setup is unclear; we’ll improve docs quickly.

## Branching & PRs
- Create feature branches from `main`: `feature/<short-description>`
- Keep PRs small and focused.
- Add tests where feasible.
- Link issues in PR description (e.g., “Fixes #42”).

## Commit Messages (Conventional Commits)
- `feat: add parser for routes`
- `fix: correct tokenizer handling of strings`
- `docs: add HelloWorld.l1 example`
- `chore: format codebase`
- `test: add parser unit tests`

## Issues
- Use labels: `good first issue`, `help wanted`, `spec`, `compiler`, `tooling`, `docs`.
- If you file a bug, include steps to reproduce and expected behavior.

## Security
- Report vulnerabilities privately via email (to be added) or private issue.
- We will add a SECURITY.md with coordinated disclosure soon.

## License
Unless otherwise noted, contributions are under **Apache‑2.0** for core repos.
