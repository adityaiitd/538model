# F5 v1, demand and supply-side panel, round 1

Date of simulation: 24 November 2026. Everything below is a simulated hypothesis from archetype personas. None of it is customer validation, and no real person was interviewed.

Evidence labels: [notes] = the founder's research notes; [source: URL] = checked in this session; [search summary: URL] = seen in a search summary, page not opened; [panel arithmetic] = my calculation from labelled inputs; [domain knowledge, unverified].

Web budget used: 3 searches and 3 fetches. One fetch failed (HTTP 429).

---

## 0. Facts the panel worked from

### Prices and costs per hour

| Item | Figure | Label |
|---|---|---|
| Raw first-person video, India, sold to buyers | $1-10 per hour | [search summary: https://www.metaintro.com/blog/india-workers-robot-training-data-2026] |
| Packaged first-person video, India, resale | $15-50 per hour; rates fell about 30% from January to June 2026 | same search summary |
| Indian worker pay for capture | Rs 450-500 per hour (about $5-6) | same search summary |
| US gig pay for capture | $20-50 per hour; $30 per hour in one current listing | [notes]; [search summary: opentrain.ai listing] |
| Automated labeling of robot video | $9 per video-hour; $29 with hand tracking and activity labels | [notes]; [search summary: https://fourweekmba.com/ai-perceptron-puts-robot-video-labels-at-9-an-hour-astra-76/] |
| Small-lot marketplace list price | $90-1,800 per recorded hour, 10-hour minimum; first-person listings at $90-270 | [search summary: https://www.roboticscenter.ai/fr/marketplace] |
| Teleoperation, fully loaded | $118-200 per hour, attributed to one vendor (SVRC, April 2026) through an aggregator | [search summary]; [notes] |

No audited figure for what buyers pay per hour was found. All figures above are vendor list prices, worker pay or aggregator claims.

### Volumes

| Fact | Label |
|---|---|
| Figure's Index app: 264,000 downloads, 108 countries, 44,000 weekly active contributors, 16M videos, $15M paid to contributors, about 30 minutes of video uploaded per second, target of 100x growth in a year | [search summary: https://figure.ai/news/introducing-index and https://alphasignal.ai/news/figure-s-index-app-pays-44-000-people-to-train-its-humanoid-robots] |
| Memories.ai: 1M+ hours in first beta month on $16M raised; target above 10M hours by March 2027; sells to three of the top five labs; price not disclosed; automated blurring and labeling with sampled manual review | [source: https://fortune.com/2026/11/10/exclusive-in-the-race-for-robot-training-data-ex-meta-researchers-startup-turns-to-gig-workers-with-cameras/] |
| Scale: 150,000+ robot hours delivered; 1,000+ demonstration hours a day; 10 robotics customers added in 2025 | [notes] |
| XDOF: $70M raised, about 20 customers, revenue undisclosed | [notes] |
| Generalist AI: 500,000+ hours, up from 270,000 five months earlier, adding 10,000 hours a week | [source: https://jumptask.io/blog/egocentric-data-market-review/] (vendor blog) |
| Dyna: pretrained on 1M+ hours of first-person video; score rose from 20% to 53% between 1,000 and 1,000,000 hours | [notes] |
| JD.com and Suqian: target of 10M hours over two years; eight Chinese cities opened collection centres | [source: jumptask.io, citing Xinhua] |

### Panel arithmetic on those facts

- 30 minutes per second is 1,800 hours per hour, or about 1.3M hours a month and 15.8M hours a year, at one buyer's own app. [panel arithmetic]
- $15M paid for 16M videos is about $0.94 per video. If a video averages 5-10 minutes, the contributor payout is about $6-11 per hour. [panel arithmetic; video length is my assumption]
- Memories.ai cannot have paid more than a few dollars per hour: 1M hours in one month against $16M raised in total. [panel arithmetic]
- Scale at 1,000 hours a day is 365,000 hours a year. At $118-200 per hour that is $43-73M a year. The incumbent may already be at the founder's target. [panel arithmetic; Scale's price is not known]

### Legal ground

- With the sole exception of California, enacted US state data-protection statutes exclude workers and their data. [search summary: https://www.bu.edu/bulawreview/files/2026/06/KIM-LEAVITT.pdf]
- Illinois biometric privacy law requires written release before collecting biometric identifiers, with statutory damages of $1,000 (negligent) or $5,000 (reckless) per person after the 2024 amendment. Hand geometry, face and voice are in scope. [domain knowledge, unverified]
- About a dozen US states require all-party consent to record audio, including California, Illinois, Washington, Pennsylvania and Florida. [domain knowledge, unverified]
- In a unionised US workplace, new recording technology is a mandatory subject of bargaining. In Germany a works council must agree to technical monitoring of employees. [domain knowledge, unverified]
- June 2026 reporting on Indian factories: consent was obtained through management, workers were not told the data would be sold, and footage was reused to rank workers by active time. Workers are resisting. [search summary: https://www.eweek.com/news/factory-workers-cameras-ai-robot-training/; https://truthout.org/articles/indian-workers-are-resisting-efforts-to-train-their-ai-robot-replacements/]

---

## 1. Panel cost model for the founder's product

### First-person video captured in workplaces, per accepted annotated hour

| Cost line | Low | High | Basis |
|---|---|---|---|
| Worker bonus, including staffing markup | $3.6 | $5.6 | Personas 8 and 9 |
| Site fee to the employer | $2.0 | $5.0 | Personas 7 and 8 |
| Rig depreciation and breakage ($800-2,500 rig, 1,500-2,500 hour life) | $1.0 | $1.5 | [domain knowledge, unverified] |
| Field technicians (one per 25 rigs) | $1.5 | $2.0 | [domain knowledge, unverified] |
| Upload, storage, blurring, quality control | $1.0 | $2.0 | [domain knowledge, unverified] |
| Annotation (automated plus sampled human review) | $3.0 | $10.0 | $9-29 list price for automated labels |
| Subtotal per captured hour | $12.1 | $26.1 | |
| Rejected hours (idle, occluded, duplicate) | 25% | 30% | [domain knowledge, unverified] |
| **Cost per accepted hour** | **$16** | **$37** | [panel arithmetic] |

The gig model (worker's own phone or a $150 kit, at home, no site fee, no field technician) delivers raw hours at $1-11. The workplace model costs two to five times more per hour and must sell at a premium to exist.

### Teleoperation on customer robots at leased sites, per delivered hour

| Cost line | Low | High |
|---|---|---|
| Operator, loaded | $30 | $42 |
| Site lease, power, network | $6 | $12 |
| Supervisors, quality control, robot technicians | $10 | $18 |
| Subtotal per staffed hour | $46 | $72 |
| Robot uptime (customer hardware) | 65% | 55% |
| **Cost per delivered hour** | **$71** | **$131** |

[panel arithmetic on domain knowledge, unverified]. At a $135 price the gross margin is between 3% and 47%, and is governed by the uptime of robots the company does not own.

---

## 2. Buyers

### Persona 1. Head of data, humanoid robot company with in-house collection

- **Who:** runs a consumer capture app with tens of thousands of weekly contributors and an internal five-stage curation pipeline.
- **Incentives and constraints:** measured on hours, diversity and cost per useful hour. The board has been told collection is a proprietary asset. Buying from a vendor that also sells to rivals contradicts that story.
- **Alternatives:** own app at about $6-11 per hour of contributor payout; own deployment customers' sites for industrial capture; own robots for teleoperation.
- **Decision:** refuses a program. Signs one paid pilot.
- **Price and terms:** 3,750 hours at $20 per annotated hour ($75,000), in commercial kitchens and laundries only, captured to the company's own camera specification, work-for-hire with full assignment. No teleoperation purchase.
- **Reasons:** the app already produces more than 1M hours a month; the vendor's entire 1,000,000-hour proposal equals about three weeks of internal intake. The company wrote publicly that vendors missed its throughput, diversity and quality bar [notes]. The only gap is places a consumer app cannot enter.
- **What would change it:** proof of 50 or more workplace categories the app cannot reach, at under $15 per hour, exclusive, with a measured gain on the company's own evaluation. Even then the ceiling is about $1-2M a year.

### Persona 2. Head of data, robot foundation-model company, $1bn+ raised, no manufacturing

- **Who:** buys from three or four vendors already (the Scale and XDOF type). Owns some robots and handheld capture devices, owns no factories or homes.
- **Incentives and constraints:** needs robot-action data on its own embodiments first, and human video second as cheap pretraining. Budget is held by research, on quarterly plans. Will not commit beyond two quarters because the data recipe changes every few months.
- **Alternatives:** incumbent teleoperation vendors; in-house operators at $60-120 per loaded hour; gig-video vendors at single-digit dollars per hour.
- **Decision:** signs two paid pilots. If the evaluation shows lift, signs quarterly purchase orders. Does not sign an annual or multi-year contract.
- **Price and terms:**
  - First-person video: 20,000 hours at $18 annotated ($360,000). Program afterwards: about 150,000 hours a year at $14 ($2.1M), non-exclusive.
  - Teleoperation: 4,000 hours in a quarter at $135 ($540,000), on the buyer's robots, buyer's task list, all data assigned to the buyer. Program afterwards: up to 40,000 hours a year ($5.4M).
  - 30-day termination, pay per accepted hour, rejection rights on quality.
- **Reasons:** this is the only persona with both the budget and the habit of buying outside. The founder's $40-150 for video is two to eight times what gig vendors charge. Annotation is not worth a premium because the buyer runs its own labeling models.
- **What would change it:** a larger commitment needs (a) hours per site capped at a few hundred so diversity holds, (b) wrist-level views and calibrated depth, (c) a measured gain per 10,000 hours on its own benchmark. A price of $40 needs tactile or force data, which the brief does not offer.

### Persona 3. Research lead for robotics, large technology company or frontier lab

- **Who:** leads a world-model or robot-model group. Three of the top five labs already buy first-person video from a gig vendor [source: Fortune, 10 Nov 2026].
- **Incentives and constraints:** wants millions of hours of diverse video cheaply; wants raw footage plus calibration and consent records; does annotation internally. Vendor onboarding (security, privacy, legal) takes three to five months.
- **Alternatives:** gig-video vendors; internal employee capture programs [notes]; licensed archives; public video; simulation.
- **Decision:** paid pilot. A program only after the pilot passes privacy review and shows diversity.
- **Price and terms:** 20,000 hours at $15 ($300,000). Program: 300,000 hours a year at $10 ($3M), non-exclusive licence, perpetual, with deletion on consent withdrawal. No teleoperation purchase; the lab runs its own robot rooms.
- **Reasons:** at this buyer the unit is the raw hour with provenance. "Densely annotated at 100 times the value" is an annotation vendor's estimate [notes], and this buyer does not pay for it.
- **What would change it:** workplace categories unavailable from gig vendors, clean consent, and a price at or under $10. Exclusivity is not wanted and not paid for on pretraining video.

### Persona 4. Head of data operations, industrial or warehouse robotics company with deployed fleets

- **Who:** runs hundreds to thousands of picking or mobile robots at customer sites.
- **Incentives and constraints:** already logs every pick, failure and remote-assist intervention from its own fleet at near-zero marginal cost.
- **Alternatives:** own fleet logs; own remote-assist operators.
- **Decision:** refuses both products. $0.
- **Reasons:** human hand video does not map to suction or parallel grippers. Teleoperation on "the customer's own robots" is what this company's remote-assist team already does. It also regards the founder as a competitor for access to its customers' sites.
- **What would change it:** nothing at the program level. At most a $50,000 site survey before a new deployment.

### Persona 5. Procurement and legal lead (buyer side)

- **Who:** owns vendor approval, privacy, ownership and exclusivity terms.
- **Decision:** approves pilots under a master agreement on conditions. Refuses any program until a consent audit passes.
- **Terms required:**
  - Individual written consent from every wearer and every regular co-worker; signage and blurring for bystanders; audio off unless all parties consent.
  - Biometric release for Illinois residents; separate handling for California and the EU.
  - Warranty that no third-party confidential material is in frame (client goods, shipping labels, screens). At a 3PL this is the 3PL's customers' property.
  - Uncapped indemnity for privacy, publicity and labour claims; $10M+ cyber and media liability cover; audit rights over consent records; deletion within 30 days of a withdrawal.
  - Commissioned teleoperation data: assigned outright, exclusive. First-person video: non-exclusive perpetual licence is acceptable at commodity prices. Exclusivity on video is available only if the vendor accepts two to four times the price not being paid.
- **Reasons:** consent obtained through an employer is weak consent. The Indian factory reporting is the precedent every privacy counsel now cites. An uncapped indemnity from a start-up with $5-10M is worth little, so legal limits volume instead.
- **What would change it:** an independent consent audit, insurance in place, and a first lot delivered with no bystander or client-material leakage.
- **Time cost:** three to five months from first meeting to an approved master agreement. [domain knowledge, unverified]

### Persona 6. Finance lead for the data budget

- **Who:** approves price per hour against alternatives.
- **Benchmark table used:**

| Source | Cost per hour |
|---|---|
| Internet video | about $0 plus compute |
| Simulation | cents per hour of compute |
| Own consumer app | $6-11 payout |
| Overseas raw video | $1-10, falling |
| Overseas packaged video | $15-50, down about 30% in H1 2026 |
| Automated annotation | $9-29 list; less in-house |
| In-house teleoperation | $60-120 loaded |
| Vendor teleoperation | $118-200 |

- **Decision:** refuses $40-150 for video. Authorises up to $12 per annotated hour at program scale, $20-25 for hard-to-reach workplaces in lots of 50,000 hours or less, and $110-140 for teleoperation.
- **Budget:** at a $1bn-funded model company, external first-person video is $5-15M a year and external teleoperation $10-30M a year, split across three to five vendors. [domain knowledge, unverified]
- **Reasons:** the price of the standard unit fell 30% in six months. A falling commodity is bought quarterly, not committed annually.
- **What would change it:** evidence that one workplace hour replaces more than three gig hours on the buyer's own benchmark.

---

## 3. Supply side

### Persona 7. Vice president of operations, third-party logistics company, 40 warehouses

- **Who:** runs sites under contracts with brand owners at 3-6% operating margin. [domain knowledge, unverified]
- **Incentives and constraints:** measured on units per labour hour, safety incidents and contract renewals. Most customer contracts prohibit photography and disclosure of volumes, labels and layouts. Several sites are unionised.
- **Alternatives:** do nothing; or give access directly to a robot maker in exchange for early deployment. Large 3PLs already host humanoid pilots [notes].
- **Decision:** refuses company-wide capture. Allows a pilot at 2 of 40 sites.
- **Terms:**
  - Only multi-client sites with no restrictive customer clause, or sites where the customer consents in writing.
  - Site fee of $4 per rig-hour or 12% of data revenue, whichever is higher.
  - The founder pays the worker bonus and any lost productivity above 2%.
  - Full indemnity; rigs certified against snag and heat hazards; no audio; no capture of screens or labels.
  - 3PL keeps the right to licence the same access to robot makers it partners with. No exclusivity.
- **Yield:** 2 sites x 30 volunteers x 1,200 hours is about 72,000 captured hours in year one, about 50,000 accepted. [panel arithmetic]
- **Reasons:** the downside is losing a customer contract worth tens of millions for a site fee worth $200,000-300,000.
- **What would change it:** customer consent site by site (three to six months each), one clean year, and a fee nearer $6 per hour. A realistic year-two ceiling is 8-10 sites.

### Persona 8. Chief operating officer, staffing firm; and commercial kitchen and hospitality operator

**Staffing firm**
- **Decision:** signs a supply agreement, but it does not deliver sites.
- **Terms:** the bonus runs through payroll at the usual 35-45% markup, so a $3 bonus costs $4.20; plus $1 per hour to the firm.
- **Reason:** it likes the bonus as a retention tool. The host employer controls the premises, not the staffing firm, so each client must consent separately.

**Kitchen and hospitality operator (60 kitchens, some hotel laundries)**
- **Decision:** allows a pilot in 3 kitchens. Refuses guest rooms and front of house.
- **Terms:** $3 per rig-hour site fee, $3 per hour worker bonus, food-safe rigs, no audio, 30-day exit.
- **Yield:** 60 kitchens x 8 cooks x 35% opt-in x 1,800 hours is about 300,000 hours a year at full rollout. [panel arithmetic]
- **Reasons:** operator, employer and site owner are the same party, so consent is simpler than in logistics. Heat, steam and grease shorten rig life.
- **What would change it:** nothing blocks the pilot. Expansion depends on zero incidents. The limit is on the demand side: no buyer wants 300,000 hours from one chain's near-identical kitchens.

### Persona 9. Warehouse worker; and union or labour-law representative

**Worker ($18-22 per hour)**
- **Decision:** wears the rig, on conditions.
- **Terms:** at least $4 per hour extra, truly voluntary, no use for discipline or rate-setting, pause control, nothing recorded in break rooms or toilets.
- **Opt-in expected:** 30-50% of a shift. [domain knowledge, unverified]
- **Reason for the rest refusing:** "I am training my replacement, and my manager gets the footage."

**Union or labour-law representative**
- **Decision:** refuses at unionised sites until bargained. Allows a pilot under a side letter.
- **Terms:** written bar on use for discipline, time study or rate-setting; worker right to withdraw and delete; bystander consent; no retaliation for opting out; a per-hour payment set in the agreement; notice and bargaining over any automation the data supports.
- **Time:** 6-12 months to bargain. In Germany a works council agreement is required first.
- **What would change it:** a signed side letter plus an independent audit that the employer never receives identifiable footage.

---

## 4. What the test questions returned

| Question | Panel answer |
|---|---|
| Price today, raw first-person video | $1-11 per hour (overseas or gig). US workplace capture has no observed market price. |
| Price today, annotated first-person video | $10-25 per hour at program scale; $15-50 overseas packaged and falling; $90-270 only for lots of tens of hours. |
| Price today, teleoperation | $110-160 per delivered hour at program scale; $118-200 quoted loaded. |
| Hours bought | Pilots of 4,000-20,000 hours. Programs of 40,000-300,000 hours a year per buyer per vendor. Nobody on the panel bought 1,000,000 hours from one vendor. |
| Do they buy outside at all | Personas 2 and 3 yes. Persona 1 almost no. Persona 4 no. |
| Quality and diversity required | Hours capped per site and task (a few hundred), wrist-level views, calibrated multi-view, consent records, rejection rights. Diversity is counted in distinct environments, not hours. |
| Exclusivity | Teleoperation on the buyer's robots is assigned outright and cannot be resold. First-person video is non-exclusive and resellable, at commodity prices. |
| Do workplaces allow capture, and at what charge | Kitchens yes, at $3 per hour. Logistics at 2 of 40 sites, at $4 per hour or 12% of revenue. Unionised sites only after bargaining. Workers want $3-5 per hour. |
| Buyers and hours for $40M | See below. |

### What $40M requires

| Route | Price | Hours | Operational meaning |
|---|---|---|---|
| Founder's case, video only | $40 | 1,000,000 | No panel buyer accepts the price at this volume. |
| Video only at panel price | $12 | 3,330,000 | About 2,200 worker-years of rig time at 1,500 hours each; more than 100 sites. |
| Teleoperation only | $135 | 296,000 | About 200 operators and 100-150 customer-owned robots; 81% of the incumbent's stated daily throughput. |
| Panel's best mix | $25M teleoperation + $15M video | 185,000 + 1,250,000 | Two buyers at $8-10M each and six to eight at $2-4M. |

Summing the purchase orders the panel would actually sign: pilots of about $1.3M in year one, and programs of about $10.5M a year if every pilot converts (persona 2: $7.5M; persona 3: $3M; persona 1: nil). Reaching $40M needs roughly four clones of persona 2, in a market where the best-funded specialist has about 20 customers in total.

---

## 5. Five most damaging objections

1. **The price of the standard unit is already below the founder's cost.** Program-scale video clears at $8-25 per annotated hour and fell 30% in six months. Workplace capture costs $16-37 per accepted hour. [search summary: metaintro.com; panel arithmetic]
2. **The buyers with the money supply themselves or buy from gig vendors.** One buyer's app takes in about 1.3M hours a month; one gig vendor delivered 1M hours in a month on $16M of total funding. [source: Fortune; search summary: figure.ai]
3. **Site access belongs to employers who have better offers.** A 3PL gives 2 of 40 sites, keeps the right to deal directly with robot makers, and charges a fee. This is lesson 1 of the earlier study: the scarce input belongs to someone else. [domain knowledge, unverified; notes]
4. **Hours from few sites are worth little.** Buyers cap hours per site and task. A million hours needs thousands of environments, which is the consumer model, not the employer model. [domain knowledge, unverified; Dyna and Fortune items support the demand for diversity]
5. **The one product with a firm price, teleoperation, is a staffing business on someone else's robots.** Deliverables are assigned to the buyer, uptime is outside the vendor's control, and the incumbent already runs 1,000 hours a day. [notes; panel arithmetic]

Also raised: consent through an employer does not survive legal review without individual releases; unionised and European sites take 6-12 months.

---

## 6. Numbers in the brief the panel disputes

| Brief | Panel's corrected value | Basis |
|---|---|---|
| Video at $40-150 per annotated hour | $8-25 at program scale; $20-30 for hard-to-reach workplaces in lots under 50,000 hours | Overseas packaged $15-50 and falling; automated labels $9-29; gig vendors' implied costs |
| Teleoperation at $150-250 | $110-160 | Loaded quote of $118-200; buyer's in-house cost of $60-120 |
| Programs of 100,000-1,000,000 hours, ordered quarterly | Pilots of 4,000-20,000 hours; programs of 40,000-300,000 hours a year, cancellable at 30 days | Personas 2, 3, 6 |
| 1,000,000 hours at $40 is $40M | 1,000,000 hours is $10-14M | Persona 6 ceiling |
| One humanoid company committed over $1bn to data and compute | Addressable by an outside vendor: about $0-2M a year | The commitment funds its own app and compute; it had paid contributors $15M in total |
| Annotated data worth 100x raw and 20x the cost | Buyers pay 1.5-3x raw | Buyers label in-house; automated labels cost $9-29 per hour |
| Gross margin 35-45% | 15-30% blended | Panel cost model; the largest human-data vendor reports 33% [notes] |
| No supplier near $40M | True as disclosed. The incumbent's stated throughput implies $43-73M a year | [panel arithmetic] |

---

## 7. Conditions that turn each "no" into a "yes"

- **Persona 1:** exclusive workplace categories its app cannot reach, under $15 per hour, with measured lift. Ceiling $1-2M a year.
- **Persona 2 (annual commitment):** per-site hour caps, wrist and depth views, tactile or force signals, and a measured gain per 10,000 hours on its own benchmark.
- **Persona 3 (program):** a passed privacy review and price at or under $10.
- **Persona 4:** no condition found.
- **Persona 5:** independent consent audit, $10M+ insurance, one clean delivered lot.
- **Persona 6 ($40 per hour):** proof that one workplace hour replaces more than three gig hours.
- **Persona 7 (beyond 2 sites):** written consent from each warehouse customer, one clean year, $6 per hour.
- **Persona 8:** staffing firm needs each host employer's consent; kitchen operator expands after zero incidents.
- **Persona 9:** a bargained side letter and an independent audit of what the employer can see.

---

## 8. Panel estimates for this version

| Estimate | Value |
|---|---|
| Probability of a first paid commercial delivery within 9 months | 70% |
| Probability of $40M gross recognized revenue in a trailing twelve months by month 18 | 4% |
| Probability of $100M by month 36 | 5% |
| Gross margin in year five if it works | 22-30% |
| Equity value in year five if it works | $250-500M, on $150-250M of revenue at 1.5-2.5x |

Revenue type: re-ordered each quarter on short purchase orders. It is not recurring, and it is contracted only for the current quarter.

The pilot is easy to win and the program is not. Pilot budgets sit with researchers and several buyers will pay $75,000-540,000 to test a new source. The step from there to $40M depends on a price premium for workplace footage that no buyer on this panel granted.
