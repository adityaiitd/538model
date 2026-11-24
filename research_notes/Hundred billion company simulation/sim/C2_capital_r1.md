# C2 v1, capital and competition panel, round 1

Simulated on 24 November 2026. Everything below is a simulated hypothesis from archetype personas. It is not customer or investor validation. No real person was interviewed and no quote is real.

Evidence labels used:
- [notes] = `financial_infrastructure.md`
- [source: URL] = opened and read in this session
- [source, snippet-level: URL] = figure came from a search-result summary; page not opened
- [domain knowledge, unverified] = panel's own knowledge of market practice, not checked
- [derived] = panel arithmetic on labelled inputs

Web budget used: 4 searches, 4 fetches (the cap of 8).

---

## 0. Facts the panel checked that change the brief

| Item | Brief / notes say | Checked value | Label |
|---|---|---|---|
| Aon Data Center Lifecycle programme | $3.5bn (April 2026) | $5bn from July 2026, third increase in about a year; covers construction all risks, delay in start-up, property damage and business interruption | [source: https://www.insurancebusinessmag.com/us/news/technology/data-center-values-outstrip-insurance-capacity-as-ai-buildout-accelerates-597876.aspx] |
| Marsh | Nimbus $2.7bn | Nimbus $2.7bn (construction) plus Stratus, launched August 2026: up to $10bn single-placement capacity for the operational phase, drawing on 30 traditional and alternative capital providers | same source |
| Mutual highly-protected-risk insurer | not in brief | FM Intellium limit raised to $5bn in January 2026; FM says it insures about 1,100 data centers with $250bn of insurable value and 25+ years of experience | [source, snippet-level: https://www.insurancejournal.com/news/national/2026/01/13/854094.htm] |
| "Typical limits $1.5-3.5bn" | brief | S&P and LGT now describe $5-10bn as the conventional single-risk limit; site values $20-30bn (S&P) or $30-45bn+ (LGT) | [source: https://www.artemis.bm/news/insurance-capacity-constraints-for-data-centres-to-drive-ils-use-sp/] and the insurancebusinessmag source above |
| Other 2025-26 entrants | not in brief | Fidelis Partnership committed $1.6bn to data center risk in 2025 including a $250M Lloyd's construction consortium, with a Blackstone-backed syndicate adding capacity from 1 January 2026 | [source, snippet-level: https://www.insurancebusinessmag.com/reinsurance/news/breaking-news/fidelis-commits-1-6-billion-in-data-center-capacity-through-lloyds-consortia-569161.aspx] |
| | | ATA facility, up to $750M, 10+ re/insurers including Arch, Munich Re Specialty and SCOR (January 2026) | [source: https://www.reinsurancene.ws/ata-introduces-750m-insurance-facility-to-support-global-ai-infrastructure/] |
| | | Ryan Specialty Tera, $1bn+ per policy | [notes] |
| Single-reinsurer line | not in brief | Roughly $250M net from one top reinsurer on one data center construction project; $10bn on one site means 40 or more carriers | [source, snippet-level: search summary of trade press, page not identified] |
| Alternative capital | "funded by ILS funds" is the founder's edge | An ILS manager was already discussing collateralised reinsurance for data centres with insurers for the 1 January renewals; LGT's ILS arm publishes its own data center premium projections | [source, snippet-level: https://www.insuranceinsider.com/sample-content/ils-market-scopes-potential-for-data-centre-risk-transfer]; insurancebusinessmag source above |
| Pricing direction | "capacity did not grow" | Lockton Q1 2026: buyers "benefiting from favourable market conditions", an influx of new capacity in UK, US and Asia, competitive rating structures. No rate numbers given | [source: https://global.lockton.com/ae/en/news-insights/data-centre-market-update-q1-2026-or-insurance-trends-risk-insights] |
| Lender demand | lenders require cover | Moody's (March 2026): investors including Blackstone reportedly passed on data center debt for lack of insurance. This supports the demand claim | [source: insurancebusinessmag, 18 Nov 2026, above] |
| Accumulation | one tornado | Texas and Virginia hold more than 40% of current and planned US capacity; over a quarter sits where there are three or more large-hail days a year; about 40% is in zones with significant tornado exposure (Swiss Re sigma 3/2026) | same source |

Panel reading: the shortage is real at the top of the largest towers and in construction with delay cover. It is also being filled at a rate of several billion dollars of per-risk limit every few months by parties that already hold the paper, the engineering staff and the broker position. A $300M vehicle is 3-6% of one current facility [derived: 300/5,000 and 300/10,000].

---

## 1. Panel capital model

### Inputs

| Input | Founder | Panel | Basis |
|---|---|---|---|
| Limit to collateral | 5.0x ($1.5bn on $300M) | 1.0-1.5x at launch, 3x at best after 3 clean years | "Collateralized reinsurance" means collateral equal to limit less premium. Leverage on a per-risk book where one line is 33-83% of capital needs a fronting carrier to take uncollateralized credit risk on a new unrated vehicle with no vendor model. [domain knowledge, unverified] |
| Line size | $100-250M | $30-50M | Investor and bank concentration limits of 10-17% of net asset value per risk. [domain knowledge, unverified] |
| Rate on line, annualised | 1.5-3.0% | 0.6-1.5%, base 1.0%, falling | Layers above $5-10bn attachment on a multi-building campus are remote. Construction rates are usually quoted for the whole project term of 3-4 years, so a 1.5-3% term rate is 0.5-1.0% a year. [domain knowledge, unverified] |
| Expected loss | not stated | 0.15-0.30% of limit a year | Panel judgment; no model exists. [domain knowledge, unverified] |
| Acquisition cost | 12% fee | 28% of premium: brokerage 10%, fronting 6%, underwriting company 12% | [domain knowledge, unverified] |
| Collateral yield | not stated | 3.5% | Circle reserve return 3.5% in Q3 2026 [notes] used as a cash proxy |
| Profit commission | 15% | 15% | brief |

### Results at $300M [derived]

| Case | Limit | Premium | Investor return, no loss | Excess over cash | Expected | After one full line | Fee company revenue |
|---|---|---|---|---|---|---|---|
| Founder, 1.67% | $1.5bn | $25M | 8.1% | 4.6 pts | 6.8% | -74% ($250M line) | $5-6M |
| Founder, 2.25%, $250M lines | $1.5bn | $34M | 9.9% | 6.4 pts | 8.6% | -72% | $7-8M |
| Founder, 2.25%, $100M lines | $1.5bn | $34M | 9.9% | 6.4 pts | 8.6% | -22% | $7-8M |
| Founder, 3.0% | $1.5bn | $45M | 12.2% | 8.7 pts | 10.9% | -70% | $10M |
| Panel low | $300M | $1.8M | 3.4% | -0.1 pts | 3.2% | -13% ($50M line) | $0.4M |
| Panel base | $450M | $4.5M | 3.9% | 0.4 pts | 3.7% | -13% | $1.0M |
| Panel high | $900M | $13.5M | 5.8% | 2.3 pts | 5.1% | -19% ($75M line) | $3.1M |

Reading:
- On the founder's own numbers at mid-rate, investors earn 6.4 points over cash in a clean year and lose 22-72% on one event. One $250M loss takes 13 clean years of excess return to earn back; one $100M loss takes 5.
- On the panel's numbers, investors earn cash plus 0-2 points. That does not pay for the risk.
- The vehicle only produces an equity-like return if both founder assumptions hold together: 5x leverage and a rate on line of 2.25% or more a year. The panel believes neither.

### Recognized revenue and return on capital by scale [derived]

| Risk capital | What it has to be | Limit deployed | Premium | Investment income | Consolidated revenue (premium + investment income) | Fee company revenue (12% + 15% of profit) | Return on capital, normal year | After one full single-campus line | Correlated AI stress |
|---|---|---|---|---|---|---|---|---|---|
| $300M | Collateralized follower | $0.3-0.9bn | $2-14M (base $4.5M) | $10.5M | $12-24M (base $15M) | $0.4-3M (base $1M) | 3.4-5.8% (base 3.9%) | -13% to -19% | n/a |
| $300M, founder case | 5x leveraged | $1.5bn | $25-45M | $10.5M | $36-56M | $6-10M | 8-12% | -22% to -74% | n/a |
| $3bn | A- rated specialty carrier: excess property $4.5-9bn of limit, plus $2-7bn of residual value and credit cover | $6.5-16bn | $90-310M (base $174M) | $105M | $190-410M (base $280M) | $20-70M (base $40M no-loss, $29M expected) | 4.9-9.4% no-loss (base 6.7%), 3.9-6.0% expected | +0.3% to +2.3% (line is 5-8% of capital) | Not modelled; residual value and credit books move together |
| $30bn | A global multi-line reinsurer plus a financial guarantor. Not a niche | about $100bn+ of par and limit | about $4.3bn: $2.9bn property and construction (12% of Swiss Re's $24.2bn 2030 pool [notes]), $1.0bn credit wrap (1.25% on $80bn par), $0.4bn residual value | about $1.15bn | about $5.5bn | about $0.65bn | about 6.8% | +1.8% (a $1.5bn line) | about -53%: 10% loss on $80bn wrapped par and 50% loss on $20bn of residual value limit |

Notes on the table:
- The company can only recognize premium as revenue if it owns and consolidates the reinsurer. If outside investors own the vehicle, the company's revenue is the fee line only. The brief's "earned premium plus fees" double counts the fee, which is an expense of the reinsurer. [domain knowledge, unverified]
- Multi-year construction premium is earned over the build, weighted to the back end. First-year earned premium is perhaps 15-25% of written. [domain knowledge, unverified]
- $1bn of recognized revenue needs roughly $8-12bn of capital on a consolidated basis, or about $7bn of premium under management on a fee basis ($1bn / 14%). The second is larger than any data center premium share the panel can justify. [derived]
- $30bn would be about a quarter of all alternative reinsurance capital, which the panel puts near $120bn. [domain knowledge, unverified]

### Does scale make it more defensible, or just larger?

Just larger, with one qualification.
- Return on capital does not rise with scale. It goes 3.9% → 6.7% → 6.8% only because the larger versions add leverage through a rating and add credit and residual value risk. The property return falls with scale because the company's own capacity removes the scarcity that sets the rate.
- Single-event survivability does improve with scale (one line falls from 17-83% of capital to 5%). That is diversification, which every incumbent already has.
- The qualification: at $1bn+ with a rating, the company could lead layers, set wordings and write primary layers where attritional losses generate data. That is the business the mutual and the top reinsurers have run for 25+ years.
- At $30bn the dominant exposure is one factor: demand for AI compute. Size raises that correlation.
- Value: a balance sheet is worth 1.0-1.5x book [domain knowledge, unverified], so $30bn of contributed capital is worth $30-45bn. A fee company earning $0.65bn at a 40% margin and 15-20x earnings is worth $4-5bn. A $100bn valuation needs about $70-75bn of equity at 1.3-1.4x book, which is the combined size of the two largest European reinsurers. [derived; domain knowledge, unverified]

---

## 2. Personas

### Persona 1. Chief investment officer, pension or sovereign fund, asked to anchor the $300M vehicle

- **Who**: runs a $60-150bn fund with a 1-3% allocation to insurance-linked strategies, placed through four or five established managers. [domain knowledge, unverified]
- **Incentives and constraints**: no single position above 20-25% of any vehicle; consultants must have rated the manager; risk committee needs an independent exceedance model; liquidity terms must state how trapped collateral is handled; career risk is asymmetric (a total loss in a first-time fund is remembered).
- **Alternatives**: catastrophe bonds and existing sidecars with modelled risk; direct equity or debt in the campuses themselves; a data center sleeve from an existing ILS manager (already on offer for 1 January [source, snippet-level, Insurance Insider above]); a risk fund from a large alternative manager whose insurance affiliate already backs a data center syndicate.
- **Decision**: **refuses to anchor.** Will not commit $100M+ to a blind pool run by a first-time team in an unmodelled class.
- **Terms on which a smaller ticket is possible**: $30-50M, no more than 15% of the vehicle; fully funded with limit no more than 1.25x collateral; no line above 10% of net asset value; sponsor or lead reinsurer holds a 10-20% first-loss or pari passu stake; fee no more than 1% of capital, profit share 10% above a hurdle of cash plus 5 points with loss carry-forward; quarterly side-pocket for trapped collateral with a release schedule; target net return of cash plus 7-9 points in a clean year because the risk is unmodelled.
- **Reasons**:
  - The founder's mid case pays 6.4 points over cash against a 22-72% single-event loss [derived]. The panel base case pays 0.4 points.
  - Accumulation is not independent: 40%+ of US capacity in two states, hail and tornado exposure [source above]; serial defects in batteries or liquid cooling could hit several campuses at once [domain knowledge, unverified].
  - Trapped capital: a reported campus loss that might reach the layer freezes that line's collateral, usually with a loading on the reserve, until the claim settles. Large construction and delay claims take 2-5 years. With 5x leverage, one full loss leaves $50M supporting $1.25bn of live limit, so the fronting carrier demands a top-up or cancels, and the remaining capital is locked until the last multi-year construction policy expires. [domain knowledge, unverified; derived]
  - The fund is already long this risk through its credit and equity books ($18bn of one campus's debt sits with one bond manager [notes]).
- **Evidence that would change the decision**: a signed A-rated fronting term sheet; a named lead reinsurer co-investing 20%+; two layers with broker-confirmed terms at a stated rate; a third-party model accepted by the consultant; a team with a 10-year audited engineering-lines record.

### Persona 2. Partner, insurance-focused private equity firm

- **Who**: owns two or three underwriting platforms (a managing general agent group, a Lloyd's business, a Bermuda carrier). Fund return target 20%+ gross. [domain knowledge, unverified]
- **Incentives and constraints**: exits are priced on book value (carriers, 1.2-1.5x) or on earnings (agencies, 12-18x). Start-up carriers need $500M-1bn to obtain an A- rating and take 3 years to reach scale. [domain knowledge, unverified]
- **Alternatives**: add a data center unit to an owned platform that already has paper, licences, broker agreements and a sidecar.
- **Decision**: **refuses to back a start-up carrier. Would do it inside an existing platform.**
- **Terms**: team joins the platform; $5-10M operating budget over 3 years; $150-250M sidecar raised from the firm's own co-investors behind the platform's rated paper; founder team receives 15-20% of the unit's profit pool, vesting over 4 years. No independent company.
- **Reasons**:
  - Inside a platform, first premium is 3-6 months away at a cost of $3-5M a year. Standalone, it is 15-24 months and $25-40M of formation, fronting and capital-raising friction. [domain knowledge, unverified]
  - A $300M unrated vehicle cannot lead; a follower has no pricing power and builds no data.
  - Capacity additions in 2026 (Aon $3.5bn → $5bn, FM $5bn, Stratus $10bn, Fidelis, ATA, Tera) say the price peak is now, before the start-up is licensed. [sources above; notes]
  - Fee income of $1-10M at $300M does not carry a standalone cost base.
- **Evidence that would change the decision**: proof that the team controls flow no platform can get (a signed exclusive with a hyperscaler captive or a top-three developer), or a proprietary loss model that an incumbent lead has agreed to price from.

### Persona 3. Skeptical venture investor, $5-10M seed for the underwriting company

- **Who**: fintech and insurance seed investor. Needs a credible path to a $5bn+ outcome for the fund. [domain knowledge, unverified]
- **Decision**: **refuses.**
- **Reasons**:
  - Fee economics [derived]: 12% of $25-45M is $3.0-5.4M, plus $2-5M of profit share in a clean year. On the panel base case it is $1M. A team of 15-20 underwriters, engineers, actuaries and compliance staff costs $6-10M a year [domain knowledge, unverified].
  - Time to revenue: capital raise 9-18 months, fronting 6-12 months, first bound layer 15-24 months, and earned premium lags written premium on multi-year construction policies. The brief's 9-12 months assumes capital and paper close in parallel with no slippage. [domain knowledge, unverified]
  - The seed is a call option on a $300M raise that persona 1 has just declined.
  - $100M of fee revenue needs $833M of premium, which at 1.5% is $56bn of limit. $100M of consolidated premium needs $3.3-6.7bn of limit. Neither is reachable in 24 months from $300M without 11-22x leverage. [derived]
  - Ceiling: the best-known ILS manager exit was roughly $1bn for roughly $12bn of assets, about 8% of assets [domain knowledge, unverified]. At $3bn that is $250M; at $30bn, $2.4bn. Owning the balance sheet instead gets a book-value multiple. The realistic top is a specialty insurer worth $2-5bn after 8-10 years and several dilutive capital raises.
  - Notes section 8 found no institutional financial infrastructure company that reached $100M of net revenue in 24 months; the stated precedent for a managing agent is $400M-1bn of premium. [notes]
- **Terms that would get a term sheet**: $2-3M at a seed valuation for a capital-light underwriting agency that already holds a signed binder of $250M+ line from an A-rated carrier, a 20-25% commission, and a loss-control product sold to owners and lenders for a fee independent of risk taking.
- **Evidence that would change the decision**: signed capacity, a bound first risk, and a paid loss-control contract.

### Persona 4. Bank, letter-of-credit facility or leverage

- **Who**: insurance and funds finance desk of a bank on the regulators' approved letter-of-credit issuer lists. [domain knowledge, unverified]
- **Constraints**: a letter of credit is a direct credit substitute and carries full capital; credit committee wants diversification, a model and a track record; after the 2023 forged-collateral scandal in collateralized reinsurance, cedents verify every instrument with the issuing bank [domain knowledge, unverified].
- **Decision**: **offers only a fully cash-secured letter of credit. Refuses unsecured or partly secured leverage.**
- **Terms**:
  - Cash-secured: 100-102% cash or Treasury collateral, 35-50bp a year. This is operational convenience and gives no leverage.
  - Conditional alternative: letters of credit against uncalled capital commitments of investors rated A or better, 85-90% advance, 150-200bp, 364-day evergreen, no line above 10% of net asset value. The leverage then sits on the investors' balance sheets, which persona 1 would have to approve.
  - Net asset value loan: no more than 10-15% of value at SOFR+400-500, with a sweep on any reported loss. Not offered in year 1.
- **Reasons**: outcomes are binary per risk; a drawn letter of credit means the loss has occurred and the collateral is gone; no vendor model; one event can be 17-83% of the vehicle; multi-year construction terms outlast a 364-day facility.
- **Evidence that would change the decision**: three years of audited results, a rating, 30+ independent lines none above 5% of capital.

### Persona 5a. Top global reinsurer with an engineering lines book

- **What it has**: about $250M net per project today [source, snippet-level]; decades of construction and machinery loss data; its own risk engineers; its own sidecar platform for third-party capital; it already provides capacity behind GPU value warranties [notes].
- **Rational response**: raise its gross line and cede the increase to its own sidecar, earning an override of 5-10% and a profit share on other people's capital [domain knowledge, unverified]. That is the founder's product, offered to the same investors, with a rated lead and a track record.
- **Decision on the founder**: **will not grant authority and will not front leveraged lines.** Will accept fully collateralized follow capacity on its slips at its price and wording.
- **Effect on price**: every $1bn it adds through a sidecar lands directly in the layers the founder targets.
- **What would change it**: a pricing model demonstrably better than its own on a class where it has the data. The panel sees no route to that from a follow position.

### Persona 5b. Mutual property insurer specialised in highly protected risks

- **What it has**: $5bn per-risk limit; about 1,100 data centers and $250bn of insured value [source, snippet-level]; in-house engineering from design stage; no shareholder return target, with surplus returned to members as premium credits [domain knowledge, unverified].
- **Rational response**: raise the limit again and buy more per-risk reinsurance. It is a price floor.
- **Decision on the founder**: **no authority, no partnership.** Might buy fully funded per-risk reinsurance at its treaty price. Panel estimate of that price for remote layers: no more than 0.5-0.75% rate on line [domain knowledge, unverified].
- **Point on the founder's moat**: the telemetry and loss-control advantage the brief describes already exists here at 1,100 sites.

### Persona 5c. Big brokers' facilities and capital-markets arms

- **What they have**: the facilities ($5bn, $2.7bn and $10bn with 30 capital providers [source]); the client relationship; control of who leads; their own securities arms that place catastrophe bonds and sidecars.
- **Incentive**: more capacity lowers the client's price and raises the broker's share of wallet. Brokerage is 10-15% plus facility fees of 2.5-5% [domain knowledge, unverified].
- **Decision on the founder**: **accepts the capacity as a follower once it sits behind A-rated paper. Refuses to give a new team the pen or a lead position.** Maximum share of any layer 5-10%.
- **Competitive move**: the capital-markets arm structures a sidecar or bond from a facility lead or a hyperscaler captive straight to ILS funds. The start-up reinsurer is not needed for that.
- **What would change it**: nothing gives a newcomer the lead in under 3 years. A unique product the facility lacks (for example a non-damage delay trigger) could get a product-specific line slip.

### Persona 5d. Nvidia or a hyperscaler guaranteeing risk from its own balance sheet

- **Hyperscaler as property buyer**: 2026 capex above $600bn across five companies [notes]. A $5bn uninsured loss is under 1% of the group's annual capex [derived]. It insures to the probable maximum loss of one or two buildings and keeps the rest in a captive; S&P expects more captive use [source: Artemis above].
- **Decision**: **refuses to buy excess property at 1.5-3%.** Would pay no more than 0.3-0.5% a year for limit above $5bn, and only where a lender requires it. [domain knowledge, unverified]
- **Developers and lender-driven projects**: these do buy, because the lender requires it. This is the founder's real market. It is the non-investment-grade half of the buildout.
- **Nvidia on residual value**: already carries a $6.3bn backstop, an option on $125bn and a guaranty of up to $105bn [notes]. It wants to shed risk in $1bn+ tranches to rated counterparties, through a reinsurance broker, to large reinsurers and hedge funds [notes].
- **Decision on the founder**: **does not buy from a $300M unrated vehicle.**
- **Adverse selection**: the seller of the residual value risk sets the product roadmap that determines residual value. Documented used-GPU sales total $26.3M over three years [notes], so there is no loss history to price against.
- **What would change it**: a rated counterparty able to take $1bn+ per transaction at 1-2% a year above a 40-50% first loss kept by Nvidia or the lender. [domain knowledge, unverified]

### Persona 5e. Large alternative asset managers with insurance affiliates

- **What they have**: they own or finance the campuses (one owns 80% of a $30bn project; another holds $18bn of its debt [notes]); one already backs a Lloyd's syndicate adding data center construction capacity [source, snippet-level]; they hold the relationships with the same pensions and sovereign funds; they can raise $3-5bn under their own brand in a quarter [domain knowledge, unverified].
- **Rational response**: enter directly, pairing their capital with an established underwriting agency, and make insurance part of the financing package they already sell.
- **Decision on the founder**: **no investment.** Possible team hire.
- **Effect**: they take persona 1's allocation and they control the insured.

### Persona 6. Aggressive competing start-up (residual value insurer, parametric provider or data center agency)

- **What it already has**: live paper from A- carriers or reinsurer backing; a launched product (parametric residual value cover launched 19 November 2026; a value warranty backed by a top reinsurer; a $750M facility with three named carriers; a $1bn+ hardware programme) [notes; source: ATA above]; broker agreements; licences; some bound policies, volumes undisclosed [notes].
- **Response within 90 days**:
  - Add an excess delay product to the existing binder and announce a capacity increase.
  - Offer the founder's target investors a quota-share sidecar behind an existing book: smaller ticket, existing paper, premium already flowing.
  - Hire the founder's target underwriters and engineers.
  - Sign product exclusives with second-tier brokers.
- **Weakness the founder could exploit**: none of these has disclosed bound premium [notes], and parametric index cover carries basis risk for lenders.
- **Decision on the founder**: competes. Would acquire the team for equity if the founder brings committed capital.

---

## 3. Tests requested

| Test | Finding |
|---|---|
| Capital actually required | To write the brief's $1.5bn of limit responsibly: $1.0-1.5bn fully funded, or about $500M-1bn with an A- rating and lines capped near 5% of capital. $300M supports $300-450M of limit at launch. [domain knowledge, unverified; derived] |
| Leverage of limit to collateral | Founder 5x. Panel 1.0-1.5x at launch, 3x at best. |
| Trapped capital after a loss | Leveraged: effectively 100% of remaining capital for 2-4 years once one full line is lost. Fully funded with $50M lines: about 17% of capital per reported event for 2-5 years. |
| Return in a normal year | Founder case 8-12%. Panel 3.4-5.8% against 3.5% cash. |
| Return after a single-campus loss | Founder case -22% to -74%. Panel -13% to -19%. |
| Fee revenue versus risk revenue | Fee company $0.4-10M at $300M. Risk revenue (premium) $2-45M, which belongs to whoever owns the vehicle. |
| Premium response to new capacity | Per-risk facility limits roughly doubled to tripled in 2026 ($3.5bn → $5bn, $5bn, $10bn). Panel estimate: remote-layer rate on line falls 20-30% for each additional $5bn of per-risk capacity and reaches 0.7-1.5% within 24 months, with a floor near 0.5%. [domain knowledge, unverified] |
| Compounding advantage owned | Loss data: none from remote excess layers, which rarely see a loss. Telemetry: belongs to the owner and contractor, and the mutual already has it at 1,100 sites. Broker position: follower. Capital relationships: shared with every ILS manager. The one ownable asset would be a wording or trigger incumbents do not offer (non-damage delay, residual value), and those carry the correlation and adverse selection problems above. |

---

## 4. Numbers in the brief the panel disputes

| Brief | Panel | Basis |
|---|---|---|
| Layers attach above Aon and Marsh facilities at $2.7-3.5bn | Facilities are now $5bn (Aon), $5bn (FM) and $10bn operational (Marsh Stratus); only construction is still at $2.7-5bn | [source above] |
| Typical limits $1.5-3.5bn | $5-10bn is now described as the conventional single-risk limit | [source above] |
| $300M of collateral writes $1.5bn of limit | $300-450M | [domain knowledge, unverified] |
| Rate on line 1.5-3.0% | 0.6-1.5% annualised, falling | [domain knowledge, unverified] |
| Premium $25-45M | $2-14M, base $4.5M | [derived] |
| Unit is $1M of limit for one year | Construction commits collateral for 30-48 months plus claims run-off | [domain knowledge, unverified] |
| Recognized revenue = earned premium plus fees | Fees only unless the company owns the vehicle; never both | [domain knowledge, unverified] |
| Underwriting company revenue | $1M base, $6-10M on the founder's own assumptions | [derived] |
| First bound layer in 9-12 months | 15-24 months standalone | [domain knowledge, unverified] |
| "Insurers are short of capacity, not customers" | True at the top of the tower for lender-driven projects. Not true of hyperscalers, who self-insure by choice | [source: Artemis]; [domain knowledge, unverified] |
| "Capacity did not grow" | Per-risk facility capacity roughly doubled to tripled during 2026 | [source above] |

---

## 5. Probabilities (panel's honest estimate)

- This version reaches a first paid commercial delivery (a bound layer with premium received) within 18 months: **12%**. Inside an existing platform, as persona 2 offers, the panel would put it near 55%.
- This business reaches $1bn of annual recognized revenue within 7 years: **1%**.
