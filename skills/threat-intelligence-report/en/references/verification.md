# Verification Guide

## Source hierarchy

1. Original post, original sample, affected-organization statement, official advisory
2. Technical research, government or law-enforcement publication, research paper
3. Independent reporting by a reputable news organization
4. Repost accounts, aggregators, community commentary

Lower-tier sources can support discovery and context, but should not be the sole basis for a strong conclusion.

## Alleged breach checklist

- **Format:** Are schema, field names, encoding, dates, phone numbers, and addresses consistent with the alleged service?
- **Values:** Are domains, locations, products, and account conventions realistic?
- **Scale:** Are the claimed row count, file size, field count, and sample distribution mutually plausible?
- **Duplication:** Does it overlap with historical breaches, public data, marketing lists, or test data?
- **Freshness:** Are recent account, order, or activity timestamps present and internally consistent?
- **Provenance:** Who first published it, and who merely reposted, promoted, or resold it?
- **Reputation:** Is there verifiable sales history, administrator validation, PGP continuity, escrow, or credible buyer feedback?
- **Harm:** Could the data directly enable account takeover, phishing, impersonation, or financial fraud?

Common warning signs include `example.com`, sequential phone numbers, nonexistent addresses, uniform generated patterns, exact reuse of an older sample, and repeated reposts without an identifiable origin. Do not use one warning sign as conclusive proof.

## Campaign and malware checklist

- Separate first reporting from the date of the analyzed activity.
- Corroborate initial access, execution, persistence, C2, and payload behavior.
- Distinguish sample-specific IOCs from shared infrastructure.
- Map ATT&CK techniques only to observed behavior.
- Do not automatically merge vendor cluster names and aliases.
- Confirm CVEs, patches, products, and affected versions through official sources.

## Dark web and Telegram checklist

- Treat Telegram as a possible amplification or sales channel rather than the origin.
- Do not treat branding, logos, or “Reported by” language as proof of authenticity.
- Account for deleted posts, clones, impersonation, and scam channels.
- Distinguish intruder, seller, broker, forum operator, buyer, and promoter/reposter roles.
- Do not require joining illegal markets, purchasing data, direct messaging, or executing files.

## Verdicts

| Verdict | Meaning |
|---|---|
| Confirmed | Independent strong evidence supports the core claim and no material counterevidence remains |
| Partially confirmed | A meaningful portion is verified, but scope, freshness, or provenance remains unknown |
| Repackaged historical data | The material substantially matches previously disclosed or public data |
| Indicators of synthetic/manipulated data | Multiple unrealistic patterns and counterevidence exist, but the complete original cannot be examined |
| Unverified | Available evidence is insufficient or conflicting |

Assign `high`, `medium`, or `low` confidence separately from the verdict.

## Risk scoring

Score each dimension from 0 to 5 for internal prioritization:

- evidence strength
- data or asset sensitivity
- freshness
- distribution reach
- abuse potential

The total is a discussion aid, not an automatic verdict. Add a one-sentence rationale.

## Evidence handling

- Separate originals from processed or redacted copies.
- Record observation time, source location, account, post ID, and timezone.
- Hash files where practical.
- Collect only the minimum necessary sample and mask personal data.
- Remove details that enable reidentification or abuse from public outputs.
- State the limitation when only a screenshot is available without its original URL or timestamp.
