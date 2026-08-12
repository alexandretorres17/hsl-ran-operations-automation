# Sanitisation boundary

## Included

- readable HSL source extracted from nine historical `.hsp3` packages;
- one canonical GSM, UMTS and LTE site-acceptance script;
- original control flow, forms, report parsing and MML-building logic where safe;
- synthetic examples needed to make the preserved flow understandable;
- authorship, usage, security and validation documentation.

## Replaced

- internal e-mail addresses with `portfolio@example.invalid`;
- internal service addresses with RFC 5737 documentation addresses;
- SFTP credentials and endpoint with deliberately non-working example values;
- real site, controller and network-element identifiers with explicit examples;
- the deployment-specific IP-to-zone mapping with `EXAMPLE_ZONE`;
- operator-specific labels where they formed part of a configuration value.

## Excluded

- original `.hsp3` packages and `projConf.dsl` metadata;
- historical backup files and redundant regional duplicates;
- the 5G health-check backup carrying an explicit third-party ownership notice;
- credentials, production configuration, operational output and personal data;
- the proprietary HSL/MAE runtime and vendor documentation.

## Runtime status

The source was checked for readability, local import completeness and sanitisation. It could not be compiled or executed because the HSL interpreter and connected MAE services are proprietary and are not included in this archive.
