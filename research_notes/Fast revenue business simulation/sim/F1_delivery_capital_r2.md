# F1 v2, round 2: delivery, capital and competition panel

Date of simulation: 24 November 2026. Brief tested: `F1_v2.md` (expert quality control of long-horizon agent runs billed by the hour, with per-corpus data sales second). Same personas as round one (`F1_delivery_capital_r1.md`).

Everything below is a simulated hypothesis. No persona is a real person and no order, quote or interview is real.

Evidence labels
- [notes] = `precedents_and_lab_data.md`
- [r1] = this panel's round-one transcript and its sources
- [source: URL] = page opened or search summary obtained in this round (four web checks used)
- [DK] = domain knowledge, unverified
- [calc] = this panel's arithmetic on stated inputs

---

## 0. Facts found this round

| Fact | Label |
|---|---|
| Mercor pays contractors on a weekly cycle. It pays out over $2M a day to more than 30,000 weekly active contractors. | [source: https://mercor.com/blog/when-you-go-from-2-million-a-month-to-2-million-a-day] |
| Derived: $2M a day is about $730M a year, or about $24,000 per weekly active contractor. At $85 to $95 an hour that is about 270 hours a year, or about 5 hours a week each. | [calc] on the source above and [notes] pay rates |
| Mercor's first year: "mid-seven figures in revenue", bootstrapped through referrals. Then $50M annual run-rate in Nov 2024, $75M in Feb 2025, $100M in Mar 2025. 30 US staff and about 20 India contractors at $50M. It charged about 30% on top of the contractor's pay rate. | [source: https://ainativegtm.substack.com/p/from-zero-to-100m-arr-in-11-months], tagged [W] in the notes |
| Derived: a 30% markup on pay is a 23% gross margin on the bill, before review and payment costs. Reported gross margin was 27% in 2025 and 33% in Q2 2026. | [calc]; [notes] |
| Mercor's contractor payouts are estimated at 60 to 70% of gross revenue. | [source: search summary of sacra.com/c/mercor, estimate] |
| AfterQuery's Series A was $30M at a $300M valuation, announced when it reported a $100M run-rate. That is 3 times gross run-rate. The later $3.2bn figure is unconfirmed. | [source: search result title, pulse2.com, page not opened]; [notes] |
| AfterQuery has nearly 100,000 domain experts in finance, software, medicine and law. No gross margin or hourly pay was found. | [source: search summary, sacra.com/c/afterquery] |
| No source states the payment terms labs give suppliers. | [notes]; unchanged after this round's searches |

Consequence. The model v2 copies is the one with the best-verified fast ramp. The two leaders took about two years from founding to a $40M run-rate (Mercor: founded Jan 2023, $1M at end-2023, $34.6M to $50M at end-2024 [notes]). The 6 to 12 month ramps in the notes are measured from first meaningful revenue, not from founding.

---

## 1. Round-one objections against v2

| # | Round-one objection | Status | Why |
|---|---|---|---|
| 1 | The category is already occupied by funded brokers with up to $1bn | Unresolved, moved | The data line retreats to opportunistic sales. The lead product now enters a larger and more occupied category: Mercor about $3bn, micro1 and Handshake about $1bn each [notes]. |
| 2 | Supply is non-exclusive and owners want fast cash | Partly | No speculative purchases removes inventory risk. But owners get 48-hour cash offers [r1], so a buyer who must first find a lab order wins few corpora. Experts are also non-exclusive: they work for several platforms at once [DK]. |
| 3 | Corpus gross margin is 5% with one buyer | Resolved | Corpus margin is no longer the plan. A back-to-back order covering cost gives 10 to 25% on the few corpora sold [calc]. |
| 4 | Regulated screen traces are blocked by title and privacy law | Resolved | Dropped. Residual: insolvency archives still hold employee and customer personal data and may need a consumer privacy ombudsman's review [DK]. |
| 5 | One buyer pausing halves revenue and the borrowing base together | Unresolved | The brief concedes it. Termination moved from quarterly to 30 days, which makes it worse. |
| 6 | Labs do not sign quarterly licences | Resolved by design | Weekly hours on purchase orders match how labs buy. Revenue is now terminable at 30 days. |
| 7 | Price of $250 to $400 an hour | Resolved | v2 adopts $140 to $220. |
| 8 | Gross margin of 40 to 45% | Partly | v2 claims 30 to 35%. Panel: 22 to 26% in year one, 27 to 32% at steady state (section 2a). |
| 9 | $5 to 10M does not cover the plan | Partly | Cash need falls to $11 to 14M. With a receivables line the equity need is $7 to 9M, inside the founder's range but with no reserve for a pause (section 2c). |
| 10 | Full security review takes until month 9 to 12 | Partly | Trials can run inside the lab's own tooling, which shortens the first review to 6 to 10 weeks. Standing programs on unreleased models still need SOC 2 Type II [DK]. |
| 11 | The technical build is copyable in 6 to 9 months | Unresolved | v2 has less technology than v1. Calibration with reported inter-rater agreement is standard practice at the large suppliers [DK]. |
| 12 | Revenue is one-off, with two or three buyers | Unresolved | Repeat weekly orders, same two or three buyers. |
| 13 | The founder has no route to the researchers who hold the budget | Unresolved | Not addressed. |

---

## 2. Unit economics for v2

### 2a. One billed review hour at $180

| Line | Brief | Panel, first two quarters | Panel, steady state | Basis |
|---|---|---|---|---|
| Expert pay | 60 to 65% | $115 (64%) | $108 (60%) | Senior reviewers cost more than the $85 to $95 Mercor average [notes] |
| Calibration overlap: 5 to 12% of hours double-reviewed and not billable | not stated | $12 | $6 | [DK]. The brief's own differentiation creates this cost. |
| Second-level review and program management | not stated | $9 | $6 | [DK] |
| Rejected or credited hours | not stated | $10 | $5 | [DK] |
| Payment fees, fraud checks, identity verification | not stated | $4 | $3 | [DK] |
| Gross profit | $54 to $63 (30 to 35%) | $30 (17%) | $52 (29%), range 27 to 32% | [calc]. Mercor: 23% implied early, 27% in 2025, 33% in Q2 2026. |

Year-one average: 22 to 26% [calc].

### 2b. Experts needed for $40M

| Step | Brief | Panel | Basis |
|---|---|---|---|
| Billed hours at $180 | 220,000 | 220,000 | agreed |
| Worked hours including overlap and rejections | not stated | about 260,000 | [calc] from 2a |
| Hours per active expert per week | 12 to 17 (implied by 250 to 350 people) | 5 to 7 | Mercor's weekly actives average about 5 hours [calc on source]. Senior people with other work give less, not more. |
| Weekly active experts | 250 to 350 | 750 to 1,000 | [calc] |
| Vetted bench, with 50 to 60% active in any week | not stated | 1,400 to 1,800 | [DK] |
| Applicants screened at a 10 to 20% pass rate | not stated | 8,000 to 15,000 | [DK] |

### 2c. Working capital

| Input | Brief | Panel | Basis |
|---|---|---|---|
| Experts paid after | 2 to 4 weeks | 1 week | Mercor pays weekly [source]. A new platform cannot pay slower than the leader and keep senior reviewers. |
| Work to cash from lab | 45 to 60 days | 70 to 80 days | Monthly invoicing in arrears adds about 15 days, acceptance about 10, then net 45 to 60 [DK] |
| Working capital per $10M of annual billing | about $1.1M (implied) | $1.9M, range $1.6 to 2.3M | [calc]: receivables 75 days of $27,400 a day is $2.05M, less 8 days of expert payables at 62% |
| At $40M of annual billing | about $4.3M | $7.5M | [calc] |
| Operating burn to month 18, net of gross profit | not stated | $4 to 6M (25 to 35 staff, security, legal, recruiting) | [calc] |
| Total cash need to a $40M run-rate | $5 to 10M | $11 to 14M | [calc] |
| Receivables line at 80% of eligible billed invoices | not stated | about $4 to 5M | Unbilled work is not eligible (persona 6) |
| Equity need | $5 to 10M | $7 to 9M, with no reserve | [calc] |

---

## 3. Delivery personas

### Persona 1. Operations head who ran an expert-data business from $5M to $100M+

- **Decision.** Would take the job. This is a business the persona knows how to run. Refuses to sign up to $40M by month 18.
- **Terms.** Budget for 750 to 1,000 weekly active reviewers, weekly pay, a recruiting and vetting team of 6 to 8 from month one, and a fraud function.
- **Reasons.**
  - The ramp is gated by the first lab sponsor, then by vetted supply. Vetting senior practitioners runs 60 to 120 a month per recruiter team at the start [DK]. Reaching 1,500 vetted takes 9 to 12 months.
  - Standing weekly programs exist, but labs run them by project, 4 to 12 weeks at a time, and re-award on quality scores [DK]. Musen ended and was repriced $5 lower [notes].
  - What fails first: reviewers pasting model-written critiques, account sharing, and identity fraud. Each needs detection before the lab finds it [DK].
  - Review of a multi-hour run takes 1 to 3 expert hours. Labs will sample, not review everything, so hours per program are capped by the lab's sampling rate [DK].
- **What would change the decision on the target.** A named lab research sponsor by month 3 and a first program above $1M a quarter by month 6.

### Persona 2. Privacy and data-protection counsel

- **Decision.** Gives a clean opinion on the quality-control service. Gives a qualified opinion on corpus sales with clean title.
- **New exposures in v2.** All [DK] unless marked.
  - Reviewers employed by banks, broker-dealers, insurers and audit firms need outside-activity approval. Registered persons must disclose it. Audit staff face independence rules. Most employers will refuse work for an AI lab that touches their field.
  - Reviewers write corrections from experience. Labs require a warranty that no employer confidential information is used. The company gives that warranty and cannot verify it.
  - Contractor classification. The largest marketplace already faces contractor lawsuits [notes]. Weekly standing programs with set rubrics and calibration look more like employment than project work.
  - Insolvency archives: a court order transfers title but not freedom from privacy law. Where the debtor's privacy policy barred sale of personal data, the sale needs a privacy ombudsman's review.
- **Liability.** Breach exposure now centres on the lab's unreleased model outputs, not on personal data. The lab's contract will put uncapped confidentiality liability on the vendor.
- **What would change the decision.** Nothing needed for the service. For corpus work: the insolvency estate or the owner gives the privacy representations.

### Persona 3. Security engineer who must pass a lab's vendor review

- **Decision.** Trial review passes in 6 to 10 weeks if reviewers work inside the lab's tooling on lab-issued accounts. Standing programs on pre-release models need SOC 2 Type II, month 7 to 10.
- **Cost.** $0.5 to 0.9M in year one, lower than v1 because there is no capture agent and no owner-side review [DK].
- **Reasons.**
  - v2 concentrates the company on the exact exposure behind Meta's pause of Mercor: outside contractors seeing unreleased model behaviour [notes].
  - With 750 to 1,000 part-time reviewers on personal devices, managed browsers or virtual desktops are mandatory. Cost $40 to $80 per reviewer per month [DK].
  - One leak by one reviewer ends the largest program. The company has no second revenue line to survive on.
- **What would change the decision.** Reviewer work confined to lab-hosted environments by contract.

### Persona 4. Staff engineer asked to join as technical co-founder

- **Decision.** Refuses, more firmly than in round one.
- **Reasons.**
  - v2 is a staffing and operations company. The engineering is payouts, fraud detection, a review interface and calibration statistics. Mercor describes that stack publicly [source: mercor.com blog].
  - Equity in resold labor at a 30% gross margin is worth less than an offer from a supplier already at a $100M+ run-rate.
  - The company needs a head of operations and a senior engineer on salary plus 1 to 2%, not a technical co-founder.
- **What breaks first.** Fraud detection, then payout reliability, then per-lab rubric tooling.
- **What would change the decision.** A lab asking the company to build grading tooling it would license. Nothing in the brief suggests that.

---

## 4. Capital and competition personas

### Persona 5. Skeptical venture investor

- **Decision on the seed.** Refuses $5 to 8M at $30 to 40M post-money. Signs $4M at $16M pre-money, half at close and half on a first lab purchase order of at least $250K. Same price as round one. The data-owner condition is dropped.
- **Decision on the later round.** Refuses until: $10M recognized in the trailing six months, two labs with neither above 55%, audited gross margin of 27% or more, and one program renewed twice.
- **Reasons.**
  - v2 is cleaner to underwrite because the comparables exist. It is also, by the brief's own words, resold labor.
  - The precedents were first or early. micro1 lost 60% of its revenue overnight and Mercor's first year was mid-seven figures [notes; source]. An entrant in 2027 faces three suppliers above $1bn.
  - No researcher access and no exclusive supply. The finance background helps recruit dozens of senior reviewers, where the plan needs 750 to 1,000.
- **Value.**

| Gross revenue | Gross profit at 27 to 32% | Today's market: 3 to 10 times gross run-rate (AfterQuery at 3 times, leaders about 10 times) | Normal market: 2 to 4 times gross profit | Investor's working figure |
|---|---|---|---|---|
| $40M | $11 to 13M | $120M to $400M | $25M to $50M | $100M to $180M |
| $100M | $28 to 32M | $300M to $1bn | $60M to $130M | $250M to $500M |

- **What would change the decision.** A lab research lead as angel or adviser. A second domain where the company is the lab's top-scored vendor.

### Persona 6. Lender

- **Decision.** Improved. Offers a $2 to 3M receivables line after one full quarter of collected invoices, rising to $8 to 10M. Refuses to lend against unbilled hours or purchase orders.
- **Terms.** 85% advance on billed, accepted invoices to investment-grade obligors, 70% on unrated labs. About 9 to 11% all-in. First lien. Six months of fixed costs as minimum liquidity. All [DK], modelled on staffing-receivables lending.
- **Reasons.**
  - Hourly billing against timesheets is a familiar asset. The round-one refusal on owner advances no longer applies.
  - Concentration remains. With one obligor above 50%, the lender caps that obligor at 50% of the base unless investment grade.
  - A 30-day termination right means the base can fall by half in one cycle while weekly payroll continues.
- **What would change the decision.** A second obligor. Notice periods of 90 days.

### Persona 7. Incumbents

**(a) The largest expert marketplace**
- Does nothing while the entrant is under $20M. Above that, raises pay for the entrant's top-scoring reviewers, who already hold accounts on its platform [DK].
- Offers the lab review hours bundled with data programs at a 20 to 25% margin, below the entrant's cost structure [calc on notes].

**(b) A 2025-founded supplier at a $100M+ run-rate**
- Finance is its home domain and it has nearly 100,000 experts [source: search summary]. It already runs multi-stage checks on its own data.
- Sells the lab "review by the people who built the dataset". Its lab-researcher angels hear about new review programs first [notes].

**(c) Labs' in-house data teams**
- Review of long-horizon runs sits in the same human-data budget, with the same operations team and the same cleared vendors. It is not a separate budget [DK].
- Decision: signs a trial purchase order for 500 to 1,000 hours at $160 to $200, so $80K to $200K, if a researcher has an unfilled review need. Labs do add vendors: one uses more than a dozen for environments [notes].
- Refuses a standing commitment. Scales a vendor only on measured agreement with its own gold set.
- Moves the routine 60 to 70% of review to model graders and keeps humans for disputed and high-stakes runs [DK]. One lab is building its own human-data platform and hiring reviewers directly [notes].

**(d) A large outsourcing or professional-services company**
- New and more dangerous in v2. It employs thousands of accountants, claims specialists and finance staff with cleared employment, managed devices and security certifications already in place.
- Sells review to labs at $150 to $250 an hour as part of a wider alliance. Its staff need no outside-activity approval because the work is the employer's [DK].

**(e) Enterprise-software or workflow vendor**
- Not a competitor in v2. Appears only as a buyer (persona 8).

### Persona 8. Head of applied AI at a large enterprise-software company

- **Decision.** Signs a trial purchase order: 500 hours at $180, $90K, to review its finance and close agents against real outcomes.
- **Follow-on.** $0.8 to 1.5M a year as a standing program if reviewer findings reduce its agents' error rate on its own benchmark. Does not exceed $2M.
- **Refuses.** Corpus purchases above $300K without seeing lift first.
- **Reasons.** It lacks an in-house reviewer bench and the large marketplaces prioritise the labs. A smaller vendor that answers within a day has an opening here.
- **What would change the decision.** Nothing needed for the trial. Scale depends on measured lift.

---

## 5. Questions the brief asked

| Question | Panel answer |
|---|---|
| Why would a lab add a small vendor? | For a trial, because good review supply is short and a trial is cheap. For scale, only if the vendor scores above incumbents on the lab's gold set in a domain the lab is pushing that quarter. |
| Is long-horizon review a separate budget? | No. Same purchase, same team, same cleared-vendor list. |
| One buyer pauses | Half of revenue goes in a week, weekly payroll stops with it, fixed costs of $5 to 7M a year continue, the borrowing base halves. |
| Is this a product company? | No. It is a staffing company with a quality method. |
| Do labs in-house or automate review? | Both, for the routine share. Human review of hard, long runs stays outsourced for the next two years, at falling prices [DK]. |

**What accumulates.** Approved-vendor status at two or three labs (9 to 12 months to earn, lost in a day). Performance history on about 1,500 reviewers, who also work for rivals. Rubrics and calibration data by domain. Reviewed runs belong to the lab. Nothing prevents a rival from matching it.

**Scale.** Larger, slightly more defensible through vendor status and fixed-cost absorption. Mercor's gross margin rose from 27% to 33% as it grew [notes], so scale helps margin, but does not reduce buyer concentration.

---

## 6. Panel revenue estimate for v2

Clock starts January 2027. Review hours at $180. Corpus sales included at one in year one and two in year two, $0.5M each. All [calc].

| Period | Low (35%) | Base (50%) | High (15%) |
|---|---|---|---|
| Q1 | $0 | $0.05M | $0.3M |
| Q2 | $0.15M | $0.4M | $1.5M |
| Q3 | $0.4M | $1.5M | $4.5M |
| Q4 | $0.9M | $3.2M | $9.5M |
| Q5 | $1.2M | $5.5M | $14M |
| Q6 | $1.5M | $7.5M | $17M |
| Year 1 | $1.5M | $5M | $16M |
| Trailing twelve months at month 18 | $4M | $18M | $45M |
| Year 2 | $6M | $33M | $80M |
| Year 3 | $8M | $55M | $140M |

- Base case buyers: one lab program reaching $3 to 4M a quarter by Q6, a second lab at $1.5 to 2M, two enterprise-software buyers at $0.3M each, one corpus sale.
- Base case domains: corporate finance and accounting first, insurance from Q4, software operations from Q5.
- High case needs a lab sponsor by month 2 and 600 active reviewers by month 9.
- Low case is a trial that does not convert, or a security or fraud incident in the first program.
- Compared with round one's v1 base case ($15M at month 18, $50M in year three), v2 is about 10 to 20% higher. Weekly hours do ramp faster than corpus sales, but the gate is the same lab sponsor.

---

## 7. Numbers in the brief the panel disputes

| Brief | Panel | Basis |
|---|---|---|
| Gross margin 30 to 35% | 22 to 26% in year one, 27 to 32% at steady state | Section 2a |
| 250 to 350 part-time experts | 750 to 1,000 weekly active, 1,400 to 1,800 vetted | Section 2b |
| Experts paid in 2 to 4 weeks | 1 week | Mercor pays weekly [source] |
| Labs pay in 45 to 60 days | 70 to 80 days from work to cash | [DK] |
| $5 to 10M covers $40M of billing | $1.9M of working capital per $10M of billing; $11 to 14M total cash need; $7 to 9M equity with a line | Section 2c |
| Two or three labs at $10 to 20M a year each | One lab at $12 to 16M a year and one at $6 to 8M by month 18 in the base case | Section 6 |
| Weekly hours ramp faster | Yes, by 10 to 20% | Section 6 |
| Standing programs, 30 days' notice | Projects of 4 to 12 weeks, re-awarded on quality scores, ended at will in practice | [DK]; [notes] |

---

## 8. Verdicts

| Persona | Decision | Terms they would accept |
|---|---|---|
| 1. Operations head | Accepts the job. Refuses the $40M date | 750 to 1,000 active reviewers, weekly pay, fraud team |
| 2. Privacy counsel | Clean opinion on the service | Employer-approval and no-confidential-information warranties from every reviewer |
| 3. Security engineer | Trial in 6 to 10 weeks. Standing programs month 7 to 10 | $0.5 to 0.9M year one, work inside lab tooling |
| 4. Staff engineer | Refuses | None as co-founder |
| 5. Venture investor | Refuses $5 to 8M | $4M at $16M pre-money, half on a $250K lab order |
| 6. Lender | Offers a line after one quarter of collections | $2 to 3M rising to $8 to 10M, 70 to 85% advance, 9 to 11% |
| 7a. Largest marketplace | Ignores, then bids for the reviewers | None |
| 7b. 2025 supplier | Competes in finance | None |
| 7c. Lab in-house team | Signs a trial purchase order | 500 to 1,000 hours at $160 to $200, no commitment |
| 7d. Large outsourcer | Enters with employed staff | None |
| 7e. Software vendor | Not a competitor | n/a |
| 8. Enterprise-software buyer | Signs a trial purchase order | $90K for 500 hours, then $0.8 to 1.5M a year on measured lift |

## 9. Panel's four numbers for v2

| Measure | v1 | v2 |
|---|---|---|
| Probability of a first paid commercial delivery within 9 months | 70% | 80% |
| Probability of $40M gross recognized revenue in a trailing twelve months by month 18 | 5% | 7% |
| Probability of $100M by month 36 | 7% | 9% |
| Year five, if it works | $150 to 250M gross, 30 to 35% margin, $300 to 700M | $150 to 300M gross, 27 to 32% margin, $250 to 700M |

Revenue type: repeat weekly purchase orders, terminable at 30 days. It is neither recurring in the contractual sense nor contracted.
