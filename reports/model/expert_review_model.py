"""Bottom-up model for the second study's pick: expert review of long agent runs for AI labs (F1, final design).

Every input is an assumption taken from the research notes or the simulation panels.
Panel figures are simulated estimates, not market data. Nothing here forecasts a real company.

Revenue is gross billings recognized as principal. Gross profit is revenue less reviewer pay.

Run: python3 expert_review_model.py > expert_review_output.md
"""

# Quarterly gross revenue for the first six quarters, $M. Low and high are the delivery panel's
# round-two cases. Base is the midpoint of that panel's base case (7.5 in quarter six) and the
# fresh round-three panel's base case (4.5 in quarter six).
QUARTERS = {
    "Downside": [0.0, 0.15, 0.4, 0.9, 1.2, 1.5],
    "Base":     [0.04, 0.35, 1.3, 2.75, 4.25, 6.0],
    "Upside":   [0.3, 1.5, 4.5, 9.5, 14.0, 17.0],
}
PROB = {"Downside": 0.35, "Base": 0.50, "Upside": 0.15}

# Annual gross revenue for years 1-10, $M. Years 1-3 follow the panels. Years 4-10 are the
# founder's own extension: the downside is wound down, the base grows then flattens as model
# judges take routine review, the upside follows the panels' "year five if it works" range.
YEARS = {
    "Downside": [1.45, 5.0, 7.5, 6.0, 4.0, 0, 0, 0, 0, 0],
    "Base":     [4.4, 27.0, 45.0, 62.0, 75.0, 82.0, 86.0, 88.0, 90.0, 90.0],
    "Upside":   [15.8, 71.0, 122.0, 180.0, 230.0, 265.0, 290.0, 305.0, 315.0, 320.0],
}
GROSS_MARGIN = {  # share of revenue left after reviewer pay
    "Downside": [0.20, 0.22, 0.24, 0.24, 0.24, 0, 0, 0, 0, 0],
    "Base":     [0.23, 0.26, 0.28, 0.29, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30],
    "Upside":   [0.24, 0.28, 0.30, 0.31, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32],
}
FIXED_OPEX = {    # team, quality system, security, sales, $M a year
    "Downside": [3.0, 3.5, 3.0, 2.0, 1.0, 0, 0, 0, 0, 0],
    "Base":     [3.5, 6.5, 9.0, 11.0, 12.5, 13.5, 14.0, 14.5, 15.0, 15.0],
    "Upside":   [4.5, 11.0, 18.0, 25.0, 31.0, 35.0, 38.0, 40.0, 41.0, 42.0],
}
WORKING_CAPITAL_PER_REVENUE = 0.19   # panel: $1.9M per $10M of billing
REVENUE_PER_STAFF = 1.6              # $M of gross revenue per employee (panel precedent: about 30 staff at $100M is far higher)
EV_PER_GROSS = {"Downside": 0.0, "Base": 1.0, "Upside": 2.5}   # panel: $40M of revenue is worth $25-50M in a normal market, $100-180M today
FOUNDER_STAKE = {"Downside": 0.55, "Base": 0.45, "Upside": 0.38}
REVIEW_PRICE = 420                   # $ per accepted review at a lab (round-three buyer)
HOURLY_PRICE = 145                   # $ per billed hour (round-two rate card)


def annual(name):
    rows, cum_cash, peak = [], 0.0, 0.0
    prev_wc = 0.0
    for y in range(10):
        rev = YEARS[name][y]
        gp = rev * GROSS_MARGIN[name][y]
        ebitda = gp - FIXED_OPEX[name][y]
        wc = rev * WORKING_CAPITAL_PER_REVENUE
        cash = ebitda - (wc - prev_wc)
        prev_wc = wc
        cum_cash += cash
        peak = min(peak, cum_cash)
        rows.append(dict(year=y + 1, rev=rev, gp=gp, gm=GROSS_MARGIN[name][y], ebitda=ebitda,
                         wc=wc, cash=cash, cum=cum_cash, peak=-peak,
                         reviews=rev * 1e6 / REVIEW_PRICE, hours=rev * 1e6 / HOURLY_PRICE,
                         staff=round(8 + rev / REVENUE_PER_STAFF) if rev else 0,
                         value=rev * EV_PER_GROSS[name],
                         founder=rev * EV_PER_GROSS[name] * FOUNDER_STAKE[name]))
    return rows


