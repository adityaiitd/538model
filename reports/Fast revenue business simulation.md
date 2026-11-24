# Fast revenue business simulation

24 November 2026. Second study. The first is [Hundred billion company simulation](<Hundred billion company simulation.md>).

## Verdict

No business I tested gives you better than about a one-in-four chance of $40M of gross revenue by month 18, and that figure applies only on the loosest reading of the target.

I screened 27 ideas and took seven businesses through 17 independent panel sessions in nine versions. On trailing-twelve-month revenue the best odds were 8%. On an annualized basis (latest quarter times four) the best were 20-27%.

Two businesses came closest, in different ways.

- Buying a freight forwarder with a customs brokerage hits the number most often: 20-27% annualized, with a central path of $26M trailing at month 18 and $85M at month 36. The panels expect it to destroy value. You would be buying pass-through freight revenue at a rate peak, and equity at month 36 is put at about half the cash invested.
- Expert review of long agent runs for AI labs hits it less often: about 15% annualized, with a central path of $14-18M trailing at month 18 and $45-55M in year three. It needs $7-14M in total, has an 80% chance of a first paid delivery inside nine months, and in its 15% high case reaches $45M trailing at month 18 and over $120M in year three.

My pick is the expert review business. It scored 45 out of 100 against 39 for the forwarder. I would commit to it in stages: $1.5-2M and six months to a gate, not $10M up front. It is a three-to-five-year business, not a twenty-year one.

## The bar, and three assumptions

I treated $40M within 12-18 months and $100M within 36 months as the hard test, and $100bn as a scored aspiration only. I counted recognized top-line revenue, showed gross profit beside it, and screened out pure pass-through trading under about 10% gross margin. I counted bought revenue and tagged each candidate as organic or acquisition-led.

Your wording does not say whether $40M means a trailing year or an annual rate. I report both. The difference matters most for acquisitions: bought revenue only counts after closing, so a purchase that closes in month 9 gives nine months of trailing revenue at month 18 and a full annual rate.

## How the work was done, and its limits

Three research agents covered what the first study had not: who has actually hit this ramp on small capital, recovery businesses paid on results, and asset-backed plays around AI sites. Their notes are in [research_notes](<../research_notes/Fast revenue business simulation/>). The first study's notes carried over.

Seventeen panel sessions followed, each a separate agent playing eight to thirteen stakeholders with instructions to pursue their own interests. Redesigns went back to the same panels. New candidates and the last redesign faced fresh ones.

The limits are the same as before. Everything the panels said is simulated: no real interviews, orders or deposits. The panels run on the same model I do, so their probabilities are opinions and the sourced facts are the useful part. The method leans toward rejection. Web search ran out in every stream, and many prices and multiples are labelled unverified in the transcripts.

## What the research found

One model has hit this ramp repeatedly on small capital: supplying AI labs with expert data, environments and review.

