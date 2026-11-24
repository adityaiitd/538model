# C7 v1 demand panel, round 1: free AI research assistant for advisers, paid by product sponsors

Date of simulation: 24 November 2026. Everything below is a simulated hypothesis built from the research notes, eight web checks and domain knowledge. It is not customer validation. No real person, quote or order appears.

Evidence labels: [notes] = founder's research notes; [source: Sx] = checked this session, URL in the list below; [DK] = domain knowledge, unverified.

Web checks used: 8 of 8.
- S1: https://www.wealthmanagement.com/insights-analysis/cerulli-advisor-headcount-stagnates (search snippet: Cerulli headcount 283,137 at end-2023, +0.2% over a decade)
- S2: https://www.investmentnews.com/transformation/advisors-lean-on-outsourced-models-as-ai-adoption-surges/268136 (fetched: Escalent 2026 Advisor Brandscape, published 9 Sept 2026)
- S3: InvestmentNews search snippets citing Cerulli: independent plus hybrid RIA share of headcount rose from about 20% to 31% between 2014 and 2024; 18% of advisers and 13% of adviser-managed assets in model portfolios at end-2023. Snippet level, exact article not opened.
- S4: https://informaconnect.com/wealthmanagement/targeted-lead-gen/ (snippet: a trade publisher sells cost-per-lead content syndication to this audience). Marketing-vendor benchmarks in the same search: about $72 per qualified lead for a financial webinar, $25-75 typical, $800+ per lead at a trade show. Vendor-authored, not specific to asset managers.
- S5: https://finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai and https://americanbar.org/groups/business_law/resources/business-law-today/2026-june/ai-prompts-responses-records-or-not-here-we-come (snippets: firms are responsible for communications whether or not AI wrote them; whether prompts and responses are records is not settled)
- S6: https://www.kitces.com/blog/the-latest-in-financial-advisortech-january-2026-finny-ai-prospecting-tools-charles-schwab-zeplyn-nevis-chatgpt/ and https://www.wealthmanagement.com/financial-technology/ai-powered-financial-research-assistant-brightwave-raises-6m-in-seed-funding (snippets: existing adviser AI tools; a lab has a financial-services version of its assistant; no sponsor-funded free tool found)
- S7: https://www.morningstar.com/business/insights/blog/evergreen-fund-landscape-q3-2026 and https://www.fundssociety.com/en/news/alternatives/private-wealth-in-the-spotlight-as-the-alternative-assets-industry-booms/ (snippets: US evergreen funds above $650bn in 2026; one large manager raised $43bn from private wealth in 2025, +53%)
- Two searches for wholesaler cost and distribution spend returned no usable figure. All wholesaler, platform-fee and trade-media numbers below are therefore [DK].

---

## 0. Shared facts the personas rely on

### 0.1 What asset managers spend to reach advisers, by budget line

| Budget line | Industry size per year | Unit price | Who owns it | Label |
|---|---|---|---|---|
| External and internal wholesalers | $8-12bn (about 7,000-8,000 externals) | $600K-1M fully loaded per external; $400-1,000 per in-person meeting; $40-80 per internal-desk call | Head of sales | [DK] |
| Platform fees, revenue sharing, "data and analytics" fees paid to broker-dealers and custodians | $5bn+ | Up to 10-16 bps of assets on platform plus flat fees of $100K-1M+ per distributor | National accounts | [DK] |
| Conferences and home-office events | $0.5-1bn | $25K-250K per sponsorship; about $800+ per lead | Marketing and sales | [DK]; lead figure [source: S4] |
| Trade media, digital advertising, sponsored content, webinars to advisers | $0.4-0.7bn | $100-300 CPM on verified adviser audiences; $50-150 per named lead; $75-200 per webinar registrant | Marketing | [DK]; CPL range consistent with [source: S4] |
| Adviser and flow data purchases | $0.3-0.6bn | $100K-1M+ per manager per vendor | Sales operations | [DK] |
| Upfront placement fees on private funds sold to individuals | Several $bn | 1-3.5% at wirehouses and broker-dealers; 0% on the advisory share class used by fee-only advisers | Paid to the firm that owns the client | [DK] |

The product as described draws on line 4 (well under $1bn in total) and a slice of line 5. It does not reach lines 1, 2 or 6 without becoming a broker-dealer and a platform.

### 0.2 Who actually selects products

