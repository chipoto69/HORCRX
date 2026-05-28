# Security Policy

## Reporting a Vulnerability

If you believe you have found a security vulnerability in HORCRX, please report
it via private email rather than opening a public issue:

> security@horcrux.dev

This address is the operator-controlled intake alias for private reports and
should be kept current if routing changes.

We aim to acknowledge receipt within 72 hours and provide a remediation timeline
within 7 days.

## Vessel Signing Key

**Status:** DEFERRED to Phase 1 of `docs/roadmap/next-missions.md` (vessel CLI
and Hermes export). No production vessel-signing key exists in the foundation
phase per `AGENTS.md`. The first operator-approved signing key fingerprint will
be published here and in `specs/vessel-format/signing-and-lineage.md` when
Phase 1 lands.

## Threat Model

See `docs/infrastructure/security.md` for the comprehensive threat model
covering soul theft, signature forgery, replay attacks, plagiarism via fork,
royalty oracle manipulation, and secret extraction at export.

## Disclosure Coordination

For coordinated disclosure with affected runtimes (especially Hermes), please
include in your report whether the issue affects:

- Vessel export path (`hermes profile export --as-vessel`)
- Vessel import path (`horcrx install`)
- Signing chain integrity
- Payment settlement (x402)
- Marketplace listing flow
