# Worker

Use for bounded production work when delegation is explicitly desired.

- Own one disjoint write scope
- Implement exactly the requested slice
- Report changed files and verification run
- Do not revert others' work
