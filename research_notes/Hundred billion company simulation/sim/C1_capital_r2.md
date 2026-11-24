# C1 v2, capital and competition panel, round 2

Date of simulation: 24 November 2026. Simulated hypotheses from archetype personas. Not validation. No real person was interviewed and no quote is real.

Evidence labels: [notes] = founder research notes; [source: URL] = web search this session (snippet level); [dk] = domain knowledge, unverified; [calc] = my arithmetic on labelled inputs.

Web checks used this round: 5 of 5.

---

## 0. Panel's own numbers

### 0.1 Facts checked this round
- The "open capacity" makers are already selling to US data-center developers in gigawatt lots. HD Hyundai sold 33 HiMSEN gas engines of the 20 MW class (about 684 MW) to Aperion for about $425M in April 2026, and about 1,000 MW of 9.6 MW engines to Corban for about $675M in August 2026 for an unnamed large US technology company. That is $620-675 per kW for engines alone. No delivery dates were found. [source: https://www.datacenterdynamics.com/en/news/hyundai-heavy-industries-inks-684mw-natural-gas-turbine-supply-deal-with-aperion-to-power-us-data-center-market/] [source: https://thenextweb.com/news/hd-hyundai-corban-1000mw-engines-ai-data-centres]
- VoltaGrid's $2.0B second-lien notes due 2030 carry a 7.375% coupon. Its $3.0B revolver is asset-based and limited at all times by a borrowing base. This is the cost of money for the best-contracted fleet owner in the sector, whose anchor customer is investment grade. [source: https://www.sidley.com/en/newslanding/newsannouncements/2025/11/sidley-represents-voltagrid-in-us-2-billion-of-senior-secured-second-lien-notes]
- ProPetro guides $1.4-1.5M per MW including balance of plant; its first 550 MW averaged about $1.1M. Data-center contract talks "begin at terms of 10 years". Oil and gas contracts averaged about five years. Some previously announced oil and gas capacity is no longer under contract. It issued $690M of 0% convertible notes in May 2026. [source: https://www.fool.com/earnings/call-transcripts/2026/08/07/propetro-pump-q2-2026-earnings-call-transcript] [source: https://finviz.com/news/394123/propwr-signs-new-power-contracts-to-commit-approximately-230-megawatts-to-targa-resources-corp]
- Rental companies already sell bridging gas power with batteries in 1-2 MW blocks. No public rate was found. A Modo analysis uses an illustrative all-in price of $125/MWh for reciprocating gas engines at data centers; a vendor blog quotes $1,400-1,800 per kW for installed island-mode systems. [source: https://www.aggreko.com/en-my/sectors/data-centres/bridging-power-solutions] [source: https://modoenergy.com/research/en/us-data-center-onsite-gas-speed-to-power]
- Lenders to behind-the-meter power focus on stranded-asset risk, interruption, construction delay and the interdependence of plant and data center. A third-party-owned plant raises intercreditor problems with the data center's own lenders. A search summary reported a $700M private-credit facility to Crusoe for long-lead gas generators. No advance rate, spread or residual assumption for sub-investment-grade tenants was found anywhere. [source: https://www.ropesgray.com/en/insights/alerts/2026/06/when-power-becomes-part-of-the-capital-stack] [source: https://octus.com/resources/articles/power-islands-tap-high-yield-market-as-ai-data-centers-go-beyond-the-grid/]

### 0.2 Corrections to the founder's economics
| Item | Brief | Panel | Basis |
|---|---|---|---|
| Cost per 25 MW net block | $36.25M ($1.45M per MW) | $44-56M, mid $50M ($1.8-2.2M per net firm MW) | $1.4-1.5M is an incumbent's cost per nameplate MW at 500 MW+ scale [source: ProPetro above]. N+2 on 25 MW adds 20-40% of nameplate (Williams built 275-285 MW for 200 MW net [notes]). The 10 MW / 20 MWh grid-forming battery adds about $7-8M. Add financing cost and interest during construction [dk, calc] |
| Cash margin per block | $6.3-9.4M | $5.4M at $38,000 | Operating cost about $5.8M: service agreement at roughly $15/MWh on about 186 GWh a year, an on-site crew, insurance, emissions consumables, expected damages 1.5% [dk]. Solaris's power segment earned 45% and ProPetro's 34% [notes] |
| Price | $38,000 per MW-month | New small-site contracts clear at $45,000-58,000; panel uses $50,000 | $38,000 is a backlog average dominated by large investment-grade contracts [notes]. Incumbents' stated 4-6 year payback on $1.4-1.5M implies $37,500-48,000 for them [calc]. $125/MWh all-in less about $30 of fuel at 85% load factor is about $58,000 [source: Modo above, calc] |
| Firm contracted revenue | "Seven-year take-or-pay" | Five years of fees, $57M | Exit after year 4 on payment of 12 months [calc] |
| Debt | 55% | 40-45% of cost, about 11% | Section 1 |

### 0.3 Returns per block, seven years, pre-tax [calc]
Residual 25-30% of cost at year 7. Levered case: 45% debt at 11%, five-year tenor, 25% balloon.

| Case | Cash margin | Payback | Unlevered IRR | Levered IRR | Coverage |
|---|---|---|---|---|---|
| Brief price, brief cost, founder's mid margin | $7.85M | 4.6 years | 15.4% | 17.8% (21.4% on the founder's 55% at 9%) | 2.0x |
| Brief price, brief cost, founder's low margin | $6.3M | 5.8 years | 10.0% | 9.5% | 1.7x |
| Brief price, panel cost $50M | $5.4M | 9.2 years | 0.2% | -5% | 1.05x |
| Brief price, panel low cost $44M | $5.6M | 7.8 years | 3.0% | -1% | 1.2x |
| Clearing price $50,000, panel cost $50M | $8.9M | 5.6 years | 9.8% | 9.1% | 1.7x |
| Clearing price $50,000, panel low cost $44M | $9.1M | 4.8 years | 13.5% | 14.9% | 2.0x |

Weighted for tenant behaviour (45% run seven years; 35% release at year 4, nine months idle, $5M relocation; 20% default in year 3, twelve months idle, $5M relocation, six months of security kept):
- Brief price, panel cost: -0.1% unlevered, -5.8% levered.
- Clearing price, panel cost: 8.5% unlevered, 7.1% levered.
- Brief price and cost as the founder states them: 13.6% unlevered, 15.1% levered.

Default costs the owner about $13-16M per event against $5.7M of security [calc]. Borrowing at 11% against an asset yielding 8-10% is negative leverage.

### 0.4 Scale [calc]
Revenue is capacity fees only. Equity is 55% of cost. Enterprise value at 7x cash margin, the range for short-contract equipment owners [dk]; 9x is the investment-grade long-contract range implied by VoltaGrid's reported possible value [notes].

| Revenue | Blocks (at $38,000 / at $50,000) | Capital (brief cost / panel cost) | Equity required | Asset equity value at $38,000, panel cost | Asset equity value at $50,000, panel cost |
|---|---|---|---|---|---|
| $100M | 9 / 7 | $0.32B / $0.33-0.44B | $0.17-0.24B | $0.13B (0.55x paid in) | $0.28B (1.5x) |
| $1B | 88 / 67 | $3.2B / $3.3-4.4B | $1.8-2.4B | $1.3B | $2.8B |
| $10B | 877 / 667 | $32B / $33-44B | $17-24B | $13B | $28B |

What the company itself is worth under the brief's structure (fund owns the blocks, company holds a 10-20% carry and fees):
- $100M: $30-50M. Fee income of roughly $5-8M a year. The carry is worth nothing at $38,000 because the blocks return less than any hurdle.
- $1B: $0.4-0.5B at the clearing price (fees of about $40M a year plus a carry of about $0.14B).
- $10B: $4-5B on paper. Not reachable: 17-22 GW is about ten times all behind-the-meter capacity running in mid-2026 [notes], and the sub-investment-grade 25-150 MW segment is not that large.

Dilution:
- Fund-owned path: seed $7.5M, then about $35M, then about $100M of corporate equity for deposits and letters of credit on 15 concurrent blocks. Founders together hold about 35-40% of the company at $1B of revenue: roughly $150-200M.
- Balance-sheet path (what VoltaGrid did with $1.575B of equity and $5B of debt for 4.3 GW [notes]): $1.8-2.4B of equity at $1B of revenue leaves founders below 10%; below 3% at $10B.

---

## 1. Project finance banker / asset-based lender

**Who.** Same director; also the private-credit asset-based desk.

**Constraints.** No rating-agency method supports term debt against B-rated tenants on a contract with a year-4 exit. Sizing falls back to equipment liquidation value, as in VoltaGrid's borrowing-base revolver [source: Sidley above].

**Decision: refuses 55% non-recourse on cost. Counter-offer:**
- Advance: 60-70% of appraised orderly liquidation value, which is about 40-45% of installed cost because balance of plant, installation and soft costs (35-45% of cost) recover almost nothing on removal [dk].
- Rate: SOFR+650-850, about 10.5-12.5%. VoltaGrid pays 7.375% with an investment-grade anchor [source: Sidley above]; non-investment-grade compute loans priced SOFR+450-500 for an established sponsor [notes].
- Tenor: four to five years, inside the firm period. Full cash sweep. Coverage 1.40-1.50x on fees less operating cost. Balloon no more than 25% of the loan.
- Security: the six months of fees assigned to the lender; the release payment paid to a blocked account; direct agreement with the end tenant and an intercreditor agreement with the data center's lenders [source: Ropes & Gray above].
- Equipment: tier-one engines with a US service network and an active resale market only. Engines without a US installed base get 25-30% of cost or no loan. A marine-derived 9.6-20 MW medium-speed engine on foundations is not relocatable collateral.
- Ticket: one block is a $16-22M loan. Too small. Needs a warehouse of five or more blocks, or private credit.

**At the brief's price and real cost the loan does not size:** coverage is 1.05x [calc].

**Collateral.** Better than round one. Engines have a real secondary market: used and refurbished gas units trade at $1.3-1.7M per MW today [notes]. Three haircuts apply. Prime duty runs about 8,000 hours a year, so an engine has about 32,000 hours at year 4 and reaches major overhaul near 60,000 [dk]. Releases are correlated: grid service arriving in 2029-2031 and new maker capacity in 2028 [notes] put many bridge fleets on the market together. Removal and reinstallation cost about $5M a block [dk].

**Working capital.** Engine deposits of 20-30% of roughly $25M of equipment are $5-7.5M per block, plus permits, gas studies and engineering: $7-10M at risk before close per block. The brief's $5-10M does not cover two blocks. The customer's six months of security arrives at operation, not at signing. [dk, calc]

**What would change the decision.** Tier-one engines; price at $48,000 or more; a fleet of five blocks across at least three tenants; sponsor equity of 55-60%.

---

## 2. Partner, infrastructure / private equity fund

**Alternatives.** Buy into an existing fleet owner with allocation and crews: Blackstone took 49% of five Williams projects and invested in VoltaGrid; Solaris holds part of its fleet in a joint venture [notes].

**Decision: refuses the 45% equity at $38,000.** The fund's model shows 0-3% unlevered at real cost. It would buy blocks at close on these terms:
- Price $48,000-50,000 or higher, tier-one engines, fixed-price build.
- Target return 15-18% for sub-investment-grade tenants. At $50,000 and $50M the fund sees 8.5% unlevered and 7% levered after expected defaults, so it also needs cost at or below $44M.
- Security of twelve months, not six. No release before year 5, or a release payment of 18-24 months.
- Developer carry of 10-15% above a 12% hurdle. At the brief's price that carry never pays.

**What would change the decision.** A delivered, operating first block with measured availability; signed engine allocation with dated slots; a tenant book of five or more names.

---

## 3. Skeptical venture investor

**Decision: refuses.** Not a counter-offer this time unless the founder shows a signed equipment allocation and one signed customer contract with cash security posted.

Reasons:
- This is an equipment leasing company. Its ceiling is 6-8x cash margin less debt. The best outcome in the table is about $0.4-0.5B for the company at $1B of revenue, with founders at 35-40%.
- The company-level income is fees and a carry that is out of the money at the brief's price.
- The seed is spent on engine deposits. If the first tenant fails or the permit slips, the deposit is the loss.
- Round one's question stands: what does the company own that an oilfield-service firm with 2 GW of unsold equipment does not? Answer: nothing.

**Probability-weighted view.** Under 3% chance of a $0.5B company; expected multiple on seed below 1x.

---

## 4. Incumbents

### 4a. Oilfield-service providers with secured, uncontracted engines
- **Position.** One has about 2.6 GW secured and about 510 MW contracted [notes]; oil and gas capacity has come off contract [source: finviz above]. Capital cost $1.4-1.5M per MW with direct Caterpillar allocation; 0% convertible notes and maker finance [source: fool.com above] [notes]. Field crews already employed.
- **Response.** Serves the 25-150 MW sites itself. It already writes five-year contracts for oil and gas customers. Quotes $42,000-50,000 on five to seven years with twelve months of security. It does not need to undercut $38,000: it can deliver in 2027 from equipment in hand and the startup cannot.
- **Why the segment looks underserved.** These providers ration scarce units to the best credit first. That is a queue, not a gap. As maker capacity grows in 2028 [notes] the queue reaches the weak credits.

### 4b. Large behind-the-meter providers (Solaris, VoltaGrid type)
- **Response.** Ignore single 25 MW blocks. Take 100 MW+ sites, including sub-investment-grade tenants where a landlord or chip vendor backstops the lease [notes]. Fund at 7.4% [source: Sidley above] against the startup's 11%.

### 4c. Engine makers' finance arms
- **Decision: refuse the startup as borrower.** They lend against their own brand to fleet owners with balance sheets (one lent $172M to an oilfield-service firm [notes]). To a shell company with a B-rated tenant: 30-40% down and recourse to a parent that does not exist. They will not finance a rival's engine.
- **Korean export credit** could cover 85% of a Korean engine contract [dk], but it underwrites the borrower, so the same refusal applies.

### 4d. Equipment rental companies
- **Position.** Investment-grade balance sheets, national fleets and crews, bridging gas-plus-battery product already on sale [source: Aggreko above].
- **Response.** Rent month to month or for one to three years with no take-or-pay tail, at a higher monthly rate. A tenant unsure whether grid arrives in two years or four prefers that to a seven-year contract with a year-4 exit fee of $11.4M per block.

---

## 5. Aggressive competing start-up

**Archetype.** A developer-intermediary that has already bought non-incumbent engines in bulk: 684 MW and 1,000 MW lots from the Korean maker [source: DCD and TNW above].

- **Has:** equipment under contract, a maker relationship, and in one case a named large technology end customer.
- **Does:** places its own surplus units at mid-size sites, or sells C1 units at a mark-up. Independent equipment brokers earn 12-15% [notes].
- **C1 has that it does not:** nothing. C1 would be buying from, or behind, this competitor.

---

## Round-one objections revisited
| # | Round-one objection | Status | Reason |
|---|---|---|---|
| 1 | Nothing proprietary; incumbent already present | Unresolved | Now against larger incumbents with fleets, crews and allocation. The sourcing idea is already executed by others at GW scale |
| 2 | Price competed to cost | Partly resolved | Gas prime power is supply-constrained through 2028, so price holds. But the brief's $38,000 is below market and below its own cost of capital |
| 3 | Utility will not contract with the startup | Resolved | No utility obligation. Replaced by air-permit and gas-lateral dependence |
| 4 | Long take-or-pay for a short need; only weak credits sign | Partly resolved | Term fits the need. Weak credit is now the design. Firm revenue is five years of fees |
| 5 | Capital does not close; collateral has little value | Partly resolved | Collateral is real. Debt is 40-45% at about 11%. Pre-close cash still exceeds the company's funds |

## New objections created by the redesign
1. Equipment does not fit the product. Available engines are 9.6-20 MW medium-speed units. N+2 on 25 MW needs five 9.6 MW engines, 48 MW installed for 25 MW sold. They sit on foundations, not skids. [source: TNW above] [dk, calc]
2. Cost is $1.8-2.2M per net firm MW, not $1.45M. [calc]
3. The price is too low for the risk taken. At $38,000 and real cost the block returns 0-3% unlevered.
4. Prime duty wears out the collateral the financing relies on, and releases are correlated. [dk]
5. 99.9% availability while islanded on one gas lateral. N+2 does not cover a fuel interruption. Damages cap is $2.85M per block.
6. Air permits for 30 MW+ of engines and a gas interconnect take 6-18 months [dk]; a state blocked a pipeline for a far larger plant [notes].
7. Crews. The oilfield-service firms have them; the startup hires and trains.
8. Tenant default. Roughly one in five B-rated borrowers defaults within five years [dk]. Six months of security covers about 40% of the loss.

## Does anything compound with scale?
Scale economies exist: pooled spares cut the N+2 overbuild, regional crews spread over more sites, a fleet across tenants supports borrowing-base debt, volume earns maker allocation. Every one of these already belongs to owners 10-100 times larger. A mixed fleet of second-tier engines weakens them. Nothing here grows faster than capital deployed. No.

## Probabilities
- First paid commercial delivery within 18 months (by May 2028): 12%. Up from 10%, because no utility consent is needed and refurbished or rental units can start a site.
- $1B of annual recognised revenue within 7 years: 1.5%.
