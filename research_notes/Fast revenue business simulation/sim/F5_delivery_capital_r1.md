# F5 v1, round 1: delivery, capital and competition panel

Date of simulation: 24 November 2026. Brief tested: `F5_v1.md` (physical-work data for robotics labs, organic). Everything below is a simulated hypothesis from archetype personas. It is not customer validation. No real person was interviewed.

Evidence labels: **[source: URL]** page or search result retrieved in this session, **[notes]** `precedents_and_lab_data.md`, **[DK]** domain knowledge, unverified. Six web calls were used (three searches, three fetches; two fetches failed with 403 and 429).

## 0. Facts added by this panel's searches

| Fact | Label |
|---|---|
| Automated robot-video labelling is listed at $9 per video-hour for subtask timelines. Add-ons: 2D hand tracking $12, 3D hand tracking $14, per-hand activity labels $6. Full stack about $29 per video-hour, against about $76 for a rival model | [source: https://fourweekmba.com/ai-perceptron-puts-robot-video-labels-at-9-an-hour-astra-76/ and https://explainx.ai/blog/perceptron-egocentric-1-0-api-9-dollars-video-hour-egohome-gpt-6-astra-one-eighth-cost-2026, via search summary, vendor list prices] |
| One Indian market report: raw egocentric $1-10 per hour, packaged resale $15-50 per hour, rates down 30% from January to June 2026 as suppliers enter | [source: search summary; page not identified, probably https://startupfeed.in/?p=9184 or https://www.metaintro.com/blog/india-workers-robot-training-data-2026, which returned 429] |
| Egocentric $3-25 per worker-hour against $118-200 per loaded hour for teleoperation. Same unverified figure as in the notes; again seen only in a summary | [source: search summary, page not identified] |
| A small-lot marketplace lists packaged egocentric sets at $90-1,800 per recorded hour, 10-hour minimum; $90 for a household set, $270 for a 4K light-manufacturing set | [source: https://www.roboticscenter.ai/fr/marketplace, via search summary] |
| Contributor pay: about $6 per accepted hour described as the market standard; listings $3-15; some US postings $20-30 per hour. Rejected footage earns nothing. Figure Index reported at $6-18 per task, no published hourly rate | [source: search summary of https://aitrainer.work/guides/get-paid-to-film-yourself-doing-chores, https://remowork.life/blog/get-paid-to-record-household-chores-egocentric-ai-data-platforms-2026, https://realwaystoearnmoneyonline.com/get-paid-for-chores/] |
| Teleoperation: operator labour $25-60 per hour in the US; full programs $15 to $150+ per hour; acceptance on complex tasks 70-85%; per-hour billing puts rejected episodes on the buyer's invoice | [source: search summary of https://roboticscenter.ai/blog/robot-data-collection-cost and https://particula.tech/blog/teleoperation-vs-simulation-vs-human-video-robot-data] |
| A basic capture kit (two USB wrist cameras, mounts, head strap, hub) costs about $151 | [source: https://jumptask.io/blog/egocentric-data-market-review/, opened; vendor with a commercial interest] |
| Generalist AI passed 500,000 hours, having grown about 10,000 hours a week from 270,000. JD.com and the city of Suqian target 10,000,000 hours over two years. Eight Chinese cities opened data collection centres in March 2026. One gig network claims 18 million contributors in 150 countries | [source: https://jumptask.io/blog/egocentric-data-market-review/, opened] |
| A 2026 study: models trained on 5,000 hours of human first-person video scored 90% higher on unseen tasks than those trained on 5,000 hours of teleoperation | [source: https://jumptask.io/blog/egocentric-data-market-review/, opened; study not named or checked] |

## 1. Panel arithmetic used by all personas

### 1a. Cost per accepted annotated hour, first-person video

| Line | US workplace (the brief's model) | Offshore workplace or gig | Basis |
|---|---|---|---|
| Worker bonus per captured hour | $4-6 | $1-3 | [source: contributor pay figures above]; workplace workers are already on wages [DK] |
| Employer or facility fee | $2-5 | $0.5-1.5 | [DK] |
| Site coordinator and field technician | $1.5-2.5 | $0.3-0.6 | 1 per about 40 rigs [DK] |
| Rig depreciation, loss and repair | $1.2-2.0 | $0.2-0.5 | $1,200 synced multi-view rig, 110 captured hours a month, 12-month life, 25% annual loss [DK]; $151 kit offshore [source: jumptask] |
| Upload, storage, compute, face and audio redaction | $1.5-2.5 | $1.0-2.0 | 8-15 GB per rig-hour [DK] |
| Raw cost per captured hour | **$10-18** | **$3-8** | sum |
| Yield (accepted share of captured hours) | 65-75% | 55-70% | idle time, occlusion, misalignment, privacy scrubs [DK] |
| Raw cost per accepted hour | $14-26 | $5-13 | |
| Hand pose and action labels, model-assisted with human QA | $8-18 | $5-12 | list price $9-29 automated [source: fourweekmba]; human QA 1-2x real time [DK] |
| **Cost per accepted annotated hour** | **$22-44** | **$10-25** | |

Reading: at the brief's $40 floor a US workplace hour earns 0-45% gross margin. At the price the market is moving to (section 1c) it earns nothing unless the hour carries a real premium.

### 1b. Cost per accepted hour, teleoperation on the customer's robots (US site)

| Line | Value | Basis |
|---|---|---|
| Operator, loaded | $35-50 per paid hour | [source: roboticscenter, particula summaries] |
| Robot uptime x acceptance | 0.70 x 0.80 = 0.56 | acceptance 70-85% [source: particula]; uptime [DK] |
| Operator cost per accepted hour | $63-89 | arithmetic |
| Robot technicians, supervision, QA | $18-25 | [DK] |
| Site lease, power, network | $8-12 | [DK] |
| Data infrastructure | $3-5 | [DK] |
| **Cost per accepted hour** | **$92-131** | consistent with $118-200 loaded [notes, unverified] |
| Price in brief | $150-250 | |
| Gross margin | 15-45%, midpoint about 30% | only if the customer supplies and maintains robots at its own cost |

Throughput: one station on two shifts gives about 170-240 accepted hours a month [DK]. 100,000 teleoperation hours a month would need about 500 customer robots and 1,200 operators. No customer consigns that to a start-up. A realistic ceiling in 18 months is 30-50 stations.

### 1c. Price trajectory, panel estimate

| Product | Brief | Early 2027 | End 2027 | End 2028 | Basis |
|---|---|---|---|---|---|
| Generic first-person video, annotated, program volume | $40-150 | $12-25 | $8-15 | $4-8 | packaged $15-50 and falling 30% per half-year [source: search summary]; automated labels $9-29 [source: fourweekmba] |
| Rights-cleared US workplace video, skilled tasks, calibrated multi-view | $40-150 | $30-60 | $20-40 | $12-25 | 2-3x generic premium [DK] |
| Teleoperation on customer robots, US site | $150-250 | $150-200 | $130-170 | $100-140 | remote operators abroad at $6-12 per hour are the next step [DK] |

### 1d. Standing up 100,000 accepted first-person hours a month in US workplaces

- Rigs: 100,000 / (110 captured x 0.72 yield) = about 1,260 active rigs, 1,500 with spares. At $1,200 each: $1.8M. With mocap gloves on a fifth of workers (300 pairs at $2,000): another $0.6M. [DK]
- Workers and sites: about 1,300 workers wearing daily. At 25 consenting workers per site: about 50 sites. [DK]
- Time: each host employer needs legal review, insurance, worker consent and often its own customers' consent. 2-4 months per employer; staffing firms shorten recruitment, not host consent. **10-14 months** to reach 100,000 a month. [DK]
- Contrast: a gig model delivered 1M+ hours in its first beta month [notes, Memories.ai]. The workplace model is slower by an order of magnitude.

### 1e. Cash to month 18 (base plan: about 75,000 first-person hours a month and 30-40 teleoperation stations)

| Item | $M |
|---|---|
| Rigs, gloves, spares | 2.0-2.5 |
| Two teleoperation sites, fit-out and deposits | 0.8-1.2 |
| Pipeline and engineering team (8-10 people, 18 months) | 4.0-4.5 |
| Field operations and site onboarding (30-40 people) | 4.0-5.0 |
| Legal, privacy programme, insurance | 0.8-1.2 |
| Working capital (workers paid weekly, buyers pay in 45-75 days) | 2.5-3.5 |
| **Total** | **14-18** |

The founder's $5-10M does not reach month 18 without a seed. Rigs are a small part of the need. Payroll and working capital are the capital.

## 2. Delivery personas

### P1. Operations head, has run large first-person and teleoperation programmes
- **Incentives and constraints:** paid on accepted hours and rejection rate. Has seen programmes fail on yield, not on recruitment.
- **Alternatives:** stay with a funded collector or a lab's in-house team.
- **Numbers offered:** raw US workplace cost $10-18 per captured hour; yield 65-75%, and in warehouses only 50-60% of accepted time is manipulation because the rest is walking and scanning; rig loss and breakage 3-6% a month; one site yields about 2,000 accepted hours a month; teleoperation cost $92-131 per accepted hour. [DK]
- **Decision:** would run it as a hired head of operations. Refuses to sign up to the brief's plan of 100,000-1,000,000 hours a quarter in workplaces inside 12 months.
- **Terms:** commits to 25,000 accepted hours a month by month 9 and 75,000 by month 15, with 40 field staff.
- **Reasons:** host-employer consent is the rate limiter. Buyers now specify "manipulation-dense" hours and pay per accepted hour, so idle time is the supplier's cost.
- **Would change the decision:** a national staffing firm or contract-logistics operator signing a master agreement covering 30+ sites, with consent wording already agreed.

### P2. Capture hardware maker (head-mounted multi-camera rigs, gloves)
- **Incentives:** sells to every collector and lab. Capacity is tight because labs, Chinese city data centres and gig platforms are all ordering. [source: jumptask for the buyers; DK for capacity]
- **Alternatives:** sell the same units to the funded collector, the labelling company or directly to robot makers, who order in larger lots.
- **Decision:** **accepts a purchase order.** No exclusivity, no credit.
- **Price and terms:** synced multi-view head and wrist rig $900-1,300 at 1,500 units; mocap gloves $1,500-6,000 a pair for accurate ones, $300-1,500 for low-cost ones; 40% deposit; 10-14 weeks lead time; 12-month warranty excluding industrial wear. Glove sensors last about 200-400 working hours. [DK]
- **Reasons:** a commodity order. The maker notes it is itself packaging data from devices it has in the field.
- **Would change terms:** a 5,000-unit order with a 12-month forecast earns a 15-20% discount and a shorter lead time, still without exclusivity.

### P3. Annotation vendor (hand pose and action labels)
- **Incentives:** sells annotation to the same buyers directly. Per-hour list prices are public and falling.
- **Decision:** **signs a three-month supply contract.** Refuses exclusivity.
- **Price:** $12-18 per video-hour blended at 100,000 hours a month (automated 3D hand pose, subtask segmentation, human QA on a 5% sample); $25-40 with human-written action narration; net 30. [DK, anchored on the $9-29 list price, source: fourweekmba]
- **Quality warning:** automated 3D hand pose is off by 10-20 mm under occlusion and fails on gloved hands and tool occlusion, which is most kitchen, warehouse and laundry work. Per-frame human correction costs $200+ per hour and nobody buys it at scale. [DK]
- **Reasons and dispute:** the "100 times the value at 20 times the cost" claim [notes, Encord] comes from an annotation seller. Observed prices show packaged data at 5-15 times raw [source: search summary], not 100. The largest buyers run their own labelling models and ask for raw video plus calibration.
- **Would change the decision:** nothing makes it exclusive. A 12-month volume commitment cuts price by about 20%.

### P4. Privacy and employment counsel
- **Position:** the programme is lawful in a narrow configuration and unlawful or unmanageable outside it.
- **Permits:** commercial kitchens, laundries, light assembly and non-union warehouses, in states without a private right of action for biometrics. Conditions: written informed consent from each worker with a real option to decline; no audio (all-party consent states include California, Illinois, Washington, Florida, Pennsylvania); face blurring of bystanders before data leaves the device or the site; a published retention schedule; host employer and, where goods or premises belong to third parties, their written consent. [DK]
- **Refuses:** hotel guest areas and anywhere patients or minors appear. Illinois without a written release and retention policy, because hand and face geometry are named biometric identifiers with statutory damages of $1,000-5,000 per person [DK]. Unionised sites until bargained, since workplace cameras are a mandatory bargaining subject [DK]. EU sites until a works-council agreement exists and an employment lawful basis other than consent is documented [DK].
- **Cross-border:** sending US workplace video to offshore annotators exposes host employers' trade secrets and their customers' goods. The US rule on bulk sensitive personal data restricts biometric data on more than 1,000 US persons going to countries of concern, which rules out Chinese buyers and annotators. [DK]
- **Employment:** a third-party bonus must be counted in the regular rate for overtime; the staffing firm will demand indemnity for wage claims, joint-employer claims and injuries linked to headgear or gloves. Sensor gloves conflict with food-safety and machine-guarding rules in some tasks. [DK]
- **Cost:** $300-500K to set up, $1-2 per hour for redaction, $150-400K a year for cyber, media and errors-and-omissions cover. [DK]
- **Unpriced risk:** workers are recording data to train machines that do their jobs. Expect union campaigns and at least one host employer withdrawing after press coverage.
- **Would change a refusal:** signed collective agreement or works-council agreement; on-device redaction verified by a third party.

### P5. Robotics researcher on substitutes
- **View of the evidence:** more real data still helps. Task score rose from 20% to 53% between 1,000 and 1,000,000 hours [notes, weak]. That is 11 points per tenfold increase, so each added hour is worth a tenth of the previous decade's. Human video beat teleoperation on unseen tasks at equal hours in one 2026 study [source: jumptask, unchecked].
- **Substitutes in two years:** internet video with latent-action extraction for pretraining; generated video from world models for augmentation; and above all data thrown off by robots already deployed, which costs the maker nothing. [DK]
- **How much purchased real data in two years:** leading developers will each hold 10-100M hours of first-person video, mostly from their own apps and devices at under $5 an hour. What they will still buy: (1) small, precise teleoperation and correction sets for their own embodiment, (2) touch and force data that video cannot supply, (3) rare environments they cannot enter. Panel estimate of external robotics-data spend outside China: $150-300M in 2026, $300-800M in 2028, with first-person video a falling share of dollars and a rising share of hours. [DK, own estimate]
- **Decision as a technical buyer:** would sign a pilot of 2,000-5,000 hours at $30-50 only for calibrated multi-view data with touch or force in settings the lab cannot access. Would not buy generic workplace video at $40.
- **Would change the view:** evidence that video from real industrial workplaces transfers better than home gig video per hour by a factor above the price ratio.

### P6. Senior robotics-data engineer asked to join as technical co-founder
- **Incentives:** current pay at a lab or funded robot company of $600K-1.5M a year [DK]. Career risk of joining an operations business with no technical edge.
- **Alternatives:** stay; join the $70M-funded collector; join a robot maker's in-house data team.
- **Decision:** **declines co-founder. Offers to advise for 0.5-1%.**
- **Reasons:** the durable technical work (hand pose, retargeting human motion to robot bodies, automatic labelling) is being sold as an API at $9-29 an hour and is better inside the labs. What is left is site operations and consent paperwork. The founder has no relationships with the researchers who hold these budgets [notes: budgets sit with researchers, not procurement].
- **Would join if:** a signed anchor contract of at least $5M with a 12-month minimum; 20%+ equity; the product includes a sensor the labs do not have (touch or force) and the right to resell.

## 3. Capital and competition personas

### P7. Skeptical venture investor
- **Revenue quality:** quarterly orders, terminable for convenience, acceptance-contingent, concentrated in 2-4 buyers. Repeat but not recurring. One buyer already took this in-house because vendors missed its bar [notes, Figure].
- **Comparables:** $70M raised for about 20 customers and no disclosed revenue [notes, XDOF]. A $16M-funded gig collector with three of the top five labs [notes, Memories.ai]. A labelling company delivering 1,000+ demonstration hours a day [notes, Scale]; at $100-200 an hour that implies $36-73M annualized, so the leader is plausibly near $40M but nobody else is [panel inference]. Human-data leaders trade at about 10 times run-rate [notes, weak], but they grow 5-10 times a year at 30%+ margin with no equipment.
- **Value at $40M:** a physical capture service at 30% gross margin, falling prices and 70% concentration is worth 1.5-3 times revenue: **$60-120M**. In a hot round, up to $200M.
- **Seed decision:** **declines to lead.** Would put $1-2M into a $6M seed at $25M post-money or less, once one paid pilot is invoiced.
- **Next round decision:** **no at this description.** Yes at $20-30M on 2-3 times run-rate if: three buyers each under 40% of revenue, signed 12-month minimums covering half of next year's plan, gross margin above 40% for two quarters, and 20% of revenue from non-exclusive resale.
- **Sharpest point:** scale adds sites and payroll, not defensibility. The only asset that compounds is exclusive site access, and the employer owns it.

### P8. Incumbents responding rationally

| Incumbent | Response | Effect on the founder |
|---|---|---|
| (a) Funded robot-data collector, $70M raised | Matches teleoperation price, holds customers with 12-month agreements and robots already on its floor, offers first-person video near cost as an add-on, hires the founder's site leads | Founder is kept out of the 20 accounts that already have consigned robots. Would subcontract overflow raw video to the founder at $8-12 an hour |
| (b) Large labelling company adding capture | Already has master agreements and security approvals with every buyer; annotation is its marginal-cost product; sources video from crowd at under $10 | Undercuts any annotated-hour price. Would buy US workplace capture from the founder at $15-20 annotated, as a subcontractor |
| (c) Overseas collection operators | Sell raw at $1-5 and packaged at $15-50, falling 30% per half-year [source: search summary]. Already recording factory workers in India [source: search result title, metaintro] | "Real workers in real workplaces" is not a US-only product. Sets the price for anything not tied to a US site |
| (d) Robot makers' in-house teams | Buy raw, label themselves, use vendors for burst and diversity, dual-source, 30-day termination, will not consign more than 10-20 robots to a new vendor | Take the steady volume and leave the peaks. Largest buyer leaving removes 40-70% of revenue within a quarter |
| (e) General expert-data marketplace | Already pays contributors in 100+ countries and is reported to collect chore video at volume [notes, unverified]. Adds workplace capture by partnering with staffing firms | Most likely acquirer of a small site-access business, at single-digit to low tens of millions, as with its earlier environment-builder purchases [notes] |

All five: **none buys from the founder as a prime supplier.** Two would subcontract at $8-20 an hour.

### P9. Lender asked to finance rigs and receivables
- **Rigs:** **refuses.** Consumer-grade cameras with a 12-18 month life, 3-6% monthly loss and no resale market are not collateral. A vendor lease is possible at 12-15% with 20-30% down and a corporate guarantee. [DK]
- **Receivables:** **offers a $2-5M line after six months of billing history.** Advances 80-85% on accepted invoices to investment-grade technology companies and 50-70% on unrated venture-backed robot makers, at SOFR + 4-6%, with a 25-35% limit per debtor. [DK]
- **Reasons:** invoices are subject to acceptance and rejection, so only accepted invoices are eligible. The concentration limit bites because two or three buyers are most of the book. The best credits (large technology groups) are the ones that collect in-house.
- **Would change the decision:** take-or-pay minimums from an investment-grade buyer with no acceptance contingency.

### P10. New independent buyer: head of autonomy, agricultural or construction equipment maker
- **Need:** operator behaviour on its own machines (cab cameras, joystick inputs, machine bus signals) across many job sites. Not hand-pose video of warehouse or kitchen workers.
- **Constraints:** approved-vendor onboarding takes 4-6 months; $5M umbrella insurance; payment in 60-90 days; data must be owned exclusively by the buyer; autonomy data budget $2-10M a year in total. [DK]
- **Alternatives:** instrument its own demonstration fleet; collect through dealers and large fleet customers with existing telematics; use its current labelling vendor.
- **Decision:** **signs a paid pilot purchase order. Refuses a multi-year contract and refuses any resale right.**
- **Price and terms:** $250-400K for 3,000-5,000 instrumented operator hours across 20+ job sites at $60-100 per accepted hour, delivered over four months, with the founder supplying contractor and rental-fleet access.
- **Reasons:** what it cannot easily get is varied third-party job sites, and that is what it pays for. Volume is two orders of magnitude below the brief's programmes.
- **Would change the decision:** a pilot showing measurable gain in its autonomy metrics leads to a $1-3M annual programme, still exclusive.

## 4. Tests requested

| Test | Finding |
|---|---|
| Unit economics per hour | First-person US workplace: cost $22-44, market price moving to $20-40 for premium and $8-15 for generic. Teleoperation: cost $92-131, price $150-200, margin about 30% |
| Capital for rigs and sites | Rigs $2-2.5M for 100,000 hours a month. Total cash to month 18 is $14-18M, mostly payroll and working capital |
| Price as overseas supply grows | Generic annotated video falls about 30-40% a year to $4-8 by end-2028. Only site-specific, rights-cleared or touch-instrumented data holds a premium |
| Largest buyer goes in-house | Already happened once in this market. Expect 40-70% of revenue to stop within one quarter while site leases and field staff run on for 30-90 days |
| Reuse of a dataset | Teleoperation on a customer's robots: none. First-person video: resale possible where the first buyer accepts non-exclusive terms; panel assumes 15-30% of hours resold at 30-50% of the first price. Every buyer in this panel asked for exclusivity or camera layouts matched to its own robot |
| What accumulates | Host-employer agreements, a consented worker pool, a QA pipeline and a library whose useful life is 12-24 months. The employers own the scarce input |
| Does scale defend | No. Scale adds sites, rigs and staff linearly. Buyers pay for diversity of environments, which favours gig capture and overseas operators. The business gets larger, not harder to copy |

## 5. Panel revenue estimate

Quarter 1 starts at company formation. Figures are gross recognized revenue, $M.

| Case (probability) | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Year 1 | Trailing 12 months at month 18 | Year 2 | Year 3 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bear (35%): pilots only, anchor leaves | 0 | 0.2 | 0.5 | 0.8 | 1.2 | 1.5 | 1.5 | 4.0 | 6 | 5 or wound down |
| Base (50%) | 0 | 0.3 | 1.2 | 2.5 | 3.8 | 5.0 | 4.0 | 12.5 | 21 | 30 |
| Bull (15%): one anchor signs 500,000 hours and 40 stations | 0.1 | 1.0 | 4.0 | 8.0 | 12.0 | 15.0 | 13.1 | 39.0 | 60 | 95 |
| Probability-weighted | 0.0 | 0.4 | 1.4 | 2.7 | 4.1 | 5.3 | 4.5 | 13.5 | 22 | 31 |

Base-case build for Q6: 100,000 first-person hours at $18 ($1.8M), 18,000 teleoperation hours at $160 ($2.9M), resale $0.3M.

Even the bull case sits just under $40M at month 18.

## 6. Four numbers

| Measure | Panel estimate |
|---|---|
| Probability of a first paid commercial delivery within 9 months | 75% (a pilot of $100-400K) |
| Probability of $40M gross recognized revenue in a trailing twelve months by month 18 | 6% |
| Probability of $100M by month 36 | 4% |
| Year five if it works | Gross margin 30-35%; equity value $250-400M, most likely through sale to a labelling or expert-data company |

Revenue type: repeat quarterly orders under master agreements, terminable for convenience and subject to acceptance. Not recurring. Teleoperation is the closest to contracted.

## 7. Numbers in the brief the panel disputes

| Brief | Panel | Basis |
|---|---|---|
| First-person video $40-150 per annotated hour | $12-25 generic and $30-60 rights-cleared US workplace in early 2027; falling 30-40% a year | [source: search summaries; fourweekmba list prices] |
| A 1,000,000-hour programme at $40 is $40M | Worth $8-20M in 2027 | A gig collector delivered 1M+ hours in a month [notes]; the largest in-house buyer had paid contributors $15M in total [notes] |
| Gross margin 35-45% | 25-35% at scale; negative to 15% in year one | Section 1a, 1b |
| Programmes of 100,000 to 1,000,000 hours ordered quarterly | Achievable supply in US workplaces is 25,000 a month by month 9 and 75,000-100,000 by month 15 | Section 1d |
| "Over $1bn committed to data and compute" as demand | Mostly compute, from a buyer that collects in-house. Addressable for an outside collector: about zero | [notes] |
| "No supplier has disclosed revenue near $40M" | True as disclosed. Implied revenue of the leader is $36-73M annualized from 1,000+ hours a day | [notes] plus panel arithmetic |
| "Annotated is worth 100 times raw" | Observed price ratio is 5-15 times | [source: search summary] |
| Teleoperation $150-250 | $150-200 now is fair; capped at 30-50 stations by robot consignment, so about $6-10M a year | Section 1b |
