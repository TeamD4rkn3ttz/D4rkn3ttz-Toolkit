# D4rkn3ttz Toolkit

[English](#english) · [한국어](#한국어)

Open-source threat intelligence skills, playbooks, templates, and research utilities by [TEAM_D4rkn3ttz](https://github.com/Team-D4rkn3ttz).

## English

### Threat Intelligence Report Skill

An evidence-first workflow for turning dark web posts, Telegram messages, ransomware claims, breach samples, technical reports, IOCs, and TTPs into decision-ready cyber threat intelligence.

Key capabilities:

- separates actor claims from verified facts
- tracks provenance, reposts, dates, and timezones
- validates breach samples and identifies recycled or synthetic data
- assigns nuanced verdicts, confidence, and risk
- produces reports, internal briefings, card-news copy, and X posts
- applies victim-protection and publication-safety gates

Use the English package at [`skills/threat-intelligence-report/en`](skills/threat-intelligence-report/en).

Example prompt:

> Use the English threat intelligence report skill to verify this alleged breach, show the evidence and uncertainty, and draft a TEAM_D4rkn3ttz X post. Do not publish it.

## 한국어

### 위협 인텔리전스 리포트 스킬

다크웹 게시물, 텔레그램 메시지, 랜섬웨어 주장, 유출 샘플, 기술 보고서, IOC와 TTP를 조사·검증하여 의사결정 가능한 위협 인텔리전스로 변환하는 재사용 워크플로입니다.

주요 기능:

- 행위자의 주장과 검증된 사실 분리
- 최초 출처, 재게시, 날짜와 타임존 추적
- 유출 샘플 검증 및 과거 자료·합성 데이터 판별
- 진위 판정, 신뢰도, 위험도 평가
- 상세 리포트, 내부 브리핑, 카드뉴스, X 게시물 작성
- 피해자 보호와 게시 전 안전성 검토

국문 패키지는 [`skills/threat-intelligence-report/ko`](skills/threat-intelligence-report/ko)를 사용하세요.

사용 예시:

> 국문 위협 인텔리전스 리포트 스킬을 사용해 이 유출 주장을 검증하고, 근거와 불확실성을 제시한 뒤 TEAM_D4rkn3ttz X 게시물 초안을 작성해 주세요. 실제로 게시하지는 마세요.

## Repository structure

```text
skills/
└── threat-intelligence-report/
    ├── en/
    │   ├── SKILL.md
    │   └── references/
    └── ko/
        ├── SKILL.md
        └── references/
```

The two language packages are independently installable. Future playbooks, templates, and scripts can be added as separate top-level collections.

## Safety and ethics

This toolkit is intended for lawful, evidence-based defensive research. It does not instruct users to purchase stolen data, access illegal services, engage threat actors, use compromised credentials, execute malware, or expose victims' personal information.

## License

Apache License 2.0 is recommended for the public repository so future code and automation can be distributed under the same license.
