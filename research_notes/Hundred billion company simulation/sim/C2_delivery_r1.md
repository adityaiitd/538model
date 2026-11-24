# C2 delivery panel, round 1: can the AI-infrastructure risk carrier actually be produced?

Simulated on 24 November 2026. Everything below is a simulated hypothesis built from archetypes, not validation. No real person was interviewed and no real quote is used.

Evidence labels: **[source: URL]** = page opened or search result read this session ("snippet" = search summary only, page not opened). **[notes]** = founder's research notes. **[DK]** = domain knowledge, unverified.

Search budget used: 5 searches and 3 fetches (the limit of 8). No pricing data (rate on line, fronting fee schedule, ILS hurdle) was found in any public source; all such figures are [DK].

---

## 0. Facts checked this session that change the brief

| Brief says | Checked fact | Label |
|---|---|---|
| Aon facility $3.5bn | Aon's programme went to **$5bn on 20 July 2026**, third increase in 13 months ($2.5bn, $3.5bn, $5bn). Covers construction, delay-in-startup and operating property/BI. | [source: https://www.insurancebusinessmag.com/us/news/technology/aon-expands-data-center-insurance-program-to-5bn-amid-capacity-crunch-582902.aspx] |
| "Capacity did not grow" | FM offers up to $5bn per client on a new treaty. One Meta tower went from $2bn+ (2025) to up to $8.5bn. Construction programmes "top out at about $3-4bn". | [source: https://www.insuranceinsider.com/sample-content/data-centre-dispatches-how-the-construction-market-is-rising-to-the-challenge] |
| Capacity is unavailable | Willis (27 Jul 2026): global market can provide up to **$15bn** for large data center risks; "the capacity is there"; buyers risk being over-insured. | [source: https://www.insurancebusinessmag.com/us/news/technology/overinsured-data-centers-are-a-growing-problem-willis-says-583799.aspx] |
| Limits should track insured value | Lockton: a $10bn multi-building campus can have true exposure as low as $3bn. | [source: insuranceinsider.com, as above] |
| — | Swiss Re: industry can supply only a fraction of the limits lenders want **"at competitive rates"**. Munich Re net line about $250M per data center construction project. | [source: search snippet; Swiss Re sigma insights 07/2026 and insurancebusinessmag.com, pages not opened] |
| — | 64% of capacity under construction is outside traditional hubs, with more tornado and hail exposure (Zurich). | [source: insurancebusinessmag.com Willis article, as above] |
| — | Rates "going up a nominal amount"; premium growth comes from values, not rate. | [source: bisnow.com snippet, date unclear] |
| — | Fronting: carrier usually keeps a fee plus 10-20% of premium as retained risk (Morningstar DBRS); unlicensed reinsurers post 100% collateral; post-Vesttoo collateral exams. | [source: search snippet, insurancebusinessmag.com and mayerbrown.com, pages not opened] |
| — | BMA updated its licensing process on 29 Jan 2026; standard special purpose insurer registration is streamlined to days; a de novo Class 3B got approval in principle in April 2026. | [source: search snippet, kennedyslaw.com, insuranceinsiderils.com, bernews.com] |
| — | Casualty sidecars are about 8.7% of sidecar capacity; AM Best notes 7-10 year commitments do not fit ILS fund liquidity. Nothing found on ILS money in engineering lines. | [source: search snippet, artemis.bm and ey.com] |

Reading: the gap is real at the price buyers want to pay, and incumbents are closing it at roughly +$1.5bn per quarter. It is a price gap, not an absolute gap.

---

## 1. The arithmetic that decides everything

**Collateral.** A collateralized reinsurer posts collateral equal to limit minus net premium. On a single-site excess layer, the probable maximum loss is the full limit once the layer attaches. No fronting carrier accepts less than limit. So $300M of collateral supports about **$300-330M of limit, not $1.5bn**. [DK]

**Rate on line by layer** (annualized, US hyperscale campus, construction with delay-in-startup). [DK]

| Layer | Realistic rate on line | Who holds it now |
|---|---|---|
| Primary / working, $0-250M | 2.5-5.0% | Lead carriers (Zurich, FM, Chubb, Allianz, Starr, Liberty named as leads [source: insuranceinsider.com]) |
| Low excess, $250-750M | 0.8-1.8% | Same leads plus Lloyd's and reinsurers |
| Mid excess, $750M-2.5bn | 0.4-0.9% | Broker facilities, following markets |
| Above the facilities, $2.5-5bn+ | 0.15-0.5%; up to 1.0% in tornado/hail zones or with long delay cover | Thin. This is where the brief says it will attach |

The founder's 1.5-3.0% exists only in the working and low-excess layers, which are full and loss-active. Where the vehicle says it attaches, the rate is 0.15-1.0%.

**Investor return.** Frictional costs come off gross premium first: brokerage and facility commission 12.5-17.5%, fronting 5-7%, the company's 12% fee, 1% US federal excise tax on premium ceded to Bermuda. About 68% of gross reaches the vehicle. [DK]

- Fully collateralized at 0.5% rate on line: $1.5M gross, about $1.0M net, less expected loss. Underwriting return about 0.1-0.2% of capital a year. The investor earns Treasury yield plus nothing, with a small chance of losing a whole layer.
- Break-even for a collateral investor wanting risk-free plus 8%: rate on line must be about **13%** if expected loss is 1% of limit ((8% + 1%) / 0.685). The market pays 0.2-3%.
- The founder's own case (5x leverage, $35M premium, 50% loss ratio): margin 18.5% of $35M = $6.5M = 2.2% of capital, 1.8% after the 15% profit share. For that the investor takes a loss of 33-83% of capital from one site event. [derived from brief]

**Company economics.** 12% of $25-45M is $3.0-5.4M of fees. The team this needs costs $12-18M a year (section 9). The underwriting company loses $7-15M a year on the founder's own numbers, and more on realistic ones. [derived; cost is DK]

**Revenue definition.** The brief counts earned premium in the reinsurer plus fees. If outside investors own the reinsurer, the company recognizes only fees and profit share. If the company consolidates it, the fees eliminate. It cannot count both. [DK, accounting]

---

## 2. Persona 1: head of programs, A-rated fronting carrier

**Who.** Runs a $1-3bn fronted portfolio. Paid on fee income, fired for an uncollectable recoverable or a rating action.

**Constraints.**
- The front stays liable to the policyholder for the full limit if the reinsurer fails. AM Best charges the front for credit risk on unrated recoverables and looks at the largest gross single-risk loss. [DK]
- Program fronts are built for many small limits. A $100-250M line on one site is outside delegated-authority norms. [DK]
- The fronts with enough gross line for this (reinsurer-owned fronting units) already write data center towers for their own account and are at their site limits. [DK]
- State examiners now check collateral directly after the 2023 letter-of-credit fraud. [source: snippet, insurancebusinessmag.com]

**Alternatives.** Front for an established engineering team with a ten-year audited record, or for a broker-owned programme. Ryan Specialty's Tera already has a $625M lead binder. [notes]

**Decision.** Refuses delegated authority for $100-250M lines. Would sign a narrow programme on these terms:

| Term | Requirement |
|---|---|
| Fronting fee | 5-7% of gross premium, minimum $1.5-2.5M a year |
| Collateral | 102-105% of aggregate **limit** less net premium, in a US trust the front controls. Treasuries or government money funds only. No letters of credit from banks off its list |
| Retained share | Zero. It will not take 10-20% net on single-site data center risk it already holds elsewhere |
| Maximum line | $25M any one campus in year one, $50M after a clean 24 months |
| Authority | Every risk referred before bind. This is fronting with a veto, not a pen |
| People | Named chief underwriter with 15+ years of engineering lines, key-person termination right, two more senior underwriters, in-house risk engineers |
| Claims | Front appoints the adjuster. Team authority $250k |
| Run-off | Collateral held to end of the defects period and until every claim closes. Commutation at the front's option only |
| Other | $20M+ errors and omissions cover, quarterly audit, capital committed before signing |

**Timeline.** 4-6 months of diligence after capital is committed and the chief underwriter is under contract.

**What changes the decision.** $300M in trust, a named lead underwriter with a verifiable record, and a tier-one reinsurer co-participating on every risk.

---

## 3. Persona 2: portfolio manager, ILS fund / pension allocator

**Who.** Runs $3-8bn of mostly catastrophe risk. Offers investors annual or semi-annual liquidity. Investment committee needs a third-party model and an expected loss.

**Constraints.**
- No vendor model exists for single-site engineering and delay risk. Expected loss would rest on the sponsor's own view. [DK]
- Hurdle for an unmodelled line with a first-time manager: risk-free plus 8-12%. Catastrophe bonds pay roughly risk-free plus 5-7% with models and a secondary market. [DK]
- Construction policies run 2-4 years and cannot be cancelled. Add a 12-24 month defects period and 2-4 years for delay claims to settle. Real lock-up is **5-7 years**. AM Best flags the same mismatch for 7-10 year casualty deals. [DK; source: snippet, artemis.bm]
- Trapped collateral: the front holds 100% of limit until expiry, then a multiple of reserves. A delay claim notified late in the project freezes the layer for years. [DK]
- Single-name concentration: one $100-250M layer is 33-83% of the vehicle. Fund rules cap any one event at 5-10% of net asset value. [DK]
- Correlation with the rest of the book: the same tornado, hail or Gulf wind events already drive its catastrophe positions. [DK]
- Pension consultants want a three-year audited record before a $50M+ ticket. [DK]

**Alternatives.** Sidecars sponsored by rated reinsurers, where the sponsor retains a share of a diversified book. Catastrophe bonds.

**Decision.** Refuses the $300M vehicle. Would commit **$15-30M** to a $75-100M pilot on these terms:
- Fees: 7.5-10% override in place of 12%; 10-15% profit share only above a risk-free plus 6% hurdle, with deficit carry-forward and clawback.
- No leverage. Maximum 10% of net asset value per campus, 25% per tornado/hail zone.
- Rated front signed and chief underwriter in seat before funding.
- Independent actuarial opinion on expected loss by layer.
- Founders invest 3-5% of the vehicle alongside.
- Five-year commitment with a stated side-pocket mechanism.

**Reason.** Section 1. Fully collateralized, the layers pay Treasury yield plus 0.1-2%. Levered 5x, two site events wipe out the fund.

**What changes the decision.** Rate on line above about 10% net of costs on a fully collateralized basis, or a rated reinsurer taking 50%+ of every risk beside it.

---

## 4. Persona 3: regulator and rating agency view

**Bermuda Monetary Authority.** [DK unless marked]
- A special purpose insurer must be fully funded to its aggregate limit. The fast-track registration is for standard catastrophe structures [source: snippet, insuranceinsiderils.com]. A multi-year, multi-cedant engineering vehicle with a new manager is not standard and will get a full review.
- To write more limit than collateral, the vehicle must be a commercial class (3A, 3B or 4) with a risk-based capital requirement, a Bermuda head office, resident officers, an approved auditor and a loss reserve specialist. A de novo 3B was approved in principle in April 2026 [source: snippet, bernews.com].
- Timeline: 3-4 months to prepare the application, 1-3 months for review. The Authority will not license before capital is committed. **4-7 months after funding is firm.**

**AM Best.** [DK]
- A fully collateralized vehicle behind a front needs no rating. It also gets no leverage.
- Leverage needs a financial strength rating of A-. Start-ups that got A- in recent classes launched with roughly $500M-1.1bn.
- Largest net single-risk loss above about 10% of surplus is a concentration problem. On $300M that means **$15-30M net per campus**.
- A monoline, single-industry book with no vendor model and no loss history gets a weak business-profile assessment. A- on $300M is unlikely. A $100-250M net line makes it impossible.
- Initial rating takes 4-6 months after capital is in.

**US rules.** [DK]
- Credit for reinsurance: a US front ceding to an unauthorized Bermuda reinsurer needs 100% collateral for ceded unearned premium and loss reserves. Zero-collateral reciprocal status needs at least $250M of capital and surplus and a commercial licence class. At $300M, one loss puts the vehicle below the threshold and collateral springs back.
- That rule governs the front's statutory credit only. The front's own credit appetite (collateral to limit) is the binding constraint.
- Surplus lines: the front must be an eligible non-admitted insurer in each project state. The underwriting company needs managing general agent and surplus lines licences in Texas, Virginia, Arizona and others. 2-4 months.
- **Growth plan problem.** Offtake-default "credit wrap" is financial guaranty insurance. New York restricts it to monoline guarantors, and multiline fronts cannot issue it. It would have to be restructured as lender non-payment insurance in the London credit market, where per-obligor lines are $25-75M per insurer. Residual value insurance is a permitted line but needs its own filing and capital treatment.

**Capital actually required.**

| Goal | Capital |
|---|---|
| $1.5bn of limit, fully collateralized | about $1.45bn |
| $1.5bn of limit, rated, $25M net lines | $500M-1bn of equity, 60+ sites, and an A- the profile will struggle to get |
| What $300M supports | $300-330M collateralized; $600-900M rated, if a rating were obtained |

---

## 5. Persona 4: veteran specialty underwriter, construction and power engineering

**Who.** Thirty years of construction all-risk, erection, and power. Has led and followed data center towers.

**Loss frequency and severity.** [DK]
- Frequency sits in the bottom $50M: water damage (pipe tests, storm water through an open envelope, suppression discharge), hot-work and electrical fires, switchgear and UPS failures in testing, crane and lifting incidents, theft, defective workmanship. Expect several notifications per building per year.
- Typical claim $1-50M. Losses of $100-500M are rare but have happened in battery fires and whole-hall fire or smoke events.
- New severity drivers: lithium batteries inside or beside halls, direct liquid cooling leaks onto racks, on-site gas turbines and large battery systems during commissioning, hail on roof-mounted cooling.
- One 150MW hall fitted with accelerators carries about $5-6bn of equipment. Smoke contamination can write off a hall without structural loss. Once equipment is installed, a layer above $3-5bn is not beyond a single-building loss.
- Long-run loss ratio for engineering lines: 50-65%. Excess layers: near zero most years, several hundred percent in a bad one.

**Delay-in-startup experience.** [DK]
- This is the real severity. Lease revenue for 1GW is about $2bn a year, $5-6M a day. A six-month delay to one 200MW building is $180-240M. A neocloud's contract revenue per GW is several times that.
- Transformer, switchgear and turbine lead times run 2-4 years. Physical damage to one long-lead item can delay a phase 12-24 months. Delay layers are reached by small physical losses.
- This is why delay cover is sublimited to 12-24 months with 45-90 day waiting periods, and why it is the main limiter [notes].

**Accumulation.** [DK]
- The same site appears under construction, operating, contractor, cargo and equipment policies, and during phased handover two policies overlap.
- Sites cluster: North Texas, Northern Virginia, Phoenix, central Ohio. One hail or tornado outbreak touches several insured campuses.
- Prudent net line on $300M: **$15-25M per campus**; fully collateralized, $30-45M at most. Cap any one storm zone at 25% of capital.

**Why capacity is short.** Values rose from about $1bn to about $22bn per large site in five years [source: insuranceinsider.com]. Net lines are capped by treaties (about $250M for the largest reinsurer [source: snippet]). Lenders ask for limits above probable maximum loss. Delay cover has no pooling benefit. Every carrier is on every tower.

**Why that is not the founder's opening.** The shortage is at the price buyers will pay. Buyers respond to a 1.5-3.0% quote on a top layer by going uninsured or by negotiating lenders down to a loss limit based on probable maximum loss. Incumbents added $2.5bn of facility limit in 13 months without a rate spike [source: insurancebusinessmag.com; bisnow.com snippet].

**Would follow the new vehicle onto a slip?** Irrelevant to him; he would not cede his line. As a peer he would see it signed down to a $10-25M following line at lead terms, with no say on wording.

**On the loss-control pitch.** The lead insurer's engineers get site access and share reports. An excess follower does not get a hyperscaler's schedule telemetry. No credit in price until there is loss data.

**What changes his view.** A bound slip showing a buyer paid 1.5%+ for a layer above $2.5bn, and evidence that lenders refused a loss-limit waiver.

---

## 6. Persona 5: retrocession underwriter, large reinsurer

**Who.** Writes per-risk and specialty retrocession. Already carries a maximum net line on the same campuses through direct and treaty business.

**Constraints.** Any limit granted to the vehicle on a named campus counts against the reinsurer's own site aggregate. The vehicle is monoline with no spread, so the cover is pure risk transfer of the reinsurer's most concentrated exposure. [DK]

**Alternatives.** Use the same site capacity to write the original layer directly and keep the whole premium.

**Decision.** Declines an open single-campus total-loss cover. Would quote a named-site schedule only:
- $50-75M excess of $25M per campus.
- Rate on line 2-4%, which is equal to or above the original rate on the protected limit.
- One reinstatement at 100%. 10% co-participation by the vehicle.
- Delay-in-startup limited to 12 months. Sites where the reinsurer is already full excluded.
- Annual term, against the vehicle's 3-4 year policies. The renewal risk stays with the vehicle.

**Consequences.** The retro costs 70-150% of the original premium for the protected limit, so it removes the margin. The front will not release collateral against a retro recoverable unless the retrocessionaire signs a cut-through. [DK]

**What changes the decision.** A diversified book of 40+ sites at $10-25M lines with a proportional share offered, so the retrocessionaire shares premium and not only tail.

---

## 7. Persona 6: loss adjuster and claims lead

**Who.** Leads major engineering losses for a global adjusting firm, with forensic accountants and delay analysts.

**How delay-in-startup claims get disputed.** [DK]
- **Causation.** The policy pays only for delay caused by insured physical damage. Most mega-projects are already late for uninsured reasons: labour, late equipment, grid interconnection, permits. The fight is over the critical path and concurrent delay.
- **Baseline date.** The scheduled operation date must be documented and updated. Insureds seldom keep it clean.
- **Quantum.** If the lease start slips and the term extends, revenue is deferred, not lost. Insurers offer debt service and fixed costs. Insureds claim gross revenue. Tenant termination rights and liquidated damages decide which is right.
- **Mitigation.** Expediting and temporary power are claimed as increased cost of working and argued against the economic limit.
- **Defects.** Whether faulty design or workmanship is covered depends on the defects clause. This is the most litigated wording in construction cover.
- **Handover.** During phased occupation, the construction and operating insurers each say the loss is the other's.
- **Lenders.** Lenders are loss payees with non-vitiation protection, so the insurer pays the lender even if the insured breached conditions.
- Data center claims complexity is already being flagged in the legal press. [source: https://www.bracewell.com/resources/data-center-insurance-boom-may-obscure-claims-difficulty/, title only, not opened]

**Payment timeline.** Physical damage: interim payments in 3-6 months, settlement in 12-24. Delay claims: 2-4 years, often by arbitration. Collateral for that layer is frozen throughout.

**Residual value claims.** [DK]
- Disputes over the trigger (default, then sale below insured value), whether the sale was commercially reasonable, equipment condition, removal cost, and index versus realised price.
- The lender controls the sale and has no incentive to maximise price once insured.
- All claims arrive in the same quarter, when a new chip generation or a demand drop hits. Documented used-GPU sales total $26.3M over three years [notes], so there is nothing to adjust against.

**Staffing the claims side.** One claims lead with large-loss experience, panel adjusters, forensic accountants and delay analysts on retainer, coverage counsel in Texas, New York and London. The front will still control settlement.

**Position.** Will take the appointment for fees. Warns that as an excess follower the vehicle has no control over a claim it funds, and a new carrier that disputes its first large claim loses broker support.

---

## 8. Persona 7: senior underwriter asked to join as chief underwriting officer and co-founder

**Who.** Class head for construction and engineering at a top-ten carrier. Total pay $700k-1.2M with deferred stock. Six to twelve months of garden leave and a twelve-month non-solicit. [DK]

**What he sees.**
- Circular dependency: investors want the front signed, the front wants capital in trust, both want him named, and he wants both done before resigning.
- The 5x leverage premise fails at the first fronting meeting.
- $100-250M lines on $300M would end his market reputation at the first loss.
- Residual value and credit wrap are outside his competence.
- The fee income does not pay his team.

**Decision.** Refuses now. Would sign on these terms:
- $300M committed in escrow with a five-year lock, or $100M plus a rated reinsurer taking 50% of every risk.
- Rated front under signed term sheet.
- Three years of operating costs ($30-45M) funded by equity, not by fees.
- Base $500-600k, 15-25% of the underwriting company, buy-out of forfeited stock ($1-2M).
- Written authority to cap lines at $25-40M per campus and to refuse the residual value and credit products.

**What breaks first, in order.**
1. The capital raise: first close comes in at $50-150M, late, because of the circular dependency.
2. The leverage: the front demands collateral to limit and the premium falls to a fifth of plan.
3. Signing: brokers sign the line down, and leads refuse to let a follower change terms.
4. The first delay claim: collateral is trapped, investors cannot redeem, and fund two is not raised.
5. Fee income versus cost: the underwriting company needs new equity every year.

---

## 9. Dependencies, approvals, staffing

**Critical path.** Each step waits on the one before, and steps 1-3 wait on each other.

| # | Dependency | Realistic duration |
|---|---|---|
| 1 | Chief underwriter and two senior underwriters hired and free of garden leave | 6-12 months |
| 2 | Capital committed (anchor plus first close) | 9-18 months; first close more likely $50-150M than $300M |
| 3 | Fronting agreement, trust agreement, reinsurance agreement | 4-6 months after 1 and 2 |
| 4 | Bermuda licence (review, head office, resident officers, auditor, reserve specialist) | 4-7 months after 2 |
| 5 | US managing general agent and surplus lines licences | 2-4 months |
| 6 | Broker market-security approval at Aon, Marsh, WTW | 2-4 months each, after 3 |
| 7 | AM Best rating, only if leverage is wanted | 4-6 months after capital; A- unlikely on $300M |
| 8 | Retrocession, if wanted | Annual, named sites only |
| 9 | First signed line on a live placement | Project timing; placements take 3-6 months |

**Staff before first bind.** About 20-25 people, $12-18M a year. [DK]
- Underwriting: chief underwriter, 2-3 senior underwriters.
- Risk engineering: 3-5 engineers (electrical, mechanical, fire and battery).
- Claims lead; panel adjusters and forensic firms on retainer.
- Chief actuary; chief financial officer with reinsurance and trust accounting; chief risk and compliance officer; general counsel.
- Bermuda: resident principal representative, insurance manager, two resident directors.
- Capital markets and investor relations lead.
- Data and telemetry team for the loss-control promise.

**Failure modes not covered above.**
- Incumbent supply keeps growing and the top-layer rate falls before the first bind.
- A market loss before launch helps price but closes investor appetite.
- A market loss after launch on a site the vehicle holds: one event, 10-80% of capital depending on line size.
- AI capital spending slows. Projects are cancelled, premium is returned, multi-year policies are cut short.
- Key-person clause: the chief underwriter leaves and the front can terminate.
- Residual value and credit products correlate with the property book's own demand driver. One AI downturn hits premium volume, residual claims and credit claims together.

---

## 10. Panel estimates

**Time to first bound line.** 15-24 months from today, central case 18-20. The founder's 9-12 months needs capital and a team already in hand; incumbents launching new programmes on existing paper take 6-9. [DK]

**Maximum prudent limit on $300M.**

| Structure | Aggregate limit | Per campus | Count |
|---|---|---|---|
| Fully collateralized (what the brief describes) | $300-330M | $30-45M | 7-10 campuses |
| Rated, if A- were obtained | $600-900M | $15-25M net | 30-45 campuses, 25% cap per storm zone |
| Founder's plan | $1.5bn | $100-250M | 6-15 layers: not prudent, not frontable |

**Expected loss ratio.** 55-65% of gross as a planning figure for a mid-excess book with delay cover; 35-55% long-run for clean excess layers with extreme volatility. Acquisition and fees add 30-37 points. Combined ratio 90-100% before the cost of capital. [DK]

**Revenue actually recognized.**

| | Founder implied | Panel base case | Panel upside (full $300M deployed by month 18, lines in low/mid excess) |
|---|---|---|---|
| Year 1 | Part-year of $25-45M | **$0** | $0 |
| Year 2, fees only (reinsurer not consolidated) | $3-5M | **$0.2-0.6M** | $1.0-1.5M |
| Year 2, earned premium (reinsurer consolidated) | $25-45M | **$0.5-1.5M** | $2-4M |
| Annualized premium at full deployment | $25-45M | $2-4M on $300M of limit | $6-9M if rated and levered to $900M |

Basis: $100-300M of limit bound between months 15 and 24 at a blended 0.8-1.3% annualized rate on line, on 2-4 year policies earned along the construction exposure curve, which is back-loaded. Investment income on collateral (about $11-12M a year on $300M) belongs to investors. [derived; DK]

$100M of premium needs about $10bn of limit at 1%. That is $10bn of collateral, or a rated carrier with $3-5bn of equity.

---

## 11. Numbers in the brief the panel disputes

| Brief | Panel | Basis |
|---|---|---|
| Rate on line 1.5-3.0% above the broker facilities | 0.15-1.0% there; 1.5-3.0% only in layers below $750M | [DK] |
| $1.5bn of limit on $300M | $300-330M collateralized; $600-900M if rated | Collateral to limit; AM Best concentration [DK] |
| Standard layer $100-250M | $15-45M per campus | 5-15% of capital per site [DK] |
| Premium $25-45M a year | $2-4M collateralized; $6-9M rated | Derived |
| Licence and fronting 6-9 months; first bind 9-12 | Licence and fronting 10-16; first bind 15-24 | Section 9 |
| Revenue = earned premium plus fees | One or the other | Consolidation |
| 12% fee plus 15% profit share | Investors accept 7.5-10% plus 10-15% above a hurdle | Section 3 |
| Attaches above $3.5bn Aon facility | Aon is $5bn; FM $5bn; one tower $8.5bn; market $15bn | [source: URLs in section 0] |
| "Capacity did not grow" | Grew about $2.5bn at one facility in 13 months | [source: insurancebusinessmag.com] |
| Only a third to a half of value insured, so the rest is demand | Probable maximum loss can be 30% of value; buyers may be over-insured | [source: insuranceinsider.com; insurancebusinessmag.com] |
| Credit wrap as a later insurance product | Financial guaranty; not frontable by a multiline carrier in New York | [DK] |

---

## 12. Verdicts

| Persona | Decision | Terms they would accept |
|---|---|---|
| Fronting head | Refuses the pen for $100-250M lines. Would front a referred programme | 5-7% fee, collateral 102-105% of limit, zero retention, $25M per campus, every risk referred |
| ILS manager / pension | Refuses $300M. Would put $15-30M in a $75-100M unlevered pilot | Risk-free plus 8-12%, 7.5-10% override, 5-year lock, 10% of net asset value per site |
| Regulator / rating agency | Licence obtainable. A- on $300M with these lines: no | $500M-1bn equity for a rating; net line under 10% of surplus |
| Veteran underwriter | Says the price is wrong and the line size reckless | $15-25M lines; 1.5%+ only below $750M |
| Retrocessionaire | Declines open cover. Named-site quote only | $50-75M xs $25M, 2-4% rate on line, 10% co-participation |
| Claims lead | Takes the work. Warns collateral is trapped 2-4 years per delay claim | Front controls settlement |
| Chief underwriter candidate | Refuses now | Capital in escrow, front signed, 3 years of costs funded, $25-40M line cap, 15-25% equity |

**Panel conclusion.** As specified, the business is unworkable. The layers that are short of capacity pay 0.15-1.0%. Fully collateralized capital needs about 13%. Closing that gap needs leverage; leverage needs a rating and diversification; those need several times $300M or lines a tenth of the size planned. Rated incumbents with $10-30bn balance sheets hold exactly that advantage and are already using it.

**Probabilities (panel's honest estimate).**
- This version binds a first paid layer within 18 months: **12%**. A shrunken version (a $10-25M following line on fronted paper) is most of that.
- $1bn of annual recognized revenue within 7 years: **about 1%**.

---

## Sources opened or returned this session

- https://www.insurancebusinessmag.com/us/news/technology/aon-expands-data-center-insurance-program-to-5bn-amid-capacity-crunch-582902.aspx (opened)
- https://www.insuranceinsider.com/sample-content/data-centre-dispatches-how-the-construction-market-is-rising-to-the-challenge (opened)
- https://www.insurancebusinessmag.com/us/news/technology/overinsured-data-centers-are-a-growing-problem-willis-says-583799.aspx (opened)
- https://www.enr.com/articles/62899-report-billions-of-dollars-in-data-center-construction-risk-is-uninsured (via notes)
- https://www.swissre.com/institute/research/sigma-research/sigma-insights-07-2026-insuring-ai-data-centre-risks.html (snippet only)
- https://www.insurancebusinessmag.com/us/news/technology/data-center-scale-is-maxing-out-us-insurance-limits-598063.aspx (snippet only; probable origin of the Munich Re $250M figure)
- https://www.bisnow.com/national/news/data-center/data-center-risks-rattling-some-insurance-providers-132080 (snippet only, date unclear)
- https://insurancebusinessmag.com/us/news/excess-surplus/mga-boom-raises-operational-and-credit-exposure-for-us-fronting-insurers-567929.aspx (snippet only)
- https://www.mayerbrown.com/en/insights/resource-centers/insurtech/mga-mgu (snippet only)
- https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-bermuda-monetary-authority-updates-its-licensing-process-for-insurers (snippet only)
- https://insuranceinsiderils.com/article/28yshb7cjx5tz3tg8mozk/bma-streamlines-registration-process-for-special-purpose-insurers (snippet only)
- https://bernews.com/2026/04/verdant-rock-limited-secures-bma-approval (snippet only)
- https://www.artemis.bm/news/casualty-sidecar-capital-surpasses-2bn-as-specialised-investor-base-drives-expansion-am-best/ (snippet only)
- https://www.ey.com/en_us/insights/insurance/property-and-casualty-reinsurance-sidecars-scaling-institutional-capital (snippet only)
- https://www.bracewell.com/resources/data-center-insurance-boom-may-obscure-claims-difficulty/ (title only)

Not found anywhere public: rate on line by layer for data center towers, fronting fee schedules for large-line programmes, ILS hurdle rates for engineering risk, Bermuda collateralized-insurer capital rules as currently in force, loss ratios for data center construction books. All such figures above are domain knowledge and should be tested with a broker and a fronting carrier before anyone relies on them.