- Advisers in the US: 283,137 at end-2023, flat for a decade [source: S1]. About 290,000 today [DK].
- Independent plus hybrid RIA: 31% of headcount [source: S3], so about 88,000-90,000. Pure independent RIA about 40,000-45,000 [DK].
- 54% of advisers use asset-manager model portfolios, 35% use third-party models; self-built is still the most common method but fell in 2026; under-45 advisers who always or often use manager models rose from 20% to 29% in two years [source: S2].
- Advisers spend 34% of their time on portfolio construction and 59% on clients [source: S2].
- Panel estimate of who holds the pen: about 90,000-100,000 advisers build their own portfolios in some form. Of these, 40,000-50,000 sit at broker-dealers and may only choose from a home-office approved list. In the RIA channel, selection at firms above $1bn is done by a chief investment officer or committee. Net: about 20,000-25,000 real decision units free of a gatekeeper, plus a few thousand home-office analysts and model builders who direct most flows and whom asset managers already cover by name. [DK]

### 0.3 The comparison case

- OpenEvidence: about $300M annualized in July 2026, more than 65% of US physicians monthly, $1,000+ CPM, about 5% of inventory sold, about 20M consultations a month in January 2026 [notes]. On roughly 1.05M physicians [DK], that is about 680,000 monthly users and about $440 per monthly user per year (arithmetic on [notes]).
- The founder's own target (50,000 weekly advisers, $100M) needs $2,000 per weekly user per year, 4.5 times the comparison case.
- The notes' figures do not reconcile: 240M consultations a year at 5% sold and $1,000 CPM is $12M, not $150-300M. Either CPMs or volumes are far higher than stated, or the figures are loose. They are Sacra estimates, not filings [notes]. The comparison is weaker evidence than the brief treats it as.
- Differences that matter [DK]: a physician asks clinical questions many times a day, an adviser adds two to four new products a year; pharma has no way to pay the hospital for shelf space, asset managers do and do; a branded drug carries 80%+ gross margin, an ETF earns 3-20 bps; no home office stands between a physician and a prescription.
- Value of one adopting adviser to a sponsor [DK]: 3% of a $150M book is $4.5M. For an evergreen private fund at about 1.25% plus incentive that is $70-110K a year. For a 10 bp ETF it is $4,500 a year. So attention is physician-grade only for about 30-40 alternative managers, and their bottleneck is platform approval, not awareness.

### 0.4 Realistic sponsor revenue per active adviser (panel estimate, [DK])

| Stage | Weekly verified advisers | Sponsor revenue per weekly adviser per year | Revenue |
|---|---|---|---|
| Month 18 | 5,000-12,000 | $50-150 | $0.5-2M |
| Year 3-4 | 30,000-40,000 | $200-400 | $6-16M |
| Maturity, media only | 100,000-150,000 | $400-600 | $40-90M |

Basis: sponsors on this panel pay $60-125 for a named, opted-in lead and $5-15 for an anonymous engagement; an adviser generates 3-8 named engagements a year; demand is capped by 40-60 sponsors with budgets of $100-400K each, not by inventory.

---

## Paying side

### 1. Head of US wealth distribution, large alternative manager

- Incentives: raise $10-40bn a year from individuals; keep redemption queues down after Q1 2026, when requests at the 12 largest non-traded BDCs averaged 12.1% against 5% gates [notes]. Runs a 200-400 person private-wealth team costing $150-300M a year [DK].
- Constraints: an adviser can only buy a fund that the home office or custodian has approved and that has a subscription path through an alternatives platform. Drawdown funds offered under the no-solicitation exemption cannot be advertised.
- Alternatives: own wholesalers; education programmes on the two large alternatives platforms (which carry continuing-education credit and sit next to the order ticket); conferences.
- Decision: **paid test. Refuses an annual package.**
- Terms: $100K for two quarters, quarterly cancel. Starts only when the tool has 3,000+ verified weekly advisers. Registered evergreen vehicles only. Pays $25-40 per named, opted-in engagement of 60 seconds or more, and only for advisers whose firm already has the fund approved. Pays $0 for advisers who cannot buy.
- Reasons: budget exists for adviser education. But a tool that writes due-diligence memos on private funds will show gates, fee loads and payment-in-kind income. "I am being asked to fund the thing that scores me." If the answers stay honest, sponsoring buys little goodwill. If sponsorship softens them, advisers leave.
- Changes the decision: 15,000+ weekly advisers of whom 40%+ are at firms where the fund is approved; evidence that engaged advisers subscribed (matched by registration number against transfer-agent records). Then $400-600K a year.

### 2. Head of ETF marketing, top-ten fund manager