def main():
    print("# Model output: expert review of long agent runs for AI labs\n")
    print("Inputs are assumptions from the research notes and the simulation panels. Dollar figures in millions unless stated. "
          "Revenue is gross billings. Orders are weekly and can be stopped on 30 days' notice, so none of this is contracted.\n")

    print("## First six quarters\n")
    print("| Case | Probability | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Year one | Trailing twelve months at month 18 | Annualized rate at month 18 |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    exp_ttm = exp_ann = 0.0
    for name, q in QUARTERS.items():
        ttm, ann = sum(q[2:6]), q[5] * 4
        exp_ttm += PROB[name] * ttm
        exp_ann += PROB[name] * ann
        print(f"| {name} | {PROB[name]:.0%} | " + " | ".join(f"{v:.2f}" for v in q) + f" | {sum(q[:4]):.1f} | {ttm:.1f} | {ann:.0f} |")
    print(f"| Probability-weighted | | | | | | | | | {exp_ttm:.1f} | {exp_ann:.0f} |")
    print()

    for name in YEARS:
        print(f"## {name} case, ten years\n")
        print("| Year | Gross revenue | Gross margin | Gross profit | Fixed costs | EBITDA | EBITDA margin | Working capital | Cash flow | Cumulative cash | Peak cash need | Accepted reviews (000) | Staff | Company value | Founder stake | Founder value |")
        print("|" + "---|" * 16)
        for r in annual(name):
            em = r["ebitda"] / r["rev"] if r["rev"] else 0
            print(f"| {r['year']} | {r['rev']:.1f} | {r['gm']:.0%} | {r['gp']:.1f} | {FIXED_OPEX[name][r['year']-1]:.1f} | {r['ebitda']:.1f} | {em:.0%} | "
                  f"{r['wc']:.1f} | {r['cash']:.1f} | {r['cum']:.1f} | {r['peak']:.1f} | {r['reviews']/1000:.0f} | {r['staff']} | "
                  f"{r['value']:.0f} | {FOUNDER_STAKE[name]:.0%} | {r['founder']:.0f} |")
        print()

    print("## Revenue stages\n")
    print("| Stage | Accepted reviews a year at $420 | Or billed hours at $145 | Reviewers active each week at 5 hours | Buyers | Gross margin | Working capital $M | Staff |")
    print("|---|---|---|---|---|---|---|---|")
    stages = [("First customer", 0.25, "1 trial", 0.20), ("$10M", 10, "2 labs, 3 smaller", 0.24), ("$40M", 40, "3 labs, 6-9 smaller", 0.27),
              ("$100M", 100, "4-5 labs, 15+ smaller", 0.30), ("$1bn", 1000, "Not reachable: exceeds the review budget the panels see", 0.30)]
    for label, rev, buyers, gm in stages:
        hours = rev * 1e6 / HOURLY_PRICE
        print(f"| {label} | {rev*1e6/REVIEW_PRICE:,.0f} | {hours:,.0f} | {hours/52/5:,.0f} | {buyers} | {gm:.0%} | {rev*WORKING_CAPITAL_PER_REVENUE:.1f} | {round(8 + rev/REVENUE_PER_STAFF)} |")
    print()

    print("## Stress tests on the base case, year three\n")
    base = annual("Base")[2]
    print("| Shock | Gross revenue | Gross profit | EBITDA |")
    print("|---|---|---|---|")
    fixed = FIXED_OPEX["Base"][2]
    def row(label, rev, gm):
        print(f"| {label} | {rev:.1f} | {rev*gm:.1f} | {rev*gm - fixed:.1f} |")
    row("Base case, no shock", base["rev"], 0.28)
    row("Largest buyer (45% of revenue) pauses for the year", base["rev"] * 0.55, 0.28)
    row("Price per review falls 50%, reviewer pay falls 30%", base["rev"] * 0.5, 1 - 0.72 * 0.7 / 0.5)
    row("Reviewer pay rises 30% with no price increase", base["rev"], 1 - 0.72 * 1.3)
    row("Model judges take 70% of volume", base["rev"] * 0.30, 0.28)
    row("Market growth halves (half the revenue)", base["rev"] * 0.5, 0.28)


if __name__ == "__main__":
    main()
