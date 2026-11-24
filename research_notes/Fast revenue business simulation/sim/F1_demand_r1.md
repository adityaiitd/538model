# F1 v1 demand and supply-side panel, round 1

Date of simulation: 24 November 2026. Everything below is a simulated hypothesis built from archetypes. It is not customer validation. No real person, quote, order or interview is represented.

Evidence labels used: [source: URL], [notes] (precedents_and_lab_data.md), [domain knowledge, unverified].

Searches used: 3 searches and 3 page fetches (the limit of 6).

---

## 0. Facts checked before the personas were played

These change the brief more than any persona does.

1. Existing suppliers already buy enterprise operational data and sell it to labs.
   - micro1 announced on 9 October 2026 a commitment to spend $1bn in 12 months buying and licensing enterprise operational data, financed by Citi and Hercules Capital. It pays over $100K for a qualified partnership, over $500K for large or multi-team datasets and over $1M for highly unique data; Business Insider gives $100K-$2M for a midsize company. Eligibility starts at about 30 employees. Public terms name no buyer, exclusivity or liability terms. [source: https://letsdatascience.com/news/micro1-commits-1b-to-buy-and-license-enterprise-data-9181fe83] (secondary page citing micro1's blog, The Next Web and Business Insider; primary text not opened)
   - Mercor runs an enterprise data programme with connectors to 100+ tools (Slack, Teams, Gmail, Outlook, Salesforce, GitHub, Drive, Notion, Confluence). It targets legal, healthcare, finance and insurance (statements, underwriting files, claims), professional services and others. It pays by wire after the anonymized dataset is delivered to the buyer, typically 2-4 weeks from a signed agreement, and states SOC 2 Type II. [source: https://www.mercor.com/data/]
   - Polyshares buys operational records as principal (Slack, email, Drive, CRM, tickets, call recordings, ERP); typical licences $100K to $2M and above; average deal about $300K and about $1M revenue in its first month, both self-reported. Mode.Inc publishes indicative payouts of $100K-$5M. Brokers make six-figure offers to live companies, sometimes with 48-hour deadlines. [source: https://dealroom.co/news/170312-ai-data-brokers-are-buying-slack-email-and-crm-from-live-us-companies/] (citing Business Insider, 13 and 26 October 2026)
   - Protege (marketplace paying data partners a revenue share per use) has raised about $65M and says it has generated "tens of millions" for data partners since its 2024 seed. [source: https://siliconangle.com/2026/01/08/protege-raises-30m-grow-governed-marketplace-ai-training-data/] (via search summary)
2. Labs buy direct when the corpus is large. In the Spirit Airlines bankruptcy estate auction of de-identified email, Teams and file archives, Google paid about $10M, micro1 about $12.5M and Mercor about $7.5M. [source: https://dealroom.co/news/170312-ai-data-brokers-are-buying-slack-email-and-crm-from-live-us-companies/]
3. Labs also capture the same data at zero licence cost. Meta is installing software on US employees' work computers to capture mouse movements, clicks, keystrokes and some screenshots for AI training. [source: https://fortune.com/2026/04/21/meta-will-start-tracking-employees-screens-and-keystrokes-to-train-ai/] (via search summary). OpenAI and Handshake asked contractors to upload real files from past and current jobs, leaving redaction to the contractor. [source: https://www.outlookbusiness.com/artificial-intelligence/openai-asks-contractors-to-upload-real-world-work-to-train-next-gen-ai-agents] (secondary to Wired, January 2026)
4. Employees are often unpaid and uninformed in these deals, and a law professor quoted by Business Insider calls it an ethical grey area. [source: https://dealroom.co/news/170312-ai-data-brokers-are-buying-slack-email-and-crm-from-live-us-companies/]
5. Gartner, cited by Business Insider, puts "AI data spend" at under $1bn in 2025 and about $6.5bn in 2027. This does not reconcile with the $7-9bn of supplier run-rates in the notes; the Gartner figure probably covers licensed data only. [source: same Dealroom page] [notes]

What the checks answer:
- Do labs buy real work traces from third parties today? Yes for stored archives (documents, messages, CRM, tickets). For prospective screen and tool recordings of live regulated work, no third-party sale was found; the only confirmed case is a lab recording its own staff.
- At what price? Per company archive, not per hour: $100K-$2M for a midsize company, about $7.5-12.5M per buyer for a large airline's archive. No per-hour price was found in any source. [notes] also records no per-trajectory price.
- Is it non-exclusive? Observed deals are: three buyers bought the same estate.

---

## 1. Persona transcripts

### Buyer 1. Head of human data, frontier lab with $50bn+ revenue run-rate

- Incentives: deliver data that moves internal evaluations on long-horizon agent work this quarter; avoid a provenance or breach incident after the Mercor breach in March 2026 [notes].
- Constraints: every new data vendor needs security and legal sign-off; budget is released in quarterly themes that rotate [notes].
- Alternatives:
  - Existing approved vendors that now run enterprise-data programmes (Mercor, micro1, Turing, Surge) [source: Dealroom page above].
  - Buying large corpora direct, as Google did with the Spirit estate [source: Dealroom page above].
  - Contractors recorded doing tasks to the lab's own spec at about $130-150 per billed expert hour (Mercor pays $85-95 and marked up about 35%) [notes].
  - Own enterprise customers under opt-in data partnerships [domain knowledge, unverified].
- Decision: **paid pilot. Refuses a quarterly licence.**
- Terms: $300K-$500K for one domain, 3,000-5,000 verified hours with outcome labels, about $60-150 per hour depending on seniority of the work. Acceptance on the lab's own sampling. Net 45 from acceptance. Non-exclusive is acceptable.
- Follow-on if the pilot moves an evaluation: one-off buys of $1-3M per distinct corpus. Would pay 2-3 times that for a 6-12 month exclusive window, consistent with "exclusivity costs several times more" [notes].
- Reasons for refusing $1-5M per quarter per domain:
  1. The market prices per corpus, one-off. A subscription needs proof that hour 50,000 of claims handling from the same three firms is worth what hour 5,000 was. This buyer expects steep diminishing returns and wants breadth across firms and software stacks [domain knowledge, unverified].
  2. An unknown supplier's de-identification of screen recordings is unproven; one leaked claimant record is a headline.
  3. Approved vendors with $1bn of acquisition funding can bring the same category without a new onboarding.
- What changes the decision: a corpus no approved vendor can supply (regulated-industry traces with written consent from the data owner's clients), a third-party re-identification test, and an internal evaluation lift attributable to the pilot data.

### Buyer 2. Agent research lead, second frontier lab or large technology company AI group

- Incentives: a result on computer-use and long-horizon benchmarks within one research cycle. Holds a discretionary budget; notes say data budgets often sit with researchers, not procurement [notes].
- Constraints: wants raw data and the right to build environments in-house; many top labs now build their own environment systems and buy raw inputs [notes].
- Alternatives: employer already records its own employees' screens and keystrokes at no licence cost [source: Fortune page above]; more than a dozen RL-environment vendors [notes]; contractor capture.
- Decision: **paid pilot at a lower price. Refuses non-exclusive at the founder's price.** Disagrees with Buyer 1 on exclusivity.
- Terms: $150K-$250K for about 2,000 hours of traces plus 200-300 complete tasks with verifiable end states. Values raw trace hours at $30-100 and complete, checkable tasks at a few hundred to a few thousand dollars each, in line with environment task prices [notes]. Wants a 6-month first-look or exclusivity window on anything that works. Will not pay seven figures for data rivals receive the same quarter, because "without exclusivity a product reaches rival labs within months" [notes].
- Reasons: traces without a checkable outcome are weak training signal; internal employee capture covers generic office work; the only gap is domains the employer has no staff in (claims adjudication, accounting close for third parties).
- Expert quality control product: would use 300-500 graded runs as a trial. Pays $120-180 per expert hour, not $250-400. Mercor's average pay is $85-95 with about 35% markup [notes].
- What changes the decision: outcome-linked data (the claim's final disposition, the audit adjustment, the reopened ticket) at 90%+ coverage, and a measured lift on the group's own benchmark.

### Buyer 3. Head of data, model or agent company outside the top two ($200M+ revenue; coding, legal or finance AI)

- Incentives: improve a vertical product; show customers a quality lead. External data budget is about $0.5-3M a year in total [domain knowledge, unverified].
- Alternatives: own product telemetry and design-partner customers under opt-in terms; public and synthetic data; contractor experts through an existing vendor.
- Decision: **refuses the licence. Signs a small one-off purchase order.**
- Terms: $75K-$250K for one dataset in its own vertical, only with vertical exclusivity for 12 months or as a held-out evaluation set. Quality control: 500 expert hours at about $150, roughly $75K.
- Reasons: $4-20M a year for one domain exceeds the entire external data budget; non-exclusive data bought by the frontier labs gives no advantage over them; own customers' usage data is closer to the product.
- What changes the decision: nothing at the founder's price. At $100-300K per dataset this buyer repeats two to four times a year.

### Buyer 4. Procurement, legal and security lead at the lab

- Incentives: no incident traceable to an approved supplier. Career risk is entirely on the downside.
- Constraints since March 2026: a breach at a supplier led one lab to pause all work indefinitely and others to investigate [notes].
- Decision: **does not approve a quarterly licence. Approves a capped pilot on an expedited path.**
- Conditions for the pilot (up to about $250K-$500K):
  - SOC 2 Type I report plus a penetration test now; Type II within 12 months. A Type II report needs an observation period of 3-12 months [domain knowledge, unverified].
  - Chain of title for every dataset: the data owner's licence, and written consent from the owner's clients wherever client information appears in the work.
  - Evidence of employee notice and opt-in.
  - A re-identification test by an independent firm; no health data without HIPAA expert determination; no EU-origin employee data.
  - Cyber and errors-and-omissions cover of at least $10M; uncapped indemnity for privacy and intellectual property claims. An indemnity from a start-up with $5-10M is valued at the insurance limit and no more.
  - Right to audit, right to require deletion, termination for convenience, no minimum commitment, no prepayment.
- Timing: pilot paper in 3-6 weeks with a research sponsor; master agreement 8-16 weeks; payment net 45-60 from acceptance. First cash arrives 4-6 months after first meeting [domain knowledge, unverified]. The notes found no disclosed payment terms [notes].
- Reasons: existing suppliers' public terms carry no stated liability terms [source: letsdatascience page above], and this persona treats that as the gap it must close in contract, not as a standard to match.
- What changes the decision: Type II report, two clean deliveries, and a data owner of standing willing to co-sign provenance warranties.

### Buyer 5. Finance lead for the lab's data budget

- Incentives: cost per unit of model improvement; keep spend reallocatable each quarter.
- Benchmarks used:
  - Internal employee capture: near zero marginal cost [source: Fortune page above].
  - Contractor-generated expert traces: about $130-150 per billed hour; generalist work $16-21 an hour pay [notes].
  - Broker archives: $100K-$2M per midsize company [source: Dealroom page above].
  - Large corpus bought direct: about $10M [source: Dealroom page above].
- Decision: **funds pilots from research discretionary budget. Refuses any quarterly commitment.**
- Terms: will pay up to about 1.0-1.5 times the contractor-generated cost per hour for real traces if research shows a lift, so a ceiling near $150-200 an hour for senior professional work and $30-60 for back-office processing work. Wants a most-favoured-customer clause and a price that falls with each additional licensee of the same data.
- Reasons: the data owner's marginal cost of a trace is close to zero, so the price will be bid toward capture, processing and consent cost. Themes rotate every few months [notes], so finance operations may not be funded two quarters running.
- What changes the decision: a measured lift per dollar better than contractor data on two consecutive deliveries. Then quarterly orders, still cancellable.

### Data owner 6. Chief operating officer, large business-process outsourcing company with falling revenue

- Incentives: new revenue line; anything that offsets seat losses.
- Constraints: client master service agreements make client data the client's property and restrict use to delivering the service [domain knowledge, unverified]. Telling clients the work is being recorded for AI training invites them to ask why they should not sell it themselves or end the contract sooner.
- Alternatives: fixed cash from micro1, Mercor, Polyshares or Mode.Inc ($100K-$5M, paid in weeks) [sources above]. Large outsourcers already sell AI data services to labs themselves and can go direct [domain knowledge, unverified].
- Decision: **pilot on own internal operations and on one or two consenting clients. Refuses the 35% revenue share.**
- Terms demanded: $250K-$500K paid up front as a non-refundable advance per pilot site; 50% of sales; a minimum guarantee of $1-3M a year per 1,000 recorded seats before any wider rollout; the outsourcer keeps the right to sell direct. Non-exclusive is fine.
- Reasons: a share of unproven sales loses to a wire in 2-4 weeks. The client, not the outsourcer, is the true owner for most seats, and clients will demand their own cut, leaving perhaps 15-25% for the founder on client work.
- What changes the decision: a signed lab purchase order shown in advance, and a template client consent that at least three of its clients accept.

### Data owner 7. General counsel, regional bank or insurer

- Incentives: none that a seven-figure fee moves. Fee is immaterial against regulatory and reputational exposure.
- Constraints: customer financial information under the Gramm-Leach-Bliley Act and state insurance data laws; health information in claims under HIPAA; bank regulators' third-party risk guidance; duties to policyholders and claimants [domain knowledge, unverified]. Screen recordings carry names, account numbers, medical notes and free text in every frame.
- Decision: **refuses.**
- Reasons:
  1. Cannot certify that video and tool traces are de-identified to a standard a regulator or plaintiff would accept.
  2. A model trained on the data could reproduce fragments; liability is unbounded and lands on the institution, not on a $10M start-up.
  3. Selling customer-derived records to an AI lab is a board and regulator conversation, not a general counsel approval.
- What would be acceptable: employees re-enacting workflows in a sandbox with dummy data, or processing that stays on the institution's premises and exports only non-personal artefacts. Neither is the product in the brief. Timeline for even that: 9-18 months.
- What changes the decision: a regulator's written no-objection, a peer institution going first, and a fee in the tens of millions with insurance-backed indemnity.

### Data owner 8. Managing partner, mid-size accounting or claims-administration firm

- Incentives: partners like a fee with no delivery cost; fear client attrition more.
- Constraints: accountants' professional confidentiality rules require specific client consent to disclose client information, and US tax law makes unauthorised disclosure or use of tax return information by a preparer an offence without written taxpayer consent [domain knowledge, unverified]. Claims administrators hold files that belong to the carrier or self-insured employer, often under HIPAA business associate terms [domain knowledge, unverified].
- Alternatives: fixed offers from brokers [sources above]. Accounting roll-ups backed by a lab-affiliated investor already hold 50+ firms [notes] and can route their data to their own partner.
- Decision: **small pilot limited to the firm's own internal work and re-enacted engagements. Refuses to license client-work traces without each client's written consent.**
- Terms: fixed fee of $150K-$500K, paid up front. Revenue share is not wanted; partners cannot explain an uncertain payout to a partner vote. Estimates 5-15% of clients would consent if offered a share.
- What changes the decision: an engagement-letter addendum the firm's insurer approves, and a client-facing payment that makes consent worth asking for.

### Data owner 9. Chief privacy officer or works-council representative

- Incentives: no enforcement action, no workforce dispute.
- Constraints:
  - EU: consent from employees is generally not treated as freely given; in Germany technical monitoring of staff needs works-council agreement, which takes 6-12 months and is unlikely for a tool that trains a replacement [domain knowledge, unverified].
  - US: electronic-monitoring notice laws in several states; monitoring is a bargaining subject in unionised sites; keystroke dynamics can raise biometric-law questions in Illinois [domain knowledge, unverified].
- Decision: **refuses blanket capture. EU sites refused outright. Allows a US opt-in pilot under conditions.**
- Conditions: impact assessment; opt-in with no retaliation; a pause control for the employee; no use in performance management; on-device redaction before anything leaves the endpoint; raw recordings deleted within 30-90 days; a named employee share of proceeds; right to withdraw past recordings.
- Effect on the product: opt-in and pause controls cut usable hours. This persona expects 30-50% participation and gaps exactly where the hard cases are.
- What changes the decision: nothing for EU sites. For US sites, a clean pilot and no employee complaints over two quarters.

### Data owner 10. Senior claims adjuster or finance operations employee

- Incentives: pay; job security. Believes the recording trains the system that replaces the role.
- Decision: **opts in only at a price well above a token bonus. Otherwise refuses.**
- Terms: $400-800 a month, or about $5-10 per recorded hour, roughly a 10-20% uplift on a $30-50 hourly wage [domain knowledge, unverified]. Wants a written bar on performance use and the pause control.
- Behaviour when recorded: follows the manual, avoids shortcuts and side channels, routes sensitive files off-recording. The trace becomes less like real work [domain knowledge, unverified].
- What changes the decision: a retention or retraining commitment from the employer. Money alone gets partial participation.

---

## 2. Answers to the specific tests

| Question | Finding | Label |
|---|---|---|
| Do labs buy real work traces from third parties today? | Yes for stored archives; via brokers and direct. No confirmed third-party sale of live screen recordings from regulated work | [source: Dealroom page], [notes] |
| Price | $100K-$2M per midsize company archive; about $7.5-12.5M per buyer for one large corporate archive. No per-hour market price exists. Panel's willingness to pay: $30-100 per raw hour, $60-200 per verified senior hour with outcome | [source: Dealroom page]; panel estimate |
| Non-exclusive? | Bought, yes. Three buyers bought the same estate. But two of five buyer personas pay full price only with an exclusivity window | [source: Dealroom page]; panel |
| Speed to approval and cash | Pilot paper 3-6 weeks, master agreement 8-16 weeks, net 45-60. First cash 4-6 months from first meeting | [domain knowledge, unverified] |
| Can data owners legally sell traces containing clients' information? | Generally not without the client's consent. Outsourcers, accountants and claims administrators are custodians, not owners. Banks and insurers own more of it but will not certify de-identification of screen video | [domain knowledge, unverified] |
| Share data owners demand | Fixed cash up front, matching broker offers of $100K-$5M paid in weeks. Where a share is accepted: 50% plus an advance, and clients want their own cut | [sources above]; panel |
| Do existing suppliers do this? | Yes: micro1 ($1bn committed), Mercor, Polyshares, Mode.Inc, Protege, Turing, Surge; Google buys direct; Meta self-captures | [sources above] |

### How many buyers and domains for $40M

| Route | Arithmetic | Panel view |
|---|---|---|
| Founder's assumption | 5 buyers x $2M x 4 quarters | No buyer persona signs a quarterly licence. Only about 7-9 organisations worldwide could spend $8M a year with one new vendor in this category [domain knowledge, unverified] |
| Midsize archives at observed prices | $40M / $300K average = about 133 dataset sales a year | Polyshares reports about $1M a month; this is a $10-15M business in year one at best |
| Large corpora | $40M / $10M = 4 buyer-licences, for example 2 corpora x 2 buyers | The arithmetic works. Supply is the problem: the bank and insurer persona refused, and the one observed case was a bankruptcy estate |
| Prospective trace hours | At $75 per hour: 533,000 buyer-hours. At 2.5 licensees per hour: about 213,000 unique hours, or about 140 recorded full-time staff for a year, spread over 20-40 owners for diversity | Volume is small; the 20-40 owner contracts at 3-9 months each are not |

Panel's year-one revenue estimate for v1 as offered: 2 lab buyers at $1.5-4M each plus 3-5 smaller buyers at $0.1-0.3M each, so $3.5-9.5M.

---

## 3. Numbers in the brief the panel disputes

| Brief | Panel's corrected value | Basis |
|---|---|---|
| Dataset licences $1-5M per quarter per buyer per domain | One-off buys of $0.15-0.5M (pilot), $1-3M per distinct corpus; $7.5-12.5M only for a very large single-company archive. Nothing quarterly | Buyer personas; [source: Dealroom page] |
| Five buyers averaging $2M a quarter | 2 lab buyers and 3-5 small buyers; $3.5-9.5M in the first twelve months of selling | Panel |
| Data owner share 35% | Fixed fee up front, or 50% plus advance and minimum guarantee; on client-owned work the founder keeps about 15-25% after the client's cut | Owner personas; broker offers [sources above] |
| Quality control $250-400 per expert hour | $120-180 for this domain mix; $250+ only for physicians, senior lawyers and similar | Mercor pay $85-95 plus about 35% markup [notes] |
| Gross margin 40-45% | 25-40% blended. Hits resold to 3 buyers exceed 60%; archives bought as principal and sold to 0-1 buyers lose money; human review of screen video for personal data costs about $5-20 an hour [domain knowledge, unverified] | Panel |
| $5-10M pays for advances | Covers about 10-25 midsize owner advances at $250-500K each, turned over 3-4 times a year at net 45-60. Competes with a $1bn bank-financed buyer | [source: letsdatascience page] |
| AfterQuery and Fleet as precedents | Neither licensed enterprise data. AfterQuery sold expert-made datasets through about 100,000 professionals; Fleet engineered environments. Closest precedents are Polyshares (about $1M first month, self-reported) and Protege (tens of millions paid to partners over about two years on about $65M raised) | [notes]; [sources above] |
| Market of $7-9bn | That is all human data. Licensed enterprise data is under $1bn in 2025 rising to about $6.5bn in 2027 on one estimate; panel's guess for 2026 is $1-2.5bn | [source: Dealroom page citing Gartner via Business Insider]; panel |
| "Supply of expert headcount is not short", so the gap is open | The gap was open in February 2026 [notes]. By October 2026 at least five funded suppliers were buying this data | [sources above] |

---

## 4. Five most damaging objections, most lethal first

1. Incumbents already do this with far more money and existing approved-vendor status. micro1 has committed $1bn with bank financing; Mercor has 100+ connectors and pays owners in 2-4 weeks; Google bids direct. The founder brings $5-10M and no approval. [source: letsdatascience page; mercor.com/data; Dealroom page]
2. In the founder's chosen domains the data owner is not the owner. Outsourcers, accountants and claims administrators hold clients' information under confidentiality terms; banks and insurers will not certify de-identified screen video. The supply that can be sold quickly is small unregulated firms' own archives, which is the segment the brokers already work. [domain knowledge, unverified]
3. No buyer signs a quarterly licence. All five buyer personas offered pilots or one-off purchase orders. Revenue is per corpus, one-off, with diminishing value per extra hour from the same firms, and themes rotate every few months. [notes]; panel
4. Data owners want fixed cash now, not 35% of future sales. Matching that makes the founder a principal buyer with inventory risk against a $1bn competitor, and raises the working capital need above $5-10M. [sources above]; panel
5. Labs can get the same class of data at near-zero licence cost by recording their own staff or asking contractors to upload past work. Third-party traces are needed only for domains where labs have no staff, which are the regulated domains in objection 2. [source: Fortune page; outlookbusiness page]

Also raised: a start-up's indemnity is worth its insurance limit; opt-in capture yields 30-50% participation and altered behaviour; EU supply is closed; one privacy incident ends the company.

---

## 5. Conditions under which each "no" becomes a "yes" (their terms)

- Lab head of human data: signs repeat $1-3M orders after a pilot shows an evaluation lift, if the corpus is one no approved vendor can supply and carries client-level consent.
- Agent research lead: pays seven figures for a 6-month exclusive window on outcome-linked traces with 90%+ outcome coverage.
- Smaller model company: $100-300K per dataset with 12-month vertical exclusivity; never at $1M+ a quarter.
- Procurement and security: SOC 2 Type II, $10M+ insurance, independent re-identification test, chain of title to the owner's clients, two clean deliveries.
- Finance lead: cancellable quarterly orders after two deliveries with better lift per dollar than contractor data, with most-favoured-customer pricing.
- Outsourcer: $250-500K advance per site, 50% share, $1-3M annual minimum per 1,000 seats, a lab order shown first, and a client consent template three clients accept.
- Bank or insurer: regulator no-objection, a peer going first, insurance-backed indemnity, a fee in the tens of millions; or a re-enactment product with no real customer data.
- Accounting or claims firm: fixed $150-500K up front, insurer-approved engagement-letter addendum, client paid for consent.
- Privacy officer and works council: US only, opt-in, pause control, on-device redaction, 30-90 day deletion, no performance use, employee share.
- Employee: $400-800 a month, a written bar on performance use, and a retention or retraining commitment.

---

## 6. Panel's four numbers for this version

| Measure | Estimate | Reasoning |
|---|---|---|
| Probability of a first paid commercial delivery within 9 months | 55-60% | Four of five buyers would fund a pilot; a small US firm's own archive or a paid quality-control trial can be delivered. Regulated-domain traces will not be ready in that time |
| Probability of $40M gross recognized revenue in a trailing twelve months by month 18 | 3-4% | Needs about $3.3M a month from month 7. Supply contracts take 3-9 months each, buyers start with $150-500K pilots, and no persona commits quarterly |
| Probability of $100M by month 36 | 4-5% | The segment is growing fast on one estimate (to about $6.5bn in 2027), which helps a survivor; incumbents' capital and lab self-supply cap the share available |
| Year five if it works | Gross margin 30-40%; equity value $0.3-1.0bn | A broker with $150-300M of gross one-off sales and several funded competitors. The notes show about 10x run-rate for leaders today [notes]; the panel expects a lower multiple for a non-exclusive reseller |

Revenue type: one-off per corpus, re-ordered at the buyer's discretion each quarter. Not recurring and not contracted.

Is the business plainly unworkable? No. The market exists and pays. Version 1 is mismatched to it in four ways: quarterly licences where buyers buy one-off, a revenue share where owners take fixed cash, regulated domains where the seller lacks title, and $5-10M against a $1bn incumbent programme.
