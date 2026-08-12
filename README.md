# HSL RAN Operations Automation

A sanitised archive of HSL automation developed collaboratively by **Alexandre Torres** and **Luis Reis** for a telecom radio-access-network operations team.

The scripts ran inside Huawei's MAE/OSS environment and turned recurring operational checks and configuration preparation into guided, repeatable workflows. They combined forms, network-element discovery, MML execution, report parsing, validation and CSV or spreadsheet output.

> **Archive status**
>
> The original operational context has ended. This repository is preserved as a read-only portfolio archive and cannot run outside the proprietary HSL/MAE runtime. It is not configured for a live network.

## What the archive demonstrates

- translating manual RAN procedures into repeatable automation;
- working across GSM, UMTS, LTE and NB-IoT workflows;
- building operator-facing forms and structured reports;
- discovering network elements and selecting logic from their capabilities;
- issuing MML commands and parsing their results;
- validating configuration, hardware, alarms, licences, clock state and radio health;
- generating follow-up commands and evidence for operational review.

## Preserved workflows

| Directory | Purpose |
| --- | --- |
| `2g-migration` | Prepares and validates configuration steps for a 2G migration workflow from a structured input file. |
| `automatic-vpn` | Checks IKE state and prepares missing peer configuration for selected sites. |
| `baseband-check` | Reviews baseband-board allocation, RRU chains and available capacity. |
| `clock-status` | Checks external clock references and supports corrective clock configuration. |
| `device-ip-labels` | Audits device-IP labels and produces corrective MML commands. |
| `empty-elements` | Identifies unused or incomplete IP-related configuration elements. |
| `energy-optimisation` | Collects cell, RRU and power-counter information for energy analysis. |
| `nb-iot-preparation` | Checks prerequisites and prepares configuration and reports for NB-IoT changes. |
| `pki-certificate-preparation` | Collects board serial information and prepares a certificate-registration input file. |
| `site-acceptance` | Runs GSM, UMTS and LTE health checks covering alarms, software, licences, cells, radio tests, boards and interfaces. |

## Repository structure

```text
scripts/
  2g-migration/
  automatic-vpn/
  baseband-check/
  clock-status/
  device-ip-labels/
  empty-elements/
  energy-optimisation/
  nb-iot-preparation/
  pki-certificate-preparation/
  site-acceptance/
docs/
  sanitisation-boundary.md
tests/
  test_archive.py
tools/
  verify-public-copy.ps1
```

The original `.hsp3` packages were ZIP-compatible project containers. Only their readable `.hsl3` source files are included here; project metadata and packaged artefacts were deliberately omitted.

## Sanitisation

The public copy contains no production credentials, internal e-mail addresses, internal IP addresses, real node or site lists, deployment-specific zone mappings, customer data or operational output. Example values use `.invalid` domains and the documentation address ranges defined by RFC 5737.

Three regional GSM files were identical, as were the three regional UMTS files, so each set is represented by one canonical source file. Historical backups and a separate 5G file carrying an explicit third-party ownership notice are excluded.

See [the sanitisation boundary](docs/sanitisation-boundary.md) for the complete inclusion and exclusion policy.

## Validation

The repository can be checked without the proprietary runtime:

```powershell
python -m unittest discover -s tests -v
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\verify-public-copy.ps1
```

These checks validate archive structure, UTF-8 readability, local imports and the sanitisation boundary. They are not a substitute for execution inside an authorised MAE environment.

## Authors

This work was developed collaboratively by Alexandre Torres and Luis Reis. Luis does not currently have a GitHub account; his contribution is recorded in [AUTHORS.md](AUTHORS.md) and the repository history cannot be used as the sole attribution record.

## Use, attribution and trademarks

This repository is published for portfolio review and historical reference. No open-source licence is granted. Huawei, MAE, HSL and all other product or company names are used only to describe the original technical context. See [NOTICE.md](NOTICE.md).
