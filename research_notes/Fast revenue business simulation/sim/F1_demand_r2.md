# F1 v2 demand and supply-side panel, round 2

Date of simulation: 24 November 2026. Everything below is a simulated hypothesis built from archetypes. It is not customer validation. No real person, quote, order or interview is represented.

Evidence labels: [source: URL], [notes] (precedents_and_lab_data.md), [domain knowledge, unverified].

Web checks used this round: 4 of 4 (three searches, one page fetch).

---

## 0. Facts checked this round

1. No published lab-side bill rate for expert review of agent runs was found. Only expert pay is public.
   - Mercor's average expert pay is reported at $95, $105 or $110 an hour depending on the source; finance experts are listed from $50 an hour up to $150. [source: https://techcrunch.com/2025/10/29/how-ai-labs-use-mercor-to-get-the-data-companies-wont-share/; https://www.mercor.com/llms-full.txt] (via search summary)
   - With the roughly 35% markup in the notes [notes], the implied bill rate is about $130-150 an hour on average, and about $200 for the top finance tier. This is the panel's arithmetic, not a reported price.
2. Incumbents already sell agent evaluation by experts. Mercor's enterprise evaluation page offers expert staffing (client directs the work), "Production Rubrics" (live scoring of deployed agents against expert-built pass or fail criteria) and benchmarks. It prices per task, "rather than per head". It cites 200,000+ trained evaluation authors, under six weeks from first conversation to a reusable suite, and finance and coding case studies of 160 and 200 expert-built tasks. It states no inter-rater agreement figures and does not mention failure-step annotation of long runs. [source: https://www.mercor.com/enterprise-evals/]
3. Surge sells finished data per task or per project, so cost follows volume and difficulty, not time spent. [source: https://www.herohunt.ai/blog/mercor-vs-surge-vs-scale-ai-2026-buyer-guide/] (vendor-comparison guide, directional, via search summary)
4. Review is hybrid: model judges take the volume, humans calibrate and spot-check.
   - A Turing case study on delivering agent trajectories reports about a 90% pass rate on automated model-judge review, backed by a 20% manual spot-check. [source: https://www.turing.com/case-study/delivering-agent-trajectories-to-train-and-align-a-frontier-ai-assistant] (via search summary)
   - OpenAI reports monitoring tens of millions of internal coding-agent trajectories over five months, with about 1,000 sent to human reviewers. This is safety monitoring, not training-data review, so it shows triage practice only. [source: https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment] (via search summary)
   - A June 2026 paper argues human-in-the-loop review "does not scale naturally to modern agent development cycles" and proposes encoding expert judgement once and reusing it. [source: https://www.alphaxiv.org/abs/2606.16871] (via search summary)
   - The UK AI Security Institute notes transcripts now exceed what experts can read in full, while conclusions still depend on expert judgement. [source: https://www.aisi.gov.uk/blog/transect-making-large-scale-agentic-evaluations-easier-to-understand] (via search summary)
5. Nothing was found on the size of any lab's standing review programme, the number of expert-hour vendors a lab runs, or how new vendors are added. Persona answers on those points rest on [notes] and [domain knowledge, unverified].

---

## 1. Persona transcripts

Personas 1, 4, 5, B and C are treated as one organisation (Lab A) so orders are not counted twice. Persona 2 is Lab B. Persona 3 is the smaller buyer.

### Buyer 1. Head of human data, frontier lab with $50bn+ revenue run-rate (Lab A)

- Incentives: fill review capacity in finance and accounting without another incident; reduce dependence on one marketplace after March 2026 [notes].
- Alternatives: three approved expert-hour vendors; direct contractors on the lab's own platform; model judges.
- Decision: **signs a paid trial. Standing weekly orders follow only if the trial ranks at or above incumbents.**
- Terms: trial of 1,000 hours over four weeks at $150, about $150K. Then 150-300 hours a week at $145.
- Year one: about 4,500-9,000 standing hours over roughly 30 weeks after onboarding, $0.8-1.45M including the trial. Year two: 20,000-40,000 hours at $140, $2.8-5.6M.
- Reasons: this is how the lab buys, so the shape is right. The price must sit on the existing rate card. The calibration system earns no premium because reviewers work in the lab's tooling and the lab computes agreement itself [domain knowledge, unverified].
- What changes the decision: two quarters at the top of the vendor scorecard moves the allocation from about 10-15% of the domain to about 30%.

### Buyer 2. Agent research lead, second frontier lab or large technology group (Lab B)

- Incentives: failure-step labels on long runs to train and evaluate agents this cycle.
- Alternatives: in-house reviewers; employer's own staff; per-task vendors [source: herohunt guide above].
- Decision: **signs a pilot, priced per reviewed run, not per hour.**
- Terms: 500 runs at $350-600 each with the failure step and a written correction, about $175-300K. Hourly billing refused: it rewards slow reviewers.
- Year one: $0.4-0.8M. Year two: $1.0-2.5M.
- Reasons: failure-step annotation of multi-hour runs is a real gap in incumbents' public offer [source: mercor.com/enterprise-evals]. It is also the task most exposed to model judges within a year.
- What changes the decision: a measured gain from training on the corrections; then volume triples.

### Buyer 3. Head of data, model or agent company outside the top two

- Incentives: an evaluation suite for a finance or legal product; has no vendor-management team.
- Alternatives: Mercor's packaged evaluation offer, under six weeks to a suite [source: mercor.com/enterprise-evals]; own customers' experts.
- Decision: **signs a purchase order.** This is the best-fitting buyer in the panel.
- Terms: suite build plus 20-40 hours a week at $160-190.
- Year one: 800-2,000 hours, $0.13-0.38M. Year two: $0.3-0.6M. Corpus purchase: $0-0.3M once, only with vertical exclusivity.
- Reasons: budget is small. Values the founder's finance network more than a lab does.
- What changes the decision: nothing raises this above about $0.6M a year.

### Buyer 4. Procurement, legal and security lead (Lab A)

- Decision: **approves the trial; approves vendor status with conditions.** Services are easier to approve than data: no provenance question.
- Conditions: SOC 2 Type I now and Type II within 12 months; reviewers work only in the lab's environment; background checks; reviewer confidentiality agreements; reviewers in approved countries; $5M insurance; net 45-60; termination on 30 days; no minimums.
- New points this round:
  - Reviewers see unreleased model behaviour. A leak is a competitive incident.
  - Contractor classification: the largest marketplace faces contractor lawsuits [notes]. The lab wants indemnity for misclassification and co-employment claims.
  - Conflicts: practitioners employed by audit firms and banks need employer permission for outside work; audit independence rules may bar some [domain knowledge, unverified].
- Timing: trial paper in 3-6 weeks; vendor onboarding 6-10 weeks; first cash about 3-4 months from first meeting [domain knowledge, unverified].

### Buyer 5. Finance lead for the lab's data budget (Lab A)

- Decision: **funds the trial and cancellable weekly orders. No commitment beyond 30 days.**
- Benchmarks: direct contractors at $95-110 an hour with no markup on the in-house platform [sources in section 0; notes on in-house platforms]; incumbent vendors at about $130-150.
- Terms: vendor markup capped at about 30-35% over expert pay; volume discounts of 5% above $2M and 10% above $5M a year; pressure to move to price per accepted review.
- Year-two ceiling for this vendor: $3-6M, subject to the scorecard.
- Reasons: the same budget line as other expert hours. "Quality control of long-horizon runs" is not a separate budget.

### Persona A. Senior finance or accounting practitioner asked to join the bench part-time

- Profile: 15 years' experience, qualified accountant, controller or planning director level.
- Incentives: side income, flexible hours. Constraints: employer's outside-activity policy; 5-8 hours a week available.
- Alternatives: the large marketplaces, which list finance work from $50 to $150 an hour and average $95-110 [sources in section 0].
- Decision: **joins, non-exclusively, at $110 an hour or more with at least five hours a week guaranteed for eight weeks.** At $85-100 only retired or between-jobs practitioners join.
- Consequences:
  - At a $145-150 bill rate and 60-65% payout the founder pays $87-98, the market average, not a senior rate. Paying $120-140 to get truly senior people needs a $185-215 bill rate, above the lab's rate card.
  - The same person stays on rival platforms and moves hours to whoever pays more that week.
  - Reading four-hour agent transcripts is tiring; this persona's accuracy drops after about two hours in a sitting [domain knowledge, unverified].

### Persona B. Head of evaluations at Lab A (decides in-house, models or vendors)

- Decision: **splits the work three ways and gives the new vendor a calibration trial, not a programme.**
  - Rubric design and gold sets: in-house, with 10-30 directly contracted experts, to keep training priorities confidential [notes].
  - Volume grading: model judges, calibrated against the gold sets [sources in section 0].
  - Vendors: surge capacity, second opinions, and domains with no in-house experts.
- Volume available to vendors: per domain, 300-1,000 gold or adjudication runs a quarter, 2-4 expert hours each, two reviewers, so 1,200-8,000 hours a quarter. At $145 that is $0.7-4.6M a year per domain for all vendors together [domain knowledge, unverified; panel estimate].
- Trial: 200 runs scored against the lab's gold labels. Standing work only if agreement with gold beats incumbents by five points or more.
- View of the trend: human hours per evaluated run fall as judges improve; the number and length of runs rise. This persona expects total vendor review hours to keep growing through 2027 and will not forecast beyond that.
- Does not want the vendor's calibration system. Wants reviewers in the lab's tool.

### Persona C. Vendor manager at Lab A who already runs three expert-hour suppliers

- Incentives: fewer vendors to run, but a hedge against one supplier failing. The March 2026 breach is the reason a fourth slot exists at all [notes].
- Decision: **adds a fourth vendor only through a bake-off, at or below the current blended rate.**
- Terms: $135-150 for finance experts; published rate card; net 60; 30-day termination; weekly scorecard; right to contract the reviewers directly after six months.
- Allocation: 10-15% of the domain's volume at first; up to 30% after two top-ranked quarters.
- Reasons a new vendor gets in: a domain gap, a named researcher asking for it, or a concentration hedge. A better measurement system is not one of them.
- What ends it: one missed week of throughput, one confidentiality lapse, or a theme change. A large programme at the leading marketplace ended with 5,000+ contractors and a lower-paid successor [notes].

---

## 2. Round-one objections: status after the redesign

| # | Round-one objection | Status | Why |
|---|---|---|---|
| 1 | Incumbents already do this with far more money and approved-vendor status | **Unresolved** | The capital gap matters less because nothing is bought for stock. The competition is worse: v2 moves into the core business of marketplaces with $1-3bn run-rates each [notes], which already sell expert evaluation [source: mercor.com/enterprise-evals] |
| 2 | The seller lacks title to its clients' information | **Resolved** | No data in the lead product; corpus work limited to clean title. The cost is volume: that segment is the one brokers and labs already bid in |
| 3 | No buyer signs a quarterly licence; revenue is one-off | **Partly resolved** | Weekly expert hours match how labs buy and all three buyers place orders. Orders are terminable on 30 days and end when the theme rotates |
| 4 | Owners want fixed cash, creating inventory risk | **Resolved** | Buying only against a signed first order removes the risk. It also means losing to 48-hour cash offers, so expect 0-2 corpus sales in year one |
| 5 | Labs supply themselves | **Unresolved, in a new form** | In-house review platforms and direct contractors [notes], plus model judges handling volume [sources in section 0] |
| Also | Start-up indemnity is weak | Mostly resolved | Services carry less provenance liability. Confidentiality of unreleased model output and contractor classification replace it |
| Also | Opt-in capture, EU supply | Resolved | Dropped from the product |

---

## 3. New objections

1. **No differentiation a lab pays for.** The same practitioners work for several marketplaces at once (Persona A). Labs measure agreement in their own tools (Personas B and C). Incumbents already offer expert rubrics and per-task evaluation with 200,000+ trained authors [source: mercor.com/enterprise-evals].
2. **Price squeeze.** The lab rate card is about $135-150 [panel arithmetic from sources in section 0 and notes]. Senior practitioners want $110-140. The 60-65% payout and the lab's price cannot both hold for truly senior reviewers.
3. **Review by humans is a sample, not the volume.** Model judges gate most runs; experts calibrate and spot-check [sources in section 0]. A domain programme for all vendors is $0.7-4.6M a year at one lab (Persona B), not $10-20M for one new vendor.
4. **Conversion and poaching.** The vendor manager wants the right to contract reviewers directly after six months, and the lab's in-house platform exists to remove vendor margin [notes].
5. **Billing unit.** Lab B and the finance lead push price per accepted review. Hourly billing is the founder's whole model.
6. **Concentration.** With two or three labs on 30-day terms, one pause removes 40-50% of revenue within a week, as the founder notes. The bench then idles and leaves.

---

## 4. Numbers in the brief the panel disputes

| Brief | Panel's corrected value | Basis |
|---|---|---|
| $140-220 per expert hour, described as the round-one panels' range | This panel's round-one range was $120-180. For standing lab programmes: $135-150. For smaller buyers: $160-190. Per-run pricing of $350-600 at Lab B | Section 0; Personas C, 2, 3 |
| Gross margin 30-35% | 22-30% for a sub-scale entrant, after second-reviewer overlap the lab will not pay for, review leads and onboarding. The largest marketplace reached 33% only at about $3bn [notes] | Panel |
| 250-350 part-time experts deliver 220,000 hours | That is 12-17 hours a week each, every week. Practitioners offer 5-8. Needs 550-850 active reviewers and a bench of 1,000-1,500 | Persona A |
| Two or three labs at $10-20M a year each | Year one $0.4-1.45M per lab; year two $1.0-5.6M per lab | Personas 1, 2, B, C |
| Corpus sales $0.5-1.5M each | 0-2 sales in year one, $0-1.5M in total | Round-one evidence on cash offers |
| $5-10M covers $40M of annual billing | Agreed. About 40-45 days of expert cost on $3.3M a month is roughly $3-5M | Panel arithmetic |
| "Weekly billed hours ramp faster than one-off corpus sales" | Agreed in direction. Speed is set by vendor allocation rules (10-15% at first), not by sales effort | Persona C |

---

## 5. Orders this panel's buyers would place

| Buyer | Decision | Year one | Year two | Price |
|---|---|---|---|---|
| Lab A (personas 1, 4, 5, B, C) | Trial, then standing weekly orders | 5,500-10,000 hours; $0.8-1.45M | 20,000-40,000 hours; $2.8-5.6M | $140-150 an hour |
| Lab B (persona 2) | Pilot, then per-run orders | 1,000-1,800 runs; $0.4-0.8M | $1.0-2.5M | $350-600 a reviewed run |
| Smaller model company (persona 3) | Purchase order | 800-2,000 hours; $0.13-0.38M | $0.3-0.6M | $160-190 an hour |
| Corpus sales, all buyers | Opportunistic | $0-0.3M | $0-1.0M | One-off |
| **Total** | | **$1.3-2.9M** | **$4.1-9.7M** | |

Reaching $40M needs roughly 15 times this panel's year-one orders. There are not 15 times as many labs. The route is one lab making the company its primary vendor for a domain at $10-20M a year, which no persona here offers a new entrant in the first year.

---

## 6. Panel's four numbers for v2

| Measure | Round one (v1) | Round two (v2) | Reasoning |
|---|---|---|---|
| Probability of a first paid commercial delivery within 9 months | 55-60% | 75-80% | A paid trial of expert hours needs no data owner; three of three buyers place a first order |
| Probability of $40M gross recognized revenue in a trailing twelve months by month 18 | 3-4% | 5-6% | The model now matches the verified fastest ramp in the notes, and more than a dozen entrants reportedly pass $10M [notes]. The panel's own buyers order $1.3-2.9M in year one |
| Probability of $100M by month 36 | 4-5% | 5% | More time helps; in-house platforms and model judges cap a late entrant's share |
| Year five if it works | Gross margin 30-40%; $0.3-1.0bn | Gross margin 25-33%; $0.2-0.6bn | Resold labour at $150-300M gross is $40-90M net. The panel does not expect today's multiples of about 10 times run-rate [notes] to hold for a vendor with 30-day orders |

Revenue type: repeat weekly orders on purchase orders terminable at 30 days. Not contracted. Not recurring in the subscription sense.

Is v2 plainly unworkable? No. It is a real, ordered service and a more honest design than v1. It is also an undifferentiated entry into the most crowded part of this market at a price set by the incumbents.
