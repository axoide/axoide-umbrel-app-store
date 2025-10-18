# AI Agent Instructions for axoide-umbrel-app-store

## Project Overview
This repository is an Umbrel Community App Store that currently contains the Freqtrade trading bot application. The project follows specific conventions for Umbrel app store integration.

## Key Architecture Components

### 1. App Store Configuration
- `umbrel-app-store.yml`: Defines the app store ID (`axoide`) and name
- Each app must prefix its ID with the app store ID (e.g., `axoide-freqtrade`)

### 2. Application Structure
Each application (like `axoide-freqtrade`) consists of:
- `docker-compose.yml`: Container configuration
- `umbrel-app.yml`: App metadata for Umbrel UI
- `data/`: Configuration and strategy files
- `assets/`: App images and resources

## Important Patterns and Conventions

### Docker Configuration
- Services use bridge networking for isolation
- Environment variables follow the `APP_*` naming pattern
- Port mapping uses high-range ports (>10000) for Umbrel compatibility
- Container logging is configured with rotation (10MB, 3 files max)

### Configuration Management
- App configurations are stored in `data/config.json`
- Sensitive data (API keys, secrets) should be parameterized
- Strategy files go in `data/strategies/`

## Integration Points

### Umbrel Integration
```yaml
# Example app integration (umbrel-app.yml)
id: "axoide-freqtrade"    # Must start with app store ID
name: "Freqtrade"
category: "Finance"
version: "1.0.0"
port: 11081               # External port for UI access
```

### Docker Services Communication
- Freqtrade API runs on port 8080 (internal)
- FreqUI interface runs on port 8081 (internal)
- Services communicate via `freqtrade_network` bridge network

## Development Workflow

1. App Store Development:
   ```bash
   # 1. Create new app directory
   mkdir axoide-your-app
   # 2. Add required files:
   #    - docker-compose.yml
   #    - umbrel-app.yml
   #    - README.md
   ```

2. Testing:
   - Always test in dry_run mode first
   - Verify port mappings don't conflict
   - Ensure data persistence works with Umbrel's volume mapping

## Common Gotchas
- App IDs must start with app store ID (`axoide-`)
- Use `${APP_DATA_DIR}` for data persistence
- Docker images should support both ARM (Pi) and x86 architectures
- Keep logging configuration to prevent disk space issues

## Reference Files
- Template Structure: `umbrel-app-store.yml`
- App Configuration: `axoide-freqtrade/docker-compose.yml`
- Example Config: `axoide-freqtrade/data/config.example1.json`