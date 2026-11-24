# C3 v1 demand panel, round 1 (simulated, 24 Nov 2026)

Brief tested: `C3_v1.md` (AI-run billing office, 4.5% of net collections, three-year contract, 45-day go-live, +2 points net collection rate and -20% days in AR within six months or fees refunded).

Everything below is a simulated hypothesis from archetype personas. It is not customer validation. No real people, quotes or orders.

Evidence labels: [source: URL], [notes] = founder's research notes, [DK] = domain knowledge, unverified.

Web searches run: 8 of 8. None returned a current MGMA cost-to-collect benchmark for physician groups, a published volume-discount tier for large groups, or any AI-native vendor's fee schedule. Those three gaps matter and are filled with [DK] below.

---

## Facts checked before the panel

| Fact | Value | Label |
|---|---|---|
| Hospital cost-to-collect best practice | fell from 3% to 2% of cash | [source: https://www.hfma.org/revenue-cycle/kpis/7295/] (dated, hospital-only) |
| Outsourced billing, market range | 4-10% of net collections; 5-8% for small to mid-sized practices | [source: https://www.carepatron.com/blog/how-much-do-medical-billing-services-cost/] (vendor blog) |
| Size discount | solo practice 10-12%, multi-provider group 4-7%; one vendor advertises from 2.99% | [source: web search summary of vendor blogs, 24 Nov 2026; originating pages not individually verified] |
| athenahealth pricing | custom, usually a percentage of collections, third-party estimates 4-8%; clearinghouse included | [source: https://www.business.com/reviews/athenacollector], [source: https://softwarefinder.com/emr-software/athenahealth/pricing] (unofficial) |
| Candid Health | $120M Series D, July 2026; >$219M raised; 200+ organisations; clients are medical groups, MSOs, digital health, EMR companies; 190% growth in contracted run-rate | [source: https://www.businesswire.com/news/home/20260721951537/en/], [source: https://fiercehealthcare.com/health-tech/candid-health-secures-120m-series-d-funding-ai-powered-rcm-ramps] |
| Commure | $70M at $7B, May 2026; claims >85% of revenue cycle work completed without a human; 500+ organisations; expanding into specialty practices | [source: https://www.commure.com/press-releases/commure-raises-70m-at-7b-valuation-to-transform-healthcare-operations-using-ai] (company claim) |
| Procode AI | $10M Series A, July 2026, AI billing for private-practice surgeons, bought a billing firm | [source: https://hitconsultant.net/2026/07/28/procode-raises-10m-series-a-ai-surgical-rcm-billing/] |
| Homecare Homebase | sells its own Revenue Cycle Services to multi-state home health and hospice operators | [source: https://www.prweb.com/releases/homecare-homebase-revenue-cycle-services-increase-visibility-and-flexibility-setting-new-industry-standards-302181666.html] |
| MatrixCare | sells RCM, coding and documentation review for home health and hospice | [source: https://www.matrixcare.com/revenue-cycle-management-rcm-for-home-health-and-hospice] |
| Tennr | $101M Series C at $605M (June 2025); deepest vertical is DME; does prior-authorization submission in payer portals | [source: https://fortune.com/2025/06/18/tennr-health-tech-ai-patient-referral-ivp-a16z-lightspeed-iconiq-series-c/], [source: https://www.mobihealthnews.com/news/tennr-openai-test-ai-agents-prior-authorization] |
| Waystar | 42.8% EBITDA margin; launched autonomous claim resubmission Q3 2026; performance contracts defer its revenue | [notes] |
| Epic Penny | AI billing/coding used by 200+ organisations | [notes] |
| Lab deployment ventures | $5.5B of capital, preferred access to the PE investors' portfolio companies | [notes] |

---

## Persona 1. CEO, PE-backed orthopedic/GI management services organisation

**Who.** 120 physicians, 9 acquired practices, 4 surgery centers, $180M collections. Central billing office of 70 US staff plus an offshore vendor doing coding and AR follow-up. Sponsor is in year 3 of a 5-year hold.

**Incentives and constraints.** EBITDA at exit. Lender covenants on leverage. Physician partners paid on collections, so any cash dip is felt in their monthly draw. A three-year contract outlives the hold period and must be assignable to a buyer.

**Actual cost to collect.** [DK]
- 70 in-house staff at $62K loaded: $4.3M
- Offshore vendor, 60 seats at about $28K: $1.7M
- Clearinghouse, statements, lockbox, tools: $0.9M
- Management and compliance audit: $0.6M
- Total $7.5M = 4.2% of collections. Net collection rate 95.5%. Days in AR 41.

**4.5% versus current.** $8.1M, which is $0.6M more than today. The only case for buying is the 2-point lift ($3.6M). He does not believe 2 points exists above 95.5% once workers' compensation and personal-injury lien receivables (about 12% of orthopedic revenue [DK]) are excluded.

**Alternatives.** (a) Offshore-enabled incumbent quoting 2.8-3.5% at this volume [DK]. (b) ModMed's own billing service, since GI and orthopedics are that vendor's core specialties [DK]. (c) Candid or Commure, which have named MSOs as a target segment and far more capital [source: Business Wire, Commure release above]. (d) His sponsor's own AI programme: the lab deployment ventures get preferred access to PE portfolios [notes], and a sponsor would rather own the capability than rent it at 4.5%.

**Decision.** Refuses the three-year contract. Runs a **paid pilot**: one newly acquired 12-physician practice ($16M collections) plus all denials older than 120 days across the group.

**Terms.** Pilot practice at 3.5% of collections; aged denials at 12% of cash recovered. Six months. Full-group price he would sign later: 3.0% base plus 20% of collections above an audited baseline, termination for convenience on 90 days after month 12, free assignment on change of control.

**Reason.** The fee is above his cost, the lift is unproven, and the downside (physician cash) is his job.

**What would change it.** Two referenceable orthopedic or GI groups above $50M with 12 months of audited cohort data; price at or below 3.5%; guarantee backed by escrow.

---

## Persona 2. COO, multi-state home health and hospice operator

**Who.** 38 branches in 7 states, $150M revenue: 60% home health, 40% hospice. Homecare Homebase. Central billing team of 34 plus outsourced OASIS and coding review.

**Payer facts.** [DK] Hospice is about 90% Medicare per diem; collection is near 100% once the notice of election is timely. Home health is roughly half Medicare fee-for-service under 30-day payment periods and half Medicare Advantage paid per visit with heavy authorization. Several of her states are under Medicare's pre-claim review demonstration.

**Actual cost to collect.** [DK] Billing and collections about 2.3% of revenue ($3.4M). Outsourced coding and OASIS review about $35 per chart, another $1.2M. Hospice alone runs under 1%.

**4.5% versus current.** $6.75M against $4.6M including coding. On the hospice book she would be paying 4.5% ($2.7M) for work that costs her about $0.5M. Refused outright for hospice.

**Guarantee.** Meaningless on Medicare fee-for-service where net collection is already about 99%. A vendor paid on collections who touches diagnosis coding under the home health payment model is an audit target; the clawback lands on her provider number.

**Alternatives.** Homecare Homebase's own revenue cycle service [source: PRWeb above]; MatrixCare-type bundled services [source]; specialist home health billing firms at 2-4% [DK].

**Decision.** Refuses the contract. **Paid pilot** limited to Medicare Advantage authorizations and Medicare Advantage receivables in two states.

**Terms.** $18-25 per authorization obtained, plus 10% of cash recovered on Medicare Advantage receivables older than 90 days. No percentage on Medicare fee-for-service or hospice. If it converts: blended fee no higher than 2% of home health collections, hospice excluded or at 0.75%.

**Reason.** The pain is Medicare Advantage authorizations and underpayments, not the whole revenue cycle. One flat percentage across her payer mix overcharges on the easy 70%.

**What would change it.** Segment pricing by payer; written agreement that vendor bears audit recoupments caused by its coding; proof the vendor can operate inside Homecare Homebase without that vendor's objection.

---

## Persona 3. CFO, 300-bed community hospital system on Epic (outside target)

**Who.** $450M net patient revenue, 2 hospitals, 140 employed physicians. Runs Epic as a hosted instance from a larger regional system [DK: common arrangement for hospitals this size].

**Actual cost to collect.** 2.9% ($13M) [DK; consistent with HFMA 2-3% best practice, source above].

**4.5% versus current.** $20.3M. A $7M increase. Not a conversation.

**Constraints.** Bond covenant on days cash on hand; a 10-day cash dip during transition is a reportable event [DK]. She cannot grant a third party build access to Epic without the host system and Epic agreeing [DK]. Epic's own AI billing tool is already at 200+ organisations [notes]. End-to-end outsourcers offer rebadging of her staff and balance-sheet-backed guarantees at about 3-4.5% of net patient revenue [DK]; Ensemble alone manages $55B [notes].

**Decision.** **Refuses.** No pilot of the product. The only door open is a pure contingency review of already written-off denials and underpayments at 15-20% of recoveries [DK], which is a different, commoditised business with many vendors.

**Reason.** Price is 55% above her cost, the vendor has no Epic access path, and the board would not put $450M of cash through a start-up.

**Verdict on the boundary.** The "not on Epic" boundary is real and should be treated as hard. The founder's growth plan step "then hospitals" has no visible entry.

**What would change it.** Nothing within three years short of an Epic-sanctioned integration, a price under 2.5%, and an investment-grade guarantor.

---

## Persona 4. Owner, durable medical equipment supplier

**Who.** $24M revenue: sleep therapy and resupply, oxygen, mobility, glucose monitors. Brightree. 31 staff in intake, documentation, authorization and billing. Owner signs alone.

**Actual cost to collect.** [DK] About 10.5% of revenue ($2.5M) when intake, documentation chasing and authorizations are included; billing-only outsourcing quotes run 5-9%. Write-offs from missing documentation about 9% of billed.

**4.5% versus current.** $1.08M against $2.5M. This is the only persona for whom the price is plainly attractive, **if** the scope includes intake and documentation chasing (physician office phone and fax), which is where his cost sits. If the founder's scope starts at a clean order, the saving falls to roughly $0.5M and he loses interest.

**Trust in AI.** High for documentation qualification and resupply; he already evaluated Tennr [source above]. Low for anything that could trigger a Medicare audit extrapolation.

**Alternatives.** Brightree's own billing service [DK]; Tennr for intake [source]; offshore billing at 4-6% [DK].

**Decision.** **Paid pilot**, converting to a contract. Six months on the sleep and resupply line ($9M of collections) at 4.5%. Will then sign three years **only** with termination for convenience on 60 days after month 12.

**Terms.** 4.5% accepted. Vendor absorbs fee on any recouped claim and pays 50% of audit recoupments traced to its documentation decisions. Scope must include intake.

**Reason.** Clear saving, single decision-maker, no committee. But he is small: $1.08M a year at full conversion, and his 9%-of-billed documentation problem is labor-heavy for the vendor.

**What would change it to an immediate three-year signature.** A reference from another supplier on Brightree and the exit clause.

**Note for the founder.** Most suppliers are under $20M revenue and the national consolidators run billing in-house [DK]. This segment says yes fastest and is worth least per client.

---

## Persona 5. CFO, physician group

**Who.** Physician-owned multispecialty and orthopedic group, 70 physicians, $90M collections, on athenaOne. Monthly partner draws tied to collections. $6M revolving credit line with a fixed-charge covenant.

**Actual cost to collect.** [DK] athenahealth fee about 4.5% of collections ($4.05M) covering software, clearinghouse, claim submission and part of denial work [range 4-8% per source above]; in-house staff of 22 at $1.4M (1.6%). Total about 6.1%, of which only 1.6% is labor the founder can replace.

**4.5% versus current.** The founder's fee stacks on top of the athenahealth fee unless the group changes its practice management system, which it will not do. Net: pays $4.05M to replace $1.4M of staff. Refused on arithmetic.

**Cash flow.** Billing transitions typically cost 10-25% of cash for 60-120 days [DK]. At 15% for 90 days that is $3.4M, more than half the credit line, and it lands in partner draws. First cash from a new vendor's claims arrives 30-45 days after first submission; legacy receivables must be run out by the old team for 90-120 days, so he pays twice for a quarter.

**Guarantee.** Capped at fees refunded. Six months of fees is $2.0M against a plausible $3.4M shortfall. It is a rebate from a company that may not exist, paid after the damage. The measures are gameable by the party holding the pen: net collection rate rises if the vendor reclassifies write-offs as contractual adjustments; days in AR falls 20% if old balances are written off.

**Decision.** **Refuses** the contract. Would authorise a **paid pilot** only on denials and receivables older than 120 days at 10-12% of recoveries.

**Terms he would sign for full scope.** Fee no higher than the labor replaced (about 1.5% here; 3.0-3.5% for a group with no percentage-based software fee). 25% of fees held in third-party escrow until guarantee measured. Net collection rate measured by date-of-service cohort, adjustment codes controlled by the group, audited by his accountants. SOC 1 Type II report, since the vendor posts cash. $10M errors-and-omissions and $10M cyber cover. Termination for convenience on 90 days.

**What would change it.** Escrow or a letter of credit; an audited reference; a price that nets against what athenahealth already charges.

---

## Persona 6. Compliance and procurement lead

**Who.** Chief compliance officer who also runs vendor risk for a multi-site provider group. Has a veto, not a vote.

**Findings.** [all DK unless marked]
1. **Liability stays with the provider.** Claims go out under the group's identifiers. False Claims Act exposure is treble damages plus roughly $14,000-$28,000 per claim. The vendor's standard liability cap (12 months of fees) does not cover it.
2. **The incentive design is the problem.** A percentage of collections plus a bonus-like guarantee for raising collections 2 points, with coding done autonomously and humans seeing only exceptions, is the fact pattern federal guidance on third-party billing companies warns about. She requires a certified coder's sign-off on 100% of claims for the first 90 days and a 5% independent audit sample after, at 95% accuracy. That removes most of the claimed automation in year one.
3. **Percentage fees are restricted in some states.** New York treats percentage-based billing fees as fee-splitting; such clients need flat or per-claim pricing. Medicare reassignment rules require payments to land in an account the provider controls.
4. **Security review.** Since the 2024 clearinghouse breach, third-party risk is a board item. Minimum: SOC 2 Type II, penetration test, named sub-processors, business associate agreements flowing down to every model provider with zero retention and no training on patient data. A start-up needs 6-12 months of operating history for Type II; a HITRUST certificate takes 9-15 months.
5. **Offshore.** Medicare Advantage plans require offshore attestations; several state Medicaid contracts and at least two state laws restrict storing patient records abroad. US-only processing, including human reviewers, must be contractual. This raises the founder's cost to serve.
6. **Payer portals.** Most portal terms prohibit automated access and shared credentials. The January 2027 interfaces [notes] cover Medicare Advantage, Medicaid and exchange plans only, exclude drugs, and do not cover employer-sponsored commercial plans, which are most of an orthopedic group's revenue.
7. **AI-written appeals** carrying clinical assertions need clinician attestation.

**Decision.** **Blocks** signature of the three-year contract as drafted. Will approve a limited **pilot** after an 8-10 week security and legal review.

**Terms.** Uncapped indemnity for coding errors and data breach; $10M+ insurance; right to audit; US-only; human sign-off as above; exit assistance for 180 days.

**What would change it.** SOC 2 Type II in hand, an external coding audit history, and an insurer-backed indemnity.

---

## Persona 7. IT lead, practice management and EHR systems

**Who.** Runs the practice management system and interfaces for a group that has grown by acquisition, so he has three systems: athenaOne, eClinicalWorks and NextGen. Peers in post-acute run PointClickCare, Homecare Homebase and Brightree.

**Access reality by system.** [DK unless marked]

| System | How a third party gets in | Does the vendor bundle billing? |
|---|---|---|
| athenahealth | Works as users inside the system or via marketplace partner programme with fees. Cannot replace athenahealth's claim engine. | Yes. Billing work is part of the percentage fee [source above]. Now marketed as "AI-native" [source: https://www.athenahealth.com/]. |
| eClinicalWorks | User logins; limited interfaces | Yes. Own service advertised at about 2.9% of collections. |
| NextGen | Interfaces available; own service arm | Yes |
| ModMed | Partner programme | Yes, own billing service, roughly 4-7% |
| PointClickCare | Marketplace partner programme; history of blocking automated access | Partly |
| Homecare Homebase | Closed; partner approval needed | Yes [source: PRWeb above] |
| Brightree | Limited interfaces | Yes |

**Effort.** With logins and screen automation: fast to start, breaks on every vendor release, and may breach vendor terms. With certified partner access: 3-9 months per vendor and a revenue share to the vendor of perhaps 10-20%. Client-side effort: half an engineer for three months plus the security review.

**Go-live.** 45 days is not credible. Re-pointing electronic remittance and payment enrollments with payers takes 30-90 days by itself. If the vendor works inside the existing system and clearinghouse and changes no enrollments: 75-100 days. If it brings its own clearinghouse: 120-180 days. Each additional practice management system is a separate project.

**Decision.** No signature authority. **Recommends against** the three-year contract; supports a pilot on one system with read-only access for 30 days first.

**What would change it.** Certified partner status with his specific vendors and a named reference on the same system and version.

---

## Persona 8. Director of the existing billing office

**Who.** Runs 70 staff at the organisation in persona 1. Twenty years in. Her staff are the ones replaced.

**Interest.** Keeping the department, stated plainly. But her operational objections are factual. [DK]
- About 40-50% of denials originate at registration and scheduling (eligibility, wrong plan, missing referral). The vendor does not control the front desk and will blame it when the guarantee is missed.
- Credentialing and enrollment gaps for newly acquired physicians cause a large share of the rest. Out of the vendor's scope.
- Workers' compensation and personal-injury liens are paper, state fee schedules and attorney negotiation. AI vendors exclude them or do them badly.
- Implant and surgery-center billing has contract-specific carve-outs that live in her team's heads.
- The transition depends on her staff transferring knowledge while knowing they are being let go. Attrition in the 45 days will cause the cash dip. Retention bonuses for 40 key staff at $7,500 each: $300K, not in the founder's model.

**Counter-proposal: buy software, keep the function.** AI coding at roughly $1-3 per encounter, automated claim status and resubmission from the clearinghouse (Waystar launched this in Q3 [notes]), AI follow-up agents priced per task. Cut 25 of 70 seats by attrition over 12 months and reduce the offshore vendor by half. Result: cost to collect from 4.2% to about 3.1% ($5.6M), saving $1.9M with no cutover risk and no three-year lock. This beats the founder's 4.5% by $2.5M a year before any collection lift.

**Decision.** **Opposes.** Will cooperate with a pilot on receivables older than 120 days and low-balance denials her team does not reach, at contingency.

**What would change it.** An offer to rebadge her team into the vendor (as hospital outsourcers do) with 12-month employment guarantees. That makes the founder a labor-heavy outsourcer on day one.

---

## Cross-persona answers to the test questions

- **Actual cost to collect.** Hospital 2.9%; home health and hospice 2.3% (3.1% with coding); specialty MSO 4.2%; physician group on percentage-priced software 6.1% of which 1.6% is replaceable labor; DME 10.5% including intake. [DK]
- **Does 4.5% beat it?** Only for DME, and only if intake is in scope.
- **What they pay incumbents.** 2.8-3.5% quoted to $100M+ groups; about 2.9% from one EHR vendor; 2-4% in home health; 5-9% in DME; 4-8% athenahealth all-in. [DK, sources above]
- **Switching risk.** 10-25% of cash for 60-120 days; larger than six months of fees, so the fee-refund guarantee does not cover it. [DK]
- **Trust in AI coding and appeals.** Finance and compliance require human sign-off for at least 90 days and audit sampling after.
- **EHR vendor bundling.** Yes in six of the seven systems named.
- **Sales cycle and go-live.** $50M+ groups: 6-12 months to sign, 75-180 days to go live, so 9-18 months from first meeting to steady cash. DME owner: 1-3 months to sign. [DK; Waystar's own "longer implementation cycles" in notes]
- **Software in-house instead?** Preferred by personas 1 (partly), 3, 7 and 8.

## Numbers in the brief disputed

| Brief | Panel's corrected value | Basis |
|---|---|---|
| Incumbents charge 4-8% | 5-8% only for small practices; 2.8-4% at $50M+ of collections | sources above plus [DK] |
| 4.5% is a discount | At or above actual cost for every persona except DME | persona arithmetic [DK] |
| Go-live in 45 days | 75-180 days after signature | persona 7 [DK] |
| +2 points net collection rate | Achievable only where baseline is under about 93%; well-run targets sit at 95-97% | [DK]; creates adverse selection |
| Guarantee "affordable" | Expect 30-50% of early clients to miss at least one prong at month 6; refund exposure up to 100% of first-half fees | panel estimate |
| Cost to serve 40% in year one | 70-100% with US-only staff and mandated human sign-off; 45-60% with an offshore blend that compliance restricts | $50M client today uses about 40 staff; $0.9M buys 15 US staff |
| Cost to serve toward 20% | 35-45% at maturity; 43% EBITDA is Waystar's software margin, not a service margin | [notes], [DK] |
| 45 clients averaging $50M | First 30 clients more likely average $10-25M, so $100M of revenue needs 110-220 clients at 4.5%, more at market price | persona 4 is the fast yes |
| "Few vendors offer outcome pricing" | Percentage of collections has been the standard physician billing price for decades | sources above |
| January 2027 mandate as a trigger | Binds payers, covers government-programme plans only, excludes drugs; delivered to providers through their EHR vendor | [notes], [DK] |

## Panel probabilities

- First paid commercial delivery within 18 months: **70%** (almost certainly a DME supplier or a small group, or a contingency pilot on aged receivables, not a $50M three-year contract).
- $1 billion of annual recognized revenue within 7 years: **2%**. It needs $22B of collections under management at 4.5%, or about $33B at the 3% large groups will pay, against funded AI-native rivals and EHR vendors that own the system access.