- Incentives: flows and brand at lowest cost per dollar gathered. US adviser digital and trade budget of $20-50M [DK].
- Constraints: a 10 bp product earns $1,000 a year per $1M allocated. Custodian omnibus accounts hide which RIA bought, so attribution is weak.
- Alternatives: trade publishers and an ETF data-and-media firm that already sell verified adviser impressions, leads and engagement data; paid placement in model marketplaces; custodian programmes.
- Decision: **paid test from the experimental media budget.**
- Terms: $50-75K for one quarter at $150-300 CPM on verified impressions, or $60-100 per opted-in named lead. Will not pay $40-150 for an "engagement" that is an impression or a click.
- Reasons: 54% of advisers now use manager models [source: S2]. The buyer who matters is the model builder, and that person is already covered. Individual-adviser attention for ETFs is cheap and plentiful.
- What they would pay more for: the intent data. $100-250K a year for weekly aggregated query trends by channel and firm size once the audience passes 20,000 advisers. This competes with existing data purchases, not media.
- Changes the decision: audience of 20,000+ and a holdout test showing lift in flows at firm level. Ceiling then $250-400K a year, not $1-2M.

### 3. National sales manager, mid-size active manager with shrinking wholesaler force

- Incentives: cover RIA territories that 25 externals can no longer reach (down from 40). Paid on gross sales.
- Constraints: firm in net outflow; does not own the marketing budget; can redirect one vacant wholesaler seat worth $600-800K [DK].
- Alternatives: internal desk with purchased adviser data; trade-publisher lead programmes; hybrid wholesalers.
- Decision: **signs a paid test.** The most willing payer on the panel.
- Terms: $60K for six months, or $75-125 per lead, where a lead is name, registration number, firm, assets and the question asked. Year two up to $250K if leads produce $50M+ of trackable gross sales.
- Reasons: a named adviser with stated intent is worth more to an inside desk than a webinar registrant.
- Refuses if: leads are anonymous or aggregated. "Without the name I cannot call anyone, and then it is just advertising, which is not my budget."
- Note: this buyer's terms require the exact data practice that personas 7, 9 and 10 refuse.

### 4. Chief marketing officer, annuity and life carrier

- Incentives: sales through independent marketing organisations, broker-dealers and banks, paid by commission of 1-7% [DK].
- Constraints: content must pass insurance advertising rules state by state, and communications rules for registered products. Producers are identified by a national producer number, not the registration number the tool verifies.
- Alternatives: marketing organisations, carrier wholesalers, a commission-free annuity platform for fee-only advisers, rate-comparison data vendors.
- Decision: **refuses.**
- Reasons: the launch audience (fee-only independent RIAs) writes under 5% of annuity sales [DK] and is hostile to commissioned product. No audience, no spend.
- Changes the decision: 10,000+ verified insurance-licensed producers and broker-dealer reps using it weekly. Then a $25-50K test.

### 5. Finance chief of the asset manager

- Incentives: distribution cost per dollar of gross sales. Benchmark: a wholesaler at $600K-1M produces $150-400M of gross sales, so 20-40 bps [DK].
- Constraints: a new vendor above $250K needs procurement, vendor-risk review and a business case. No net-new budget line. 83% of enterprises converted fewer than half of AI pilots to production, and 77% re-evaluate vendors at least every six months [notes].
- Decision: **approves tests up to $100K from the existing marketing line, cancellable quarterly. Refuses $1M annual.**
- Arithmetic given: a $1M package must show $250-500M of attributable gross sales to match a wholesaler. With 100 sponsors sharing the audience, each holds about 1% of attention. No sponsor can reach that.
- Measurement required: engagement reported by adviser registration number so it can be matched to sales and transfer-agent data. Aggregate reach numbers are not accepted.
- Preferred model: pay on outcome. Outcome-based pricing is what enterprise buyers most want and least often get [notes]. Would pay 10-25 bps on subscribed dollars, but only to a registered broker-dealer under a selling agreement, and only if it replaces an existing platform fee instead of adding to it.

### 6. Chief compliance officer of the asset manager

- Permits [DK]: static, pre-approved, clearly labelled units shown only to verified professionals, treated as institutional communications, with controls against forwarding to the public. Registered funds only, with performance shown under fund advertising rules.
- Refuses [DK]:
  - Any sponsor influence on the AI answer, its ranking or which funds it names. If the firm pays and the generated text describes its fund, the text can be attributed to the firm, and nobody can pre-review generated text. Firms are responsible for communications whether or not AI wrote them [source: S5].
  - Sponsor content inside "client-ready explanations". That is a retail communication with filing requirements.
  - Any promotion of funds sold under the no-solicitation exemption. Only registered vehicles or offerings that permit general solicitation.
  - Per-subscription payments to anyone who is not a registered broker-dealer. For non-traded REITs and BDCs such payments count toward the 10% cap on underwriting compensation.
