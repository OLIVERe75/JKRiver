# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest `main` | Yes |
| Older commits | No |

## Reporting a Vulnerability

**Please do NOT open a public issue for security vulnerabilities.**

Email **mailwangjk@gmail.com** with:

1. Description of the vulnerability
2. Steps to reproduce
3. Impact assessment (if known)

### Response Timeline

- **Acknowledgement:** within 72 hours
- **Status update:** within 7 days
- **Fix or mitigation:** as soon as reasonably possible

## Scope

### In Scope

- SQL injection or query manipulation
- Path traversal (file read/write outside intended directories)
- Shell command injection via `shell_exec` or similar
- Unintended data exposure (profile data, credentials, API keys)
- Authentication or authorization bypass

### Out of Scope

- Vulnerabilities in third-party dependencies (report upstream)
- Denial of service attacks
- Physical access attacks
- Social engineering

## Disclosure

We follow coordinated disclosure. We will credit reporters in the changelog unless anonymity is requested.
