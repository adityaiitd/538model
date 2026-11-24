# F4 v1 demand and seller panel, round 1 (simulated, 24 Nov 2026)

Brief tested: `F4_v1.md` (hospital payment recovery, entered by buying a small underpayment and denial recovery firm; 18-25% of recoveries; AI agents work every claim; $40M by month 18 and $100M by month 36 through three to four acquisitions plus organic growth).

Everything below is a simulated hypothesis from archetype personas. It is not customer validation. No real people, quotes, interviews or orders.

Evidence labels: [source: URL], [notes] = `contingency_recovery.md` Part B and the first study's C3 panel, [DK] = domain knowledge, unverified.

Web calls used: 6 of 6 (3 searches, 3 page fetches). Gaps that stayed open: no disclosed price or multiple for any 2025-2026 sub-$50M recovery-firm deal; no published contingency percentage in any hospital contract or tender; no primary figure for underpayments recovered by claim-size band. Those are filled with [DK] and flagged.

---

## Facts checked before the panel

| Fact | Value | Label |
|---|---|---|
| Underpayments as share of hospital net patient revenue | 1-3% (HFMA estimate relayed by a vendor); 0.5-1% (R1's analysis, relayed by the same vendor) | [source: https://www.mdclarity.com/comparison/best-healthcare-underpayment-recovery-services] |
| Vendor contingency fees, list | "typically 20 to 35 percent"; most vendors pure contingency, no upfront fee | [source: same], [notes] |
| Vendor-claimed time to first recoveries | Cloudmed "usually within 60 days"; general target 60-90 days from contract execution; under 40 hours of hospital IT time | [source: same] (vendor claims) |
| Secondary-pass yield, one case | 13-hospital, 300-site system on Epic. Prior primary vendor: $1.7M recovered in four years. Secondary vendor: $1.8M from the same claims pool against the primary's $1.0M, and $2.2M in its first nine months. Primary had worked only higher-dollar variances. | [source: https://www.aspirion.com/180-more-revenue-same-claims-more-recoveries-with-our-secondary-zero-balance-review/] (vendor case study) |
| Public hospitals tender this work | A Hawaii public hospital ran a tender for zero-balance account audit; fee is a monthly contingency on cash received from payers on reprocessed accounts | [source: https://www.bidnetdirect.com/hawaii/hilomedicalcenter/solicitations/25-0324-RFP-Zero-Balance-Accounts-Audit-Services/0000379139] |
| Incumbents already sell "AI" | Aspirion markets AI contract modeling on closed accounts at HFMA chapters (May and July 2026); EnableComp bought Helix for technology that finds underpayments rules-based audits miss | [source: https://www.hfma.org/wp-content/uploads/2026/07/therevenuealreadyearned-july2026-aspirion-centralpa.pdf], [source: https://pulse2.com/enablecomp-acquires-helix-advisory-as-platform-recovers-about-3-billion-annually-for-1000-hospitals/] |
| Who is buying small recovery firms | EnableComp (Welsh Carson): H/ROI Jan 2026, Helix Aug 2026. Knowtion Health (Arsenal Capital): Switch RCM. Aspirion (Linden): FIRM RCM. Med-Metrix: Vitalware $147M. All but the last undisclosed. | [source: pulse2 above], [source: https://www.arsenalcapital.com/news/knowtion-acquires-switch-rcm], [notes] |
| Initial denial rate | 11.65% in 2025 to November (11.41% in 2024); first half 2026 10.63% against 12.00%; private payers 19.98% against 21.44% | [source: https://www.hfma.org/revenue-cycle/denials-management/battle-of-the-bots-intensifies-over-denials/]; first-half 2026 figures from search summary of Kodiak coverage at https://www.techtarget.com/revcyclemanagement/news/366651012/Insurers-deny-less-just-to-claw-back-more-later-analysis and https://www.healthcarefinancenews.com/news/lower-denials-do-not-lead-improved-cash-performance-hospitals (pages not individually fetched) |
| Payers deny less and claw back more | Recoveries from appeals on paid accounts fell to 2.21% of receivables in first half 2026 from 2.48%; commercial final denial rate up 9.1% year on year to 2.89%; lower denial rates did not raise provider cash | [source: same search summary, not individually fetched] |
| Overturn rates | About 70% of denials overturned after appeal (Premier); clinical denial overturn 42.1% in 2025, down from 42.7% (Kodiak) | [source: HFMA article above]; [source: search summary] |
| Cost of one appeal | $57.23 per claim (Premier, 2023) | [source: HFMA article above] |
| AI on the provider side | Appeal letter drafting from 15 minutes to 8-10; one large system reports recovery rate up about 15% from AI appeal writing; a nurse reviews 8-10 medical-necessity denials a day against about 3,500 for an agent in the same period | [source: HFMA article above] |
| AI on the payer side | Denials within seconds of submission; payers reviewing smaller claims than before; underpayments such as DRG downgrades and emergency-level reductions now more common than outright denials | [source: HFMA article above] |
| Cloudmed scale | $1.5B recovered in 2021 from 400+ systems including 47 of the top 50; fee revenue about $480-550M a year after the deal | [notes] |
| R1 contract terms | Contingency; one to three years; 30-60 day payment terms; fees booked as contract assets before cash | [notes] |

Panel arithmetic used throughout:
- Acquired firm: $12M of fees on 30 hospitals is $400K per hospital. At a blended 20% that is $60M recovered, $2M per hospital.
- Human break-even on a small balance: $57 an appeal [source] divided by a 20% fee is a $286 variance, or about $410 at a 70% overturn rate. With agents at $10-15 per appeal [DK] the break-even falls to $70-110. The new pool is therefore variances between roughly $75 and $400.

---

## Persona 1. Founder-owner of an underpayment and denial recovery firm, $12M revenue, 30 hospital clients

**Who.** Started the firm 14 years ago after running managed-care contracting at a health system. 62 staff, of which 9 are senior auditors who know the payer contracts. 30 hospitals are 11 legal customers: three systems are 55% of revenue. EBITDA $3.6M (30%) after adding back his own pay. [DK: typical profile]

**Incentives and constraints.** One exit in his life. Wants cash at close, a known buyer, staff kept. Receives two to four inbound calls a quarter from sponsor-backed platforms [DK]; EnableComp alone closed two such purchases in 2026 [notes].

**What he knows that the brief does not.** [DK]
- 9 of 11 contracts are terminable for convenience on 30-90 days. 7 need the hospital's written consent to assign or have a change-of-control notice clause. Every business associate agreement must be re-signed.
- 2025 revenue included $1.4M from one payer settlement project that will not repeat. Underlying revenue is $10.6M.
- Yield per client falls 5-10% a year unless he adds scope, because each finding gets fixed at source by the hospital and the payer.
- His rate has fallen from 25% to a blended 19.5% over six years.

**Alternatives.** Sell to a platform at 8-11x EBITDA with 20-30% rolled into its equity and a second payout at its exit; recapitalise with a minority investor; do nothing and take $3M a year.

**Decision. Refuses** the brief's structure (3-8x, seller note, acquisition debt). **Sells** on his terms only.

**Price and terms.** $36-40M (10-11x EBITDA, about 3.2x revenue). At least 80% cash at close. Seller note no more than 10% of price, secured, 10% coupon, two-year maturity. Earn-out only as an addition above $36M, never as a substitute. Proof of committed funds before exclusivity; no financing condition; 75 days from letter of intent to close. He stays 18 months, not longer. Will not warrant client retention.

**Reason.** A first-time buyer with $5-10M of his own money is a less certain close than a platform with a fund behind it, so the newcomer must pay the same or more, not less. A seller note from a thinly capitalised buyer is a loan to a start-up secured on his own former clients.

**What would change it.** A named institutional equity partner on the letter of intent; a written promise of no staff cuts for 12 months (which conflicts with "three times the claims per analyst"); price parity with the best platform bid. He would take 5% less from a buyer who keeps the name and the people.

---

## Persona 2. Healthcare-services M&A banker (sell-side, lower middle market)

**Who.** Runs four to six revenue-cycle sale processes a year for businesses with $2-15M of EBITDA.

**Who is buying in 2026.** Sponsor-backed platforms: EnableComp (Welsh Carson), Knowtion (Arsenal), Aspirion (Linden), Revecore (GrowthCurve), Med-Metrix [notes, sources above]; plus CorroHealth, Ensemble, R1 (private since 2024), FinThrive, Savista [DK]. New in 2025-2026: funds raised to buy service firms and automate them, and the AI labs' deployment ventures with $5.5B and sponsor portfolios [notes]. A typical process contacts 30-50 buyers and receives 8-15 indications [DK].

**Multiples.** [DK; no disclosed comparables found]
- Under $2M EBITDA, founder-dependent, two clients over half of revenue: 4-6x. These are the 3-8x deals in the notes and they are cheap for a reason.
- $3-5M EBITDA, clean underpayment and denial book: 8-11x.
- $5-15M EBITDA: 10-13x. Technology-led with software revenue: 12-16x.
- Platforms themselves trade at 13-17x, so they can pay 10x and still gain on day one. A stand-alone buyer cannot.

**How many are left.** Independent firms with $8-15M of revenue whose main line is hospital underpayment, zero-balance or denial recovery: 25-40 in the United States. 5-8 change hands in a normal year. Perhaps 3-4 are actually buyable in the next 12 months, and each will be shown to every platform. [DK]

**Debt.** Cash-flow lenders at this size are small-business investment funds and lower-middle-market credit funds: 2.5-3.5x EBITDA, 11-13% all-in, with a customer concentration covenant. At-will contingency revenue sits at the bottom of that range. On $3.6M of EBITDA that is $9-12M. [DK]

**What the founder's capital buys.** One deal at $38M: $10M senior debt, $3.5M seller note, $24.5M equity. The founder's $5-10M is 20-40% of the equity. The rest comes from a sponsor or family office, which makes the founder an independent sponsor with a promote, not an owner.

**Timeline.** Search to letter of intent 3-5 months. Quality-of-earnings, client calls, lender and documents 60-90 days. First close in month 6-9 at the earliest. A second deal of $15-20M revenue ($45-65M price) cannot be financed until the first shows two clean quarters, so it closes in month 15-20. [DK]

**Decision.** Will put the founder on the buyer list only with an equity commitment letter for $20M+. Would advise her client to prefer a platform at the same price.

**What would change it.** Committed fund capital, a signed operating chief executive from the sector, and willingness to pay 10x.

---

## Persona 3. Vice president of revenue cycle, five-hospital system, existing client of the acquired firm

**Who.** $1.2B net patient revenue, Epic. The acquired firm is her primary zero-balance underpayment vendor at 20%, recovering about $4.0M a year, so she pays it $800K (6.7% of its revenue). She also has an aged-denials vendor at 14%, a complex-claims vendor (workers' compensation, veterans, motor vehicle) at 18%, and a transfer-DRG vendor. Four contingency vendors in total. [DK]

**Incentives.** Net revenue, cost to collect, and a board directive since the 2024 clearinghouse breach to cut the number of vendors holding patient data [notes, C3 persona 6].

**Does she keep the vendor after a change of owner?** Yes, for now. She does not terminate on the news. She uses the consent-to-assign clause as leverage.

**Decision. Keeps, conditionally. Does not expand to denials.**

**Terms.**
- Consent to assignment in exchange for a rate cut from 20% to 17% and a fresh 12-month term with 60-day termination for convenience.
- The two named senior auditors on her account stay for 12 months, or she may terminate on 15 days.
- No AI processing of her data until information security clears the new owner (persona 8).
- Small balances: a six-month pilot on variances under $250 for two payers approved by contracting (persona 7), at 17%, not at a premium.
- Denials stay with the current vendor at 14% and her 11-person internal team.

**Arithmetic for the vendor.** Rate cut costs $120K. Small-balance pilot might add $0.4-0.6M of recoveries, $70-100K of fees. Net: flat to slightly down.

**Probability she is still a client 12 months after close.** 80% if the auditors stay; 50% if either leaves; she rebids the slot at month 12 regardless. [panel estimate]

**What would change it.** To expand scope she wants proof on her own data: a no-fee parallel run showing 15%+ more dollars than the current process on the same accounts.

---

## Persona 4. Chief financial officer, $3bn health system using a large recovery vendor

**Who.** 14 hospitals, Epic, in-house underpayment team of 12 working accounts for the first 60 days after zero balance. Primary vendor is one of the three largest, at 13% on underpayments. Secondary vendor at 20% receives accounts 6 months after the primary closes them. Timely-filing and dispute windows in her payer contracts are 12-18 months. [DK]

**Sequence she runs.** Internal (days 0-60) → primary (months 2-8) → secondary (months 8-14) → occasional third pass before the window shuts. Separate vendors for denials, complex claims, transfer DRG and coding validation. Seven contingency vendors in all, and procurement has told her to get to five. [DK]

**Rates she pays.** Primary 13%, secondary 20%, third pass 22-25%. Each renewal has come down 1-2 points. [DK]

**Decision. Does not replace the primary. Does not give the secondary slot.** Signs a newcomer only for a **third-pass placement**: accounts closed more than nine months and already passed by both vendors, plus variances under $300 that neither vendor works.

**Terms.** 20% (she will not pay 25% to a firm whose pitch is that its cost per claim is lower). 12 months, 30-day termination, non-exclusive. Vendor-risk review and contracting take 5-7 months before any data moves. Monthly invoicing on cash posted, net 45.

**Expected yield.** $2-3.5M of recoveries a year, $0.4-0.7M of fees. The Aspirion case shows the scale: a second pass at a 13-hospital system produced $2.2M in nine months [source].

**Reason.** Her incumbent has 400+ systems of payer-behaviour data [notes] and a balance sheet. A $12M firm under a new owner is a vendor-risk finding. She will also ask the incumbent to drop its dollar threshold now that it uses agents too, which costs her nothing.

**What would change it.** Secondary slot at the next tender (18 months out) if the third pass beats the incumbent secondary's dollars per account by 25% for two quarters. Primary slot: not available to a firm under $100M of revenue.

---

## Persona 5. Revenue cycle director, 200-bed independent hospital, no underpayment vendor

**Who.** $280M net patient revenue, Meditech, 38 billing staff, one contract analyst who keeps rates in spreadsheets. No contract modeling in the billing system. Chief financial officer signs; no committee. [DK]

**Why no vendor today.** A previous vendor left in 2022 after the easy findings ran out, and extracting remittance files takes her one IT analyst who is always busy. She gets a vendor call most weeks. [DK]

**Decision. Signs as a new client, primary placement.** This is the fastest yes on the panel.

**Terms.** 22% on the first-pass lookback (18 months of closed accounts), stepping to 18% on current flow from month 13. Two-year term, 60-day termination for convenience. Fee due only on cash posted. Vendor builds the contract model from her PDFs at its own cost.

**Timing.** First meeting to signature 2-4 months. Security questionnaire and data extract 6-10 weeks. First findings 30-45 days after data. Payer reprocessing 30-90 days. Vendor's invoice paid net 45. **Signature to vendor's first cash: 4-6 months. Steady run rate: month 9-12.** [DK; vendor claims of 60-90 days in sources above refer to first recoveries posted to the hospital, not vendor cash]

**Yield.** Underpayments at 0.5-1% of net revenue [source] is $1.4-2.8M a year. First-year recoveries with the lookback: $2.5-3.5M, fee $0.55-0.75M. From year two: $1.2-1.6M recovered, fee $0.22-0.29M.

**Reason.** She has no leverage and no alternative capacity; contingency costs her nothing up front. Owner identity matters little to her. References from two hospitals on Meditech matter.

**What would change it to no.** A request for more than 20 hours of her IT analyst, or any up-front fee.

---

## Persona 6. Chief financial officer, large surgical-center operator and affiliated physician group

**Who.** 60 surgery centers and 400 physicians, $900M collections. Central business office with a six-person payer-compliance team. Payment is by fee schedule and case rate with implant carve-outs. [DK]

**Economics.** Fee-schedule underpayments are a table lookup. Subscription software does it [source: MD Clarity page lists software-with-service options]. Average variance per claim is $40-150 outside implants [DK]. Implant and high-cost-supply carve-outs are the only large-dollar category.

**Decision. Refuses** a standing contingency contract on the whole book: he would be paying 20-25% of money his own team mostly collects. **Signs one limited engagement:** a one-time 24-month lookback on implant carve-outs and the top three commercial payers.

**Terms.** 18% of cash recovered, fee capped at $400K, 9 months, no renewal clause. Ongoing detection he buys as software at a flat fee, $150-300K a year.

**Reason.** Small average balances, simple contracts, in-house capability. A percentage is the wrong price for a lookup.

**What would change it.** A flat-fee product. That is a software sale, not this business.

---

## Persona 7. Managed-care contracting director (same system as persona 3)

**Who.** Negotiates and holds the 40-odd payer contracts. Maintains the Epic contract model. Every underpayment the vendor finds is either a payer error or her team's modelling error.

**Constraints.** [DK]
- Payer contracts are confidential. Disclosure to an agent is allowed under equivalent confidentiality. Nothing permits use of her rates to benchmark other hospitals or to train a shared model.
- Contract dispute clauses set a window (90-365 days from remittance), a form, and a channel. Several require disputes one claim at a time through the payer portal; two allow bulk "projects" by spreadsheet. Three contracts require meet-and-confer before mass disputes, then arbitration.
- Two of her five largest payers are in renewal talks in 2027. A flood of small-balance appeals in the hospital's name during talks is something she must control.

**Decision. Does not veto the change of owner. Restricts scope.**

**Terms.**
- She chooses which payers are placed. The two in renewal are excluded from small-balance mass appeals; findings on them come to her as a list to use at the table.
- Settlement authority stays with her. If she settles a bulk project at 65 cents, the vendor's fee is on cash received.
- Monthly root-cause report. Once a root cause is fixed, later claims are not vendor-fee-eligible.
- Contract terms are not to leave the vendor's tenant for her system, and are not used for any other client.

**Effect on the vendor.** 25-35% of the small-balance pool is off limits or converted to a negotiated settlement in year one. The root-cause clause is what makes yield decay 5-10% a year. [panel estimate]

**What would change it.** Nothing on the renewal payers. On the rest, a clean six-month record with no payer complaints.

---

## Persona 8. Compliance and information-security lead (same system)

**Who.** Runs vendor risk and privacy. A veto, not a vote.

**Findings on a change of owner plus an AI rollout.** [DK unless marked]
1. Change of control triggers a full vendor re-assessment: new business associate agreement, new sub-processor list, new insurance certificates. 8-12 weeks.
2. The acquired firm's security attestation covers its current process. Agent-based processing with a model provider is a new system: she needs a SOC 2 Type II report that covers it (6-12 months of operating history [notes, C3 persona 6]), zero retention and no training on patient or contract data, and a penetration test.
3. Offshore: US-only for data and human reviewers. Medicare Advantage plans require offshore attestations and some states restrict storage abroad [notes, C3]. If the acquired firm's margin depends on an offshore team, that team cannot touch her accounts.
4. Appeals go out under the hospital's name and identifiers. She requires a human sign-off on every clinical appeal and a 5% monthly audit of contract-variance appeals. A fabricated citation in an appeal is the hospital's misstatement to a payer.
5. Payer portals: shared credentials and automated access breach most portal terms [notes, C3]. The vendor must use its own delegated accounts, which each payer issues in 2-6 weeks and can revoke.
6. Liability: uncapped for breach, $10M cyber and $5M errors-and-omissions cover.

**Decision. Allows the existing manual service to continue under an interim consent. Blocks agent processing** until items 1-5 clear: 3-6 months per client after close.

**Effect.** "Three times the claims per analyst" does not start at close. Across 11 customers with different review queues, full rollout takes 6-12 months. [panel estimate]

**What would change it.** A current Type II report and HITRUST certificate at the buyer level that already cover the agent system, obtained before the acquisition.

---

## Persona 9. Vice president of payment integrity, large commercial insurer

**Who.** Owns pre-pay editing, post-pay audit and provider dispute operations. Measured on medical cost savings and on administrative cost per dispute.

**What he sees in 2026.** Dispute volume from providers up 20-30% a year, most of it machine-written [DK]. His own side auto-adjudicates within seconds and reviews smaller claims than before [source: HFMA article].

**How he responds to a vendor appealing every underpayment with agents.**
1. **Pays what is owed, then closes the hole.** A true contract-configuration variance is paid at 85-90% within 45-90 days: state prompt-pay law and the contract leave little choice [DK]. The configuration is corrected within one or two quarters, so that error produces no further vendor fees.
2. **Channels volume.** Disputes must come through the portal or dispute interface in structured form, one claim each, inside the window. Non-conforming submissions are rejected without review. Portal terms bar automated access and shared logins; delegated accounts that flood the queue are throttled or revoked. [DK]
3. **Converts bulk to projects and settles.** Thousands of sub-$300 disputes on one root cause become a single project settled at 60-75 cents, in exchange for a release. [DK]
4. **Defends the clinical dollars.** DRG downgrades, level-of-care and medical-necessity disputes are where the money is. Machine-written appeals there are answered by machine; overturn runs near 42% [source: search summary], not the 70% seen across all denials [source: HFMA article].
5. **Shifts to post-pay.** Fewer front-end denials, more audits and offsets after payment. Provider recoveries from appeals on paid accounts fell from 2.48% to 2.21% of receivables in a year while denial rates also fell [source: search summary]. A provider that disputes everything moves up his audit selection list.
6. **Rewrites the contract at renewal.** Dispute window cut from 180 to 90 days; mutual 12-month lookback; a de minimis threshold ($25-50) below which neither side adjusts; mandatory meet-and-confer before bulk disputes. [DK]

**Net effect he expects.** Agents raise the vendor's gross recoveries on his book by 5-10% in the first year. The gain decays within 12-18 months as configuration fixes, settlement discounts and contract language take effect. [panel estimate]

**Decision.** Not a buyer. **Opposes, within the law.** He cannot refuse valid contract variances.

**What would change it.** Nothing commercial. A regulator-mandated electronic dispute standard would remove his channel controls.

---

## Cross-persona answers to the six test questions

**1. Does a hospital keep a vendor after a change of owner?**
Mostly yes for 12 months, at a price. Expected first-year effect on a $12M book [panel estimate]:
- Logo retention 85-90% if the seller and senior auditors stay; 65-75% if they do not.
- Rate concessions of 2-3 points on the 60-70% of revenue where consent is needed: -8% to -10% of revenue.
- One non-repeating project in the seller's base year: -$1.4M in persona 1's case.
- Net: an acquired "$12M" is $9.5-11M of repeatable revenue in the first 12 months before any growth.

**2. Contingency rates today and direction.** [DK; list rates 20-35% per notes and source]

| Placement | Small independent | Mid system | Large system ($3bn+) |
|---|---|---|---|
| Underpayment, primary | 20-25% | 17-20% | 12-15% |
| Underpayment, secondary | n/a | 20-25% | 18-22% |
| Third pass, small balance | n/a | 22-28% | 20-25% |
| Aged denials | 15-18% | 12-15% | 10-14% |
| Complex claims | 20-25% | 18-22% | 15-20% |

Direction: down 1-2 points per renewal. Agents lower every vendor's cost, hospitals know it, and persona 4 refuses a premium for small balances. Blended realised rate for a growing book: 16-19%, not 18-25%.

**3. How many vendors in sequence, and where a newcomer starts.**
Large systems: internal team, then primary, secondary and sometimes a third pass on underpayments, with separate vendors for denials, complex claims, transfer DRG and coding: 4-7 contingency vendors. Mid systems: 3-4. Independents: 0-2. A newcomer starts at third pass in large systems, secondary in mid systems, primary only at independents. An acquirer inherits the seller's slots, which is the real asset bought.

**4. Signing to first cash.**
Independent: 4-6 months from signature, 6-10 months from first meeting. Large system: 5-7 months of review before data moves, then 3-4 months; 9-14 months from first meeting. Existing client, new scope: 3-6 months because of the security re-review. Steady run rate at month 9-12 after signature.

**5. How much more is recovered by working small balances.**
- Against a competent primary that works down to $250-400: +10-20% of dollars, on 3-5 times the claim count. Variances of $75-400 are 60-70% of underpaid claims and 8-15% of underpaid dollars. [DK]
- Against a primary that only works large variances: +80% on the same pool in the one case found [source: Aspirion], a vendor's best example.
- After personas 7 and 9 (excluded payers, settlements at 60-75 cents, root-cause fixes): a durable +8-12% in year one, less after.
- On a $12M book that is $1.0-1.5M of fees, not the $8M of organic growth in the brief.

**6. Clients and recovered dollars for $40M of fees.**
- At a realised 18%: **$222M recovered a year**. At 16%: $250M. At 20%: $200M.
- At the acquired firm's yield of $400K per hospital: **100 hospitals** (about 35-40 customers).
- As secondary or third pass at $0.5-0.7M per multi-hospital system: **55-80 systems**.
- As primary at independents ($0.25-0.3M a year after the lookback): 130-160 hospitals.
- In net patient revenue: Cloudmed recovered about 0.2-0.25% of the revenue of its client base ($1.5B on 400+ systems [notes], revenue base my estimate). At 0.2-0.7%, $222M needs **$32-110B of hospital net revenue under contract**, roughly 2-8% of all US hospital revenue [DK for the national total of about $1.4T].

---

## Numbers in the brief disputed

| Brief | Panel's corrected value | Basis |
|---|---|---|
| Buy at 3-8x EBITDA, "roughly $15-40M" | 8-11x for a clean $3-5M EBITDA book: $30-40M for $12M of revenue. 3-6x buys concentrated, founder-dependent books. The brief's own range is also inconsistent: 3-8x of $3.6M is $11-29M. | Personas 1 and 2 [DK]; platforms trade at 13-17x and five are bidding [notes, sources] |
| Funded by founder's $5-10M, seller note and acquisition debt | Debt 2.5-3.5x EBITDA ($9-12M); seller note at most 10% of price; equity needed $22-26M per deal | Persona 2 [DK] |
| Price 18-25% of recoveries | 16-19% blended realised; 12-15% for large-system primary; falling 1-2 points per renewal | Rate table above [DK]; first study found 10-15% for aged denials [notes] |
| "About $12M acquired" | $9.5-11M repeatable in the first 12 months after rate concessions, attrition and one-off projects | Personas 1, 3 [panel estimate] |
| Organic growth from $12M to $20M | $11-14M at month 12 after close. Small balances add $1.0-1.5M; cross-sell to existing clients is blocked by incumbents in the other slots | Personas 3, 4, 7, 8 |
| Three times the claims per analyst after closing | Starts 3-6 months after close per client, complete in 6-12 months; claims per analyst triple, dollars rise 10-20% | Persona 8; small-balance arithmetic |
| Second acquisition of $15-20M in time for month 18 | Closes month 15-20 at $45-65M; contributes 0-3 months of recognised revenue by month 18 | Persona 2 [DK] |
| $40M by month 18 | Trailing-twelve-month recognised revenue at month 18: $12-20M. Run rate at month 18 if both deals close: $25-32M | Close dates; revenue counts only after close |
| $100M by month 36 from three to four acquisitions | Needs $65-80M of acquired revenue at about 3x revenue: $200-240M of purchases, $110-140M of equity. There are 25-40 such firms and five platforms buying them | Persona 2 [DK] |
| Cloudmed and R1 as precedents | Cloudmed was itself a ten-year roll-up of 400+ systems sold at the 2022 peak; R1's $119M to $690M was that purchase, not organic growth | [notes] |
| Sales cycle 6-12 months | Holds for mid and large systems; add 4-7 months from signature to first cash. Independents 2-4 months plus 4-6 | Personas 4, 5 |
| AI raises recoveries | +5-10% gross on a given payer in year one, decaying within 12-18 months; incumbents already deploy the same tools | Persona 9; [sources: HFMA, Aspirion, EnableComp] |

---

## Is this a product company or an outsourcer?

Outsourcer. Every persona priced it as labour on contingency: hospitals demanded lower rates when told the cost per claim had fallen, the seller valued it on EBITDA, the lender on EBITDA, and the banker placed it at 8-13x EBITDA. The only software-like buyer (persona 6) wanted a flat fee instead. The scarce inputs belong to others: the payer contract belongs to persona 7, the dispute channel to persona 9, the client relationship to the seller's auditors.

---

## Panel probabilities and year-five view

- **First paid commercial delivery within 9 months: 50%.** Two routes: close an acquisition by month 9 (40-45%: needs a willing seller at 10x, $20M+ of outside equity and a lender inside one cycle), or sign an independent hospital organically and receive cash by month 9 (15%, since signature plus 4-6 months leaves 3-5 months to sell with no track record).
- **$40M of gross recognised revenue in a trailing twelve months by month 18: 4%.** It requires roughly $40M of revenue acquired and closed by month 6, about $120M of purchases.
- **$100M by month 36: 6%.** Possible only as a sponsor-funded roll-up winning 4-6 auctions against five established platforms.
- **Year five if it works.** Revenue $90-120M. Gross margin 45-55%; EBITDA margin 22-28% ($22-30M). Enterprise value 11-14x EBITDA: $280-420M. Net debt $90-130M. Equity $180-300M, of which the founder holds 20-35% after outside equity: $40-100M.
- **Revenue type.** Contingency fees under one-to-three-year contracts that are terminable for convenience on 30-90 days. It repeats but is re-earned each month from new payer errors; nothing is contracted as a minimum. First-pass lookbacks at new clients are one-off (persona 5's year-one fee is about 2.5 times the later run rate).
