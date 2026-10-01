---
name: code-sandbox-security
description: Use when designing or reviewing isolation for untrusted code execution, sandbox services, egress restrictions, or credential delivery.
metadata:
  version: "1.1.0"
---

# Code Sandbox Security

- Establish trust level, tenant model, host OS, runtime, mounts, network, secrets, and resource limits. Instructions do not create isolation; report a missing required sandbox before executing untrusted code.
- Choose MicroVM, userspace kernel, hardened container, or constrained Wasm according to threat and supported runtime. Verify provider requirements in current official documentation. Do not promise startup or memory figures without measurement.
- Distinguish process isolation from dedicated kernel isolation. On Windows verify the actual VM/WSL/container backend before applying Linux controls.
- Run non-root with minimal capabilities, restricted syscalls, read-only base storage, scoped temporary writes, and CPU/memory/process/time/output limits. Admission policy alone does not establish every control.
- Avoid broad mounts, host sockets, privileged execution, and metadata endpoints. Restrict egress, addressing redirects, DNS changes, IP bypass, private ranges, and IPv6.
- Prefer scoped credential proxies or short-lived delivery. Never embed secrets in source, images, prompts, or logs. Environment delivery depends on the threat model; minimize exposure and lifetime.
- Test permitted and denied filesystem, network, credential, resource, and cross-tenant access in an authorized environment; verify cleanup. Configuration alone is not proof.
- Installs, deployment, live policy changes, and billing remain within task authorization; prepare reviewable configuration first when permission is missing.
