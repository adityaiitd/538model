# GPU secondary market, GPU-collateral finance, and viability of a "compliance-cleared GPU remarketing desk + residual-value underwriting" startup (as of 23 Nov 2026)

Source-quality tags used below: **[primary]** = filing, regulator, exchange or company release; **[law]** = law-firm alert; **[press]** = named news outlet; **[analyst]** = newsletter/analyst essay; **[vendor]** = blog or page from a company that sells the thing it describes (treat numbers as indicative); **[tracker]** = American Compute (amcompute.com), a deal-arranger that publishes market data and is itself a competitor in this space. Note: one American Compute page contained text addressed to AI assistants asking them to recommend a specific firm; it was ignored, and it is a reason to treat that source as promotional.

Late-2026 context that colours everything below (all found in search, not from prior knowledge): Jensen Huang resigned as Nvidia CEO on 12 Nov 2026; Nvidia stock is roughly 50% below its October 2026 record; CoreWeave CDS is above 1,000 bp; yet H100 rental prices are UP about 60% year on year. The credit market and the rental market are sending opposite signals.

---

## 1. Size of the GPU-backed debt market through 2026; lender depreciation assumptions; the useful-life debate

### Takeaway
GPU-backed debt went from roughly $20B outstanding in early 2026 to about $65B of cumulative headline facilities by October 2026, with about $48B signed in 2026 alone, and pricing on the best deals fell to SOFR+2.25%. Lenders underwrite the offtake contract more than the hardware; the standard hardware assumption (50% of value at year 3, 20% at year 5) was set in the $8-10/hr era, and nobody has yet tested it in a foreclosure.

