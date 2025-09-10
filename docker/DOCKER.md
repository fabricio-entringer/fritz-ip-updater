# Docker Usage Guide

## Quick Start with Make Commands (Recommended)

The project includes a Makefile with convenient Docker commands:

1. **Setup environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your actual credentials
   ```

2. **Build and run the container:**
   ```bash
   make docker-up
   ```

3. **View logs:**
   ```bash
   make docker-logs
   ```

4. **Stop the container:**
   ```bash
   make docker-down
   ```

5. **Other useful commands:**
   ```bash
   make docker-build    # Build/rebuild the Docker image
   make docker-restart  # Restart the container
   make docker-ps       # Show container status
   ```

## Alternative: Direct Docker Compose Commands

If you prefer using Docker Compose directly:

1. **Setup environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your actual credentials
   ```

2. **Build and run the container:**
   ```bash
   docker-compose --env-file .env -f docker/docker-compose.yml up -d
   ```

3. **View logs:**
   ```bash
   docker-compose --env-file .env -f docker/docker-compose.yml logs -f
   ```

4. **Stop the container:**
   ```bash
   docker-compose --env-file .env -f docker/docker-compose.yml down
   ```

## Manual Docker Commands

### Build the image:
```bash
docker build -t fritz-ip-updater .
```

### Run the container:
```bash
docker run -d \
  --name fritz-ip-updater \
  --restart unless-stopped \
  -v $(pwd)/data:/app/data \
  -e FRITZBOX_HOST=fritz.box \
  -e FRITZBOX_USER=your_username \
  -e FRITZBOX_PASSWORD=your_password \
  -e DUCKDNS_TOKEN=your_token \
  -e DUCKDNS_DOMAIN=your_domain \
  -e UPDATE_INTERVAL_MINUTES=interval_in_minutes \
  fritz-ip-updater
```

## Image Features

- **Tiny size**: Based on Alpine Linux (~50MB total)
- **Security**: Runs as non-root user
- **Resource efficient**: Limited to 64MB RAM and 0.1 CPU
- **Persistent data**: Mounts `./data` directory for logs and IP tracking
- **Health check**: Built-in container health monitoring

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FRITZBOX_HOST` | FritzBox IP or hostname | `fritz.box` |
| `FRITZBOX_USER` | FritzBox username | Required |
| `FRITZBOX_PASSWORD` | FritzBox password | Required |
| `DUCKDNS_TOKEN` | DuckDNS API token | Required |
| `DUCKDNS_DOMAIN` | DuckDNS subdomain | Required |
| `UPDATE_INTERVAL_MINUTES` | Interval for execution, in minutes | `5` |


## Make Commands Reference

All Docker operations can be performed using these convenient Make commands:

| Command | Description |
|---------|-------------|
| `make docker-up` | Start the container in detached mode |
| `make docker-down` | Stop and remove the container |
| `make docker-logs` | View container logs (follow mode) |
| `make docker-build` | Build/rebuild the Docker image |
| `make docker-restart` | Restart the running container |
| `make docker-ps` | Show container status |

## Troubleshooting

Using Make commands:
- Check logs: `make docker-logs`
- Check container status: `make docker-ps`
- Restart container: `make docker-restart`

Using direct Docker Compose commands:
- Check logs: `docker-compose --env-file .env -f docker/docker-compose.yml logs fritz-ip-updater`
- Check container status: `docker-compose --env-file .env -f docker/docker-compose.yml ps`
- Restart container: `docker-compose --env-file .env -f docker/docker-compose.yml restart fritz-ip-updater`