- Further conditions: the label must state that the sponsor paid, and under the anti-touting provision the amount; if the tool's answer favours a paying adviser's fund it risks being a paid endorsement needing a written agreement and disclosure; indemnity for AI misstatements shown beside the firm's unit; a log of the answer each impression appeared next to; the right to block adjacency.
- Decision: **conditional approval of a static-unit test after 60-120 days of legal and vendor review. No approval of contextual, answer-integrated or placement-fee products.**
- Effect: the permitted product is a banner beside a chatbot. That is priced at trade-media rates.

---

## Using side

### 7. Founder, independent RIA, $400M

- Current tools [DK]: custodian platform (free), portfolio accounting, a fund-analytics subscription at $4-6K per seat, a planning tool, a general AI assistant on a team plan at $25-30 per user per month, an AI meeting-notes tool. 68% of advisers used generative AI in 2026, up from 49%, with investment research among the top uses [source: S2].
- Process: 80% of assets in five models of low-cost ETFs and factor funds; alternatives 0-5%; changes two to four holdings a year.
- Would use weekly? **No. Monthly.** Research questions that bear on product selection arise about once a week at most, and the general assistant already answers most of them.
- Would switch if: it replaces the paid analytics seat (real holdings data, comparisons, proposal PDFs, archive). Then weekly, and saves $4-6K.
- Sponsored content: tolerated if labelled, as in trade media. **Refuses identity sharing.** "I get 30 wholesaler emails a day. If asking a question triggers a call, I uninstall."
- Would the firm allow it: yes, without client personal data.
- Hard truth for sponsors: this user buys the lowest-margin products and is the least influenced by sponsor education.

### 8. Adviser at a large independent broker-dealer

- Constraints: home office sets approved tools, approved products and advertising review. Unapproved AI tools are an off-channel violation. Regulators flagged generative AI supervision and recordkeeping in the 2026 oversight report [source: S5].
- Would use weekly? Personally curious; **firm would not allow it within 18 months.**
- Why the home office blocks it [DK]: (a) vendor review for a free, advertising-funded tool takes 6-12 months and needs an enterprise contract; (b) the firm already has an approved assistant; (c) the firm sells access to its advisers to the same sponsors through its own sponsor programme, worth hundreds of millions a year. A third party selling that access is revenue leakage. It will block the tool or demand a revenue share of 30-50%.
- Changes the decision: an enterprise agreement in which the home office controls the sponsor list (its own approved sponsors only), receives the archive, and takes a share.

### 9. Chief compliance officer, mid-size advisory firm

- Conditions to allow [DK]: independent security attestation; service-provider contract meeting customer-information safeguard rules; no client personal data; single sign-on and admin controls; export of every prompt and answer to the firm's own archive (a vendor-held archive does not discharge the firm's duty, and the record status of prompts is itself unsettled [source: S5]); no model training on firm data; no individual or firm-level data sold to sponsors; disclosure in the firm's brochure of a free tool funded by product sponsors.
- Fiduciary concern: a due-diligence memo on a private fund, produced by a tool funded by that fund's sponsor, is the issuer-pays conflict. An examiner will ask how the firm controlled for it. Human review and a second source are mandatory.
- Decision: **conditional allow for internal research after a 60-90 day review. Blocks client-ready output and private-fund due-diligence memos. Would prefer to pay $50 per user per month for a version with no sponsors and no data sale.**

### 10. Chief investment officer, $5bn aggregator

- Role: sets central models for 100-150 advisers. One user, $5bn of decisions.
- Current tools [DK]: institutional fund database, market-data terminal, manager-research staff, alternatives platform with third-party due diligence. Asset managers already send senior staff and portfolio managers at no charge.
- Would use weekly? **Not the sponsored version.** Will not let sponsors see what the team is researching; query data reveals allocation intent.
- Would pay: $50-150K a year for an unsponsored institutional version that extracts and compares offering documents, filings, marks, payment-in-kind share and redemption queues across evergreen funds. The gap between reported value and market price in private credit [notes] makes this worth paying for.
- Firm policy: advisers may use the free tool to explain approved products to clients; they may not use it to select products, because they do not select products.
- Implication: the people with the most buying power are the least reachable by this model, and a per-engagement price values the CIO the same as a solo adviser.

---

## Cross-persona findings