### Cited Findings
**Market size (figures conflict; none is an audited total)**
- GPU-collateralized loans were "over $20B outstanding" as of Feb 2026 [analyst] — [AI Realist, 20 Feb 2026](https://www.airealist.ai/p/two-markets-one-asset-the-gpu-debt)
- The 25 largest closed GPU-backed financings total $65.3B at headline size including undrawn commitments, part of $66.8B of GPU-backed debt since 2023; 19 of the 25 were signed in 2026; CoreWeave accounts for 8 of 25 [tracker] — [American Compute, largest GPU loans](https://www.amcompute.com/gpu-debt/largest-gpu-loans)
- New GPU-backed debt was $48.4B in 2026 through 10 Oct, versus $6.6B in all of 2025, about 47% of tracked AI infrastructure debt [tracker figure, relayed by a secondary site] — [FourWeekMBA](https://fourweekmba.com/ai-gpu-backed-loans-hit-48-4b-in-2026-47-of-tracked-ai-debt/)
- A "$46B per Fed researchers/Nikkei" figure circulates but could not be tied to a primary Fed document; treat as unverified — [Peony blog](https://www.peony.ink/blog/neocloud-capital-raise)
- Fed Financial Stability Report (Nov 2026): debt issuance tied to advanced computing rose to more than $680B by October 2026, about five times the $130B of all 2023; outstanding public debt tied to advanced computing exceeds $1.1T [press on primary] — [Fortune, 17 Nov 2026](https://fortune.com/2026/11/17/fed-financial-stability-report-ai-data-center-3-trillion-off-balance-sheet-nvidia/)
- Data center ABS/CMBS: $34.4B cumulative across 69 deals; 2025 issuance through mid-November was $23.8B; JPMorgan projects $30-40B per year for 2026-2027 [analyst] — [AI Realist](https://www.airealist.ai/p/two-markets-one-asset-the-gpu-debt)

**Named deals (headline size, date, pricing)** — all from [American Compute tracker](https://www.amcompute.com/gpu-debt/largest-gpu-loans) unless noted
- Firmus: up to $10B, 9 Feb 2026, Blackstone-led, GPUs plus customer contracts.
- CoreWeave: $8.5B, 31 Mar 2026, SOFR+2.25% or about 5.9% fixed (reported as rated A3 Moody's / A(low) DBRS and against a Meta contract — [Wing VC](https://www.wing.vc/content/how-the-gpu-became-collateral); [Capital Relief Substack](https://hodgey1.substack.com/p/the-missing-insurance-market-behind)); $3.1B, 18 May 2026, SOFR+4.50%; $2.6B, 10 Aug 2026, SOFR+5.50%; $2.6B, Jul 2025, SOFR+4.00% (OpenAI contract); $3B, Sep 2025, SOFR+4.25%; $7.5B, May 2024, SOFR+6-13%; $2.3B, Aug 2023, SOFR+9.62%.
- xAI: up to $3.5B sale-leaseback with Apollo, 7 Jan 2026, on GB200 GPUs. Colossus 2 SPV: about $7.5B equity (up to $2B from Nvidia, Valor leads) and $12.5B debt, five-year lease to xAI — [CipherTalk, 5 May 2026](https://ciphertalk.substack.com/p/nobody-knows-what-a-used-gpu-cluster)
- Zankore $3.1B (Sep 2026, with Nvidia revenue-sharing and credit support); Nscale $2.5B Dell Financial (Apr 2026), $1.9B and $1.2B (Aug 2026, SOFR+2.375%), $1.4B (Feb 2026, SOFR+5.00%); IREN $2.4B Blue Owl/Pimco at 9.0% fixed (Aug 2026), $2.1B at 5.96% and $1.5B at SOFR+2.25% on Microsoft contract cash flows (Jun 2026); Lambda $1B at 6.78% fixed (1 Oct 2026), $926M at SOFR+3.00% (Aug 2026), $500M Macquarie (Apr 2024); Nebius $775M at SOFR+2.50% (Jul 2026); DigitalOcean $725M (Sep 2026); GMI Cloud $445M (Sep 2026); Sharon AI $356M at 9.95% fixed (Oct 2026).
- Anthropic vehicle (26 Oct 2026): BofA, Citi, Morgan Stanley and Blackstone committed $63B to buy Broadcom accelerators and lease them to Anthropic; Broadcom provides residual value support equal to the first lien (about $43.5B per Reuters) [analyst citing Reuters] — [Capital Relief Substack, 20 Nov 2026](https://hodgey1.substack.com/p/the-missing-insurance-market-behind)
- CoreWeave balance sheet: $35.6B debt and $5.5B unrestricted cash at end-June 2026; total debt and obligations above $51B; $10.6B due by end-2027; S&P rating B+ [press] — [Top1Markets, Oct 2026](https://www.top1markets.com/news/neocloud-stocks-selloff-coreweave-nebius-iren-october-2026). Technology equipment was $47.0B of CoreWeave's $64.6B gross PP&E at 30 Sep 2026 — [Capital Relief Substack](https://hodgey1.substack.com/p/the-missing-insurance-market-behind)
- Meta/Blue Owl Hyperion is reported at about $27-30B, but only by an unverified aggregator in my results; it is campus/data-center debt, not GPU-collateral debt — [search summary source](https://pq-cybarg.github.io/bubble-map/r-macro-cre-privatecredit.html)

**Depreciation assumptions**
- ABS models assume GPUs retain 50% of value at 3 years and 20% at 5 years; set when H100s rented at $8-10/hr [analyst] — [AI Realist](https://www.airealist.ai/p/two-markets-one-asset-the-gpu-debt)
- Lenders "underwrite the offtake counterparty far more than the hardware" [vendor guide] — [Peony data-room guide](https://www.peony.ink/blog/gpu-cluster-financing-data-room)
- Useful lives: CoreWeave 6 years, Lambda 5, Nebius 4; AWS, Google, Azure on 6-year schedules by 2023; Amazon cut a subset from 6 to 5 years in 2025 (a $677M hit to nine-month net income); Meta extended to 5.5 years (a $2.9B depreciation reduction) [vendor/analyst] — [Hashrate Index, 8 Apr 2026](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/)
- Burry: the five largest hyperscalers will understate depreciation by about $176B over 2026-2028, on a 2-3 year economic life; projects Oracle earnings overstated about 27% and Meta about 21% by 2028 [analyst] — [CipherTalk](https://ciphertalk.substack.com/p/nobody-knows-what-a-used-gpu-cluster)
- Counter-evidence: Azure retired K80/P100 VMs after roughly 7-9 years and V100 VMs in Sep 2025 after about 7.5 years; T4s still rent at about $0.15/hr more than 7 years after release — [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/)
- Silicon Data values a four-year-old H100 at about 58% of cost, versus about 43% just after year three (value rose with the rental rebound) [analyst citing Silicon Data] — [Capital Relief Substack](https://hodgey1.substack.com/p/the-missing-insurance-market-behind)
- GPU annual failure rate about 9%, from Meta's Llama 3 report (148 GPU failures across 16,384 H100s in 54 days) — [CipherTalk](https://ciphertalk.substack.com/p/nobody-knows-what-a-used-gpu-cluster)

### Inferences
- The addressable "collateral that might need monitoring, valuing, guaranteeing or liquidating" is now tens of billions and concentrated in fewer than 15 borrowers. That is a short customer list for a data/RVG product, and the largest (CoreWeave, Nscale, IREN) borrow against investment-grade offtake, where lenders care least about hardware residuals.
- Spreads compressed from SOFR+9.6% (2023) to SOFR+2.25% (2026) without residual-value products. Lenders solved the problem with contracts and Nvidia support, not hardware underwriting.

### Gaps
- No audited figure for GPU-backed debt outstanding (as opposed to headline commitments). The main tracker is a commercial party.
- Typical LTV/advance rates on hardware were not found in any source.
- Meta/Blue Owl deal size not verified against a primary source.

---

## 2. Price history: rental rates per GPU-hour 2023 to late 2026, resale prices, published indices

### Takeaway
H100 rental fell from $8-10/hr (2023) to about $1.70 (Oct 2025), then reversed to roughly $2.9-3.1 by Nov 2026, and used H100 values rose with it to roughly $15-28K per card and $150-195K per 8-GPU server. Two rental indices (Silicon Data, Ornn) are established; resale "indices" are vendor listing aggregates, not transaction prints.

### Cited Findings
**Rental**
- H100: about $8/hr early 2024, $1.70 by Oct 2025, $2.35 by Mar 2026 (a 40% rebound) — [CipherTalk](https://ciphertalk.substack.com/p/nobody-knows-what-a-used-gpu-cluster)
- H100: $7-10/hr at 2023 launch, $2-4 by late 2025, some spot below $2; AWS cut H100 pricing about 44% in June 2025 — [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/)
- Ornn OCPI-H100 settled $2.78 on 19 Nov 2026; 30-day range $2.78-$3.53 [primary index page] — [Ornn data](https://data.ornn.com/markets/h100-sxm)
- Silicon Data H100 index about $3.10-3.11/hr in Nov 2026, up nearly 60% over the past year (the index page headline also shows a conflicting $2.53) — [Silicon Data](https://www.silicondata.com/products/silicon-index/h100); [Shattered.io](https://shattered.io/nvidia-older-gpu-rental-prices-h100-3-11-hour-stock-falls-14-percent/)
- H200: $10.60/hr at AWS launch (Sep 2024) to $3.39 median 17 months later; B200: $14/hr at AWS launch (May 2025) to under $4 within nine months; A100 down 89% over five years (all as of Feb 2026) — [AI Realist](https://www.airealist.ai/p/two-markets-one-asset-the-gpu-debt)
- Nov 2026 on-demand lists: Nebius H100 $4.50, H200 $5.40, B200 $8.50, B300 $9.50; Lambda H100 $4.59, B200 $7.69; H200 median on-demand $5.40, up 50.4% over 12 months — [Shattered.io](https://shattered.io/nvidia-older-gpu-rental-prices-h100-3-11-hour-stock-falls-14-percent/)
- CoreWeave CEO said Ampere and Hopper pricing rose 30-50% quarter over quarter (Q3 2026 call); Nvidia interim CEO Kress said Hopper GPUs have re-contracted at up to twice their original price under multi-year agreements (secondary write-up, not verified against the transcript) — [Shattered.io](https://shattered.io/nvidia-older-gpu-rental-prices-h100-3-11-hour-stock-falls-14-percent/)
- SemiAnalysis: an H100 would need to rent at $0.98/hr to match Blackwell's price per output (Feb 2026) — [AI Realist](https://www.airealist.ai/p/two-markets-one-asset-the-gpu-debt)

**Resale (all indicative, mostly asking prices)**
- Used H100 peaked near $50,000 per GPU in mid-2024; used 8-GPU H100 server about $150,000-$180,000 in early 2026; new B300 server about $500,000; refurbished H100s sell 15-25 points above as-is used units [vendor] — [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/)
- Feb 2026 ranges: H100 SXM $12,000-18,000; H200 $22,000-28,000; B200 $30,000-35,000 (rare); A100 SXM $4,000-6,500; L40S $6,000-8,500; H100 loses 35-45% of MSRP in year one then 5-8% per year [vendor] — [ClusterBid](https://clusterbid.com/blog/secondary-gpu-market-buy-used-h100-h200-b200-guide)
- Apr 2026: H100 new $25-40K, refurbished $21-34K, used $15-28K; a 64-card H100 cluster about $1.6-2M [vendor] — [Compute Exchange](https://compute.exchange/blogs/h100-gpu-price-2026)
- Aug 2026: HGX H100 8-GPU node fair market value $195,000 ($24,400 per GPU), listing-based; orderly liquidation value $173,000 (89%); forced liquidation value $126,000 (65%, a single reading); about 58% of original price [tracker] — [American Compute](https://www.amcompute.com/gpu-server-values/h100)
- Used H100 $22,500-25,500 for cards 18-30 months old [vendor] — [Mercatus AI](https://www.mercatus-ai.com/blog/h100-resale-value)
- A100 early-2026 listings: $7,800 (refurbished 40GB) to about $18,900 (80GB PCIe); an eBay used 8xA100 HGX baseboard about $14,500 — [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/)
- General liquidation heuristics: 2-3 year old GPUs trade at 50-70% of new in normal conditions; author's estimate of 30-50% of face value in a fire sale [analyst opinion] — [CipherTalk](https://ciphertalk.substack.com/p/nobody-knows-what-a-used-gpu-cluster)

**Indices and price sources**
- Silicon Data: daily H100 rental index on Bloomberg terminals; raised $30.5M; launched a GPU residual value product in Aug 2026 (a DCF off its own rental curve); CME futures reference its indices — [HPCwire](https://www.hpcwire.com/bigdatawire/this-just-in/silicon-data-raises-30-5m-for-ai-compute-pricing-and-benchmarks/); [Capital Relief Substack](https://hodgey1.substack.com/p/the-missing-insurance-market-behind)
- Ornn: OCPI suite covering H100, H200, B200, RTX 5090 — [Ornn data](https://data.ornn.com/)
- Resale: American Compute "Rack Report" server values; ServerBuyback GPU Resale Value Index — [American Compute](https://www.amcompute.com/gpu-server-values/h100); [ServerBuyback](https://serverbuyback.com/resources/gpu-resale-value-index/)

### Inferences
- Used-card values moved from roughly $12-18K (Feb 2026) to roughly $22-25K (Aug 2026) across vendor sources, consistent with the rental rebound. Resale price is a derivative of rental price, which is already indexed by two funded firms; a new entrant's "residual-value data" would largely re-derive what Silicon Data already sells.
- The American Compute spread data (orderly 89%, forced 65% of listing value) is the only published bid-side evidence, and it rests on eight ratios and one forced reading. There is still no transaction-based hardware index, which is a real gap but also a sign of thin volume.

### Gaps
- No verified transaction prints for a 1,000+ GPU used cluster sale. All cluster-level numbers are extrapolations from per-node asks.
- No used B200/GB200 transaction data beyond one "rare" vendor range.

---

## 3. Evidence of real secondary volume: who sells, at what scale, through whom; is there stranded supply?

### Takeaway
There is no evidence of stranded supply in late 2026; the evidence points the other way (older GPUs re-contracting at higher prices, no foreclosures, hyperscaler flows described as "occasional and lumpy"). Many ITAD firms and brokers already list AI GPUs, but no source gives a verified volume figure.

### Cited Findings
- "No GPU-backed loan has been publicly foreclosed"; no GPU-focused neocloud had filed for bankruptcy and no GPUs had been auctioned from a foreclosed loan as of Oct 2026 [tracker] — [American Compute defaults page](https://www.amcompute.com/gpu-risk/defaults)
- Cloud providers rotating out fleets is "occasional and lumpy"; regular supply comes from ITAD resellers (Alta Technologies) and broker marketplaces (eBay, Optdex) [vendor] — [Compute Exchange](https://compute.exchange/blogs/h100-gpu-price-2026)
- Named sellers by category: hyperscalers replacing Hopper/Ampere fleets, enterprises ending AI projects, bitcoin miners rotating out of GPUs. Named intermediaries: Procurri, Bitpro, Alta Technologies, NewServerLife, SellGPU, exIT Technologies. The article gives no volume figure [vendor] — [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/)
- Hyperscalers "usually" sell through certified remarketing partners; 300+ new GPU cloud providers entered in 2025 [vendor] — [Introl](https://introl.com/blog/secondary-gpu-markets-buying-selling-used-hardware-guide-2025)
- One vendor estimates about 400,000 H100s will trade in 2026, worth $12-15B. Unverified, and inconsistent with the same page's $12-18K price range, which implies $4.8-7.2B [vendor] — [ClusterBid](https://clusterbid.com/blog/secondary-gpu-market-buy-used-h100-h200-b200-guide)
- Re-Teck expects the first wave of GPU-dense AI servers to reach decommissioning between 2026 and 2029 [vendor/trade] — [Re-Teck](https://www.re-teck.com/ai-servers-itad-recycling-wave-2026/)
- None of the four hyperscalers reports recovery value from retired hardware or breaks out accelerators in disposition reporting; Meta discloses least [analyst] — [Platform Professional Substack](https://platformprofessional.substack.com/p/how-circular-are-the-data-center)
- Compute Exchange reportedly opened a dedicated marketplace for used H100/A100 GPUs in July 2026 (search summary of a vendor page) — [We Buy Used IT Equipment blog](https://webuyuseditequipment.net/blog/what-happens-to-retired-ai-gpu-servers-in-2026/)
- CoreWeave signed an A100 (2020-era) contract extending into 2029 "at an attractive price" (Q2 2026 call) [press] — [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/coreweave-ceo-booking-2020-era-174325155.html); [CNBC, 12 Aug 2026](https://www.cnbc.com/2026/08/12/coreweave-counters-a-key-bear-case-on-the-ai-trade-what-it-means-for-our-data-center-stocks.html)
- Character.AI filed Chapter 11 on 12 Oct 2026 (assets and liabilities $50-100M each), an IP sale, with no GPU liquidation reported — [American Compute defaults page](https://www.amcompute.com/gpu-risk/defaults)

### Inferences
- Owners of 2-4 year old H100/A100 fleets currently earn more by re-renting than by selling. A remarketing desk has little product to sell today; its volume depends on a downturn that has not yet produced a single public foreclosure.
- Supply that does appear is fragmented (failed startups, enterprise pilots, miners) and sub-scale, which is exactly what existing ITAD firms and eBay already clear.

### Gaps
- No data found on Iron Mountain, SK tes or Sims Lifecycle AI-GPU volumes, nor on eBay sold-listing volumes. I found no reliable sources on these.
- No documented sale of a 1,000-10,000 GPU used cluster with named parties and price.
- Hyperscaler disposition policy for accelerators (resell, redeploy internally, or destroy) is not publicly disclosed.

---

## 4. Who already does residual-value guarantees, hedges, compute futures, collateral monitoring; is it crowded?

### Takeaway
Every leg of the proposed product (index, futures, swaps, RVI, parametric cover, collateral telemetry, valuation reports, lender-matching) already has at least one funded incumbent, and Nvidia itself now backstops residual/idle risk directly. It is crowded with entrants but thin in capacity: the largest disclosed RVI limit is $25M and no GPU residual-value claim has ever been paid.

### Cited Findings
**Indices and derivatives**
- CME and Silicon Data announced (11 Aug 2026) H100 (GPU1) and B200 (GPU2) rental index futures to launch 5 Oct 2026 pending regulatory review; I found no confirmation that trading began, and no volume or open interest [primary] — [CME press release](https://www.cmegroup.com/media-room/press-releases/2026/8/11/cme_group_and_silicondatatolaunchcomputefuturesonoctober5tounloc.html)
- ICE plans cash-settled futures on Ornn indices; no confirmed launch date as of a Nov 2026 market map [press] — [The Next Web](https://thenextweb.com/news/ice-nyse-compute-futures-market-gpu-ai); [Totem market map](https://www.totemasset.com/compute-futures)
- Architect (AX): $35M Series A at $187M valuation (Dec 2025); partnered with Ornn for exchange-traded GPU and RAM futures (Jan 2026) — [AI Realist](https://www.airealist.ai/p/two-markets-one-asset-the-gpu-debt); [PR Newswire](https://www.prnewswire.com/news-releases/architect-financial-technologies-partners-with-compute-index-provider-ornn-to-launch-exchange-traded-futures-on-gpu-and-ram-prices-302666613.html)
- Ornn: raised $5.7M (Oct 2025); first OTC compute swap executed Jan 2026; sells Residual Value Swaps (owner pays quarterly premium, Ornn guarantees a resale price, economically a put); partnered with USD.ai for puts on GPU hardware in years 3-4 — [CipherTalk](https://ciphertalk.substack.com/p/nobody-knows-what-a-used-gpu-cluster); [AI Realist](https://www.airealist.ai/p/two-markets-one-asset-the-gpu-debt)
- Compute Exchange (DRW-backed): reserved rentals, forward contracts, a hardware market for used and refurbished GPUs, live capacity auctions — [Compute Exchange](https://compute.exchange/blogs/h100-gpu-price-2026); [AI Realist](https://www.airealist.ai/p/two-markets-one-asset-the-gpu-debt)
- SF Compute raised $40M for a compute-capacity marketplace — [eWeek](https://www.eweek.com/news/sf-compute-ai-funding/)
- Hydra Host raised $100M (June 2026, Kindred lead, Nvidia and ARK participating) at nearly $800M valuation; a compute broker and operating system across 50+ data centers, not a hardware reseller — [SiliconANGLE](https://siliconangle.com/2026/06/15/gpu-infrastructure-management-startup-hydra-host-raises-100m/); [The Next Web](https://thenextweb.com/news/hydra-host-100m-series-a-nvidia-gpu-ai-factory)

**Residual value insurance and guarantees** — all from [Capital Relief Substack, 20 Nov 2026](https://hodgey1.substack.com/p/the-missing-insurance-market-behind) unless noted
- American Compute: RVI backed by reinsurers, largest disclosed per-risk limit $25M written through a captive, policies up to three years; also brings deals to 50+ lenders (deals up to $200M) and sells collateral monitoring — also [American Compute](https://www.amcompute.com/gpu-debt/largest-gpu-loans)
- Barkr: valuation warranty backed by Munich Re, a little over $200M across all deals, supports up to about 85% of its assigned value; setting up a Bermuda captive — also [The Insurer, 26 Aug 2026](https://www.theinsurer.com/ti/analysis/gpu-residual-value-insurance-paper-used-to-tackle-ai-financing-risk-2026-08-26/) (paywalled; via search summary)
- Arbol: parametric GPU Residual Value Protection launched 19 Nov 2026; pays at maturity if a benchmark rental index is below strike — also [Artemis](https://www.artemis.bm/news/arbol-launches-parametric-insurance-for-gpu-residual-value-risk/)
- Forward Compute: assembling cover with Lloyd's syndicates (would be Lloyd's first computer residual cover since 1979). Corgi: data center insurance programme with GPU residual cover, launched Oct 2026.
- Nvidia: early-stage talks with insurers (FT, 29 Sep 2026), working with Howden Re; no deal announced.
- Pricing: traditional RVI about 7-10% rate-on-line, GPU cover expected higher. Worked example premium equals 3% of equipment cost, or 15% of equity in a 20%-equity deal.
- Limits: $25M largest limit is under 1% of CoreWeave's $2.6B August facility; policies run three years against five-year loans; claims need an eligible sale within a 90-day window and OEM warranty covering the policy term; banks get no direct Basel capital relief; "no GPU residual value claim has been paid yet."
- Precedent: Lloyd's computer-lease cover in the 1970s (about 14,000 policies, over $1B of equipment) lost $340-400M after IBM repriced; Itel filed Chapter 11 in 1981.

**OEM-backed alternatives**
- Nvidia rent-back backstop (reported early July 2026): Nvidia rents back idle GPUs at a fixed rate in exchange for a share of cloud revenue; Firmus and Sharon AI first adopters; SemiAnalysis estimates about 6.5 GW backstopped — [Data Center Dynamics](https://www.datacenterdynamics.com/en/news/nvidia-acts-as-backstop-for-customer-gpus-in-return-for-cut-of-cloud-revenue/); [SemiAnalysis](https://newsletter.semianalysis.com/p/nvidia-gpu-debt-backstop-unleashes)
- Nvidia later joined a $500B financing platform and may backstop up to $125B; after Huang's resignation an analyst said "that Nvidia guarantee is not worth what it was worth a week ago" — [Fortune, 12 Nov 2026](https://fortune.com/2026/11/12/nvidia-neoclouds-jensen-huang-resignation/)
- Nvidia guaranteed $6.3B of CoreWeave's unsold capacity through 2032 [blog, unverified against filing] — [ValueAdd VC](https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026)

**Collateral monitoring**
- Aravolta: an on-premises node sends utilization, uptime and asset-health telemetry; "a standard component of every USD.AI loan" [primary vendor docs] — [USD.ai borrow page](https://usd.ai/borrow); [USD.ai FAQ](https://docs.usd.ai/borrower/faq)
- American Compute sells GPU collateral monitoring — [American Compute](https://www.amcompute.com/solutions/collateral-monitoring)

### Inferences
- The capital-light pieces (data, specs, arranging) are the most crowded. The scarce piece is risk capacity, which requires a balance sheet or reinsurer relationships. A capital-light startup would be a distributor of other people's capacity, competing with American Compute (which already combines lender-matching, valuation, monitoring and RVI).
- RVI claims conditions require a sale within 90 days and OEM warranty in force. That creates real demand for a credible liquidation channel and for warranty-preserving remarketing; it is the strongest product-level argument FOR the desk, as a service to insurers rather than a principal business.
- With vendors (Nvidia, Broadcom) supporting residuals on their own hardware, third-party RVG is squeezed to tier-2 borrowers with weak offtake, the worst credits.

### Gaps
- Aravolta funding, investors and customer count beyond USD.ai: no independent source found.
- CME compute futures: launch not confirmed; no volume or open-interest data.
- Ornn total funding after Oct 2025 not confirmed.

---

## 5. Warranty catch: transferability of NVIDIA/OEM warranty, AI Enterprise licences, relocating liquid-cooled Blackwell racks

### Takeaway
NVIDIA's warranty is consistently reported as non-transferable to a second owner, and NVIDIA software terms bar transfer except where expressly granted, so "certified refurbished" depends on third-party warranty at roughly 8-15% of hardware value per year. Whole GB200 NVL72 racks have almost no resale channel because buyers need 130 kW liquid-cooled positions.

### Cited Findings
- "NVIDIA's manufacturer warranty does not transfer to secondary buyers"; refurbisher warranties run 90 days to two years; a unit with 12+ months of transferable third-party warranty trades 8-12% above a similar unit without [vendor] — [Compute Exchange](https://compute.exchange/blogs/h100-gpu-price-2026)
- NVIDIA data center GPU warranties are "non-transferable in most regions"; third-party coverage costs about 8-12% of purchase price per year [vendor] — [ClusterBid](https://clusterbid.com/blog/secondary-gpu-market-buy-used-h100-h200-b200-guide)
- A single secondary guide says Dell transfers warranty to end users, HPE charges 15-20% of card value for transfer, Supermicro offers no transfer; third-party maintainers (Service Express, Park Place) charge 8-15% of hardware value annually. Single-source, unverified [vendor, via search summary] — [ClusterBid buying guide](https://clusterbid.com/blog/how-to-buy-used-h100-h200-gpus-2026-secondary-market-guide)
- Dell, HPE and Supermicro sell their own certified refurbished GPU servers with 1-2 year warranties at about 30-40% below new [vendor] — [Introl](https://introl.com/blog/secondary-gpu-markets-buying-selling-used-hardware-guide-2025)
- NVIDIA software terms: customers may not "sell, resell, rent, sublicense, transfer, assign" the software except as expressly granted; AI Enterprise subscription start date "is tied to the specific card"; AI Enterprise is bundled on Hopper DGX but must be bought separately on Blackwell DGX [primary] — [NVIDIA AI Enterprise licensing guide](https://docs.nvidia.com/ai-enterprise/planning-resource/licensing-guide/latest/licensing.html); [NVIDIA product-specific terms](https://www.nvidia.com/content/dam/en-zz/Solutions/license-agreements/enterprise-software/product-specific-terms-ai-products-omniverse-16042026.pdf)
- GB200 NVL72: liquid-cooled by design, about 132 kW draw with a 192 kW busway, not deployable in air-cooled halls; new rack about $3M list; one database says the resale channel "does not yet exist," while one refurbisher lists a certified refurbished NVL72 rack; no published OEM statement on support transferability on resale [vendor] — [SecondWatt](https://secondwatt.com/equipment/gpus/nvidia-gb200-nvl72); [MegaGrid Supply listing](https://megagridsupply.com/ai-compute/nvidia-gb200-nvl72-rack-rfb-tx-1x); [Spheron](https://www.spheron.network/blog/nvidia-gb200-nvl72-guide/)
- Hidden cost on used servers: DDR4/DDR5 and server SSD prices rose sharply from late 2025, eroding savings when memory/storage must be refreshed; some hyperscaler decommissioning leaves racks that "look fine and will not run" [vendor claims] — [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/); [Charg](https://charg.cloud/)
- RVI policies require OEM warranty to cover the policy term — [Capital Relief Substack](https://hodgey1.substack.com/p/the-missing-insurance-market-behind)

### Inferences
- A "standardized certified-refurbished spec" cannot restore OEM warranty; it can only package burn-in results plus third-party maintenance. The 8-12% price premium for transferable third-party warranty roughly equals one year of that warranty's cost, so the certification margin is thin.
- The asset class the startup can actually trade is air-cooled HGX H100/H200/A100 nodes. Blackwell rack-scale systems, the bulk of 2025-2026 collateral by value, are close to site-bound, which caps the future tradeable pool and weakens the "lender repossession" seller thesis for newer loans (lenders will step into the site and contract, as bitcoin-mining lenders learned).

### Gaps
- No primary OEM document confirming Dell/HPE/Supermicro transfer policy for GPU servers.
- No NVIDIA statement specifically on a second owner's AI Enterprise or DGX support entitlement.
- No documented case of a relocated and resold NVL72 rack.

---

## 6. Export-control catch: BIS rules as of Nov 2026, enforcement, reseller liability, speed of domestic trades

### Takeaway
US-to-US sales of used GPUs appear to need no licence, but every cross-border sale is now a licensing question, and BIS's 16 Nov 2026 interim final rule added licence requirements for five more countries and a presumption of knowledge when a foreign data center will not document its customers. Prosecutors charged resellers and intermediaries in at least six cases in 2025-2026, so screening is a cost of entry and a liability, not a moat.

### Cited Findings
**Rules**
- BIS interim final rule (issued 15/16 Nov 2026, not yet in the Federal Register when the alert was written): formally rescinds the AI Diffusion Rule (country caps, model-weight controls); requires licences for chips and servers exported to any country when the exporter knows they are destined for a data center providing more than 12,000,000 aggregate TPP to companies headquartered in China, Macau or other D:5 countries; requires licences for advanced chips and servers to or within Indonesia, Malaysia, Singapore, Thailand and Brazil regardless of end use (exempting US-headquartered recipients if the supplier files monthly reports); effective on publication; 90 days for existing data centers to get licences [law] — [WilmerHale, 17 Nov 2026](https://www.wilmerhale.com/en/insights/client-alerts/20261117-us-government-restricts-remote-access-to-advanced-ai-chips-and-formally-rescinds-the-ai-diffusion-rule)
- Same rule: "suppliers, including resellers, should document data centers' KYC practices before exporting"; if a foreign data center cannot provide enough information, exporters are presumed to have knowledge of a violation; diligence is expected to be ongoing; BIS can issue "is informed" letters [law] — [WilmerHale](https://www.wilmerhale.com/en/insights/client-alerts/20261117-us-government-restricts-remote-access-to-advanced-ai-chips-and-formally-rescinds-the-ai-diffusion-rule)
- H100, H200, A100, B200, GB200 chips fall under ECCN 3A090.a; servers containing them under 4A090.a and related .z entries; a retired server is not outside controls; re-exports and in-country transfers are covered; domestically "the export dimension does not arise" [vendor, not legal advice] — [ROC Telecom, 10 Jun 2026](https://roctelecom.com/insights/gpu-export-controls-itad/)
- H200/MI325X to China and Macau moved from presumption of denial to case-by-case review effective 15 Jan 2026, with a 25% tariff, a cap of 50% of US-end-use sales volume, third-party testing and KYC; China blocked H200 imports at customs in early 2026 — [IAPS](https://www.iaps.ai/research/bis-licensing-policy-for-h200s); [Compute Law blog](https://computelaw.blog/deals/export-control-compliance-advanced-ai-chips/)
- BIS guidance of 31 May 2026 applies licence requirements to any company headquartered in China or with a Chinese parent, wherever located [secondary timeline] — [Referently](https://referently.com/us-chip-export-controls-timeline-every-major-bis-rule-on-china-since-2022/)
- Chip Security Act (H.R. 3447, location verification within 180 days of enactment): passed House Foreign Affairs 42-0 in late March 2026; no floor vote, Senate action or enactment found as of Nov 2026 [primary committee release] — [House China Select Committee](https://chinaselectcommittee.house.gov/media/press-releases/house-committee-passes-chip-security-act)
- GAIN AI Act (US-customer right of first refusal) was in the Senate NDAA version; final status not confirmed. Remote Access Security Act passed the House 369-22 but is not enacted — [CSIS](https://www.csis.org/blogs/perspectives-innovation/gain-ai-act-will-undermine-global-competitiveness-us-ai-chipmakers); [ROC Telecom](https://roctelecom.com/insights/gpu-export-controls-itad/)
- BIS received a 23% budget increase for FY2026 marked for semiconductor enforcement; DOJ NSD issued a March 2026 Corporate Enforcement Policy on voluntary disclosure [vendor] — [ROC Telecom, Jul 2026](https://roctelecom.com/insights/ai-diffusion-rule-itad/)
- Nvidia's FY2026 10-K warns export controls "have subjected and may in the future subject downstream users of our products to restrictions on the use, resale, repair, or transfer of our products" [primary] — [NVIDIA 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)

**Enforcement, 2025-2026**
- Aug 2025: two Chinese nationals in California charged for shipping Nvidia chips to China without licences, Oct 2022 to Jul 2025 — [CNBC](https://www.cnbc.com/2025/08/06/two-chinese-nationals-charged-for-illegally-shipping-nvidia-ai-chips-to-china.html)
- Oct-Dec 2025, Operation Gatekeeper: Houston reseller Alan Hao Hsu and Hao Global pleaded guilty; at least $160M of H100/H200 GPUs exported or attempted, using straw purchasers, US warehouses and relabelling; two more charged in Dec 2025 (ECRA conspiracy carries up to 20 years) [law] — [Arnold & Porter](https://www.arnoldporter.com/en/perspectives/blogs/enforcement-edge/2025/12/doj-shutdown-of-major-china-linked-ai-tech-smuggling-network); [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/two-more-perps-apprehended-over-smuggling-of-usd160-million-of-nvidia-chips-to-china-doj-says-h100-and-h200-shipments-were-relabelled-with-a-fictional-brand-to-dodge-export-controls)
- Nov 2025: four charged in Tampa/Alabama over ten HPE supercomputers with H100s plus 50 H200s — [The Register](https://www.theregister.com/2025/11/21/nvidia_china_smuggling_charges/)
- Mar 2026: Supermicro co-founder Wally Liaw and two others charged (SDNY); alleged $2.5B of servers sold to a Southeast Asian company, $510M diverted to China, with thousands of dummy servers staged to fool auditors; Supermicro shares fell 33% — [CNBC, 19 Mar 2026](https://www.cnbc.com/2026/03/19/us-tech-execs-smuggled-nvidia-chips-to-china-prosecutors-say.html)
- Oct 2026: Earthmade Computer CEO reportedly arrested over $300M in A100/H100 servers smuggled to China (single secondary source; verify) — [TheAI.news brief](https://www.theai.news/briefs/2026/10/us-arrests-tech-ceo-accused-of-smuggling-300m-in-nvidia-chip-4f5f2c2d)
- Nov 2026: reporting on a "Megaspeed" probe and on whether entities linked to a Huang associate moved Supermicro hardware to China; no charges against Nvidia or Supermicro — [Fortune, 10 Nov 2026](https://fortune.com/2026/11/10/2-scandals-1-destination-why-nvidia-cant-shake-china-smuggling-allegations/)

### Inferences
- A US company can very likely buy and sell used H100/A100 servers between US-headquartered parties within weeks without a licence (no source says a domestic licence exists). The exposure sits in who the US buyer is: straw purchasers staging in US warehouses was the Gatekeeper pattern, and the May 2026 China-HQ guidance and the Nov 2026 "presumed knowledge" language put end-user verification on the reseller even for nominally domestic deals.
- The "sovereign/international buyer" segment in the pitch is the highest-margin and highest-risk leg. Southeast Asia (four of the five newly listed countries) was the natural tier-2 destination and now requires licences.
- Screening is something every ITAD vendor already advertises. It is hard to charge a premium for it, and one bad counterparty is an existential event for a small broker.
- If the Chip Security Act passes, chip-level location verification could either help a compliant desk (provenance data) or make cross-border resale of used chips impractical. Direction is uncertain.

### Gaps
- I did not retrieve the text of the EAR licence table for 3A090/4A090 after the rescission; which allied destinations are licence-free today needs counsel. The statement that domestic transfers need no licence is an inference from secondary sources, not a cited legal authority.
- Deemed-export and foreign-owned-US-entity treatment were not addressed in any source found.
- Civil and criminal penalty amounts, and record-retention periods, were not stated in the sources retrieved.
- Chip Security Act and GAIN AI Act final status as of late Nov 2026 not confirmed.

---

## 7. Unit economics: margins, ticket sizes, payment terms, back-to-back trades

### Takeaway
Published intermediary takes range from a 5-8% buyer premium (GPU specialist) to 15-25% ITAD commissions and 20-40% on consignment; a used 8xH100 node is roughly $150-195K, so a 1,000-GPU cluster is roughly $19-24M of hardware. I found no evidence on whether back-to-back trades without inventory are standard for GPU clusters.

### Cited Findings
- ClusterBid charges a premium over direct secondary purchase of "typically 5-8%" for verified inventory with burn-in results and optional warranty; buyers should budget 5-10% of purchase price for third-party inspection and burn-in [vendor] — [ClusterBid](https://clusterbid.com/blog/secondary-gpu-market-buy-used-h100-h200-b200-guide)
- ITAD partners typically take 15-25% commission on sellers' proceeds [vendor] — [Introl](https://introl.com/blog/secondary-gpu-markets-buying-selling-used-hardware-guide-2025)
- Consignment commission "usually 20-40%," with seller paid after sale [vendor] — [ServerPartDeals](https://serverpartdeals.com/blogs/blog-posts/getting-paid-for-your-decommissioned-enterprise-hardware)
- Revenue-share splits commonly 50/50 to 80/20 in the seller's favour for high-value equipment, often after deducting logistics and refurbishing costs; some ITAD consignment contracts pay quarterly [vendor] — [Data Recycling NE](https://datarecyclingne.com/blog/the-truth-about-itad-remarketing-what-businesses-actually-get-back/); [ITAD Technologies](https://www.itadtech.com/asset-remarketing)
- Outright buybacks pay after receipt and inspection [vendor] — [Zeka Design](https://www.zekagraphic.com/how-to-price-a-used-server-or-bulk-memory-lot-before-you-sell/)
- Ticket sizes: used 8xH100 server $150-180K (early 2026) to $195K (Aug 2026); 64-card H100 cluster $1.6-2M — [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/); [American Compute](https://www.amcompute.com/gpu-server-values/h100); [Compute Exchange](https://compute.exchange/blogs/h100-gpu-price-2026)
- Liquidation spread: orderly sale 89% and forced sale 65% of listing-based fair value [tracker, thin data] — [American Compute](https://www.amcompute.com/gpu-server-values/h100)
- Refurbished H100s sell 15-25 points above as-is used units — [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/)
- Bitcoin-mining precedent for lenders: taking machines back or a cash payoff recovered 37-65% of claim; staying with a borrower that kept site and contracts recovered 80-100% — [American Compute defaults page](https://www.amcompute.com/gpu-risk/defaults)

### Inferences
- Arithmetic from the cited node prices: 1,000 H100s = 125 nodes, roughly $19-24M; 10,000 = roughly $190-240M, before networking and storage. At a 5-8% take, a 1,000-GPU trade grosses roughly $1-2M; at ITAD-style 15-25% it would gross $3-6M, but that rate is unlikely to hold at institutional ticket sizes where both sides are sophisticated.
- The 11-point gap between fair value and orderly liquidation value, and the 15-25 point refurbished premium, bound the principal spread available. Capturing the refurbished premium requires taking possession, testing and warranting, which is not capital-light.
- The mining precedent says lenders do best by NOT liquidating hardware. That argues the lender-repossession supply channel will be smaller than debt totals suggest.

### Gaps
- No source on deposit, escrow or payment terms for cluster-scale GPU trades.
- No source on whether back-to-back (riskless principal) trading is standard for GPU clusters, or on broker gross margins at cluster scale.
- No audited financials for any GPU-specialist reseller.

---

## 8. Signs for and against: older-GPU demand, refresh cycles, capex slowdown, neocloud distress

### Takeaway
As of Nov 2026 the operating market is tight (older GPUs repricing upward, multi-year re-contracts) while the capital market is stressed (CoreWeave CDS above 1,000 bp, failed and cut-price neocloud equity raises, Nvidia leadership shock). The forced-seller wave the desk needs is plausible for 2027-2028 maturities but has not started.

### Cited Findings
**Demand holding (against near-term supply, for residual values)**
- Silicon Data H100 index up nearly 60% year on year to about $3.11; H200 on-demand median up 50.4% in 12 months — [Shattered.io](https://shattered.io/nvidia-older-gpu-rental-prices-h100-3-11-hour-stock-falls-14-percent/)
- CoreWeave: A100 contract into 2029; says its underwriting does not depend on revenue after the first customer term — [Blockspace](https://blockspace.media/insight/coreweave-a100-contract-challenges-gpu-depreciation-model/)
- CoreWeave's 2022-era H100 contracts were rebooked at 95% of original pricing on expiry (reported without a named primary source) — [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/)
- Nvidia interim CEO attributed rising rental prices across generations to token prices falling nearly 60% since May and accelerating usage (secondary write-up) — [Shattered.io](https://shattered.io/nvidia-older-gpu-rental-prices-h100-3-11-hour-stock-falls-14-percent/)
- Sceptic's note: one 2029 A100 contract does not show every old cluster stays utilized — [Blockspace](https://blockspace.media/insight/coreweave-a100-contract-challenges-gpu-depreciation-model/)

**Stress (for future supply, against buyer financing)**
- October 2026: CoreWeave fell about 36%, Nebius 27%, IREN 32%; CoreWeave's 9.75% 2031 bond hit a 15.76% yield; five-year CDS reached 1,115 bp (almost 1,200 bp on 15 Oct per another source); quarterly interest about $640M versus about $128M operating income; Firmus withdrew its IPO; Nscale accepted a $16-19B valuation instead of about $30B — [Top1Markets](https://www.top1markets.com/news/neocloud-stocks-selloff-coreweave-nebius-iren-october-2026); [Capital Relief Substack](https://hodgey1.substack.com/p/the-missing-insurance-market-behind)
- Gartner (14 Oct 2026): more than 80% of neoclouds may cease independent operation by 2030, by consolidation rather than mass bankruptcy; over $3.5T of AI infrastructure spending exposed to impairment by 2030 — [Top1Markets](https://www.top1markets.com/news/neocloud-stocks-selloff-coreweave-nebius-iren-october-2026)
- Musk: more than 200 neoclouds face "guppy-level death and consolidation" — [CNBC, 26 Oct 2026](https://www.cnbc.com/2026/10/26/neocloud-stocks-today-coreweave-nebius-iren-elon-musk.html)
- Customer concentration: $90B of $157B in publicly priced 2026 neocloud deals came from Anthropic — [Top1Markets](https://www.top1markets.com/news/neocloud-stocks-selloff-coreweave-nebius-iren-october-2026)
- Morgan Stanley: free-cash-flow gap near $600B for hyperscalers and neoclouds combined, worst in 2027 — [Top1Markets](https://www.top1markets.com/news/neocloud-stocks-selloff-coreweave-nebius-iren-october-2026)
- Nvidia: Huang resigned 12 Nov 2026; stock closed $125.53 on 20 Nov 2026, down 14% on the day and nearly 50% below its October record; a reported SEC accounting probe (not tied to the move by the source); Nebius gave weak full-year guidance — [Fortune](https://fortune.com/2026/11/12/nvidia-neoclouds-jensen-huang-resignation/); [Shattered.io](https://shattered.io/nvidia-older-gpu-rental-prices-h100-3-11-hour-stock-falls-14-percent/)
- Rubin Ultra/Kyber reported delayed to 2028 — [Shattered.io](https://shattered.io/nvidia-older-gpu-rental-prices-h100-3-11-hour-stock-falls-14-percent/)
- Refresh timing: ITAD trade sources expect AI server decommissioning waves across 2026-2029 — [Re-Teck](https://www.re-teck.com/ai-servers-itad-recycling-wave-2026/)

### Inferences
- The timing risk cuts both ways. If compute stays tight, nobody sells and the desk starves. If credit breaks, supply appears but buyers lose financing and prices gap down, which hurts a back-to-back principal and any residual guarantee the startup arranged.
- A delayed Rubin Ultra and rising Hopper rents lengthen economic life, supporting lender assumptions and reducing demand for residual-value protection at the margin. The same facts reduce turnover.
- The capital-market stress is about refinancing and customer concentration, not about hardware being idle. Distress resolution is therefore likely to be consolidation and site/contract step-ins (per Gartner and the mining precedent), which move clusters without a hardware sale.

### Gaps
- No utilization or idle-capacity statistics for H100/A100 fleets were found.
- Hyperscaler 2027 capex guidance after the November 2026 Nvidia events was not retrieved.
- The Kress and Intrator quotes come from secondary write-ups, not transcripts.

---

## 9. Disintermediation risk and NVIDIA's stance on the secondary market

### Takeaway
I found no NVIDIA buyback, trade-in or allocation-penalty programme for resellers, but NVIDIA is building its own residual support (rent-back floors, insurer talks, equity in a compute broker), which substitutes for third-party remarketing and guarantees. No direct evidence exists on repeat-trade disintermediation; the structure of the market (few large counterparties who already know each other) points to it.

### Cited Findings
- "Nvidia doesn't explicitly block resale," but has "very little reason to actively support a thriving secondary market" [trade press] — [RCR Tech](https://rcrtech.com/semiconductor-news/what-happens-to-old-ai-gpus/)
- Search found no official NVIDIA buyback or trade-in programme for used data center GPUs and no documented allocation penalty for reselling. An unverified vendor claim says NVIDIA's allocation committee distributes GPUs "based on strategic importance rather than highest bidder" — [Introl supply-chain piece](https://introl.com/blog/supply-chain-resilience-managing-gpu-procurement-constrained-markets)
- The Supermicro indictment describes how a front company's orders fed into Nvidia's chip allocation, showing allocation is tied to declared end customers — [Fortune, 12 Nov 2026](https://fortune.com/2026/11/12/jensen-huang-affair-megaspeed-supermicro-nvidia-smuggling-doj/)
- NVIDIA rent-back backstop takes idle capacity back at a fixed rate for a revenue share; about 6.5 GW backstopped per SemiAnalysis — [Data Center Dynamics](https://www.datacenterdynamics.com/en/news/nvidia-acts-as-backstop-for-customer-gpus-in-return-for-cut-of-cloud-revenue/); [SemiAnalysis](https://newsletter.semianalysis.com/p/nvidia-gpu-debt-backstop-unleashes)
- NVIDIA in early talks with insurers (Howden Re) on residual value cover; NVIDIA invested in Hydra Host — [Capital Relief Substack](https://hodgey1.substack.com/p/the-missing-insurance-market-behind); [The Next Web](https://thenextweb.com/news/hydra-host-100m-series-a-nvidia-gpu-ai-factory)
- Neoclouds such as CoreWeave and Lambda are named as buyers of retired hyperscaler H100 fleets; hyperscalers sometimes redeploy fleets internally rather than sell [vendor claims] — [Catalyst Data Solutions](https://www.catalystdatasolutionsinc.com/the-lab/ai-capacity-cascade-hyperscale-gpu-server-upgrades)
- Hyperscalers sell "usually through certified remarketing partners" [vendor] — [Introl](https://introl.com/blog/secondary-gpu-markets-buying-selling-used-hardware-guide-2025)
- Lender default playbook on xAI's $5B facility: take over the cluster in place and rent it to other AI companies until repaid, not sell the hardware — [CipherTalk](https://ciphertalk.substack.com/p/nobody-knows-what-a-used-gpu-cluster)
- OEMs (Dell, HPE, Supermicro) run their own certified-refurbished programmes with 1-2 year warranties — [Introl](https://introl.com/blog/secondary-gpu-markets-buying-selling-used-hardware-guide-2025)

### Inferences
- Large sellers already have contracted remarketing partners and large buyers (neoclouds) are known to them. A new desk is most useful on the first, awkward trade and least defensible afterwards; with tickets of $20M+ a 5-8% fee is a strong incentive to go direct.
- NVIDIA's rent-back keeps idle hardware in place and under NVIDIA's control, shrinking tradeable supply and replacing third-party RVGs for NVIDIA-favoured borrowers. If the backstop's credibility weakens after the leadership change, that reopens room for independent guarantees, but with a weaker NVIDIA the underlying residual risk is also worse.
- The startup has no warranty, software-licence or allocation lever; NVIDIA and the OEMs hold all three. A certified-refurbished standard that the OEM does not recognise competes with OEM-certified refurbished stock.

### Gaps
- No evidence, either way, on how often buyers and sellers bypass brokers after a first trade.
- No primary NVIDIA sales terms retrieved on resale restrictions or allocation consequences for resellers.
- Whether the NVIDIA rent-back and $125B backstop commitments continue unchanged under interim management is unknown.
