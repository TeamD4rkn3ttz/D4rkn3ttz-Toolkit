# TEAM_D4rkn3ttz Toolkit

[English](#english) · [한국어](#한국어)

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Validate skills](https://github.com/TeamD4rkn3ttz/D4rkn3ttz-Toolkit/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/TeamD4rkn3ttz/D4rkn3ttz-Toolkit/actions/workflows/validate-skills.yml)

An open, evidence-first collection of reusable cyber threat intelligence skills maintained by [TEAM_D4rkn3ttz](https://github.com/TeamD4rkn3ttz).

## English

### Available skill

#### Threat Intelligence Report — English

[`skills/threat-intelligence-report/en`](skills/threat-intelligence-report/en) turns dark-web posts, Telegram messages, ransomware claims, breach samples, technical reports, IOCs, and TTPs into decision-ready intelligence.

It helps analysts:

- separate threat-actor claims from verified facts;
- preserve provenance, dates, repost relationships, and timezones;
- assess whether leaked data is new, recycled, synthetic, or still unverified;
- express verdicts, confidence, risk, and intelligence gaps consistently;
- produce reports, briefings, card-news copy, and draft social posts; and
- apply victim-protection and pre-publication safety checks.

Example:

> Use the English threat intelligence report skill to verify this alleged breach, show the supporting evidence and uncertainty, and draft a TEAM_D4rkn3ttz X post. Do not publish it.

### Installation

Copy the English package into your Codex skills directory:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/threat-intelligence-report/en \
  "${CODEX_HOME:-$HOME/.codex}/skills/threat-intelligence-report-en"
```

Restart Codex after installation so the skill can be discovered.

## 한국어

### 제공 스킬

#### 위협 인텔리전스 리포트 — 국문

[`skills/threat-intelligence-report/ko`](skills/threat-intelligence-report/ko)는 다크웹 게시물, 텔레그램 메시지, 랜섬웨어 주장, 유출 샘플, 기술 보고서, IOC와 TTP를 검증 가능한 위협 인텔리전스로 변환합니다.

분석가는 이 스킬을 활용해 다음 작업을 수행할 수 있습니다.

- 위협 행위자의 주장과 검증된 사실 분리
- 출처, 날짜, 재게시 관계와 타임존 보존
- 유출 데이터의 신규성, 재활용, 합성 또는 미확인 여부 평가
- 판정, 신뢰도, 위험도와 정보 공백의 일관된 표현
- 리포트, 브리핑, 카드뉴스와 소셜 게시물 초안 작성
- 피해자 보호와 게시 전 안전성 검토

사용 예시:

> 국문 위협 인텔리전스 리포트 스킬을 사용해 이 유출 주장을 검증하고, 근거와 불확실성을 제시한 뒤 TEAM_D4rkn3ttz X 게시물 초안을 작성해 주세요. 실제로 게시하지는 마세요.

### 설치

국문 패키지를 Codex 스킬 디렉터리로 복사합니다.

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/threat-intelligence-report/ko \
  "${CODEX_HOME:-$HOME/.codex}/skills/threat-intelligence-report-ko"
```

설치 후 Codex를 재시작하면 스킬을 검색할 수 있습니다.

## Repository layout

```text
.
├── skills/
│   └── threat-intelligence-report/
│       ├── en/                 # Independent English skill
│       │   ├── SKILL.md
│       │   └── references/
│       └── ko/                 # 독립된 국문 스킬
│           ├── SKILL.md
│           └── references/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   └── PULL_REQUEST_TEMPLATE.md
├── CONTRIBUTING.md
├── SECURITY.md
├── NOTICE
└── CITATION.cff
```

The Korean and English packages are independently installable and must remain independently usable. Shared improvements should be evaluated for both languages without forcing literal translations.

## Validation

Run the same repository checks used by GitHub Actions:

```sh
python3 scripts/validate_skills.py
```

The validator checks skill frontmatter, package boundaries, required references, and relative Markdown links.

## Responsible use

This toolkit is intended for lawful, evidence-based defensive research. Do not use it to purchase stolen data, access illegal services, engage threat actors, use compromised credentials, execute malware, or expose victims' personal information.

See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a change and [SECURITY.md](SECURITY.md) when reporting a vulnerability.

## Citation and license

Citation metadata is available in [CITATION.cff](CITATION.cff). The toolkit is licensed under the [Apache License 2.0](LICENSE).
