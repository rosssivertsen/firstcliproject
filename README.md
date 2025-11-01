# firstcliproject

## Overview

First CLI Project with enterprise-grade automation and change control.

## Features

- **Automated CI/CD Pipeline** with GitHub Actions
- **Change Control System** with branch protection
- **Quality Gates** (Testing, Linting, Security Audits)
- **Automated Deployment** scripts
- **Comprehensive Documentation** with CHANGELOG

## Quick Start

### Development
```bash
npm run dev
```

### Deployment Commands
```bash
npm run deploy              # Quick deploy
npm run pipeline:full       # Full pipeline (dev → staging → prod)
npm run pipeline:direct     # Direct deployment (dev → prod)
npm run promote:staging     # Promote to staging
npm run promote:production  # Promote to production
```

### Quality Commands
```bash
npm run build               # Production build
npm run lint                # Code quality check
npm run test                # Run tests
npm run security            # Security audit
```

## Branch Strategy

```
main (Production) ← staging (UAT) ← development (Integration)
```

### Branch Protection Rules
- **main**: Production releases only
- **staging**: User acceptance testing
- **development**: Active development and integration

## Documentation

- [CHANGELOG.md](./CHANGELOG.md) - Version history
- `/docs` - Technical documentation

## Automation

All automation scripts are located in `/scripts`:
- `deploy.sh` - Environment-specific deployment
- `configure-project.sh` - Project setup

## CI/CD Pipeline

GitHub Actions workflow located at `.github/workflows/ci-cd.yml`:
- Quality gates (linting, testing, security)
- Automated testing
- Staged deployments
- Branch management

## Author

Ross Sivertsen

## License

MIT