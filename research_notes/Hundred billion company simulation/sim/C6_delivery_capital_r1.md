# C6 v1, delivery, capital and competition panel, round 1

Date of simulation: 24 November 2026. Everything below is a simulated hypothesis by archetype personas. It is not customer, lender, regulator or investor validation. No real person was interviewed and no real order exists.

Evidence labels: [notes] = ai_services.md; [brief] = C6_v1.md; [source: URL] = checked in this session (read through search summaries, not the full original, unless stated); [DK] = domain knowledge, unverified.

Searches and fetches used: 8 of 8.

## 0. Facts checked for this panel

- OpenAI "Project Mercury" (reported October 2025): more than 100 former investment bankers (JPMorgan, Morgan Stanley, Goldman Sachs, Evercore, KKR and others) paid about $150 an hour as contractors to build Excel models for IPOs, restructurings and LBOs, one model per contractor per week. [source: https://www.bloomberg.com/news/articles/2025-10-21/openai-looks-to-replace-the-drudgery-of-junior-bankers-workload] [source: https://www.entrepreneur.com/business-news/openai-is-paying-ex-investment-bankers-to-train-its-ai]
- Mercor APEX-Agents (January 2026): 480 tasks, 160 each in investment banking, management consulting and corporate law, set in 33 simulated worlds. Investment banking: 10 worlds, 160 tasks, expert time to do a task 1.36 hours on average (law 2.40, consulting 1.69). Best investment-banking score at launch 27.3%. The leaderboard now shows much higher scores for newer models (not verified). [source: https://arxiv.org/pdf/2601.14242] [source: https://www.mercor.com/blog/introducing-apex-agents/]
- Mercor announced on 9 July 2026 that it would acquire Deeptune, an environment builder that had raised a $43M Series A led by Andreessen Horowitz in March 2026. [source: https://fortune.com/2026/03/19/andreessen-horowitz-ai-startups-deeptune-series-a/] [source: https://letsdatascience.com/news/mercor-acquires-deeptune-to-build-agent-training-environment-ea6c1b73]
- Fleet: in talks in April 2026 to raise at least $50M at about $750M, on about $60M annualized revenue. Derived: 12.5x run-rate. [source: https://sacra.com/c/fleet] [source: https://kucoin.com/news/flash/ai-training-firm-fleet-eyes-750m-valuation-amid-60x-revenue-surge]
- Epoch AI, state of RL environments (January 2026, fetched directly): tasks mostly $200-2,000, "$20k per task would be rare but possible"; exclusive deals 4-5x non-exclusive; one source discards a task at about a 70% pass rate; labs are doing "substantially more in-housing" to avoid vendor margin and keep priorities confidential; labs worry contractors use LLMs instead of doing the work; robust graders take "many many iterations"; a neolab saw contracts of $300-500K. The article gives no data on IP ownership, expert pay, hours per task or rejection rates. [source: https://epoch.ai/gradient-updates/state-of-rl-envs]
- US bank supervisors replaced SR 11-7 on 17 April 2026 with SR 26-2 (OCC Bulletin 2026-13, FDIC joined). It explicitly does not apply to generative and agentic AI. Third-party models stay fully within the bank's own model risk management. It is principles-based and sets no prescriptive requirements. [source: https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm] [source: https://www.orrick.com/fr-FR/Insights/2026/04/Agencies-Overhaul-Model-Risk-Management-Guidance-for-Banks-Heres-What-Changed] [source: https://www.moodys.com/web/en/us/insights/banking/from-sr117-to-sr262-managing-model-risk-when-models-dont-stand-still.html]
- EU AI Act: the Digital Omnibus defers high-risk obligations for stand-alone Annex III systems (which include credit scoring) to 2 December 2027, and Annex I product systems to 2 August 2028. [source: https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/] [source: https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes]
- AIUC closed a $40M Series A on 15 September 2026 (Ribbit), $55M raised in total. Its AIUC-1 standard is a third-party audit of AI agents modelled on SOC 2, about 5,000 risk and attack combinations. Reported as certified: Cursor, ElevenLabs, Fin, Harvey, KPMG, Lovable, UiPath. Certification is paired with insurance through a Lloyd's partnership. No revenue disclosed. [source: https://siliconangle.com/2026/09/15/ai-agent-certification-startup-aiuc-raises-40m-to-begin-auditing-frontier-models/] [source: https://www.securityweek.com/aiuc-raises-40-million-to-certify-enterprise-ai-agents/]
- Deloitte expanded its AI Controls and Assurance offering on 12 August 2026 (AI risk assessments, model validations, control redesign, standards-readiness). EY offers AI assurance services for audit and non-audit clients. No revenue disclosed. [source: https://www.deloitte.com/us/en/about/press-room/deloitte-expands-end-to-end-ai-controls-and-assurance-capabilities.html] [source: https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/]

Not found: any vendor's cost per task, rejection rate, IP terms, or certification revenue.

## 1. Panel's own model

### 1.1 Terminology problem in the brief

The brief prices "one verified environment" at $500-2,000. The market data it cites prices a task at $200-2,000 and an environment (a replica of a product or a world that hosts many tasks) at $20K-300K [notes]. What the brief describes is a task plus a share of a world. All figures below are per accepted task.

### 1.2 Cost per accepted finance task, 2027

| Item | Basis | $ |
|---|---|---|
| Authoring: 6-10 expert hours at $150 | APEX task takes 1.4-2.4 h to do [source above]; authoring (source files, prompt, rubric, gold solution) is about 4x doing time [DK]; $150 is what a lab pays direct [source above] | 900-1,500 |
| Independent expert review, 1.5-2.5 h at $175 | [DK] | 260-440 |
| Internal rework, about 30% of drafts fail first QC | [DK] | 350-580 |
| Grader engineering and difficulty calibration (64-128 rollouts per task) | calibration norm [source: Epoch]; cost [DK] | 200-500 |
| Share of the world (fictional company, data room, tool mock-ups), $8-15K per world over about 16-40 tasks | APEX has 16 tasks per world [source above]; cost [DK] | 200-600 |
| Recruiting, vetting, payments, fraud control, 8-12% of expert pay | [DK] | 120-250 |
| Rejection at customer acceptance, 10-15% | [DK] | 200-400 |
| Total | | 2,200-4,300, central 2,500 |

Cross-check: one banker-built model a week at $150 an hour is $1,500-3,000 of authoring alone at 10-20 hours a week [derived from source above; hours are an assumption].

AI-assisted authoring: the panel gives a 20-25% net reduction by year three, not 50%. Two reasons. A task is only saleable if current models fail it (2-30% pass rate [source: Epoch]), so each model release raises the required length and seniority of the task. Labs also fear model-written content from contractors [source: Epoch] and will ask for disclosure of AI use and may price it down [DK].

### 1.3 What that does to margin

| Sale | Price per task | Cost per task | Gross margin |
|---|---|---|---|
| Non-exclusive, one licensee, founder's midpoint | 1,250 | 2,500 | -100% |
| Non-exclusive, three licensees at $800 | 2,400 | 2,500 + 3 x 150 harness conversion | -23% |
| Non-exclusive, five licensees at $800 | 4,000 | 3,250 | 19% |
| Non-exclusive, three licensees at $1,500 | 4,500 | 2,950 | 34% |
| Exclusive or custom at 4x $900 | 3,600 | 2,700 (bespoke harness and spec) | 25% |
| Founder's 55-65% target | needs about 4 licensees at $2,000 (61%) or 6 at $1,400 (60%) | | |

- If the reported $200-2,000 range spans exclusive and non-exclusive sales, the non-exclusive price is $300-800, not $500-2,000 [inference from notes].
- Only three to five labs buy finance libraries at all. Selling every task to every one of them at $800 gives 19%.
- The panel's blended estimate: 20-25% in year one, about 37% in year two, 42% in year three, 45% in year five. The sector reference is 30-40% for labor resale [notes]; "some RL-as-a-service startups lose money" [notes].

### 1.4 Reusable versus bespoke

- Share of revenue from tasks licensed to more than one buyer: 15% in year one, 30-35% by year three [DK]. The rest is specified by one lab, built to its harness, tool interface and its model's failure modes, and sold exclusive or as work for hire.
- Share of cost that is reusable across buyers (authoring tools, worlds, grader framework, expert bench): about 25% [DK].
- A training licence is perpetual in effect: weights cannot be untrained. A "subscription" is a series of one-time sales that continues only while each refresh is worth buying.

### 1.5 Obsolescence

- A task is dropped at about a 70% pass rate [source: Epoch]. APEX investment banking went from 27% at best in January 2026 to much higher within the year [source above, later scores unverified].
- Useful life as training data: 6-12 months. As held-out evaluation: 9-18 months, shorter once it has been run through a lab's API. Panel amortises the library over 12 months, so half the catalogue value disappears each year [DK].
- Residual value after models pass: regression-test use only, 5-10% of original price [DK].

### 1.6 Working capital

- Experts are paid weekly; labs pay net 45-60 after a 2-4 week acceptance test [DK]. Cash gap 75-100 days of cost of sales.
- Building a library before selling it: 1,500 tasks x $2,500 = $3.75M per domain. The six domains in the brief are $22M before the first licence. A seed round cannot fund this. The founder starts with customer-funded custom work in one domain, which is the business the brief was trying not to be.

### 1.7 Revenue, margin and value, panel estimate

Conditional on reaching a first delivery (probability in section 4). Market basis: Anthropic discussed over $1B a year on environments [notes]; assume $3-5B across all labs in 2027, 25-35% non-coding professional work, 20-30% of that finance and adjacent regulated fields: $250-450M, of which 30-40% in-house [DK]. That leaves $150-300M shared among the marketplaces and 35+ specialists [notes].

| | Year 1 (2027) | Year 2 (2028) | Year 3 (2029) | Year 5 (2031) |
|---|---|---|---|---|
| Revenue, base ($M) | 2.5 | 12 | 28 | 55 |
| Revenue, range ($M) | 0.5-6 | 5-30 | 8-70 | 0-200 |
| of which labs | 2.3 | 10.5 | 23 | 35 |
| of which enterprise software and financial firms | 0.2 | 1.5 | 3.5 | 10 |
| of which certification | 0 | 0 | 1.5 | 10 |
| Gross margin | 22% | 37% | 42% | 45% |
| Operating cost ($M) | 4.0 | 9 | 15 | 21 |
| EBITDA ($M) | -3.5 | -4.6 | -3.2 | +3.8 |
| Largest customer share | 70-90% | 55-65% | 45-55% | 30-40% |
| Equity value a rational market assigns ($M) | 12-20 (seed post-money) | 80-150 | 200-350 | 200-450 |

- Equity raised to year five: $35-45M.
- Valuation basis: 8-10x run-rate while growth exceeds 300% (Fleet 12.5x [source above]); 4-8x revenue at $55M growing 30-50% with quarter-length contracts; public testing-and-certification and data vendors trade at 2-4x revenue [DK]. The 30x net multiple in the notes belongs to marketplaces that doubled in six months and is not a steady-state price. Appen was valued at $4.3B with five clients at 80% of revenue [notes] and lost almost all of it [DK].
- Year five is wide because junior finance work may be solved by 2029. Demand then moves to longer, senior tasks that fewer experts can write, or it stops. Probability-weighted year-five revenue is about $40M and value about $150-250M.
- If the largest customer leaves in year three: revenue falls about 50% within 90 days. Expert cost is variable and falls with it. Fixed cost of about $15M stays, so cash burn rises from $3M to roughly $9M a year. Scale AI lost two labs within months [notes].
- Upside case (certification named in bank procurement, revenue about $200M): $1.5-2.5B, probability under 8%.

## 2. Delivery personas

### 2.1 Operations head, ex expert-data business above $50M revenue

- Incentives: has seen acceptance disputes, expert fraud and a customer leaving in one quarter. Paid to keep margin and cash.
- Findings: cost table in 1.2. First-pass internal reject rate 25-40%; customer reject 10-20% in the first two quarters with any new lab, falling to 5-10% [DK]. Quality control is 25-30% of direct cost and does not shrink with scale because each lab changes its spec roughly quarterly [DK]. Expert fraud (LLM-written submissions, identity sharing) runs 5-15% of new contractors and needs proctoring and forensic review [DK; the concern is in source: Epoch].
- Experts multi-home. The same ex-banker works for a lab direct at $150, for a marketplace, and for this company. A bench is not an owned asset.
- Decision: would not run this at the brief's prices. Would run it as custom work at $3,500-4,500 per accepted task with 30% paid on order.
- Disputes: gross margin 55-65% (says 35-45% at steady state); AI halving hours (says 20-25%).
- Would change view: two labs each licensing the same 1,000 tasks at $1,500 or more; measured customer reject below 8% for two quarters.

### 2.2 Compliance counsel, investment bank or audit firm

- Constraints: outside-activity approval is required for registered staff; firm templates, models and workpapers are firm property; client information is confidential by contract and by professional rule; auditors must stay independent of audit clients, and the labs' largest investors and cloud partners are audit clients of the large firms [DK].
- Decision: refuses outside-activity approval for any current employee. Reasons: (1) the work is training software to do the firm's own product; (2) the firm has, or is negotiating, its own commercial arrangement with a lab (Goldman Sachs is an investor in Anthropic's deployment venture [notes]); (3) no way to prove an employee did not reuse a firm template or a real deal; (4) for audit staff, a paid relationship with a vendor to an audit client's affiliate is an independence question nobody will sign off for a side job.
- Former staff: cannot be stopped from working, but remain bound by confidentiality. Counsel sends a reminder letter and will sue on evidence of a real deal file in a dataset.
- Consequence for the founder: authors are former bankers and auditors only, and every dataset is synthetic. Labs will ask for uncapped or 2-3x-fees indemnity on IP and confidentiality, and audit rights over author provenance [DK]. One contaminated file is a product recall.
- The firms that hold the real files can sell access to labs themselves. The Benchling-Anthropic pattern and the FactSet and Intuit integrations [notes] show labs prefer the data owner.
- Would change view: a firm-level contract in which the firm is paid, controls the content and takes the reputational credit. That makes the firm the supplier and the start-up a tooling contractor.

### 2.3 Staff research engineer weighing the technical co-founder seat

- Position: employed at a frontier lab weeks before a listing at a reported $1.5-2T [notes]. Compensation is mostly equity about to become liquid [DK].
- What breaks first, in order:
  1. Graders. A leveraged buyout model or an audit workpaper has no unit test. Rubric grading by a model is noisy and exploitable; graders need many iterations [source: Epoch]. Expect a quarter of engineering time on grader disputes.
  2. Harness drift. Every lab has its own sandbox, tool interface and difficulty target. "One library, many buyers" becomes a porting job per lab per quarter.
  3. Held-out leakage. Running a private test through a vendor's API hands the vendor the prompts unless retention is contractually zero and verified. Each certification cycle needs fresh tasks: 200-500 tasks x $2,500 = $0.5-1.25M, more than the $150-500K fee unless at least five vendors share a cycle.
  4. Conflict. The same company sells training tasks to the lab whose model powers the agent it certifies. Any rival can say the test was trained on.
  5. Difficulty treadmill, as in 1.5.
- Decision: does not leave. Would advise for 0.5-1% equity.
- Terms to leave: equal co-founder equity, a signed paid lab order of at least $2M, a closed seed of at least $8M, and a salary of $300K. Even then prefers joining an environment company already at $50M with a liquid package.

### 2.4 Standards and regulator view

- United States, banks: no requirement and no recognition. SR 26-2 excludes generative and agentic AI and keeps third-party models inside the bank's own validation [source above]. A vendor's certificate does not replace the bank's own testing; the bank cannot delegate that responsibility [DK].
- United States, insurance: state bulletins based on the NAIC model make the insurer responsible for third-party AI and let examiners ask for documentation. No certification scheme [DK].
- United States, securities: no agent certification rule [DK].
- European Union: high-risk duties for credit scoring and life and health insurance pricing start 2 December 2027 [source above]. For those Annex III uses the conformity assessment is the provider's own internal control, not a notified body [DK, not confirmed by the search]. Harmonised standards are late [DK].
- What exists: ISO/IEC 42001 certificates for AI management systems from accredited bodies [DK]; AIUC-1 as a private scheme tied to insurance [source above]. Neither is recognised by a financial supervisor.
- What recognition would take: an accredited scheme under ISO/IEC 17065 or 17025 (12-24 months), then a standard, then a rule citing it: 3-7 years in total [DK]. Accreditation requires impartiality: a certification body may not supply or advise on the thing it certifies [DK]. A company selling training data to the labs fails that test unless the certifier is a separately owned and governed entity.
- Decision: will not recognise or require. Probability that a US bank supervisor requires third-party agent certification by 2031: under 10%.
- Would change view: a public failure of an agent at a supervised firm with customer harm, followed by legislation.

## 3. Capital and competition personas

### 3.1 Skeptical venture investor

- Revenue quality: quarter-length statements of work, termination for convenience, acceptance-based billing, perpetual licence on delivery. This is project revenue. Not ARR.
- Concentration: 70-90% from one lab in year one, about half in year three. Mercor at $2B gross still has 91% from two [notes].
- Competitors: Mercor (owns APEX with investment-banking tasks since January 2026, bought an environment builder in July 2026), Fleet ($60M, $750M), Handshake, Surge, Turing, 35+ seed-stage specialists, and the labs' own teams (100+ ex-bankers since 2025) [sources above; notes]. The founder is at least 12 months late in finance.
- Exits observed: Deeptune sold four months after a $43M Series A; Mechanize reported acqui-hired [notes, unverified]. The category is consolidating into marketplaces before specialists reach scale.
- Seed decision: refuses at the founder's plan. Would put $3-4M in at $15M post-money if there is a technical co-founder from a lab and a signed paid pilot of at least $500K.
- Series A decision: refuses until $8-10M run-rate, three lab customers with none above 50%, gross margin at or above 40%, and at least 1,000 tasks each licensed to two or more buyers. Then $20-25M at $100-140M post-money.
- Plausible exit: $150-600M to a marketplace, a financial-data vendor or a testing firm. Above $1-3B needs a mandated certificate. Probability of an outcome above $1B: 5-8%.

### 3.2 Incumbents responding rationally

(a) Largest expert-data marketplace. Already sells this. Bids the same lab requests at cost plus 30-40% with the lab owning the output, which the lab prefers. Raises pay 20% for the founder's best 50 authors. Publishes its own benchmark free to set the reference. If the start-up gets lab-qualified, offers $20-80M for the team.

(b) Environment specialist above $50M revenue. Has approved-vendor status, harness integrations and security review done at each lab. Adds a finance vertical in one quarter by contracting 20-30 former bankers when a lab asks. Does not need to own the IP because it wins on delivery speed.

(c) Labs' in-house teams. Keep building in-house for anything that reveals training priorities [source: Epoch]. Buy from the start-up as overflow: master agreement plus quarterly statements of work, 30-day termination for convenience, acceptance testing, net 45-60, perpetual irrevocable right to train and keep derived weights, most-favoured pricing, no publicity. Non-exclusive library: yes, at $300-800 per task and $0.5-2M per domain per year, for evaluation breadth. Time-limited exclusivity: refused. A window as long as the task's useful life is ownership in all but name, and the lab will not let work built around its model's weaknesses be resold to a rival. Decision: signs a $250-500K paid pilot statement of work, lab-owned or perpetually exclusive.

(d) Large consulting or audit firm with an AI assurance line. Already selling AI controls and assurance to the same banks [source above] and holds the board and regulator relationships. Ignores the start-up. If its benchmark gains users, licenses it as a test tool for $100-300K a year or builds one, and keeps the engagement fee. Its own limit: independence rules restrict what it can do for audit clients. That gap is real but small.

(e) AI assurance start-up. $55M raised, a named standard, an insurance partner and the reference customers the founder would need [source above]. Adds a finance performance module. Buys test content from several suppliers including this one at $200-500K a year. Tells every buyer that the founder's company trains the models it tests.

### 3.3 Lender asked to finance lab receivables

- Obligor credit: strong. Anthropic held $112.4B of cash in June 2026; OpenAI raised $122B in March 2026 [notes].
- Problems are not credit: 100% concentration in two or three obligors; invoices are valid only after acceptance; rejection and credit-note risk; quarter-length contracts so the borrowing base can halve in 90 days; set-off rights; anti-assignment clauses in lab agreements; no collateral value in a library that decays 50% a year.
- Decision in year one: refuses. No collection history.
- Decision after six months of collections with dilution below 5%: lends. Terms: 80% advance on accepted invoices under 60 days old; no advance on unbilled work, backlog or library; obligor concentration limit waived to 50% each for these names; all-in cost 10-12% plus warrants [DK]; minimum monthly billings $1M; facility $2-5M; springing cash dominion; notification to the labs.
- Covers about 60% of the working-capital gap. The library build stays equity-funded.

### 3.4 New independent buyer, head of data partnerships at an enterprise-software company with its own models

- Robotics variant: refuses. Finance tasks are irrelevant to the product.
- Enterprise-software variant (accounting, ERP or financial-data vendor): owns real workflow data and its own tool interface. Needs an outside test of its agent, not training volume.
- Decision: signs a purchase order for a one-off evaluation set. 400 tasks at $450 = $180K, plus $40K to adapt to its tool interface. Non-exclusive, perpetual internal-use licence, net 60, right to reject 10%.
- Refuses a $2-10M annual subscription. Budget for external evaluation content is $200-500K a year [DK]. For staffing volume it would use a marketplace already on its approved vendor list.
- Certification: would pay $50-150K a year per agent if at least two of its bank customers name the certificate in procurement. Today none does. Compares it with a SOC 2 audit at $30-150K [DK].
- Would change view: a bank customer making the certificate a contract condition.

## 4. Answers to the founder's test questions

- Unit economics: cost about $2,500 per accepted task. A non-exclusive task needs four licensees at $800, or two at $1,500, just to break even.
- Reusable share: 15% of revenue in year one, about a third by year three.
- Contract terms: quarterly, terminable, acceptance-based, perpetual training rights. Labs take non-exclusive libraries cheaply and insist on owning or permanently controlling anything bespoke.
- Largest customer leaves: revenue down about half in a quarter, burn triples.
- What accumulates: grader tooling, harness adapters, a score history if the benchmark is used. Competitors reproduce the first two in one or two quarters. The score history only has value if the benchmark is seen as independent, which the training business undermines.
- IP after models pass: 5-10% of original price.
- Scale: larger, not more defensible. Cost per task does not fall much, experts multi-home, and the marketplaces hold the supply-side scale.
- Certification: no regulator requires it, a funded competitor holds the reference customers, and the fee does not cover fresh held-out tasks without five or more vendors per cycle.

## 5. Numbers in the brief the panel disputes

| Brief | Panel | Basis |
|---|---|---|
| $500-2,000 per environment, non-exclusive | $300-800 per task non-exclusive; $2,000-4,500 exclusive or custom | [source: Epoch]; exclusive is 4-5x |
| $2-10M per lab per domain per year | $0.5-2M non-exclusive; more only as custom work | contracts six to seven figures a quarter per vendor, neolab $300-500K [source: Epoch] |
| Time-limited exclusivity at 4x | Labs require perpetual exclusivity or ownership | useful life 6-12 months |
| Expert hours halve with AI assistance | Net cost down 20-25% by year three | rising difficulty bar; labs restrict model-written content |
| Gross margin 55-65% | 22% year one, 42% year three, 45% year five | section 1.3 |
| Certification $150-500K per agent per task family | $50-150K | SOC 2 comparison; no mandate |
| $100M from five buyers at $10-20M each | At most two labs spend $10M+ with one finance vendor; base case $55M in year five | section 1.7 |
| "Coding is covered, finance is next" | Finance has been worked in-house since October 2025 and benchmarked since January 2026 | [sources above] |

## 6. Probabilities

- First paid commercial delivery within 18 months: 60%. The bar is low (labs use more than a dozen vendors [notes]), but there is no technical co-founder and vendor onboarding takes 2-4 months.
- $1 billion of annual recognized revenue within 7 years: 0.5%.