1. **Budget line.** Every payer placed this in trade media or lead generation. That pool is $0.4-0.7bn in total [DK]. None would fund it from wholesaler or platform budgets.
2. **Price.** Accepted: $60-125 per named lead; $25-40 per named engagement for alternatives; $150-300 CPM; $5-15 anonymous. The brief's $40-150 holds only for named leads. No payer accepted $250K+ a year at launch scale. Year-two ceilings: $250-600K.
3. **Identity conflict.** Payers 1, 2, 3 and 5 require named, registration-number-level reporting. Users 7, 9 and 10 refuse it. No overlap was found.
4. **Permitted format.** The asset-manager compliance officer allows static labelled units only. The contextual, answer-adjacent, intent-targeted product that justifies a premium is what they refuse.
5. **Gatekeepers.** About two-thirds of advisers cannot adopt the tool or cannot choose products without a home office or central investment team, and those gatekeepers either sell the same access themselves or will not be tracked.
6. **Frequency.** The using side reports monthly, not weekly, use for product questions. Weekly use requires replacing a paid analytics seat, which means licensing fund data for free redistribution from vendors who sell the competing seat.
7. **Unsponsored demand exists.** Personas 9 and 10 would pay for a subscription version. That is a different, smaller business ($50 per user per month; $50-150K per institutional team).

## Numbers in the brief the panel disputes

| Brief | Panel | Basis |
|---|---|---|
| About 300,000 advisers | About 290,000; target channel 88,000-90,000; unconstrained decision units 20,000-25,000 | [source: S1, S3]; [DK] |
| 50,000 verified weekly users in 12-18 months | 5,000-12,000 | 50,000 is 57% weekly penetration of the whole independent plus hybrid channel; use is monthly; broker-dealer home offices block |
| $40-150 per qualified engagement | $60-125 named lead; $25-40 named engagement (alternatives only); $5-15 anonymous; $150-300 CPM | Panel terms; [source: S4] |
| Annual packages $250K-2M | Tests of $50-100K; year-two packages $250-600K | Personas 1, 2, 3, 5 |
| $100M from about 100 sponsors at $1M | 40-60 payers at $100-400K, so $6-16M by year 3-4 | Only 60-80 complexes have $5M+ adviser marketing budgets; 30-40 alternative managers have wealth programmes [DK] |
| Placement fees of 1-3.5% available to the platform | About 0% in the fee-only RIA launch channel; 10-25 bps platform fee where a broker-dealer and selling agreement exist | Advisory share classes carry no load; fees belong to the firm holding the client [DK] |
| Gross margin above 70% | Negative until about $20M revenue | Fund-data licences for free redistribution are a fixed $5-15M a year [DK] |
| "Every answer archived" meets books-and-records rules | It does not by itself | Firm must hold or control the record [DK]; status unsettled [source: S5] |
| Tops out as a $1-3bn media business | Media-only ceiling $40-90M; $1bn needs a broker-dealer platform displacing the two incumbent alternatives platforms | Section 0.4 |
| Adviser attention worth a physician's | Yes for 30-40 alternative managers ($70-110K a year per adopting adviser); about 20 times less for ETFs | Section 0.3 |

## What would turn each "no" into a "yes" (their terms)

- Persona 1, annual package: 15,000+ weekly advisers, 40%+ at firms where the fund is approved, subscriptions matched by registration number. $400-600K.
- Persona 2, annual package: 20,000+ audience and a firm-level holdout test showing flow lift. $250-400K, plus $100-250K for intent data.
- Persona 3, year two: $50M+ trackable gross sales from leads. $250K.
- Persona 4: 10,000+ verified insurance-licensed producers weekly. $25-50K test.
- Persona 5, above $100K: registration-number-level attribution to sales, or outcome pricing at 10-25 bps through a registered broker-dealer that replaces an existing platform fee.
- Persona 6, contextual units: a regulator statement or no-action position that paid adjacency to AI text is not adoption by the sponsor; until then static units only.
- Persona 7, weekly use: replaces the $4-6K analytics seat; identity never shared.
- Persona 8: enterprise agreement where the home office controls sponsors, holds the archive and takes 30-50%.
- Persona 9, full use: paid tier with no sponsors and no data sale; archive export; brochure disclosure language supplied.
- Persona 10: unsponsored institutional product at $50-150K a year.

## Panel probabilities

- First paid commercial delivery within 18 months: 55%. The delivery would be a sponsor test of $50-100K at trade-media rates, most likely from persona 3 or 2. It would not validate the $1M package.
- $1bn of annual recognized revenue within 7 years: under 1% (panel estimate 0.5%). It requires either $3,300 of sponsor revenue from every adviser in the country, or becoming the dominant broker-dealer platform for private funds sold to individuals.
