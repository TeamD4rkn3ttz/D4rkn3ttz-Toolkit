# Representative Examples

## Validate an alleged customer database

Prompt:

> A forum user claims to be selling 30 million Korean customer records. The sample looks fake. Verify it and draft an X post.

Expected behavior:

1. Preserve the original claim, sample context, claimed scale, and observation time.
2. Examine email domains, phone numbers, addresses, dates, and value distribution.
3. Search for overlap with historical breaches, public datasets, and test data.
4. Actively look for evidence against the initial “fake” hypothesis.
5. Assign a nuanced verdict and confidence.
6. Present the evidence before the public-post draft.
7. Do not publish without approval.

Good assessment:

> The sample contains repeated example.com addresses, sequential phone numbers, and addresses that could not be validated. These findings are strong indicators of synthetic data. Because the complete original dataset was unavailable, the current verdict is “indicators of synthetic or manipulated data” with medium confidence.

Avoid:

> This is obviously 100% fake.

## Summarize a ransomware analysis

Prompt:

> Summarize this ransomware research article for our weekly threat report.

Expected behavior:

1. Verify the publication date and dates of the underlying activity.
2. Separate initial access, execution chain, payloads, impact, and IOCs.
3. Corroborate material technical claims with primary sources.
4. Explain novelty, audience relevance, and defensive actions.
5. Do not invent attribution, victim counts, or impact.

## Identify a Telegram repost

Prompt:

> A statement appeared in a threat-actor Telegram channel. Determine whether it is new and prepare a post.

Expected behavior:

1. Search for the earliest identical wording, image, and link.
2. Determine whether the channel is original, impersonating, promoting, or reposting.
3. Lead with “not a new release” when no new incident evidence exists.
4. Do not redistribute victim data or high-risk original material.

## Work with incomplete evidence

Prompt:

> Identify the responsible group and write a report from this screenshot.

Expected behavior:

- List only what is directly observable.
- Do not assign a group without sufficient evidence.
- Request the smallest useful set of missing data: original URL, timestamp, file, hash, or logs.
- Provide a current assessment, plausible hypotheses, intelligence gaps, and next verification steps.
