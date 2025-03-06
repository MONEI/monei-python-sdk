# Publishing to PyPI

This project uses GitHub Actions to automatically publish new releases to PyPI. When a new GitHub release is created, the package will be built and published to PyPI.

## Setting up PyPI API Token

To set up automatic publishing to PyPI, you need to create a PyPI API token and add it to your GitHub repository secrets:

1. **Create a PyPI API token**:
   - Log in to your PyPI account at https://pypi.org/
   - Go to your account settings
   - Under "API tokens", create a new API token with the scope set to the project name (`Monei`)
   - Copy the token (you won't be able to see it again)

2. **Add the token to GitHub repository secrets**:
   - Go to your GitHub repository
   - Navigate to "Settings" > "Secrets and variables" > "Actions"
   - Click "New repository secret"
   - Name: `PYPI_API_TOKEN`
   - Value: Paste the PyPI API token you copied
   - Click "Add secret"

## Creating a Release

To publish a new version to PyPI:

1. Update the version number in `pyproject.toml`
2. Commit and push your changes
3. Create a new release on GitHub:
   - Go to "Releases" in your repository
   - Click "Draft a new release"
   - Create a new tag with the version number (e.g., `v1.2.7`)
   - Add release notes
   - Click "Publish release"

The GitHub Action will automatically build and publish the package to PyPI.

## Workflow Details

The publishing workflow uses [uv](https://github.com/astral-sh/uv) for dependency management and package building. The workflow:

1. Sets up Python with uv
2. Installs dependencies
3. Runs tests to ensure everything is working
4. Builds the package
5. Publishes the package to PyPI

You can see the full workflow configuration in `.github/workflows/publish.yml`. 