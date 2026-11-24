# C3 v1, capital and competition panel, round 1

Date of simulation: 24 November 2026. Everything below is a simulated hypothesis from archetype personas, not customer or investor validation. No real person is quoted.

Evidence labels: [notes] = the founder's research notes (ai_services.md, biotech_health.md); [source: URL] = checked in this session (8 web calls used; several via search summary only, marked "summary"); [dk] = domain knowledge, unverified.

---

## 0. Panel's own numbers (used by all personas)

### 0.1 Facts checked

- Percentage-of-collections billing fees: most quotes for small and mid-sized practices 5-8%, range 4-10%; one offshore-backed vendor advertises from 2.99% [source: https://www.carepatron.com/blog/how-much-do-medical-billing-services-cost/ ; https://medsolercm.com/blog/medical-billing-services-cost , summary].
- athenahealth's own published estimate: practices spend about 3-4% of revenue on collections-related cost [source: https://newmarketpitch.com/blogs/news/ai-revenue-cycle-management-business-model].
- R1 RCM: taken private at $8.9B enterprise value (Aug 2024); 2023 revenue about $2.25-2.3B, adjusted EBITDA $614M. Implied 3.9x revenue, 14.5x EBITDA, 27% EBITDA margin (panel arithmetic) [source: https://www.fiercehealthcare.com/finance/towerbrook-cdr-take-health-tech-company-r1-rcm-private-89b-deal , summary].
- Waystar: 2026 revenue guidance $1.277-1.287B, 42.8% adjusted EBITDA margin, 1,488 clients above $100K; its acquired AI unit (Iodine) is seeing revenue deferred as clients move to performance contracts; autonomous claim resubmission launched Q3 2026 [notes].
- Funded AI revenue-cycle competitors: Candid Health $120M Series D (July 2026, Sixth Street Growth), about $219M raised in total, 190% growth in contracted run-rate and 180% net dollar retention in 2025, valuation tripled since Feb 2025 [source: https://fortune.com/2026/07/22/candid-health-raises-120-million-to-take-on-americas-280-billion-medical-billing-mess/ , summary]; claims >95% touchless on a defined workflow [source: newmarketpitch URL above]; revenue about $57M (estimate) [notes]. Adonis $40M Series C, March 2026 [source: https://hitconsultant.net/2026/03/25/adonis-40m-series-c-funding-ai-revenue-cycle-management-claim-denials/ , summary]. Amperos $16M Series A (Bessemer) for denial agents [source: https://hitconsultant.net/2026/04/22/amperos-health-16m-series-a-agentic-ai-denial-management-rcm/ , summary]. Arintra $25M Series B and Charta $55M Series B (autonomous coding and chart review) [source: https://www.fiercehealthcare.com/finance/arintra-banks-25m-series-b-funding-round-ai-driven-revenue-assurance-platform , summary]. Smarter Technologies about $150M revenue; Commure $7B valuation; Epic's Penny billing agent at 200+ organizations [notes].
- Legal: percentage-based billing fees are treated as fee-splitting in New York (and barred for New York Medicaid billing agents); Florida has been listed as restrictive; Illinois voided such contracts until a statutory carve-out; federal Medicare rules allow a percentage fee only where the agent does not receive the payment; the OIG flags percentage fees as an upcoding risk [source: https://www.foley.com/insights/publications/2008/07/illinois-law-prohibits-percentagebased-compensatio/ ; https://www.hbma.org/rcmadvisor/january-february-2026-volume-31-issue-2/percentage-based-medical-billing , both via summary; sources are partly old and should be re-checked by counsel].
- Theoretical fee pool: hospital plus physician and clinical spending about $2.74T (CMS 2024); 1% is $27B, 3% is $82B [source: newmarketpitch URL above]. Revenue cycle outsourcing sized at about $34B [notes].

### 0.2 Numbers in the brief the panel disputes

| Brief | Panel figure | Basis |
|---|---|---|
| 4.5% undercuts incumbents at 4-8% | 4-8% is the price for practices under about $5M. A $50M group pays 3.0-4.0% outsourced or spends 3-4% in-house. 4.5% is at or above its current cost. | athenahealth 3-4% estimate [source]; 2.99% advertised floor [source]; eClinicalWorks has advertised its billing service near 2.9% [dk] |
| Average client $50M | First 10 clients average $10-20M; 100 clients average about $20-25M | A physician collects roughly $0.7-1.3M a year, so $50M is 40-70 physicians, the top of the 20-500 clinician band; groups that size usually have a central billing office or belong to a private-equity platform [dk] |
| Go-live in 45 days | 90-150 days to full claim flow | Payer electronic enrollment (claims, remittance, funds transfer) takes 30-90 days per payer; practice-system integration; parallel run [dk] |
| Cost to serve 40% in year one | 65-90% of revenue in a client's first year including implementation | Third-party pass-through (clearinghouse, eligibility, statements, payments) 8-15%; inference and voice calls to payers 7-13%; reviewers, coders, account management 22-31%; implementation $150-300K per client [dk, panel build] |
| Cost to serve falls to 20% | 40-50% at 4.5%; worse as the fee falls | R1 at scale earned 27% EBITDA [source]; no outsourcer discloses 80% gross margin; cost floor of about 0.8-1.2% of collections for pass-through plus exceptions [dk] |
| $100M needs $2.2B under management | Correct arithmetic, but it needs $2.2B live for a full year; at the panel's 5-year fee (about 2.5%) it needs $4B | See 0.3 |
| Prior-auth mandate in Jan 2027 creates demand | The mandate binds payers (Medicare Advantage, Medicaid, CHIP, exchange plans), not commercial employer plans, and the provider-side incentive runs through certified EHR technology | CMS-0057-F [notes]. It lowers prior-auth labor for every vendor and favours the EHR vendor. |
| Guarantee "refunded to cover the shortfall" | As worded, uncapped. A 2-point shortfall on $50M is $1M a year against $2.25M of fees. | Panel arithmetic |

### 0.3 Fee path, five years (panel estimate, $20-50M groups)

| Year | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---|---|---|---|---|
| Fee, % of net collections | 4.0-4.5 | 3.6 | 3.1 | 2.7 | 2.2-2.5 |

Reasons: (1) at least seven funded AI vendors plus incumbents with 27-43% EBITDA margins that can give up 100 basis points [notes][source]; (2) offshore outsourcers already quote about 3% [source]; (3) software vendors unbundle to per-claim prices ($2-5 per claim is 1.6-4% of collections at about $125 per claim, falling toward $1-2 for clean claims) [source: newmarketpitch; dk]; (4) support resolution fell from $1.90 to $0.99 once incumbents matched [notes]. The price does not go to the support-ticket floor, because pass-through and exception handling cost about 1% of collections, and small practices keep paying 4-5% because service cost per account is fixed. Three-year contracts delay repricing by one renewal, no more.

### 0.4 Cash and guarantee, one $50M client (panel build, [dk])

- Steady fee $187.5K a month. Sign at month 0, go-live month 4, fees ramp 15% / 55% / 85% / 100% over months 5-8 because the fee follows cash from new claims (30-50 days to payment). Invoices monthly in arrears, paid in about 45 days.
- Cash out: customer acquisition $200K, implementation $250K, running cost $112K a month from go-live.
- Trough about month 7: minus $0.75M (34% of annual contract value). Six months after go-live: invoiced $853K, collected $478K, spent $1.12M, net minus $0.64M.
- Cumulative cash breakeven 16-18 months after signing; 22-24 months if a refund is paid. Add six to nine months of sales cycle before signing.
- Guarantee: fees at risk in the window $853K. Probability of missing at least one metric at six months: 40% (range 30-55%). Reasons: days in receivables usually rise during a vendor transition; net collection rate can only be measured on cohorts aged about 120 days, so only one or two months of the vendor's own claims are measurable; groups already at 95-97% have less than 2 points of headroom; front-desk errors and late physician sign-off stay with the client. Expected refund at 50% of at-risk fees: $170K per client, 20% of first-six-month fees, about 2.6% of three-year contract revenue. That is affordable if capped at fees paid. Uncapped, tail loss is $0.5-1.0M per client, and adverse selection (well-run groups sign for six free months) can push the miss rate above 60%.
- Accounting: refundable fees are variable consideration; revenue in the guarantee window is constrained until the test is passed. Waystar's Iodine disclosure is the live example [notes].
- For 45 clients in 24 months: peak working capital $20-30M, guarantee reserve $8-15M, operating burn $40-60M a year. Reaching $100M needs roughly $150-250M of equity. Consistent with "enterprise health AI gets to $100M in five to seven years with $500M+ raised" [notes].

### 0.5 Revenue, margin and value at 10, 100 and 1,000 clients (panel estimate)

| | 10 clients | 100 clients | 1,000 clients |
|---|---|---|---|
| Plausible date | mid-2028 | 2030-31 | 2033-35, if ever |
| Average collections per client | $15M | $22M | $25M |
| Blended fee | 4.0% | 3.6% | 2.6% |
| Contracted run-rate | $6M | $79M | $650M |
| Recognized revenue (ramp, constraint) | $2.5-3.5M | about $65M | about $600M |
| Gross margin | 10-20% | 45-50% | 50-55% |
| EBITDA | minus $18-25M | minus 5% to plus 5% | 20-25%, about $130-150M |
| Rational acquirer value | $15-40M (team and code) | $200-400M (3-5x revenue) | $1.7-2.2B (12-15x EBITDA, R1 multiple) |
| Venture or public value | $80-200M post-money on narrative | $0.6-1.0B growth round | up to $3.3B at 5x revenue |
| Top-client share of revenue | 25-30% | 5-8% | under 2% |

Founder's own assumptions at 1,000 clients ($50M average, 4.5%, 80% gross margin) give $2.25B revenue and perhaps $17-25B of value. Even that is not $100B, and it requires $50B under management, which means hospitals, where Epic holds 42% of hospitals and 55% of beds [notes] and Ensemble alone manages $55B [notes]. A $1B revenue line at a 2.5% fee needs about $40B under management, the size of R1.

### 0.6 What accumulates, and who else has it

| Asset | Grows with each client? | Reproducible? | Contract right available? |
|---|---|---|---|
| Payer rule and denial-pattern knowledge | Yes, but depreciates in 12-18 months as payers change edits and deploy their own models [dk] | Yes. A clearinghouse sees far more: 45 clients is about 18M claims a year, under 0.5% of what a national clearinghouse processes [dk] | Only if the business associate agreement allows de-identification and aggregate use. Mid-market clients on vendor paper usually accept; private-equity platforms and larger groups strike it [dk] |
| Payer rates | No advantage: negotiated rates are public under price-transparency rules [dk]; cross-client use of a client's fee schedule can breach its payer contract [dk] | Yes | Often no |
| Integrations to 15-25 practice and post-acute systems | Yes | Yes, with money. The system vendor can charge a toll or restrict write access [dk] | Depends on the EHR vendor, not the client |
| Payer enrollments, portal credentials | Per client, not portable | Yes | Belong to the client |
| Workflow labels from human exception review | Yes; the best proprietary asset | Partly; every funded competitor is collecting the same | Yes on vendor paper |
| Switching cost | Moderate: three-year term, transition pain | Same for every outsourcer; industry churn 8-15% a year [dk] | n/a |

Verdict on scale: it makes the company larger and somewhat cheaper to run. It does not create a network effect. The claimed endpoint, a clearing network between providers and payers, already exists and is owned by clearinghouses, some of them payer-owned [dk].

---

## 1. Venture debt and receivables lender

**Who.** Credit officer at a specialty lender that does venture term loans and receivables lines for healthcare services and software.

**Incentives and constraints.** Paid on yield with zero tolerance for principal loss. Credit committee wants a sponsor, 12+ months of runway after funding, and collateral that does not disappear when the borrower fails. Receivables lines advance only on earned, billed, uncontested invoices under 90 days, with concentration limits (no debtor above 15-20%) and a dilution reserve [dk].

**Assessment.**
- The collateral is a fee owed by unrated physician groups, contingent on their collections and subject to refund for six months. Invoices inside the guarantee window are ineligible (offset risk). On a growing book, that is most of the receivables.
- "Fund the refund guarantee" is a request to lend against a contingent liability. No credit committee does that. As worded, the liability is uncapped.
- Legal dilution: percentage fees are restricted in New York and scrutinised elsewhere; Medicare billing-agent rules stop the vendor from controlling the lockbox, so fees cannot be netted at source [source: Foley and HBMA via summary]. The lender cannot rely on cash dominion over client collections.
- Audit clawbacks: home health and equipment suppliers are Medicare-heavy; recoupments arrive two to four years later and clients will demand fee refunds on them [dk].
- Customer concentration at 10 clients is 25-30% in one name.

**Decision.** Refuses at seed. Refuses to fund the guarantee at any stage. After a Series A of at least $25M from a recognised sponsor, offers:
- Venture term loan of $5-8M (20-30% of the round), floating rate about 10-12% all-in, 12 months interest-only, warrants at 0.5-1% coverage, minimum cash covenant of six months' burn, material adverse change clause [dk].
- Receivables line of up to $3-5M: 80% advance on invoices issued after a client's guarantee window closes, 15% debtor cap, guarantee refunds counted as dilution with a dollar-for-dollar reserve.

**Alternative it would rather fund.** A private-equity-backed billing roll-up with contracted fees, no refund clause and positive EBITDA, at 3-4x leverage.

**What changes the decision.** Guarantee capped at 25-50% of fees paid in the window and conditioned on baseline thresholds; 12 months of refund history across 20+ clients with refunds under 5% of revenue; client contracts with a monthly minimum fee; average client payment under 45 days; no client above 15%.

---

## 2. Private-equity partner whose firm owns a large revenue cycle outsourcer

**Who.** Operating partner; portfolio company manages tens of billions of hospital and physician revenue with 20,000+ staff, mostly offshore.

**Incentives.** Protect an asset bought at about 14x EBITDA with leverage [source: R1 deal as the reference]; hit an exit in three to five years; show an AI margin story to the next buyer.

**Threat assessment.**
- Hospitals: none for three years. The start-up's stated segment excludes Epic sites.
- Physician groups above $30M: moderate from 2029. The danger is price, not lost logos: every funded AI vendor quoting 3% resets renewals.
- Its cost advantage over us is smaller than it thinks. Offshore staff cost $12-18K a year against $55-70K for US billers [dk]; BLS mean wage for billing clerks is $51K before benefits [notes]. Our cost to serve physician accounts is already about 1.5-2% of collections. Agents take perhaps another third out, and we can buy the same agents.
- KLAS shows our own category has unhappy clients and little visible AI benefit so far [notes]. That is the opening the start-up has, and it is real.

**Buy, copy or crush.**
- Copy: yes, now. License denial, coding and payer-call agents from two or three vendors, deploy on offshore teams, pass 10-15% of the saving to clients at renewal (the pattern TCS and Accenture already follow [notes]).
- Crush: not as a campaign. In head-to-head deals above $30M of collections we quote 3.0-3.5% with 10-20% of fees at risk against service levels, and we offer to rebadge the client's billing staff, which a start-up cannot credibly do.
- Buy: not before proof. Would pay 4-6x revenue, $100-300M, once it shows $20M+ of recognized revenue, 70%+ of claims untouched by humans on audited data, and cost to serve under 1.5% of collections across at least three practice systems. Below that, hire its engineers.

**What changes the decision.** Audited touchless rate above 85% on full-scope accounts and a three-year cohort with net retention above 100% would move the price to $0.5-1B and make it urgent.

---

## 3. Skeptical venture investor (seed and Series A)

**Who.** General partner at a multi-stage fund that has seen 15 revenue-cycle pitches in two years.

**Product company or outsourcer.** Outsourcer with software inside. Evidence: revenue is a share of someone else's cash, licensed coders review exceptions, each client needs an implementation, and the guarantee is a service-level promise. Comparable margins: R1 27% EBITDA at $2.25B [source]; Waystar 43% as a software and network business [notes]. This lands between them, closer to R1.

**Gross margin trajectory (panel 0.2, 0.5).** 10-20% at 10 clients, 45-50% at 100, 50-55% at 1,000, on a fee falling from 4.5% to about 2.5%. Automation gains go mostly to customers through price. The founder's 80% is not supported by any comparable.

**Against funded competitors.** Candid has $219M, 190% growth and a seven-year head start and is still estimated near $57M of revenue [source][notes]. Adonis, Amperos, Arintra, Charta, Smarter Technologies, Commure and Waystar's own agents cover every sub-task [source][notes]. The pitch has one differentiator, full takeover with a refund guarantee for non-Epic groups, and that is a contract term any of them can copy in a quarter.

**Likelihood of $100M of revenue in 24 months.** Under 1%. It needs $2.2B live for a full year. With a 6-9 month sales cycle, a 3-4 month go-live and a 4-month fee ramp, the first signed client produces full fees in month 13-17. Panel expectation at month 24: $3-8M run-rate, 6-12 clients. No health company that sells to providers has reached $100M in 24 months; the fast ramps sold to consumers or pharma [notes].

**Plausible exit.** Weighted view: 55% wind-down or acqui-hire ($0-40M); 30% sale to an outsourcer, clearinghouse or EHR vendor at $100-400M; 12% independent scale at $0.6-1.5B; 3% above $2B. Probability-weighted about $150-200M. A $100B outcome is not in the distribution.

**Decision.** Passes on the seed as written. Would sign a $4-5M seed at $20-25M post-money only for a narrowed version: one specialty, two practice systems, fee-at-risk capped at 25% of fees, percentage fee replaced by a flat or per-claim fee in restricted states. Series A ($25-35M at $120-180M post) only on: 10 live clients, $5M+ contracted run-rate, gross margin above 45% including humans and implementation, refunds under 5% of revenue, audited touchless rate above 80%, and one client above $40M of collections live for six months.

**What changes the decision.** Evidence that cost to serve is under 1.5% of collections on real accounts, or a distribution deal with a practice-system vendor that makes the company the embedded billing service.

---

## 4. Incumbents responding rationally

### (a) Clearinghouse and revenue-cycle software vendor, 40%+ margins
- **Position.** Processes claims for thousands of providers; sees payer behaviour across the market; already has autonomous resubmission and performance contracts in its AI unit [notes].
- **Response.** Does not take over staff (it would halve the margin). Sells denial-prevention and appeal agents to its 1,488 large clients [notes] on contingency: 10-20% of recovered dollars, or 0.5-1.0% of collections on top of subscription, no implementation, no staff change. Partners with outsourcers for full takeover.
- **Effect.** The client keeps its billers and gets most of the uplift with no transition risk. It also strips the "payers deny with AI, you need AI" argument of exclusivity. The start-up must route claims through a clearinghouse and pays per transaction to a competitor.
- **Would it buy?** Only for a specialty it lacks (equipment suppliers, home health), at 3-5x revenue.

### (b) EHR and practice-system vendor bundling AI billing
- **Position.** Several non-Epic vendors already sell billing as a service on a percentage of collections; one has advertised about 2.9% [dk]. One large vendor's customers are on bundled percentage pricing by default [dk].
- **Response.** Puts coding, claim creation, eligibility, prior-auth submission (through the 2027 FHIR interfaces [notes]) and denial work into the subscription at no extra price; cuts the service percentage for groups above $20M; tightens interface terms for third parties that write to billing tables (certification, tolls or revenue share) [dk].
- **Effect.** For clients on a bundled vendor the start-up's 4.5% is in addition to what they already pay, so that base is closed without replacing the EHR. Elsewhere the start-up's go-live date depends on a competitor's interface queue. Information-blocking rules limit outright refusal but not delay or price [dk].

### (c) Large outsourcer with offshore labor
- **Response.** Drops to 3.0-3.5% for groups above $30M, 2.5-3.0% above $100M; matches the guarantee in diluted form (10-20% of fees at risk); offers staff rebadging and legacy receivables clean-up at contingency; buys agents from start-ups in (5).
- **Margin room.** Gross margin 40-50% on offshore labor [dk]; a 100 basis point cut still leaves a profit.
- **Effect.** The start-up loses its price advantage in the only accounts large enough to produce $2M contracts.

### (d) Epic
- **Response.** None aimed at this company. Continues extending to independent groups through hospital-hosted instances and its offering for independent groups [dk]; Penny is at 200+ organizations [notes].
- **Effect.** Three caps: the best mid-sized groups drift onto Epic through affiliation or acquisition (3-5% of target groups a year change owner, and contracts end on change of control [dk]); the "then hospitals" step is closed for 42% of hospitals and 55% of beds [notes]; and Epic sets buyer expectations that billing agents come free with the record.

### (e) Frontier-lab deployment venture or AI-enabled roll-up
- **Position.** Two lab ventures hold $5.5B and get preferred access to their investors' portfolio companies; Thrive Holdings raised $2B at $12B with 70+ service businesses [notes]. The investor lists overlap with owners of large revenue-cycle and practice-system assets [dk].
- **Response.** Buys billing companies at 5-8x EBITDA (about 1x revenue) and automates behind an unchanged client relationship: no sales cycle, no go-live, no guarantee, revenue from day one. Alternatively, forward-deployed engineers install agents inside the private-equity-owned outsourcer in (2).
- **Effect.** Collections under management are acquired faster and with debt, not equity. The roll-up pays about 1x revenue for live accounts; the start-up spends 0.4-0.6x first-year revenue per account in acquisition, implementation and expected refunds, then waits 16-24 months for the cash. The roll-up also holds the legacy receivables and staff the start-up has to fight for.
- **Would it buy this company?** No. It buys books of business and uses lab models directly.

---

## 5. Competing start-up with $50M+ raised, already selling revenue-cycle agents

**Who.** Archetype: founded 2019-2022, $100-250M raised, 100+ provider customers, $30-80M of revenue [source for the type: Candid, Adonis; notes].

**What it already has.** Claim engine and rules for several hundred payers; integrations with the main non-Epic practice systems; payer-call voice agents; coder review team; clearinghouse contracts at volume price; touchless rate above 90% on defined workflows [source: newmarketpitch]; case studies; a balance sheet that can carry fee-at-risk.

**Pricing today.** 2.5-4.0% of collections for platform plus service on $10-100M groups, or a platform fee plus $2-4 per claim; aged-receivables recovery at 12-18% contingency [dk].

**Response to C3.**
1. Matches the headline in the same quarter: "25% of fees at risk on agreed metrics", capped, with baseline set by a third party.
2. Quotes 3.0% in any deal where C3 appears. It can fund this for three years.
3. Sells the low-risk entry: agents on top of the client's existing staff and system for 90 days, conversion to full service later. No go-live cliff.
4. Signs preferred-partner agreements with two or three practice-system vendors.
5. Tells buyers what its own tests showed: full refund guarantees attract groups that already perform well and want six free months.

**Would it buy C3?** Only for a specialty team (equipment, home health) at under $30M.

**What would worry it.** C3 owning a specialty where documentation rules are the barrier (equipment suppliers, home health under Medicare) with a per-claim cost half of its own.

---

## 6. New buyer: CFO, 40-physician independent multi-specialty group

**Who.** About $42M of net collections; 18 billing staff in a central office; a non-Epic record system with a national clearinghouse; adjusted net collection rate 94.5%, 41 days in receivables, 11% first-pass denials; current cost to collect about 3.6% ($1.5M) [dk, archetype]. Physician-owners vote on any contract above $250K. Their monthly draw is paid out of collections.

**Alternatives this quarter.** Four AI vendors; the record vendor's bundled agents at no added price; the clearinghouse's denial agent on contingency; an offshore outsourcer at 3.2%; do nothing.

**Arithmetic.**
- C3 at 4.5% costs $1.89M against $1.5M today: $390K more, plus severance for 18 staff.
- Promised uplift of 2 points is worth $840K a year if it happens.
- A typical transition dip of 10% of cash for two months is $700K out of physician draws [dk]. The guarantee refunds fees (at most about $700K in the window at this size), not lost or delayed cash, and pays after the damage.
- Three-year lock-in with a company that has no three-year history.

**Decision.** Refuses C3 as priced and structured. Does not pay a deposit. Signs instead a 12-month, limited-scope contract for denial appeals and receivables older than 90 days at 12-15% of recovered dollars, with whichever vendor integrates fastest with the current system, most likely the clearinghouse or the funded start-up in (5). Keeps the billing office.

**Terms on which this CFO would sign full scope.** Fee at or below 3.0% of net collections (flat or per-claim if state law requires); 12-month initial term, then termination on 90 days' notice; baseline set by an independent party on a 12-month look-back; a cash-flow floor during transition (vendor advances the difference if monthly collections fall below 95% of the trailing average); staff offered roles or severance funded by the vendor; data and work queues returned in a usable format; three reference clients of similar size and specialty mix live for a year; errors-and-omissions cover of at least $5M and indemnity for coding errors by the agents.

**What changes the decision.** A peer group in the same state on the same record system showing audited results after 12 months.

---

## 7. Panel conclusions

### Five most damaging objections
1. The price is not a discount for the clients that make the plan work. Groups near $50M pay or spend 3-4% today, and the fee is heading to about 2.5% in five years as funded rivals and offshore outsourcers match. [source: athenahealth 3-4%, 2.99% advertised; notes: Fin $1.90 to $0.99; dk for the path]
2. The route to scale is slow and cash-hungry by construction: 6-9 month sale, 3-4 month go-live, fee ramp tied to claim payment, revenue constrained during the guarantee. $100M in 24 months is under 1%; $150-250M of equity is needed to get there at all. [notes: Waystar/Iodine deferral, five-to-seven-year precedent; dk for timeline]
3. Nothing proprietary accumulates faster than competitors accumulate it. Clearinghouses see two orders of magnitude more denial data, payer rates are public, integrations are purchasable, and the practice-system vendor controls access. Scale gives a larger outsourcer, valued like one (R1: 3.9x revenue, 14.5x EBITDA). [source: R1; notes: Waystar; dk]
4. The guarantee as worded is uncapped, invites adverse selection, pushes about 40% of clients into refunds, cannot be financed with debt, and still fails to address the buyer's real fear, which is a cash dip during transition. [dk, panel build]
5. Better-capitalised entrants reach the same accounts without a sales cycle: roll-ups buying billing companies at about 1x revenue, lab deployment ventures inside private-equity-owned outsourcers, and record vendors bundling agents at no added price. Percentage fees are also legally restricted in some states and raise upcoding exposure when paired with AI coding. [notes: lab ventures, Thrive; source: fee-splitting via summary; dk]

### Conditions that turn each "no" into a "yes" (their terms)
- Lender: Series A closed; guarantee capped at 25-50% of window fees with baseline thresholds; refunds under 5% of revenue across 20+ clients; no client above 15%.
- PE owner: $20M+ recognized revenue, audited 70%+ touchless on full scope, cost to serve under 1.5% of collections; then $100-300M.
- Venture investor: narrowed seed (one specialty, two systems, capped fee-at-risk); Series A on the proof list in section 3.
- Clearinghouse, record vendor, outsourcer, roll-up: no purchase; a specialty gap (equipment, home health) at 3-5x revenue for the clearinghouse only.
- Competing start-up: under $30M for a specialty team.
- CFO: 3.0% or less, 12-month term, independent baseline, cash-flow floor, staff plan, three peer references.

### Probabilities (panel's honest estimate)
- This version (full takeover, percentage fee, three-year term, refund guarantee) reaches a first paid commercial delivery within 18 months: 70%. The first client will be a $5-20M group, on a shorter term and a capped guarantee.
- This business reaches $1B of annual recognized revenue within 7 years: 1%.
