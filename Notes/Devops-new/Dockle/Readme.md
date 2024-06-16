# Dockle

Dockle is a container image linter that helps identify best practices and potential security vulnerabilities within Docker images. It scans Docker images and provides a list of suggestions and warnings, helping you improve the security and compliance of your container images.

## Key Features

- **CIS Benchmark Checks**: Dockle checks Docker images against the CIS Docker Benchmark, providing suggestions for improving security.
- **Best Practices**: It identifies potential issues related to best practices, such as user configuration, health check implementation, and file permissions.
- **Vulnerability Detection**: While Dockle focuses on configuration and best practices, it can be used in conjunction with other tools like Trivy for comprehensive vulnerability scanning.

## Level Definitions

Dockle has 5 check levels:

| LEVEL  | DESCRIPTION                                             |
|--------|---------------------------------------------------------|
| FATAL  | Critical issues that must be addressed                  |
| WARN   | Issues that should be reviewed and fixed if necessary   |
| INFO   | Informational messages about best practices             |
| SKIP   | Checks that were skipped because target files were not found |
| PASS   | Checks that passed with no issues found                 |

## Installation

You can find the detailed installation instructions on the [Dockle GitHub page](https://github.com/goodwithtech/dockle#installation).

### Basic Installation

#### Using Docker

```sh
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock goodwithtech/dockle <image_name>
```

#### Using Homebrew (macOS)

```sh
brew install goodwithtech/r/dockle
```

#### Downloading Binary

Download the Dockle binary directly from the [Dockle GitHub releases page](https://github.com/goodwithtech/dockle/releases) and place it in your `PATH`.

## Usage Examples

### 1. Basic Dockle Scan

```sh
dockle [YOUR_IMAGE_NAME]
```

This command runs Dockle to scan the Docker image specified by `[YOUR_IMAGE_NAME]`. It checks for security issues and adherence to best practices.

### 2. Dockle Scan with JSON Output

```sh
dockle -f json -o results.json [IMAGE_NAME]
```

This command runs Dockle on the specified Docker image (`[IMAGE_NAME]`) and outputs the results in JSON format to a file named `results.json`. The `-f` flag sets the output format, and `-o` specifies the output file.

### 3. Set Non-Zero Exit Code on Warnings or Errors

```sh
dockle --exit-code 1 [IMAGE_NAME]
```

By default, Dockle exits with code 0 even if there are problems. This command uses the `--exit-code` option to exit with a non-zero exit code if WARN or FATAL alerts are found during the scan.

### 4. Specify Specific Checks to Ignore

```sh
dockle -i CIS-DI-0001 -i DKL-DI-0006 [IMAGE_NAME]
```

This command runs Dockle on the specified Docker image and ignores the checks with IDs `CIS-DI-0001` and `DKL-DI-0006`. The `-i` option is used to specify checks to ignore.

### 5. Docker Hub Authentication

To authenticate Dockle with Docker Hub, set the following environment variables:

```sh
export DOCKLE_AUTH_URL=https://registry.hub.docker.com
export DOCKLE_USERNAME={DOCKERHUB_USERNAME}
export DOCKLE_PASSWORD={DOCKERHUB_PASSWORD}
```

These commands set environment variables for Docker Hub authentication. The `DOCKLE_AUTH_URL` variable specifies the Docker registry URL, and `DOCKLE_USERNAME` and `DOCKLE_PASSWORD` are set to your Docker Hub username and password.

## Advanced Usage

### Integrating Dockle with CI/CD

Dockle can be integrated into CI/CD pipelines to enforce container security and best practices checks as part of the build process. Here is an example using a GitHub Actions workflow:

```yaml
name: CI

on: [push]

jobs:
  dockle:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Build Docker image
        run: docker build -t my-image .

      - name: Run Dockle
        run: docker run --rm -v /var/run/docker.sock:/var/run/docker.sock goodwithtech/dockle my-image
```

## Conclusion

Dockle is a valuable tool for improving the security and compliance of Docker images by ensuring they follow best practices and security guidelines. It can be easily integrated into development workflows, making it a crucial part of a robust DevOps security strategy.
