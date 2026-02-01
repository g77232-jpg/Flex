# Dependency install attempts

Attempts to install `python-docx` failed because outbound network access to package repositories is blocked by a proxy returning HTTP 403 responses. This was observed for both `pip install python-docx` and `apt-get update`, which could not reach the package indexes through the configured proxy.
