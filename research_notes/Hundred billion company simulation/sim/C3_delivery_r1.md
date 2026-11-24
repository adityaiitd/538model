# C3 delivery panel, round 1: AI-run billing office paid on collections

Date of simulation: 24 November 2026. Brief tested: `C3_v1.md`.

Everything below is a simulated hypothesis. Personas are archetypes. No real person was interviewed and no real order exists.

Evidence labels: **[notes]** = founder research notes; **[source: URL]** = web search run for this panel (8 searches, all read through search summaries, not the original pages); **[DK]** = domain knowledge, unverified.

## Summary verdict

The product can be delivered, but not at the stated cost, speed or guarantee. Model capability is not the constraint. The constraints are access (practice-management systems, payer portals, payer enrollment), accountability (False Claims Act exposure on a contingency fee) and working capital.

| Founder figure | Panel figure | Basis |
|---|---|---|
| 4.5% of net collections | 2.5-4.0% for a $50M client; 5-8% only for small practices; expect 3.0-3.5% by 2029 | Fee falls with client size [DK]; small-practice quotes 5-8% [source: https://www.carepatron.com/blog/how-much-do-medical-billing-services-cost/] |
| Cost to serve 40% in year one | 60-71% run-rate for a live client; 73-95% with guarantee reserve and implementation; above 120% of fees recognized in a client's first contract year | Cost stack below |
| Cost to serve 20% at scale | 45-50% at a 4.5% fee; 55-60% if the fee falls to 3.5% | Cost stack below |
| Go-live in 45 days | 90-150 days on an already-integrated system; 150-240 days for a new system or care setting | Payer enrollment, security review, partner certification [DK] |
| Six-month guarantee, refund to cover shortfall | 12 months, measured on matured cohorts, capped at 25-50% of period fees | Net collection rate needs 120 days of run-out [DK] |
| 45 clients averaging $50M | 110-150 clients averaging $15-20M | $50M groups mostly run central billing offices with offshore captives [DK] |
| Cash conversion | First fee cash 6-8 months after signing; unrestricted cash about month 12-13; payback 14-20 months | Timeline below |
| Onboarding capacity | 1-2 clients of $50M per team per quarter in year one; 3-4 at maturity on one repeated stack | Operator and engineer personas |

## Cost stack for one $50M specialty-group client ($2.25M fee)

Volume assumptions [DK]: about 278,000 claims a year at $180 average payment; initial denial rate about 12% [source: https://www.hfma.org/technology/ai/predict-prevent-perform-the-ai-evolution-of-denials-management/], so about 33,000 denials; about 22,000 prior authorizations; about 30,000 patient calls. A legacy vendor needs about 26 full-time staff for this account [DK]. Onshore loaded cost $68K (billing clerk mean wage $51,070 [notes] plus 33%); offshore loaded cost $16K [DK].

| Line | Year one | % of fee | At scale (year 5) | % of fee |
|---|---|---|---|---|
| Operations labor | 17 staff, half onshore, $714K | 32% | 8-9 staff, 40% onshore, $315K | 14% |
| Supervision, quality audit, compliance | $180K | 8% | $110K | 5% |
| Client success | $60K | 3% | $55K | 2.5% |
| Clearinghouse and data interchange | $125-180K | 5-8% | $110K | 5% |
| Model inference and voice | $135-270K | 6-12% | $135K | 6% |
| Practice-management access (licenses, interface fees, marketplace share) | $70-110K | 3-5% | $90K | 4% |
| Insurance and security certification | $55K | 2.5% | $45K | 2% |
| Run-rate subtotal | | 60-71% | | 39% |
| Guarantee reserve | $225-450K | 10-20% | $70-110K | 3-5% |
| Implementation, amortized over three years | $70-100K a year | 3-4% | $70K | 3% |
| Total | | 73-95% | | 45-50% |

Patient statements and card fees (about 3% on the 10-20% of collections paid by patients [DK]) are assumed to be passed through. If absorbed, add 5 points.

Automatable share of legacy task hours [DK]: 55-65% today with good integration; 30-40% realized in year one; 65-70% by year five. Twenty percent cost to serve needs roughly 90% automation, no access tolls and no price erosion. None of the three is plausible.

## Cash timeline for one client

| Event | Month from signature |
|---|---|
| Contract, business associate agreement, security review | 0-1.5 |
| Go-live | 3-5 |
| First payer payments on new claims | 4-6.5 |
| First invoice paid (monthly in arrears, net 30, paid in 30-45 days) | 6-8 |
| Guarantee window closes, fees no longer refundable | 9-11 at six months; 15-17 at twelve |

Peak cumulative cash deficit per $50M client: $1.0-1.5M [DK estimate]. Forty-five such clients need $45-70M of working capital before research and development. Fees inside the guarantee window are variable consideration, so they should be held as restricted cash and may not be recognizable as revenue [DK].

---

## Persona 1: Partner manager, frontier model provider

- **Who:** runs application-layer accounts in healthcare. The same company has a healthcare product and a $1.5B deployment venture [notes].
- **Incentives:** token volume, no channel conflict with larger accounts, no exclusives.
- **Facts:** the lab launched a healthcare offering in January 2026 with a coverage-database connector and a prior-authorization review skill, aimed at appeals and revenue cycle; one large health system planned to deploy it in revenue cycle [source: https://www.anthropic.com/news/healthcare-life-sciences; https://www.beckershospitalreview.com/healthcare-information-technology/ai/why-anthropic-is-targeting-health-systems-with-claude/]. The lab has 11,900+ customers above $100K a year and no customer above 10% of revenue [notes]. At $100M of revenue this startup would spend $6-10M a year on inference, which gives no leverage.
- **Alternatives:** sell the same models to Waystar, athenahealth, Candid, R1 and to the client's own billing office. The deployment ventures have preferred access to private-equity portfolio companies [notes], and private-equity-backed physician groups are the founder's $50M clients.
- **Decision:** signs a standard enterprise agreement with a business associate agreement and zero data retention. Refuses exclusivity, price protection beyond 12 months, any non-compete, and any priority on capacity.
- **Terms:** list price less 0-15% at a $1-5M annual commitment. Model retirement on 6-12 months' notice [DK].
- **Reasons:** the account is small; the deployment venture will pitch the same groups an in-house version that keeps their staff and cuts 30-40% of them.
- **Failure mode:** in June 2026 export restrictions led one lab to disable its top models for all customers for a period [notes]. A billing office with one model supplier stops submitting claims that day.
- **What would change it:** $25M+ annual commitment, or the startup becoming the venture's chosen delivery partner for healthcare portfolio companies.

## Persona 2: Product lead, claims clearinghouse and payments network

- **Who:** owns channel-partner pricing and payer connectivity.
- **Incentives:** transaction volume, protecting payer contracts, selling its own AI. The clearinghouse launched autonomous claim resubmission in Q3 2026 and runs at about a 43% EBITDA margin [notes].
- **Decision:** signs the startup as a channel partner. Does not block it. Refuses data rights and network bypass.
- **Terms [DK]:** claims $0.25-0.45 each; eligibility $0.12-0.25; claim status $0.08-0.15; prior-authorization transactions $0.50-2.00; minimum commitment $150-300K a year for three years; list less 15-25%. Response data may be used only for the submitting client, not for cross-client training. No resale and no use of payer connections to build a competing network.
- **Reasons:** billing companies are a normal channel. The startup's planned "clearing network" is the clearinghouse's own business, so the contract forbids it.
- **Dependencies exposed:** payer enrollment for claims, remittances and electronic funds takes 30-90 days per payer per tax ID if the submitter changes [DK]. Payer-owned portals restrict automated logins and charge for interface access [DK]. A single clearinghouse is a single point of failure, as the February 2024 outage at the largest one showed [DK]. Running two adds 1-2 points of cost.
- **What would change it:** above 20M transactions a year earns top-tier pricing. Nothing earns data rights.

## Persona 3: Partner-program lead, records and practice-management vendor

- **Who:** controls interface access and the marketplace for an ambulatory or post-acute system.
- **Incentives:** protect bundled revenue cycle revenue. One major ambulatory vendor prices its whole platform as a percentage of collections, paid only when the practice collects [source: https://athenahealth.com/why-choose-us/ehr-costs]; third-party estimates put that at 4-8% [source: search summary of review sites, unverified]. It announced AI-native capabilities in August 2026 [source: https://www.athenahealth.com/about/press-releases/ai-native-ehr-capabilities-athenaone]. Other vendors sell billing services at or below 3% [DK].
- **Decision:** admits the startup to the standard partner program. Refuses preferred status, bulk write access to billing tables, and any tolerance for agents logging in as users.
- **Terms [DK]:** $20-60K a year program fee plus 10-25% revenue share or $50-150 per provider per month; certification takes 3-9 months per vendor.
- **Reasons:** a client on a percentage-of-collections platform would pay twice, so the startup is confined to the work the vendor leaves undone. For every other system the vendor's own service is the cheaper bundle. Interfaces cover clinical data well and billing write-back poorly, so the startup either works inside the client's system as named users or runs its own claims engine. The first breaks terms of use. The second forces payer re-enrollment and ends the 45-day claim.
- **Regulatory lever for the startup:** information-blocking rules cover billing records and a post-acute vendor lost a case over blocking automated access [DK]. That helps in court, not in a 45-day implementation.
- **Also:** the 2027 prior-authorization measure for clinicians requires the request to use data from certified records technology [source: https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f]. The records vendor is the gate to the new interface.
- **What would change it:** the startup bringing 200+ of the vendor's practices as a reseller, or giving equity and revenue share as one scribe company did [notes].

## Persona 4: Vice president of payment integrity, large commercial payer

- **Who:** owns denials, pre-payment review, post-payment audit and recovery.
- **Incentives:** medical-cost savings targets; contingency vendors paid 15-25% of recoveries [DK]; exposure to new state laws.
- **Facts:** seven states passed laws in 2026 limiting AI as the sole basis for denials or downcoding, including Washington, Iowa, Alabama, Indiana and Utah, after Arizona in 2025 [source: https://www.beckerspayer.com/policy-updates/7-ai-health-insurance-state-laws-passed-in-2026/]. Denial rates averaged near 12% in 2025 and trade press describes a "battle of the bots" [source: https://www.hfma.org/revenue-cycle/denials-management/battle-of-the-bots-intensifies-over-denials/]. No 2026 data was found on how payers treat AI-written appeals.
- **Decision:** refuses any cooperation. Will not buy payer-side work from a company that files appeals against it.
- **Response to AI appeals at volume [DK]:** move friction from denials, which can be appealed, to front-end edits, documentation requests and pre-payment review; flag providers whose visit-level coding shifts after the vendor arrives; enforce one reconsideration and one appeal within 60-180 days; require portal submission under individual credentials with bot detection; run post-payment audits 12-24 months later.
- **Effect on the founder's numbers:** sustainable lift in net collection rate from appeals is 0.5-1.5 points, not 2 or more [DK]. Recoupments arrive after the vendor has been paid, so the contract must refund fees on clawed-back claims.
- **Prior-authorization interface:** will comply on 1 January 2027 for Medicare Advantage, Medicaid and exchange plans, for items and services but not drugs [notes]. Employer self-funded business is outside the rule.
- **What would change it:** nothing on the provider side. A separately owned and walled-off payer product might be evaluated after 2028.

## Persona 5: Regulator and enforcement view

- **No license is needed to start.** Coders and billers are certified, not licensed [DK]. The brief's "licensed coders" is wrong.
- **Privacy:** the company is a business associate of every client and its model supplier is a subcontractor. Offshore access to patient data is barred by some Medicaid and client contracts [DK]. A breach at a vendor serving 45 clients means 45 notifications.
- **False Claims Act:** the enforcement working group lists record-system manipulation as a priority, and February 2026 inspector-general guidance flagged AI-generated prompts to physicians [source: https://www.proskauer.com/blog/false-claims-act-roundup-series-q1-2026-increased-government-enforcement-efforts-and-circuit-court-developments]. No settlement against an AI coding vendor was found. Lawyers expect the theory to be that AI output was accepted without meaningful review [source: https://blogs.mcguirewoods.com/2026/06/16/ai-assisted-billing-could-create-fca-pitfalls-how-healthcare-companies-can-get-ahead-of-risk/]. Billing companies can be liable for causing false claims, and inspector-general guidance has long treated percentage fees as an upcoding incentive [DK]. A contingency fee, a promise to raise collections by 2 points and an AI coder is the fact pattern a whistleblower's lawyer wants.
- **Other rules [DK]:** Medicare will not pay a billing agent in its own name if its fee depends on collections, so funds must land in the provider's account. New York treats percentage billing fees as fee-splitting, so flat fees are needed there. AI voice calls to patients need prior consent. Collecting patient balances may need state collection licenses. Overpayments must be returned within 60 days of identification.
- **State AI laws** restrict payers, which helps appeals [source: https://www.hklaw.com/en/insights/publications/2026/05/states-continue-efforts-to-regulate-ai-in-healthcare].
- **January 2027 interface rule:** binds payers in regulated lines only; no single national endpoint; providers are not required to use it apart from a clinician quality measure that can be excluded [source: https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f]. It is not a launch-day unlock.
- **Decision:** no approval to grant or refuse. Conditions of operating safely: a named compliance officer, statistically valid coding audits at 95%+ accuracy, human sign-off on high-risk codes, a claim-level record of model version and reviewer kept 6-10 years. Security certification that $50M buyers demand takes 6-12 months and $150-400K [DK].

## Persona 6: Veteran operator, 2,000-person outsourced revenue cycle business

- **Decision:** would not partner or invest at these terms. Would sell the founder an existing billing company.
- **Real cost by setting [DK]:**

| Setting | Market fee | Legacy cost to serve | Note |
|---|---|---|---|
| Specialty physician groups, $50M | 2.5-4.0% | 55-65% of fee with 70% offshore | Best fit |
| Small practices under $5M | 5-8% | 60-70% | High churn |
| Surgery centers | 3.5-5.5% | 55-65% | Implants, out-of-network, workers' compensation |
| Home health | 3-5% or per claim | 65-75% | Records vendors bundle billing |
| Skilled nursing | 2.5-4% or per bed | 65-75% | Medicaid-pending balances keep days in receivables at 45-60+ |
| Medical equipment | 6-10% | 65-75% | Denials 15-25%, constant audits |

- **Five settings are five products.** Pick one.
- **What is truly automatable today:** eligibility, claim submission and electronic posting are already 85-95% automated by existing software, so they free little labor. The labor is in denials, follow-up, prior authorization, coding exceptions, patient calls, enrollment and refunds. AI can take 55-65% of those hours in a clean account and 30-40% in year one.
- **Work missing from the brief:** provider enrollment and credentialing, which is a leading cause of held receivables; front-desk registration errors, which cause a large share of denials and which the vendor does not control; physician peer-to-peer calls; legacy receivables clean-up.
- **Transition:** 90-150 days. The client's billing staff must be rebadged or let go. Parallel running for 30-60 days.
- **Churn:** 8-15% a year; higher where private-equity owners merge groups. Clients of this size demand termination for convenience on 90-180 days' notice, so a three-year term is not three years of revenue.
- **Guarantee:** a well-run group at 96-97% net collection cannot gain 2 points. It will sign, miss and take the refund. Six months has only two to three months of matured claims. The vendor controls write-offs and can inflate net collection rate, and client finance chiefs know it.
- **Capacity:** one six-person implementation team does 1-2 clients of $50M a quarter in year one, 3-4 once the stack is repeated, or 6-8 clients of $5-10M on a template.
- **What would change it:** founder buys a $20-50M-revenue billing firm at 6-9 times EBITDA [DK] to inherit clients, payer enrollments and trained staff, then automates it. That is the roll-up route already funded by larger rivals [notes].

## Persona 7: Errors-and-omissions and cyber insurer

- **Decision:** quotes errors-and-omissions and cyber cover with conditions. Declines the performance guarantee.
- **Terms [DK]:** $5M combined limit at $60-150K premium and a $50-100K retention for a pre-revenue company. Billing-proceedings cover sublimited to $250K-$1M, defense costs mainly. At $100M revenue a $20-25M tower costs $1.5-3M a year, or 1.5-3% of revenue. Conditions: human review on coding, quarterly external coding audit, multi-factor authentication, incident response plan, an affirmative AI endorsement where the form otherwise excludes AI.
- **Exclusions:** contractual guarantees, fee refunds, liquidated damages, knowing violations, treble damages and civil penalties, prior acts.
- **Reasons:** the guarantee is a business risk, not an error. There is no loss history. The research notes found no source on liability terms in outcome-priced AI contracts [notes].
- **Effect:** the guarantee is self-insured from the balance sheet. Clients of this size ask for $5-10M of each cover and uncapped indemnity for privacy breaches and false claims.
- **What would change it:** 12-24 months of audited performance on 10+ clients, a guarantee capped at 25% of fees, and a 20% co-insurance. Then a warranty-style product at 3-8% of the guaranteed amount is possible.

## Persona 8: Senior engineer at a health-AI company, asked to be technical co-founder

- **Decision:** no to this version.
- **Reasons:** five care settings, full scope, 45-day go-live and an uninsurable guarantee is four hard problems at once. Funded rivals are years ahead: one raised a $120M Series D in July 2026, another a $40M Series C in March 2026, with further rounds of $16M, $25M and $27M for denial and coding specialists [source: https://fiercehealthcare.com/health-tech/candid-health-secures-120m-series-d-funding-ai-powered-rcm-ramps; https://fintech.global/2026/03/26/adonis-bags-40m-to-transform-ai-revenue-cycle-management/; https://hitconsultant.net/2026/04/22/amperos-health-16m-series-a-agentic-ai-denial-management-rcm/]. One of them is still estimated at about $57M of revenue after seven years [notes].
- **What breaks first, in order:**
  1. Access. Fifteen-plus practice-management systems with no billing write interface; browser agents on those screens and on payer portals fail on layout changes, multi-factor prompts and bot detection.
  2. Compounding error. At 97% accuracy per step over 12 steps, 69% of claims finish untouched. The other 31% flood the human queue.
  3. Slow feedback. Whether a claim was coded right is known 30-120 days later, and gold-standard audit labels cost money.
  4. Payer rule drift across 1,000+ payers, revised quarterly.
  5. Supplier risk: model retirements, rate limits, the June 2026 shutdown [notes]. Needs two suppliers from day one.
  6. Data rights. Client contracts and clearinghouse terms block cross-client training, so the claimed learning advantage does not accrue by default.
  7. Phone work. Payer call centers with 45-minute holds; some refuse automated callers [DK].
- **Terms to join:** one specialty, two practice-management systems, denials and receivables follow-up first, own claims engine by month 12, $15M+ seed, a co-founder who has run a billing operation, 20-35% equity.
- **What would change it:** three signed design partners on one system with written interface access from the vendor.

---

## Dependencies, approvals and bottlenecks

| Item | Owner | Lead time | Failure mode |
|---|---|---|---|
| Model supply under a business associate agreement | Lab | 2-6 weeks | Outage, retirement, price change, lab competes |
| Clearinghouse channel contract | Clearinghouse | 4-8 weeks | Minimums, no data rights, outage |
| Payer enrollment per tax ID | Each payer | 30-90 days | Blocks go-live if submitter changes |
| Payer portal access | Each payer | 1-4 weeks per payer | Bot detection, terms of use |
| Practice-management integration | Records vendor | 3-9 months per vendor | Fees, refusal of write access, rival bundle |
| Security certification | Auditor | 6-12 months | Blocks $50M buyers |
| Compliance program and coding audit | Company | 3-6 months | False Claims Act exposure |
| Insurance | Carrier | 4-8 weeks | Guarantee excluded |
| Certified coders, billers, enrollment specialists | Labor market | Continuous | Shortage is the brief's own selling point |
| Client's front desk and physicians | Client | Continuous | Vendor is guaranteed against errors it does not control |
| Working capital | Investors | Before first client | $1.0-1.5M deficit per $50M client |

## Probabilities

- First paid commercial delivery within 18 months, this version: **55%**. A small client on a narrowed scope is achievable; a $50M client live in 45 days with the six-month guarantee is not.
- $1 billion of annual recognized revenue within 7 years: **2%**. It needs $22-29B of collections under management, which is 40-50% of the $55B+ that one leading hospital outsourcer manages [notes], assembled from sub-hospital clients while the fee falls.
