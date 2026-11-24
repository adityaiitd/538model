# F1 v1, round 1: delivery, capital and competition panel

Date of simulation: 24 November 2026. Brief tested: `F1_v1.md` (real-work data licensed from enterprises, plus expert quality control of long-horizon agent runs).

Everything below is a simulated hypothesis. No persona is a real person and no order, quote or interview is real.

Evidence labels
- [notes] = `precedents_and_lab_data.md`
- [source: URL] = page opened or search summary obtained in this session (six searches and fetches used)
- [DK] = domain knowledge, unverified
- [calc] = this panel's arithmetic on stated inputs

---

## 0. Facts found in this session that change the brief

The brief treats licensed enterprise work data as an open gap. It is already a funded, crowded category.

| Fact | Label |
|---|---|
| micro1 announced on 9 Oct 2026 a commitment to spend $1bn in twelve months buying and licensing enterprise operational data, financed by Citi and Hercules Capital. It pays $100K to $2M per midsize company, usually wants the whole corpus, targets companies with more than 30 employees, US first. No exclusivity terms are published. | [source: https://letsdatascience.com/news/micro1-commits-1b-to-buy-and-license-enterprise-data-9181fe83] |
| Mercor runs a self-serve enterprise data program: 100+ tool connectors (Slack, Teams, Gmail, Outlook, Salesforce, GitHub, Drive, Notion), eight industries including finance and insurance, flat payout by wire 2 to 4 weeks after signing, no fees, automated anonymization, SOC 2 Type II. No revenue share. | [source: https://www.mercor.com/data/] |
| Other brokers: Polyshares (buys as principal, licences $100K to $2M+, self-reported about $1M revenue in its first month and average deal near $300K, unaudited), Mode (payouts $100K to $5M), Appen, Surge, Turing, SimpleClosure (wind-downs, nearly 100 transactions, $10K to $100K each). | [source: https://dealroom.co/news/170312-ai-data-brokers-are-buying-slack-email-and-crm-from-live-us-companies/] |
| Spirit Airlines bankruptcy auction for de-identified email, Teams and file archives: Google bid about $10M, Mercor about $7.5M, micro1 about $12.5M. A lab bid directly against the brokers. | [source: same dealroom page] |
| Gartner, quoted by Business Insider: AI data spend from under $1bn in 2025 to about $6.5bn in 2027. | [source: same dealroom page, secondary] |
| Employees are "often unpaid and uninformed"; a law professor calls the practice an ethical grey area; experts contest the anonymization claims. | [source: same dealroom page; search summary of MIT Technology Review and Gizmodo coverage, Oct 2026] |
| No page found confirms an outsourcing company selling screen recordings to a lab. The nearest report is Meta logging its own staff's keystrokes and screen snapshots. | [source: search summary, cxtoday.com, not opened] |
| No price per hour of computer-use trace was found. Contractor pay for workflow recording is $25 to $100 an hour in job postings. | [source: search summary, opentrain.ai postings] |

Consequence. The route the founder proposes to "show" is already shown. Supply prices are set by brokers who pay cash in weeks. The one part not yet visibly supplied is prospective screen and tool capture with outcomes from regulated operations, which is also the part with the heaviest legal and security load.

---

## 1. Unit economics computed by the panel

### 1a. Quality control: one billed expert hour

| Line | Brief | Panel | Basis |
|---|---|---|---|
| Billed rate | $250 to $400 | $140 to $220, midpoint $180 | Mercor pays $85 to $95 on average and up to $200, with a markup near 35% [notes]. Bankers are paid about $150 [source: search summary, aiweekly.co]. |
| Expert pay | not stated | $110 (61%) | [notes] ranges |
| Second-level review, 1 reviewer per 10 graders | not stated | $11 | [DK] |
| Rejected or uncredited hours, 8 to 15% | not stated | $18 | [DK] |
| Platform, payments, fraud checks | not stated | $5 | [DK] |
| Gross profit per hour | not stated | about $36, 20% in the first two quarters, 28 to 33% at steady state | [calc]; Mercor's gross margin is 27 to 33% [notes] |

### 1b. Dataset: one corpus of 22,000 verified hours, finance operations, from a 300-seat outsourcing site

| Step | Figure | Label |
|---|---|---|
| Seats 300, opt-in 70%, 25 capturable hours a week, 12 weeks | 63,000 raw hours | [calc] on [DK] assumptions |
| Yield after idle time, duplicates, failed redaction, no outcome match: 35% | 22,000 verified hours | [DK] |
| First-sale price, $50 per verified hour (panel assumption; plausible range $20 to $80) | $1.10M list | No market price exists [notes]. Anchor: a commissioned expert hour costs a lab $130 to $300. |
| Lab rejection and credits 15% | $0.94M net | [DK] |
| Data owner at 35% of net | $0.33M | brief |
| Employee bonuses, 210 people at $300 | $0.06M | [DK] |
| Capture agent deployment and owner integration | $0.06M | [DK] |
| Compute and storage, $1.50 per raw hour | $0.09M | [DK] |
| Human redaction review on a 20% sample, plus task segmentation and outcome linking | $0.30M | [DK]; counsel (persona 2) requires the human pass |
| Legal review and expert determination per corpus | $0.05M | [DK] |
| Gross profit on first sale | about $0.05M, 5% | [calc] |
| Second buyer at 60% of first price | adds $0.56M revenue, $0.33M gross profit | [calc] |
| Third buyer at 35% of first price | adds $0.33M revenue, $0.19M gross profit | [calc] |

| Buyers per corpus | Revenue | Gross margin |
|---|---|---|
| 1 | $0.94M | 5% |
| 2 | $1.50M | 25% |
| 3 | $1.83M | 31% |

The brief's 40 to 45% needs three buyers per corpus and either a price above $70 per hour or no human redaction pass. Panel estimate for the blended business in years one and two: 22 to 32%.

### 1c. Resale to second and third buyers

| Limit | Effect | Label |
|---|---|---|
| Labs pay several times more for exclusivity and non-exclusive products reach rivals within months | Second buyer pays 50 to 70% of the first price, third 30 to 50% | [notes] |
| Each lab has its own format, tool mix and task taxonomy | 40 to 60% of a corpus fits the second buyer without rework | [DK] |
| The owner's licence is non-exclusive both ways, so the owner can also sell the same archive to micro1 or Mercor | A lab that already holds the corpus pays nothing for the duplicate | [source: micro1 and Mercor pages show no exclusivity] |
| Themes rotate every few months | A corpus has 6 to 12 months of sale life | [notes] |
| Panel estimate | 1.5 to 1.8 paid buyers per corpus in years one and two | [calc] |

### 1d. Cash conversion

| Stage | Weeks | Label |
|---|---|---|
| Data owner legal, security and client-consent work | 8 to 16 | [DK] |
| Capture agent rollout | 4 to 8 | [DK] |
| Capture period | 6 to 12 | [DK] |
| Processing and review | 3 to 4 | [DK] |
| Lab acceptance | 2 to 4 | [DK] |
| Payment, net 45 to 60 in practice | 6 to 9 | [DK]; no lab payment terms are disclosed [notes] |
| First owner contact to cash | 29 to 53 weeks | [calc] |

Archive-only deals (documents, tickets, mail) run 12 to 20 weeks, but that is the segment micro1 and Mercor already buy for cash.

Cash tied up at a $40M run-rate, half quality control and half data [calc]:
- Receivables at 75 days: $8.3M
- Less owner share payable on collection: $1.5M
- Advances and minimum guarantees outstanding to owners: $3 to 5M
- Total: $10 to 12M. A receivables line at 80% covers about $6.6M. Equity needed for working capital: $4 to 5M.
- Add net operating burn to month 18 of $6 to 7M (35 to 45 staff, security, legal, less gross profit).
- Total cash need to reach a $40M run-rate: $12 to 18M. The founder's $5 to 10M covers the base case, not the target case.

---

## 2. Delivery personas

### Persona 1. Operations head who ran an expert-data business from $5M to $100M+

- **Incentives and constraints.** Paid on delivered, accepted hours and on gross margin. Has seen two programs end with one email.
- **Alternatives.** Run the quality control line alone as labor resale. Buy archives as principal like the existing brokers.
- **Decision.** Would not take the job as designed. Would take it if the launch were quality control plus archive licences, with screen capture as a funded experiment.
- **Numbers.**
  - Real cost per delivered quality-control hour: $144 on a $180 bill [calc, section 1a].
  - Rejection: 15 to 25% on the first three batches, 8 to 12% once rubrics settle [DK].
  - Staffing: 1 reviewer per 10 graders, 1 program manager per $4 to 6M of annual billing, 6 to 8 people in redaction review per 100,000 verified hours a quarter [DK].
  - Ramp shape: a pilot of $0.1 to 0.5M, then a program of several million, matching [notes] ("pilots a few hundred thousand to $1M, mature programs several million to tens of millions"). Programs end at a model release or a theme rotation with zero to two weeks of notice [notes: Musen ended and was repriced $5 lower].
  - Terms: net 30 to 60 on paper, cash at 45 to 75 days after acceptance. Experts are paid every one to two weeks [DK].
- **Reasons.**
  - Two products need two different operations. Quality control is a workforce business. Data licensing is a legal and engineering business with a 7 to 12 month cash cycle.
  - Yield is the variable nobody has measured. At 20% yield instead of 35%, cost per verified hour rises about 60% and the first sale loses money [calc].
  - A founder with no researcher contacts starts with procurement, and data budgets sit with researchers [notes].
- **What would change the decision.** A measured yield above 35% on a real 5,000-hour capture. A lab research lead who names the spec and accepts a sample. Billed quality-control rate confirmed above $200.

### Persona 2. Privacy and data-protection counsel

- **Incentives and constraints.** Signs the opinion that data owners and labs rely on. Personal and firm exposure if a de-identification claim fails.
- **Decision.** Refuses to give a clean opinion on screen recordings from insurance claims, health-related operations, customer calls or any EU workforce. Will give a qualified opinion on US corporate finance operations and accounting close inside a single company that owns its own data, after an expert determination.
- **What de-identification actually requires.** All [DK] unless marked.

| Regime | Requirement | Effect on the brief |
|---|---|---|
| HIPAA | Sale of protected health information needs individual authorization. De-identified data is outside the rule only by Safe Harbor (18 identifiers removed, including any unique number and full-face images) or Expert Determination. A business associate may de-identify only if its agreement allows it. | Health and disability claims screens are out unless the insurer itself contracts and an expert certifies each corpus. |
| GLBA and Regulation P | A service provider that receives nonpublic personal information may use it only for the purpose it was disclosed for. Aggregate or blind data with no identifiers is outside the definition. | An outsourcer cannot license bank or insurer customer data. Only the institution can, and only after de-identification. |
| US state privacy laws | California covers employee data. "Deidentified" requires reasonable measures, a public commitment not to re-identify and contractual flow-down to every recipient. A sale of identifiable data triggers notice and opt-out. | Every lab contract must carry a no-re-identification covenant with audit rights. Labs resist audit rights. |
| Call recordings | All-party consent states. Callers consented to "quality and training", not to sale for model training. Recent California wiretap cases turn on a vendor's capability to use recordings for its own purposes. | Customer-operations audio is out. Text tickets after redaction are possible. |
| GDPR | Employee consent is rarely valid because of the power imbalance. German works councils have co-determination over monitoring tools. The anonymisation standard is strict and screen video of work will rarely meet it. | No EU or UK capture. US, India and Philippines only, each with its own statute. |
| Contract and professional duty | Outsourcing master agreements bar any use of client data beyond the service. Audit clients are covered by professional confidentiality. Finance screens can show material non-public information and card numbers. | The outsourcer does not own what it would sell. The client must sign, which makes it a three-party deal. |

- **Why automated redaction is not enough.** At 98% recall and 40 identifier instances per hour, 100,000 hours leave about 80,000 exposed instances [calc on DK assumptions]. A human pass on a sample plus expert determination is the minimum. This is why section 1b carries $0.35M of review and legal cost per corpus.
- **Who is liable after a breach.** The data owner stays the regulated party and makes the notifications. The start-up indemnifies, but owners value that indemnity at the insurance limit. A seed-stage company can buy about $5 to 10M of cyber and technology errors cover for roughly $150K to $400K a year [DK]. Labs ask for uncapped or high-cap intellectual property and privacy indemnities and tightened terms after the March 2026 Mercor breach [notes for the breach; DK for the terms].
- **What would change the decision.** Data owner is the principal and its own counsel signs. Capture limited to synthetic or sandboxed copies of systems. Per-corpus expert determination. No audio. No health data.

### Persona 3. Security engineer who must pass a frontier lab's vendor review

- **Incentives and constraints.** Judged by whether the company passes review and never becomes the next Mercor.
- **Decision.** Can pass a restricted pilot review in 2 to 4 months. Cannot pass full review for programs touching unreleased model outputs before month 9 to 12.
- **Requirements and cost.** All [DK].
  - SOC 2 Type I in 6 to 8 weeks. Type II needs a 3 to 6 month observation window, so the report arrives in month 6 to 9. ISO 27001 often requested as well.
  - Separate tenant per lab. No shared graders across labs on the same project without the lab's consent.
  - Graders on managed browsers or virtual desktops. No local download of agent runs.
  - Annual penetration test, single sign-on, immutable access logs, sub-processor list, 24 to 72 hour breach notice.
  - First-year cost $0.6 to 1.2M including two or three security hires.
- **The harder review is on the supply side.** The capture agent records screens on machines that process regulated data. The data owner's own security office must approve it. At a bank or insurer that takes 3 to 9 months and often ends in refusal. At a mid-market outsourcer it takes 4 to 8 weeks, but then the outsourcer's clients must be told.
- **Reasons.** The quality-control product puts unreleased model behaviour in front of outside contractors, the exact exposure behind Meta's pause [notes]. One incident ends the company, because unlike Mercor it has no other lab revenue to fall back on.
- **What would change the decision.** $1M security budget approved before the first pilot. Capture done inside the owner's environment with only redacted output leaving.

### Persona 4. Staff engineer at a data-tooling company, asked to join as technical co-founder

- **Incentives and constraints.** Total compensation about $600K to $900K. Has offers from funded suppliers whose equity is priced at $1bn to $20bn [notes for the valuations; DK for the pay].
- **Alternatives.** Join a 2025-founded supplier at a $100M+ run-rate with lab researchers on the cap table. Start a narrower tooling company selling redaction or capture to all the brokers.
- **Decision.** No as offered. Yes at 20 to 25% equity with standard vesting, $250K salary, and three things in hand first: one lab research lead who has written the spec, two data owners signed with counsel's opinion, and $5M closed.
- **What breaks first, in order.** [DK]
  1. Yield. Real work is 50 to 70% email, waiting and repetition. The share of hours with a linkable outcome is unknown.
  2. Redaction in video. Free-text fields, scanned documents, chat pop-ups and second monitors defeat pattern rules. Every miss is a reportable event.
  3. Capture on locked-down endpoints. Citrix, virtual desktops and endpoint protection block or degrade recording agents.
  4. Lab specifications. Formats change each quarter and each lab differs, so the "standard unit" is not standard.
  5. Outcome linking. Matching a trace to the final claim decision or the closed ledger needs access to the system of record, which widens the legal scope.
- **Reasons.** Nothing in the build is protected. Mercor already advertises automated extraction and anonymization across 100+ tools [source: mercor.com/data]. A competent team reproduces the pipeline in 6 to 9 months.
- **What would change the decision.** Evidence that labs pay more than $70 per verified hour for screen traces. An exclusive supply agreement with real volume.

---

## 3. Capital and competition personas

### Persona 5. Skeptical venture investor

- **Asked for.** $5 to 8M seed now, $20 to 40M later.
- **Incentives and constraints.** Needs a path to a $1bn+ outcome. Has seen the category's revenue quality: one-off orders, two or three buyers, gross billing.
- **Alternatives.** Put the same money into a supplier already at a $100M+ run-rate, or into a broker with first-month revenue.
- **Decision on the seed.** Refuses $5 to 8M at a $30 to 40M post-money valuation. Would sign a term sheet for $4M at $16M pre-money, half released at close and half on a first lab purchase order of at least $250K plus two data owners under licence with an outside legal opinion.
- **Decision on the later round.** Refuses until all four hold: $15M recognized in the trailing six months, three or more buyers with none above 45%, gross margin of 30% or more on audited numbers, and repeat orders from two buyers.
- **Reasons.**
  - Revenue quality. Quarterly orders, no commitments, a six to twelve month product life [notes]. The investor counts it as repeat purchase-order revenue and values it on gross profit.
  - Concentration. Most firms in the category have one to three customers. Mercor draws 91% from foundation-model companies [notes].
  - Comparison. micro1 has $1bn of bank-financed buying power in this exact product. Mercor has the connectors and the lab accounts. AfterQuery's angels are lab researchers [notes]. The founder brings sales skill, which every funded rival also has.
  - Founder fit. Strong on the supply side, where enterprise selling matters. Weak on the demand side, where researchers decide.
- **Value.**

| Gross revenue | Gross margin | Gross profit | Hot market (leaders at about 10x run-rate, about 30x net [notes]) | Normal market (2 to 4x gross profit; Appen fell from $4.3bn to about one times revenue [notes]) | Investor's working figure |
|---|---|---|---|---|---|
| $40M | 28% | $11M | $150M to $300M, discounted for concentration | $25M to $45M | $80M to $150M |
| $100M | 32% | $32M | $500M to $1bn | $65M to $130M | $250M to $500M |

- **What would change the decision.** An exclusive, multi-year supply agreement with a top-ten outsourcer or insurer. A named lab research lead as an angel or adviser. Evidence of resale to three buyers.

### Persona 6. Lender asked to finance lab receivables and advances to data owners

- **Incentives and constraints.** Credit committee, advance-rate policy, concentration limits of 25 to 35% per obligor unless the obligor is investment grade [DK].
- **Decision on receivables.** Not at launch. Yes after two quarters of collection history with at least two obligors: a $3 to 5M revolving line, later up to $10M.
- **Terms.** All [DK].
  - Advance 85% on accepted invoices to investment-grade obligors (Alphabet, Microsoft, Meta, Amazon). 70% on unrated labs.
  - Eligible only after written acceptance and under 90 days old. Dilution reserve of 10 to 15% for rejections and credits.
  - Rate about 9 to 11% all-in plus an unused fee. First lien on all assets. Springing cash dominion. Minimum liquidity covenant of six months of fixed costs.
  - Anti-assignment clauses in lab agreements must be waived or the lender relies on the statutory override for accounts.
- **Decision on advances to data owners.** Refuses. An advance is an unsecured prepayment for an intangible licence that cannot be repossessed or resold by a lender. Advance rate 0%.
- **Reasons.**
  - The receivable exists only after acceptance, so the lender finances the last 60 days, not the 6 to 10 months before it.
  - Concentration. With two obligors, one pause cuts the borrowing base in half within a month.
  - The Citi and Hercules financing for micro1 [source: letsdatascience page] was written against a $1bn run-rate and a $4bn equity valuation, not against a start-up.
- **What would change the decision.** Purchase orders with take-or-pay minimums. A third obligor. $10M or more of junior equity in the company.

### Persona 7. Incumbents responding rationally

**(a) The largest expert marketplace**
- Already runs the program [source: mercor.com/data]. No new decision is needed.
- Response: raise payouts to owners in the entrant's target domains. A flat wire in two to four weeks beats a 35% share of uncertain sales from an unknown company. Bundle licensed data into existing lab labor contracts at low or no margin.
- Can pay owners 60 to 80% of the lab price because its margin comes from labor [calc on notes' 33% gross margin].
- Would buy the entrant only for a supply contract or a team, at well under $50M. It bought Sepal and Deeptune [notes].

**(b) A 2025-founded supplier at a $100M+ run-rate**
- Already sells finance reasoning data and has lab staff as angels [notes].
- Response: add capture of its own experts doing real tasks in replica tools, which avoids enterprise privacy law entirely. Sign the two or three best data owners exclusively with minimum guarantees the entrant cannot match.
- Tells labs that staged expert traces with clean rights are safer than enterprise traces with contested consent.

**(c) Labs' in-house data teams**
- Sources they already have: own enterprise customers under design-partner agreements, own employees [notes: The Information headline], direct bids in auctions (Google bid about $10M for Spirit) [source: dealroom page], and an in-house human-data platform [notes].
- Decision: signs a pilot purchase order of $150K to $400K for a novel, well-documented corpus. Refuses any quarterly commitment. Refuses exclusivity pricing from an unproven vendor.
- For quality control: buys from the two or three vendors already cleared, at $130 to $200 an hour. A new vendor gets a 500 to 1,000 hour trial if a researcher sponsors it.
- Provenance diligence requires the vendor to name the source. The lab then knows whom to call.

**(d) A large outsourcing company deciding whether to sell its own data**
- Does not own client data. Its master agreements bar secondary use [DK].
- What it can sell: its own back-office work, internal process documents and client-approved programs.
- Decision: refuses a 35% share from a start-up. Would accept a fixed fee or minimum guarantee of $1 to 5M a year, non-exclusive, from the bidder with the largest balance sheet. That is micro1 or a lab directly.
- Larger outsourcers prefer a direct lab partnership that also advances their own automation. A broker's cut adds nothing they need.
- Signs with a start-up only for a small, low-risk program to learn the price, then renegotiates or leaves.

**(e) Enterprise-software or workflow-recording vendor that already captures this data**
- Customers own the data. The vendor's terms let it use opted-in telemetry for its own models, not sell it.
- Response: keep the data to train its own agents. Tighten export terms so bulk extraction for third-party training breaches the customer's licence. A messaging platform did this to its interface terms in 2025 [DK].
- Effect: connector-based extraction, the cheapest supply route, can be closed by the platform owner at will.
- Would not partner. Might appear as a buyer (persona 8).

### Persona 8. Head of applied AI at a large enterprise-software company

- **Incentives and constraints.** Ships agents inside its own suite. Has in-product telemetry but nothing on what users do in other tools. Budget of $5 to 15M a year for outside data and evaluation. Procurement takes three to five months [DK].
- **Alternatives.** Its own customers under opt-in. Commissioned expert traces from an existing supplier. The existing brokers.
- **Decision.** Signs a pilot purchase order: $200K for 4,000 verified hours in accounts payable and month-end close, $50 an hour, with outcome labels, a provenance file, a no-re-identification covenant and an indemnity backed by at least $5M of insurance.
- **Refuses.** Quarterly orders of $1 to 5M. Any corpus with audio or health data.
- **Follow-on.** $1.0 to 1.5M a year if its internal evaluation shows a measurable lift on its own agent benchmarks.
- **Quality control.** Would buy 500 hours at $160 to $200 to grade its finance agent. Uses its own customer-success staff for the rest.
- **Reasons.** Cross-application traces are the one thing it cannot collect. Legal exposure is the gating item, more than price.
- **What would change the decision.** A second corpus from a different owner that reproduces the lift. Clean expert determination.

---

## 4. Questions the task set

**What happens when the largest buyer pauses?**
- With two or three buyers the largest is 45 to 60% of revenue. Revenue halves within days [notes: Meta and Mercor, Scale, micro1 losing 60% overnight].
- Fixed costs continue: about $7 to 9M a year at a $40M run-rate [calc]. Advances already paid to owners are sunk. Minimum guarantees stay owed.
- The receivables line shrinks at the same moment (persona 6).
- Survival needs six months of fixed costs in cash and no guarantee longer than one quarter.

**Do data owners or labs cut out the middleman?**
- Labs: yes for large owners. Provenance diligence names the source, and a lab has already bid directly at auction.
- Large owners: yes. They take fixed fees from the largest bidder or deal with a lab.
- Small and mid-size owners: no. Below 30 to 50 employees diligence costs kill deals [source: dealroom page], and mid-size firms need a broker. That is the long tail, and micro1 and Mercor already serve it.

**What accumulates?**
- Capture and redaction pipeline: reproducible in 6 to 9 months.
- Supply contracts: non-exclusive, so no.
- Catalogue: yes, but with a 6 to 12 month sale life.
- Grader calibration data and rubrics: partly. Graded runs belong to the lab.
- A clean legal and security record: real, slow to build, lost in one incident.

**Does scale make it more defensible or merely larger?**
- Mostly larger. Fixed security and legal costs spread over more revenue, and a wider catalogue helps cross-sale.
- The buyers remain the same five to eight organisations and the supply remains non-exclusive.
- It becomes defensible only with exclusive multi-year supply, which needs minimum guarantees and therefore the capital the incumbents already have.

---

## 5. Panel revenue estimate

Clock starts January 2027. Prices: datasets $50 per verified hour first sale, quality control $180 an hour. All [calc] on the panel's assumptions.

### Base case, first six quarters

| Quarter | Dataset buyers and domains | Dataset revenue | Quality-control hours and buyers | Quality-control revenue | Total |
|---|---|---|---|---|---|
| Q1 | None. Pipeline build, SOC 2 Type I, two owners in legal | $0 | Recruit 150 graders | $0 | $0 |
| Q2 | Enterprise-software buyer pilot, accounts payable, 3,000 hours | $0.15M | 1,000 hours, one lab trial | $0.18M | $0.33M |
| Q3 | Lab A, finance operations, 10,000 hours. Software buyer second batch | $0.70M | 2,500 hours, one lab | $0.45M | $1.15M |
| Q4 | Lab A repeat. Lab B pilot, insurance property claims text | $1.30M | 6,500 hours, two buyers | $1.20M | $2.50M |
| Q5 | Lab A two domains, Lab B, software buyer. First resale of a corpus | $2.20M | 13,000 hours, two labs | $2.40M | $4.60M |
| Q6 | Three buyers, three domains (finance operations, accounting close, claims text) | $3.00M | 19,000 hours | $3.50M | $6.50M |

### By year

| Period | Low case (35%) | Base case (50%) | High case (15%) |
|---|---|---|---|
| Year 1 (Q1 to Q4) | $1M | $4M | $14M |
| Trailing twelve months at month 18 (Q3 to Q6) | $3M | $15M | $42M |
| Year 2 (Q5 to Q8) | $4M | $29M | $70M |
| Year 3 | $5M or wound down | $50M | $120M |

- High case requires a lab research sponsor by month 3, one owner with 1,000+ seats, and quality control scaling as pure labor resale.
- Low case is one failed redaction, one refused security review at an owner, or no lab sponsor.
- Base case mix by year 3: quality control 55%, datasets 45%. Buyers: two labs, two enterprise-software companies, one smaller model developer.

---

## 6. Numbers in the brief the panel disputes

| Brief | Panel | Basis |
|---|---|---|
| Dataset licences $1 to 5M per quarter per buyer per domain | Pilot $0.15 to 0.5M, then $0.5 to 1.5M per corpus, one-off | Licensed operational datasets run $50K to $1M+ [notes]. Average broker deal near $300K [source: dealroom page]. A whole airline's archive drew $7.5 to 12.5M [same]. |
| Quality control $250 to 400 an hour | $140 to $220 | Expert pay $85 to $200 with about a 35% markup [notes] |
| Owners accept a 35% revenue share | Owners take flat cash, $100K to $2M, in two to four weeks. Effective supply cost 45 to 60% of sales after unearned advances | [source: micro1 and Mercor pages] |
| Gross margin 40 to 45% | 22 to 32% in years one and two | [calc, section 1] |
| Five buyers at $2M a quarter | Two to three buyers at $0.5 to 1.5M a quarter by month 18 | [notes: most firms have one to three customers] |
| $5 to 10M covers the plan | $12 to 18M of cash to reach a $40M run-rate | [calc, section 1d] |
| AfterQuery and Fleet as precedents | Not comparable. Both produce data with their own contractors or engineers. Neither depends on an enterprise's legal department. | [notes] |
| Enterprise work data is under-supplied | Archive data is now supplied by at least six funded brokers. Only regulated screen traces with outcomes remain open. | [sources in section 0] |

---

## 7. Verdicts

| Persona | Decision | Terms they would accept |
|---|---|---|
| 1. Operations head | Refuses the design | Quality control plus archive licences first. Screen capture as an experiment. |
| 2. Privacy counsel | Refuses clean opinion on claims, calls, health, EU | Owner as principal, expert determination per corpus, US corporate finance only |
| 3. Security engineer | Pilot review in 2 to 4 months. Full review month 9 to 12 | $0.6 to 1.2M first-year budget |
| 4. Staff engineer | Refuses | 20 to 25% equity, a lab spec, two owners signed, $5M closed |
| 5. Venture investor | Refuses $5 to 8M | $4M at $16M pre-money in two tranches |
| 6. Lender | Refuses at launch. Refuses owner advances outright | $3 to 5M line after two quarters, 70 to 85% advance, 9 to 11% |
| 7a. Largest marketplace | Competes on owner payouts | Acquires for team or supply under $50M |
| 7b. 2025 supplier | Competes with staged traces and exclusives | None |
| 7c. Lab in-house team | Signs a pilot purchase order | $150K to $400K, no commitment |
| 7d. Large outsourcer | Refuses revenue share | $1 to 5M fixed, non-exclusive, from the largest bidder |
| 7e. Software or recording vendor | Refuses. Tightens export terms | None |
| 8. Enterprise-software buyer | Signs a pilot purchase order | $200K for 4,000 hours at $50. Then $1.0 to 1.5M a year on proven lift |

## 8. Panel's four numbers

| Measure | Estimate |
|---|---|
| Probability of a first paid commercial delivery within 9 months | 70% |
| Probability of $40M gross recognized revenue in a trailing twelve months by month 18 | 5% |
| Probability of $100M by month 36 | 7% |
| Year five, if it works | $150 to 250M gross revenue, 30 to 35% gross margin, equity value $300 to 700M |

Revenue type: one-off and repeat purchase orders. It is neither recurring nor contracted beyond a quarter.