| Company | Ramp | Capital before the ramp | Source |
|---|---|---|---|
| AfterQuery | $100M run-rate 14-15 months after founding, about 30 staff | Seed money, then a $30M round announced at the $100M mark | [Decrypt](https://decrypt.co/377231/afterquery-ai-tradining-data-unicorn-y-combinator) |
| micro1 | $7M to over $100M of annual rate during 2025 | $6.6M until September 2025 | [Sacra](https://sacra.com/c/micro1/) |
| Fleet | About $1M to $60M annualized in roughly six months | $15M seed | [Sacra](https://sacra.com/c/fleet) |
| Mercor | $614M gross in the first half of 2026, 33% gross margin | About $34M before $40M (derived) | [Sacra](https://sacra.com/c/mercor/) |

These are run-rates and estimates, not audited revenue. Total supplier revenue to labs is about $7-9bn gross in 2026 by the research agent's sum, to be read as an order of magnitude. The category is also fragile: about 91% of Mercor's revenue comes from foundation-model companies, and Meta paused all work with it after a breach in March 2026 ([TechRepublic](https://www.techrepublic.com/article/news-meta-pauses-work-with-mercor-after-data-breach/)).

Two other models hit the ramp on small capital. Neither fits you. Self-serve AI applications need product virality and stall when the model owner ships the same thing. Thin consumer or trading front-ends on rented infrastructure depend on regulatory tolerance or speculative volume.

The research found no roll-up, leasing or energy business that hit the ramp on under $20M of equity.

## The screen

Twenty-seven hypotheses, five taken to simulation, one carried over as a benchmark. The full list with reasons is in [hypotheses.md](<../research_notes/Fast revenue business simulation/sim/hypotheses.md>). Two more candidates entered after round one, both built from what the panels said.

## Simulation results

Probabilities are the panels' estimates. "Central" is their base-case revenue.

| Business and version | Entry | First paid delivery in 9 months | $40M trailing by month 18 | $40M annualized at month 18 | $100M trailing by month 36 | Central trailing revenue at month 18 | Outcome |
|---|---|---|---|---|---|---|---|
| F1 v1 Real-work data for AI labs | Organic | 55-70% | 3-5% | | 4-7% | $15M | Redesigned |
| F1 v2 Expert review of agent runs, individual experts | Organic | 75-80% | 5-7% | About 15% | 5-9% | $18M | Pick |
| F1 v3 Expert review, firm-employed teams | Organic | 82% | 4% | 8% | 5% | $10.9M | Worse than v2 |
| F2 Trucked gas as bridge fuel | Organic | 12-20% | 2-4% | | 4-6% | $11M on the success path | Rejected |
| F3 Customs duty recovery | Organic | 55-60% | Under 1% | | Under 1% | $2.2M | Rejected |
| F4 Hospital payment recovery | Acquisition | 40-50% | 2-4% | 6% | 3-6% | $12.7M | Rejected |
| F5 Physical-work data for robotics | Organic | 70-75% | 4-6% | | 4-5% | $13.5M | Rejected |
| F6 Medical billing companies | Acquisition | 20-42% | 2-3% | | 4-5% | $17.6M | Rejected |
| F7 Freight forwarder with customs brokerage | Acquisition | 33-40% | 6-8% | 20-27% | 6-9% | $26M | Closest on revenue. Rejected on value |
| Benchmark: onsite power by buying a fleet (first study) | Acquisition | 12% | Not asked | Not asked | Not asked | Model: $40M in year one if a purchase closes, which panels put at 15-18% | Not re-run |

The annualized figure for F1 v2 is my reading of the delivery panel's cases: only its high case, at 15%, has a sixth quarter above $10M.

The facts that broke each brief:

| Business | Fact | Source |
|---|---|---|
| F1 v1 | Larger suppliers already buy enterprise data with far more money. One committed $1bn. Labs buy one corpus at a time and also bid directly. | [Let's Data Science](https://letsdatascience.com/news/micro1-commits-1b-to-buy-and-license-enterprise-data-9181fe83), [Dealroom](https://dealroom.co/news/170312-ai-data-brokers-are-buying-slack-email-and-crm-from-live-us-companies/) |
| F1 v2 and v3 | The largest marketplace already sells expert evaluation of agents. One supplier describes model judges passing about 90% of work with a 20% human spot-check. A vendor with employed teams already wins $20-29M programs. | [Mercor](https://www.mercor.com/enterprise-evals/), [Turing](https://www.turing.com/case-study/delivering-agent-trajectories-to-train-and-align-a-frontier-ai-assistant), [Innodata results](https://finviz.com/news/417736/innodata-reports-record-third-quarter-2026-results) |
| F2 | A contract never repays the equipment. The leader booked $128.9M of revenue and $36.5M of EBITDA in a quarter on 919 trailers, and its record trailer order runs through 2028. | [Superior Plus Q3 2026](https://quartr.com/events/superior-plus-corp-spb-q3-2026_ofx60syO), [Hexagon](https://live.euronext.com/en/products/equities/company-news/2026-07-03-hexagon-agility-receives-significant-order-certarus) |
| F3 | Section 232 duty moved to full customs value on 6 April 2026, closing one of three pools. The last official drawback figure is about $1bn a year. | [Foley](https://www.foley.com/insights/publications/2026/05/what-every-multinational-should-know-about-the-new-rules-for-section-232-tariffs-on-steel-aluminum-and-copper-derivatives/), [GAO](https://www.gao.gov/products/gao-20-182) |
| F4 | Clean books cost 8-12 times EBITDA, about 2.5-3.3 times revenue. A newcomer starts as second or third vendor. | Panel estimates. [Aspirion case study](https://www.aspirion.com/180-more-revenue-same-claims-more-recoveries-with-our-secondary-zero-balance-review/) |
| F5 | Buyers collect in-house, and a gig collector delivered a million hours in a month on $16M of funding. | [Figure](https://figure.ai/news/introducing-index), [Fortune](https://fortune.com/2026/11/10/exclusive-in-the-race-for-robot-training-data-ex-meta-researchers-startup-turns-to-gig-workers-with-cameras/) |
| F6 | Billing firms sell at 6-11 times EBITDA, not one times revenue, and a first-time buyer needs 7-11 months to close. | [Broker guide](https://www.ctacquisitions.com/how-to-sell-a-medical-billing-company/), indicative only |
| F7 | Freight rates were at more than twice the level of a year earlier. Median first closing is month 9-13. | Search summaries of a weekly rate index, not opened in full |

### Transcript extracts

Each line is one simulated persona's decision. Full transcripts are in the [sim folder](<../research_notes/Fast revenue business simulation/sim/>).

| Business | Buyer or seller | Delivery | Capital or competitor |
|---|---|---|---|
| F1 v1 | Lab head of human data: pilot at $300-500K, no quarterly licence. | Bank general counsel refuses to certify de-identified screen video. | Largest marketplace already pays data owners cash in two to four weeks. |
| F1 v2 | Lab head: trial, then weekly orders of $0.8-1.45M in year one at $140-150 an hour. | Operations head accepts the job and refuses the $40M date. | Investor offers $4M at $16M pre-money, half released on a $250,000 lab order. |
| F1 v3 | Lab evaluation director: $250,000 trial at $420 a review, then $3.1-5.7M a year. | Accounting firm partner supplies staff off-season only and refuses acceptance risk. | Marketplace copies the offer above $5M of revenue. |
| F2 | Neocloud counters at $10-10.50 over commodity for 12 months, with trailers and a hub in place 60 days early. | Trailer maker: about $0.62M a unit, 20-25 of 50 within 12 months. | Equipment lender offers 40% of hard cost, not 60%. |
| F3 | Controller of a $300M importer signs at 15%. A $15bn manufacturer refuses. | Licensed drawback broker: she is the scarce input and would sell her book at 1.5-2 times fees. | Treasurer signs the incumbent at 12% and gives the founder a second pass. |
| F4 | Owner of a $12M firm wants $36-40M, 80% in cash. | Operator: AI lifts recovered dollars 10-20%, not three times. | Rival roll-up outbids at 9-12 times in cash. |
| F5 | Robot-model company: pilots at $18 an hour for video, $135 for teleoperation. | Operations head: 25,000 hours a month by month nine, not 100,000. | Incumbents subcontract at $8-20 an hour. |
| F6 | Owner of an $18M firm sells at $21M with at least $18M in cash. | Records vendor bans agent logins and poaches 2-4% of the book a year. | AI roll-up pays 8-11 times EBITDA in cash and closes in 60-75 days. |
| F7 | Owner of a $45M forwarder sells at $15M, $12.75M in cash, and stays 12-24 months. | Operator: cost saving is 3-6% at month 18, not 20-25%. | Growth investor refuses common equity: "no value created". |

### Decision ledger

The full ledger is in [decision_ledger.md](<../research_notes/Fast revenue business simulation/sim/decision_ledger.md>). The path of the pick:

| Version | Main objections | Change made | New risk created | Meets the bar? |
|---|---|---|---|---|
| v1 Licensed real-work data | Rivals with $1bn already buy data. Labs buy per corpus. Sellers lack title. Margin 5% with one buyer. | Lead with expert review ordered weekly. Buy data only against a first order. | Enters the most crowded segment | No. 3-5% |
| v2 Expert review, individual experts | No differentiation. Rate card $135-150 against pay of $110-140. Reviewer count three times the brief. | Supply from firms with employed staff in secured rooms. Price per accepted review. Add agent companies as buyers. | Seasonal supply. 12-week supplier minimums against 30-day customer exits. | No. 5-7% trailing, about 15% annualized |
| v3 Firm-employed teams | Firms deliver 26-30 weeks a year. Security removes a veto and earns nothing more. Margin 15-22%. | Reverted to v2, keeping price per accepted review | | No. 4% trailing, 8% annualized |

## What the second study found

1. Organic revenue in the best category reaches $11-18M of trailing revenue at month 18 in the panels' base cases. $40M was a 15% case.
2. Bought revenue fails on timing before it fails on price. A first-time buyer closes a first purchase in 7-13 months, so less than a full year of revenue lands inside month 18.
3. Revenue that is cheap enough to buy on your capital is cheap for a reason. Forwarding revenue at $0.25-0.50 per dollar is mostly freight passed through to carriers. Revenue with real margin (recovery firms, gas haulers, offshore-enabled billers) costs two to three times its own size.
4. The first study's lessons held. The scarce input has an owner: the licensed broker, the trailer fleet, the approved-vendor slot. Buyers give sole supply only to a record. AI is not an edge where every competitor has the same tools.
5. The largest clients take automation savings as fee cuts within a year.

## Scores

Your original weights, with "path to $100bn" read as ceiling.

| Business, best version | Demand /20 | Moat /20 | Ceiling /20 | Early success /15 | Capital efficiency /10 | Standard unit /10 | Founder fit /5 | Total |
|---|---|---|---|---|---|---|---|---|
| F1 v2 Expert review for AI labs | 13 | 3 | 6 | 7 | 8 | 6 | 2 | 45 |
| F7 Freight forwarder bought | 12 | 5 | 2 | 7 | 3 | 7 | 3 | 39 |
| Benchmark: onsite power, bought fleet | 15 | 3 | 3 | 3 | 3 | 8 | 3 | 38 |
| F4 Hospital recovery bought | 10 | 3 | 4 | 3 | 2 | 6 | 3 | 31 |
| F5 Physical-work data | 8 | 2 | 4 | 5 | 5 | 6 | 1 | 31 |
| F6 Billing companies bought | 10 | 3 | 3 | 2 | 2 | 6 | 3 | 29 |
| F2 Trucked gas | 7 | 3 | 3 | 2 | 2 | 8 | 3 | 28 |
| F3 Customs duty recovery | 6 | 4 | 2 | 1 | 6 | 6 | 3 | 28 |

## Why the expert review business and not the forwarder

The forwarder gets nearer your numbers. Its central path is $26M trailing at month 18 and $85M at month 36. I still reject it for three reasons from its own panels. The revenue is bought at a freight-rate peak, and a 30% fall in rates cuts gross revenue by about a fifth. Carriers and the surety want your personal guarantee on a change of owner. And the delivery panel puts equity at month 36 at $11.5M against $23.5M invested. The adviser who proposed the industry said it "satisfies a revenue target, not a wealth target".

The review business misses your numbers in its base case and keeps three things the forwarder lacks. It risks $7-8M at its worst point, not $24-36M. You know which case you are in by month six. And its high case clears your bar with a company the panels value at $250-700M.

## Growth stages and shocks for the pick

The model is [expert_review_model.py](<model/expert_review_model.py>) and its output is [expert_review_output.md](<model/expert_review_output.md>). The base case is the midpoint of two panels' base cases. Years four to ten are my own extension and are the least reliable part.

| Stage | Accepted reviews a year at $420 | Billed hours at $145 | Reviewers active each week | Buyers | Gross margin | Operating margin | Working capital | Staff | Binding supply constraint | Customer concentration |
|---|---|---|---|---|---|---|---|---|---|---|
| First customer | 600 | 1,700 | 7 | One paid trial | 20% | Negative | Nil | 8 | A lab's security review, 6-10 weeks | 100% |
| $10M | 24,000 | 69,000 | 265 | Two labs, three smaller | 24% | Negative | $1.9M | 14 | Senior finance reviewers who pass calibration | Largest over 50% |
| $40M | 95,000 | 276,000 | 1,060 | Three labs, six to nine smaller | 27% | 5-8% | $7.6M | 33 | Top-ranked status at one lab | Largest 40-50% |
| $100M | 238,000 | 690,000 | 2,650 | Four or five labs, fifteen smaller | 30% | 13-17% | $19M | 70 | Review budget across all domains. Needs task authoring as well | Largest about 35% |
| $1bn | | | | | | | | | Exceeds the review budget the panels see. Not reachable as this product | |

Capital spending is negligible. Funding is $7-14M in total: $7-9M of equity and a receivables line of $2-10M after two quarters. The panels' investor offered $4M at $16M pre-money, half released on a first lab order, which leaves you about 45% after the next round in the base case. Return on capital is high if it works, because the business consumes working capital and nothing else. At $10bn and $100bn of revenue there is no configuration of this business.

Scale makes it larger and gives it approved-vendor status, reviewer performance history and rubrics. None of those blocks a rival, and the reviewed runs belong to the lab.

Stress tests on base-case year three ($45M of revenue, $3.6M of EBITDA):

| Shock | Result |
|---|---|
| AI becomes 100 times cheaper | More agent runs to check, and cheaper model judges to check them. The panels expect judges to take 65-80% of review volume within 18 months. At 70%, revenue is $13.5M and EBITDA is negative $5.2M. |
| Model providers enter the adjacent market | They are the customers and already review in-house. The risk is a lab taking a domain fully inside, which is the largest-customer case below. |
| Price falls 50% | Even if reviewer pay falls 30%, gross profit is zero. |
| Two-year capital markets downturn | Little direct effect, since the business needs under $10M. The indirect effect is labs cutting data budgets. |
| Supplier (reviewer) pay rises 30% | Gross margin falls to 6%. EBITDA is negative $6.1M. |
| Largest customer lost | Revenue $24.8M, EBITDA negative $2.1M. Orders end on 30 days' notice, so this can happen in a month. |
| An incumbent replicates the product | Already true. The base case assumes a fourth-vendor share of 10-30% of a domain. |
| Market growth halves | Revenue $22.5M, EBITDA negative $2.7M. |
| Regulatory delay | Not a factor. No licence is needed. |
| A major delivery fails | A failed bake-off or a security incident ends the relationship. One supplier lost its largest customer overnight in 2026. |

## The 18 items, for the pick

### 1. The business in one sentence

We pay experienced accountants, bankers and insurance people by the hour to check the long jobs that AI agents do, and sell those checks to the companies building the AI.

### 2. The exact first product

An accepted review of one multi-hour agent run in corporate finance or accounting. The reviewer finds the step where the run went wrong, grades it against the lab's rubric and the real outcome, and writes the correction. Delivered inside the lab's own tooling within 72 hours. The first sale is a paid trial of about 600 reviews or 1,000 hours.

### 3. Who buys, why, and what they pay

Heads of human data and evaluation at AI labs buy it because agents now run for hours and nobody can tell at scale where they fail. In the simulation they paid $135-150 an hour or $400-450 a review. A trial was $250,000-500,000. A standing program was $3-6M a year, and primary status in a domain was $7-11M after two top-ranked quarters. Companies building finance agents and software vendors shipping agents bought $0.2-0.9M a year each. A bank and an insurer refused.

### 4. Why now and not five years ago

Five years ago there were no multi-hour agent runs to review. Lab revenue and data budgets are now large enough to pay for it, and buyers report that quality control for long tasks is short while expert headcount is not ([Epoch](https://epoch.ai/gradient-updates/state-of-rl-envs), [Sean Cai](https://seanzcai.substack.com/p/an-ai-bubble-is-a-human-data-problem)).

### 5. The existing revenue pool

Suppliers to labs run at about $7-9bn gross in 2026. Review is a small slice of that. The fresh panel put it at $4-12M per lab per domain, and at $20-60M in total outside the labs. That is a few hundred million dollars a year across all buyers and domains. $100M therefore needs either a large share or a move into authoring tasks as well as reviewing them.

### 6. Unit economics

| Item | Per review | Per hour |
|---|---|---|
| Price | $420 | $145 |
| Reviewer pay | About $315 for three hours | $105-115 |
| Gross margin | 25% | 22-28% in year one, 27-32% later |

Fixed costs are $3.5M in year one for a team of about ten, the quality system and security. Working capital is $1.9M per $10M of billing, because reviewers are paid weekly and labs pay in 45-80 days. The base case turns EBITDA-positive in year two at about $27M of revenue.

### 7. Technology and intellectual property

A calibration and quality system that measures agreement between reviewers, fraud detection, a secure work environment, and a library of rubrics. A panel engineer judged all of it copyable in six to nine months. There is no protectable intellectual property.

### 8. Competitors

Mercor, micro1, Surge, Turing, Handshake, AfterQuery and Innodata, each with $100M to $3bn of run-rate, and the labs' own teams and model judges. The company does not beat them. It can win a fourth-vendor share of one domain by ranking first in a lab's bake-off, which the vendor manager persona put at 10-15% of the domain rising to 30%.

### 9. Main objections and how the business evolved

See the ledger table above. The business moved from licensing enterprise data to selling review hours, tried firm-employed teams, and went back to individual experts with price per accepted review.

### 10. First ten target customers and five suppliers or partners

These are targets, not relationships, and none has been contacted. The reasons for OpenAI, Anthropic, Google, Meta, Nvidia and Thinking Machines Lab come from the research. The other four are from my own knowledge of who runs large agent programs.

| Target | Why |
|---|---|
| OpenAI | Has paid former bankers to build finance tasks since 2025, so finance is a funded domain |
| Anthropic | Reported data and evaluation vendor costs rose sharply in 2026 (weak source) |
| Google | Bid directly for a bankrupt airline's archive, so it buys real-work data |
| Meta | Paused its largest expert supplier after a breach and needs alternatives |
| Microsoft AI | Large in-house agent programs. Likely buys through an approved prime vendor |
| Amazon | Same route as Microsoft |
| xAI | Large-scale buyer of tutoring and review labor |
| Nvidia | Named customer of a 2025-founded data supplier |
| Thinking Machines Lab | Named customer of the same supplier |
| Intuit | Ships agents inside accounting software |

| Supplier or partner | Role |
|---|---|
| An approved prime vendor with employed teams | Subcontract route into large technology companies at 80-85% of price |
| A contractor payment provider | Weekly pay to several hundred reviewers |
| A SOC 2 auditor | Type II report, which procurement personas required |
| A receivables lender | $2-3M after one quarter, rising to $8-10M at 9-11% |
| Alumni networks of accounting and banking professionals | Reviewer supply. Panels put the needed bench at 1,400-1,800 vetted for $40M |

### 11. First five hires

1. Head of operations who has run an expert-data business past $50M.
2. Head of quality with an audit or controllership background, to own rubrics and calibration.
3. Security lead, to pass lab vendor reviews.
4. A technical lead who has worked on evaluations inside a lab. The panels' investor made a lab research sponsor a condition.
5. Head of reviewer recruiting and fraud control.

### 12. First 90 days

| Week | Work |
|---|---|
| 1 | Write kill criteria. Incorporate. Start SOC 2 readiness. Recruit the operations head and the quality head. |
| 2 | Build the first rubric set on a public finance benchmark. Start recruiting reviewers at $105 an hour. |
| 3 | Fifteen outreach conversations with human-data and evaluation leads. Open talks with two prime vendors about subcontracting. |
| 4 | Calibration run with the first 60 reviewers. Publish agreement and acceptance numbers. |
| 5-6 | Offer free 50-review calibration samples to three buyers. Answer the first vendor security questionnaire. |
| 7-8 | Convert samples into paid trials. Sign one subcontract. |
| 9-10 | Deliver the first trial. Measure acceptance rate, cost per accepted review and reviewer hours per week. |
| 11-12 | Negotiate a standing weekly program with the first buyer. Start a second domain only if the first buyer asks. |
| 13 | Day-90 review against the gate in item 18. |

### 13. Capital before the first commercial delivery

$0.8-1.5M: the first hires, security work that panels put at $0.5-0.9M in year one, and reviewer pay ahead of the first invoice. Peak cash need is about $7M in the base case and $8M in the downside.

### 14. Financial projections

Dollar figures in millions. Company value uses the panels' normal-market range for the base case and their current-market range for the upside.

| Case | Probability | Trailing at month 18 | Annualized at month 18 | Year 1 | Year 2 | Year 3 | Year 5 | Year 10 | EBITDA year 3 | Peak cash need | Company value year 5 | Founder value year 5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Downside | 35% | 4.0 | 6 | 1.4 | 5.0 | 7.5 | 4.0 | 0 | -1.2 | 8.0 | 0 | 0 |
| Base | 50% | 14.3 | 24 | 4.4 | 27 | 45 | 75 | 90 | 3.6 | 7.1 | 75 | 34 |
| Upside | 15% | 45.0 | 68 | 15.8 | 71 | 122 | 230 | 320 | 18.6 | 5.3 | 575 | 218 |
| Probability-weighted | | 15.3 | 24 | | | | | | | | | |

The base case reaches $40M of annual revenue in year three and does not reach $100M. Only the upside case meets both of your targets.

### 15. Expansion path

Authoring tasks and environments as well as reviewing them, which is how a lab's spend with a primary vendor reaches $10-20M. More professions: insurance, tax, legal operations. Testing agents for enterprises before deployment, which the bank and insurer personas put no earlier than 2028. The panels' ceiling is $120-300M of gross revenue and $200-700M of equity value in year five. There is no path to $100bn.

### 16. The three assumptions most likely to destroy the business

1. That one lab ranks the company first in a domain within two quarters. Without that it stays a trial vendor at $1-3M.
2. That human review of long runs remains a paid line while model judges improve.
3. That the spread between the lab's rate card ($135-150) and what senior reviewers accept ($105-140) stays above 25%.

### 17. Experiments that can settle these in 30 days

Budget about $200,000.

| Test | What to do | Pass | Fail |
|---|---|---|---|
| A. Will a lab pay? | Fifteen conversations with evaluation and human-data leads, each offered a paid trial. | Two signed trials of $100,000 or more | Interest without a purchase order |
| B. Can you supply quality at the price? | Recruit 60 senior finance reviewers at $105 an hour or less and run them on a public benchmark. | Agreement between reviewers of 0.8 or better and 90% of reviews accepted by an outside grader | Pay above $120, or acceptance under 80% |
| C. Is there a faster route in? | Ask two approved prime vendors for subcontract terms. | A written offer at 80% of the end price or better | No offer |
| D. Will security pass? | Complete one lab's vendor questionnaire and a SOC 2 gap assessment. | No blocking finding | A requirement that takes over six months |

### 18. Final investment decision

Yes, in stages. I would commit $1.5-2M and six months. I would not commit $10M up front or 20 years.

The gate at month six: two labs paying, and quarterly revenue of $1M or more. The base case shows $1.3M in the third quarter and the downside shows $0.4M, so the gate separates them. If it passes, raise $4-6M and add a receivables line. If it fails, stop, having spent under $2M.

Go in knowing what it is. This is a labor business with a quality system, a 25-30% gross margin, customers who can leave in 30 days, and no moat. It is the only tested design where a small, staged bet has a real chance, about one in seven, of the revenue you asked for.

## What would change this conclusion

1. If you mean an annual rate and care about the number more than the value, the forwarder is the more likely route at 20-27%. I would still not take it at 2026 freight rates. A purchase priced on average 2024-26 earnings, with the seller keeping 20%, is what the co-investor persona asked for.
2. If you can deploy $30-40M of equity on day one with a sponsor who has closed deals, the timing objection to acquisitions weakens: experienced platforms close in three to six months.
3. If a lab offers a research sponsor or a written primary-vendor path before you start, the review business moves from the base case toward the upside. That is the single most valuable thing to ask for in test A.

## Sources

Research notes with a URL on every claim: [precedents_and_lab_data.md](<../research_notes/Fast revenue business simulation/precedents_and_lab_data.md>), [contingency_recovery.md](<../research_notes/Fast revenue business simulation/contingency_recovery.md>), [fuel_equipment_leasing.md](<../research_notes/Fast revenue business simulation/fuel_equipment_leasing.md>), and the first study's six files. Briefs for every version, panel transcripts, the screen and the ledger are in the [sim folder](<../research_notes/Fast revenue business simulation/sim/>).

Company run-rates are press reports and Sacra estimates, not audited revenue. Acquisition multiples come from broker marketing pages and panel estimates and are indicative. The freight-rate figures rest on search summaries the agents could not open in full.
