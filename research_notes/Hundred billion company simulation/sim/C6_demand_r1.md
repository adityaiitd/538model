# C6 v1 demand panel, round 1 (simulated, 24 Nov 2026)

Everything below is a simulated hypothesis built from the founder brief, the research notes and eight web lookups. No persona is a real person. Nothing here is customer validation.

Evidence labels: [notes] = ai_services.md; [source: URL] = checked in this session; [dk] = domain knowledge, unverified.

## Facts checked in this session

- Exclusive deals cost about 4-5x non-exclusive, per two RL environment founders. Contracts are "six to seven figures per quarter"; one neolab researcher saw $300-500k contracts. Most tasks $200-2,000; a $20k task is rare. Labs are doing "substantially more in-housing" to avoid vendor margin and keep training priorities confidential. Tasks are discarded once they reach about a 70% pass rate. About $2,400 of compute is spent per task during RL training (Mechanize estimate). Training demand is 10-20x benchmark demand. Finance is named as a domain specialist startups cover, not ranked as a priority; enterprise workflows are the main growth area and coding remains a major source of demand. [source: https://epoch.ai/gradient-updates/state-of-rl-envs]
- Most vendors close-source their environments and serve them in exclusive contracts. Anthropic works with more than a dozen RL environment companies and is often the first customer with exclusive contracts. OpenAI buys from a smaller pool and is building an in-house human data team. "Coding is in the most amount of demand." UI gyms are a one-time purchase reused across models. Ownership terms are not stated. [source: https://newsletter.semianalysis.com/p/rl-environments-and-rl-for-science]
- Finance is already supplied. Mercor's APEX covers the investment banking associate role and Mercor bought Sepal AI in February 2026 for environments. Handshake runs finance projects with simulated investment-banking workflows and lists "evaluation on open models before exclusive delivery". [source: https://www.rl-list.com/vendors/mercor] [source: https://explainx.ai/blog/handshake-ai-frontier-lab-rl-training-data-latent-space-2026] (both low-authority directories)
- Handshake AI and McGill released BankerToolBench in April 2026: open-source, built with 502 investment bankers; best model 58.1/100; no output rated client-ready. [source: https://arxiv.org/abs/2604.11304] [source: https://the-decoder.com/500-investment-bankers-review-ai-outputs-and-find-none-ready-for-client-delivery/]
- Vals AI (independent benchmarks, including Finance Agent v2 with 927 expert-reviewed questions and a held-out split; top score 57.86%) raised a $40M Series A at about $400M in August 2026. Revenue estimates are $1.3M to $3.2M a year. [source: https://dealroom.co/news/144926-vals-ai-raises-40m-series-a-at-400m-valuation-led-by-andreessen-horowitz/] [source: https://www.vals.ai/benchmarks/fabv2]
- AIUC raised a $40M Series A on 15 Sep 2026 (total $55M). AIUC-1 certifies agents with quarterly retests, pairs the certificate with Lloyd's-backed insurance, and uses an accredited outside auditor. Certified or signed: Cursor, Lovable, Harvey, ElevenLabs, UiPath, Intercom Fin, KPMG. It has a collaboration with the Cyber Risk Institute aimed at banks. No bank customers and no prices are reported. A critic calls it issuer-pays. [source: https://siliconangle.com/2026/09/15/ai-agent-certification-startup-aiuc-raises-40m-to-begin-auditing-frontier-models/] [source: https://forkast.news/aiuc-raises-40m-to-build-the-certification-and-insurance-layer-that-makes-agent-governance-auditable/] [source: https://zeltser.com/aiuc-1-cert]
- SR 26-2 (17 April 2026) superseded SR 11-7. It is principles-based. Vendor models stay under the same model risk principles and the bank must still check they are accurate and fit for purpose. Law-firm and Moody's summaries say generative and agentic AI are outside the formal scope for now, with the agencies planning to address them later. The primary text of that carve-out was not read. [source: https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm] [source: https://www.orrick.com/en/Insights/2026/04/Agencies-Overhaul-Model-Risk-Management-Guidance-for-Banks-Heres-What-Changed] [source: https://www.moodys.com/web/en/us/insights/banking/from-sr117-to-sr262-managing-model-risk-when-models-dont-stand-still.html]
- Mercor says its workers average $110 an hour and that it pays experts up to $200. Most of its workforce are former employees of law firms and investment banks. It faces suits alleging misclassification of 30,000 workers, data-privacy breaches, and training client models on materials that may belong to others. [source: https://techcrunch.com/2025/10/29/how-ai-labs-use-mercor-to-get-the-data-companies-wont-share/] [source: https://www.law360.com/tax-authority/articles/2475907] [source: https://news.bloomberglaw.com/daily-labor-report/ai-data-trainers-suits-open-new-misclassification-fight-frontier]

---

## Persona 1. Head of human data and evaluations, frontier lab ($50bn+ run-rate)

**Who.** Owns sourcing of expert data and environments. Runs in-house environment engineers plus five or more suppliers, including two large expert marketplaces.

**Incentives and constraints.** Measured on capability uplift per dollar and per researcher-hour. Scarce input is researcher attention for onboarding and QA, not money. Will not reveal the training roadmap to a supplier that also sells to rivals.

**Alternatives.**
- Commission exclusive finance tasks from an existing expert marketplace (30,000+ contractors, finance projects already running). [notes] [source: rl-list, explainx, above]
- Build the harness in-house and rent experts by the hour.
- Use the free open-source BankerToolBench for evaluation. [source: arXiv 2604.11304]

**Decision.** Paid pilot. No subscription.

**Terms.**
- One-quarter statement of work, $300-600k, 400-600 finance tasks.
- $400-900 per accepted non-exclusive task; up to $1,500 for tasks needing 6+ expert hours with a verified grader.
- Pay on acceptance only. Expect to reject 20-35% of delivered tasks. [dk]
- Acceptance bar: pass rate between about 3% and 70% on the current model, grader false-pass under 2%, no duplicates of public benchmark items. [source: Epoch for the pass-rate band; the rest dk]
- Anything that works gets re-ordered as exclusive custom work, not as a library.

**Reasons.**
- A library a rival also trains on gives no relative advantage. Exclusive is the market norm. [source: SemiAnalysis]
- Finance is second-tier. Coding and general enterprise workflows come first. [source: Epoch, SemiAnalysis]
- Estimated finance-domain budget at this lab for 2027, all sources including in-house: $50-150M. Share open to a non-exclusive outside library: $3-8M per supplier, and only after two good quarters. [dk]
- In-house share of environment build: about 30% now, heading to 50% or more within 24 months for domains that matter. Expert sourcing stays outside. [dk; direction supported by Epoch]

**What would change it.** Measured uplift on the lab's own held-out finance evaluation from the pilot batch; real workflow artefacts that marketplaces cannot get (licensed data rooms, actual audit files with client consent); rejection rate under 10%.

## Persona 2. Research lead for agents, second frontier lab or big-tech AI group

**Who.** Runs agent training and evaluation for long-horizon professional tasks.

**Incentives and constraints.** Wants tasks of 4-40 human hours with graders that cannot be gamed. Discretionary research budget under about $500k a quarter without committee. Vendor onboarding at a big-tech group takes 3-6 months. [dk]

**Alternatives.** BankerToolBench (free); Vals AI for independent scores; two or three seed-stage environment shops quoting similar work; in-house authors.

**Decision.** Paid pilot. Refuses the annual library.

**Terms.**
- $150-400k, one quarter, 100-200 long-horizon tasks at $1,000-2,000 each.
- Separately, $250k-1M one-off for a private held-out evaluation set, exclusive to this lab, never sold or shown to anyone else.

**Reasons.**
- Finance has headroom: best public score is 58.1/100 and nothing is client-ready. [source: decoder, arXiv]
- Disagrees with persona 1 on value of non-exclusive breadth: accepts it for evaluation coverage, not for training advantage.
- Will not treat the supplier's "independent benchmark" as held-out if same-distribution training tasks were sold to a rival lab. Scores on it would measure who bought the library.
- Training demand is 10-20x benchmark demand, so the benchmark is a small line. [source: Epoch]

**What would change it.** Evidence that tasks stay unsolved for 12+ months; grader audit by the lab's own team; a hard wall between training-task authors and benchmark authors.

## Persona 3. Procurement and legal lead at the lab

**Who.** Papers every data and environment contract.

**Constraints.** Standard paper is a master agreement with no committed volume plus quarterly statements of work. [notes: contracts last about a quarter] Custom deliverables are normally assigned to the lab. [dk]

**Decision.** Will sign a pilot statement of work up to $500k. Refuses a multi-year subscription with minimum commitment. Accepts supplier ownership only for off-the-shelf library items, on the lab's terms.

**Terms required for a non-exclusive licence where the supplier keeps ownership.**
- Perpetual, irrevocable, worldwide right to train and evaluate. Survives termination. No deletion or unlearning duty. No supplier claim on weights or outputs.
- Right to create and own model-generated variants of licensed tasks.
- The lab's feedback, failure traces and custom specifications are the lab's confidential property and may not be used to improve tasks sold to others.
- Termination for convenience on 30 days. Most-favoured pricing. No publicity.
- No restriction on the lab building similar environments.
- Provenance warranty: no employer or client confidential material used by any author; signed author attestations; audit right for the lab.
- IP and trade-secret indemnity at the greater of $10M or 5x fees; $10M+ professional and cyber cover; SOC 2 Type II. [dk]

**Reasons.**
- Open suits against an expert marketplace over misclassification, data breach and third-party materials make provenance a first-order issue. [source: Law360, Bloomberg Law]
- A seed-stage company cannot back the indemnity, so procurement caps exposure at about $1-2M a year until insurance is shown. [dk]
- A time-limited exclusivity window is not worth 4x. The 4-5x premium buys ownership or permanent exclusivity. A 6-12 month window is worth 1.5-2.5x. [dk; 4-5x from Epoch]

**What would change it.** Insurance in place; clean provenance audit; two quarters of delivery. Even then: 12-month term with quarterly volume flex, never a fixed multi-year fee.

## Persona 4. Finance chief of the lab's data organisation

**Who.** Controls a data budget in the low billions of dollars a year. [dk; consistent with notes: >$1bn discussed for RL environments at one lab, and one marketplace booking $614M in H1 2026 with 91% from two labs]

**Constraints.** Budget is reallocated every quarter by measured uplift. No annual prepay. Net-60 payment. Benchmarks every supplier against in-house cost.

**Cost benchmark.**
- In-house finance task: 4-8 expert hours at $110-200, plus 2 review hours, plus engineering and rejects: $700-2,000 fully loaded and exclusive. [source for rates: TechCrunch/Mercor; build-up dk]
- Therefore a shared task must cost a fraction of that. Target $250-600; ceiling $1,500 for multi-hour tasks.
- Counterpoint the persona concedes: a task consumes about $2,400 of training compute, so a bad task costs more than a dear one. Quality beats price. [source: Epoch]

**Decision.** Approves the pilot ($400k, Q1 2027). Refuses the $2-10M annual library. Would extend to $1-2M a quarter if acceptance exceeds 80% and researchers report uplift.

**Reasons.** Supplier margin is the first thing in-housing removes. If AI-assisted authoring halves expert hours, the lab expects the price to halve too, or does it itself.

**What would change it.** Per-task price under 40% of in-house cost at equal acceptance rate; or assets the lab cannot build (licensed real-world data).

## Persona 5. Head of AI, large bank or insurer

**Who.** Owns agent deployment across operations, credit, claims.

**Constraints.** Vendor onboarding through third-party risk and security takes 6-9 months. [dk] Does not train foundation models. Low pilot conversion is a real problem (83% of enterprises converted fewer than half). [notes]

**Alternatives.** Internal evaluation team on the bank's own data; Big Four assurance; AIUC-1 and ISO 42001 in vendor questionnaires; the lab's own deployment engineers. [source: AIUC items above] [notes: lab deployment ventures]

**Decision.** Refuses the environment library. Refuses to pay for certification of vendors' agents. Has no budget line for it.

**Who pays.** The vendor, as with SOC 2. The bank would list a recognised certificate as "preferred" in a request for proposal at zero cost to itself, and only once risk and model validation accept it.

**Possible purchase.** A private evaluation harness for three of the bank's own workflows, run inside the bank's environment on its data: $150-300k pilot, starting no earlier than Q3 2027 after onboarding. More likely bought from a Big Four firm already on the approved list.

**What would change it.** Regulator guidance naming third-party agent testing as acceptable evidence; two peer banks adopting the same certificate.

## Persona 6. Head of model risk management, regulated bank

**Who.** Second-line owner of validation under SR 26-2.

**Constraints.** Validation responsibility cannot be outsourced. Vendor evidence is an input; the bank must still confirm the model is fit for its own use, data and controls, and monitor it. [source: SR 26-2 summaries above]

**Decision.** Refuses. An outside certificate does not satisfy validation obligations. No budget line exists.

**Reasons.**
- Generic task-family tests say nothing about performance on this bank's data, prompts, tools and controls.
- Paid by the vendor and issued by a company that also sells training data to model makers: two independence problems. The file would be discounted.
- Model risk needs to inspect test items and graders. A secret held-out set cannot be inspected; a disclosed one is no longer held out.
- Agentic AI treatment is unsettled, so there is no rule a certificate could satisfy. [source: Moody's, Davis Polk via search summary]

**Value if offered free.** Might cut initial validation effort by 10-20%. [dk]

**What would change it.** Agency guidance recognising accredited third-party testing; the certifier accredited under a recognised conformity-assessment scheme and structurally separate from any training-data business; right to audit items under non-disclosure.

## Persona 7. Chief executive, AI application company selling agents into financial services

**Who.** $20-50M annual recurring revenue; sells to banks and insurers.

**Constraints.** Buys only the certificates that buyers' questionnaires ask for. Whole assurance budget is about $300-600k a year: SOC 2 $30-80k, ISO 27001 $50-100k, ISO 42001 $50-150k, penetration tests $20-50k, AIUC-1 perhaps $50-150k. [dk]

**Decision.** Refuses at $150-500k per task family. Five task families would be $0.75-2.5M a year.

**Would pay.** $30-60k one-off for an independent evaluation report to show prospects. $25-75k a year per agent for a certificate, only if at least two named banks state in writing that it shortens their proof-of-concept.

**Reasons.**
- No bank asks for it today (see personas 5 and 6).
- AIUC-1 already has brand, insurance and peer adoption. [source: SiliconANGLE]
- The certifier's main customers are the labs, whose own finance agents compete with this company. Will not hand them its agent or failure data.

**What would change it.** A lost deal where the stated reason was absence of this certificate; an insurer discount on errors-and-omissions cover tied to it.

## Persona 8. Senior finance professional recruited as expert author

**Who.** Director at an investment bank, 12 years' experience, total pay $600k-1M (about $250-450 per working hour). [dk]

**Constraints.** Outside business activity needs written pre-approval from compliance; registered staff fall under FINRA outside-activity rules. [dk] Deal models, templates and client data belong to the employer. Approval for paid work building AI training material from banking experience would almost certainly be refused. [dk]

**Decision.** Refuses while employed. $100-200 an hour is below this person's rate and carries job risk.

**Who does sign.** Former bankers, people between jobs, independent consultants, MBA students. They sign at $150-250 an hour for 10-15 hours a week, and also work for the large marketplaces at the same time. No supply lock-in. [source: TechCrunch on workforce composition and rates]

**Terms a senior reviewer would accept.** $300-400 an hour for review and sign-off, after leaving the employer or with written employer consent. Asks for more once it is clear each task is resold to several labs.

**Confidentiality limit.** Can build synthetic companies and public-filing-based cases only. Cannot bring real workpapers, credit files or claims files. The "realistic data" in the brief is therefore synthetic unless the company licenses real files from institutions.

**What would change it.** Employer-sanctioned programme (the bank itself as content partner, paid a licence fee).

---

## Cross-panel findings

**1. Non-exclusive licences with supplier ownership.** Accepted on paper by legal for off-the-shelf items, with a perpetual training right that makes the supplier's ownership worth only the right to resell. Not wanted by the buyer who matters (persona 1) for training advantage. Personas 1 and 2 disagree on value for evaluation coverage.

**2. Real prices and terms.**
- Non-exclusive finance task: $250-900; ceiling $1,500 for multi-hour work.
- Exclusive or assigned: $1,500-4,000.
- Pilot: $150-600k, one quarter.
- Steady state for a proven supplier: $1-2M a quarter per lab. No annual commitment.

**3. In-house shift.** About 30% of environment build today, 50%+ within two years in priority domains. Expert labour stays outsourced. [dk]

**4. Finance budget.** Second-tier priority. Estimated $50-150M per leading lab in 2027 across in-house and all suppliers; perhaps $200-500M across all buyers. A new non-exclusive supplier could reach $10-40M by year three. [dk]

**5. Certification budget at regulated buyers.** None found. Buyer will not pay; validator will not rely on it; vendor will pay only $25-75k and only on buyer pull.

**6. Training data plus held-out benchmark from one company.** Labs tolerate it for free marketing leaderboards (two marketplaces already do this). Researchers, model risk and application vendors all reject it for a paid, decision-grade certificate.

**7. Unit economics.** Cost per accepted long-horizon environment is about $1,800-3,000 (8-12 expert hours, review, engineering, 25% rejects). [dk] At $500-900 per sale the company needs 3+ sales per environment to reach the stated 55-65% gross margin. With 2-5 buyers, expect 30-45% in the first two years, in line with the sector's 30-40%. [notes]

## Numbers in the brief disputed

| Brief | Panel view | Basis |
|---|---|---|
| Non-exclusive $500-2,000 per environment | $250-900; up to $1,500 for multi-hour tasks | $200-2,000 is mostly exclusive pricing; exclusive is 4-5x non-exclusive [source: Epoch, SemiAnalysis] |
| $2-10M a year per lab per domain library | $0.3-0.6M pilot; $2-6M a year after two good quarters; no annual commitment | "six to seven figures per quarter" [source: Epoch] |
| Time-limited exclusivity at 4x | 1.5-2.5x for a 6-12 month window | 4-5x buys full exclusivity [dk] |
| Certification $150-500k per agent per task family | $25-75k per agent per year, vendor-paid | assurance budget build-up [dk] |
| Gross margin 55-65% | 30-45% in years 1-2 | resale count needed; sector 30-40% [notes] |
| $100M needs five buyers at $10-20M | Finance alone supports $3-8M per buyer; $100M needs 4-6 professions or exclusive work | finance budget estimate [dk] |
| "Coding is well covered"; finance is next | Coding still has the most demand; finance already served by two large marketplaces | [source: SemiAnalysis, Epoch, rl-list] |
| Experts at $100-200 an hour | $150-250 authors; $300-400 senior reviewers; employed seniors unavailable | [source: TechCrunch; dk] |
| Passed environment is worthless | Tasks retire at about 70% pass rate, roughly 6-18 months; harnesses and simulators carry over | [source: Epoch, SemiAnalysis; duration dk] |
| AI-assisted authoring halves cost | Buyers expect the price to fall with it and can do the same in-house | [dk] |

## Probabilities (panel estimate)

- First paid commercial delivery within 18 months: 70%. On the brief's stated terms (ownership kept, non-exclusive, $500+ per task, annual library): about 35%.
- $1 billion of annual recognized revenue within 7 years: 2%.
