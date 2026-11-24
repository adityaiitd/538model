"""Bottom-up ten-year model for the closest candidate found by the simulation:
contracted onsite power for compute, entered by buying a generator fleet (C1 v3).

Every input is an assumption taken from the research notes or the simulation panels.
Panel figures are simulated estimates, not market data. Nothing here forecasts a real company.

All per-MW figures are per MW sold. Spare units are included in the cost per MW sold.

Run: python3 onsite_power_model.py > model_output.md
"""

YEARS = 10

SCENARIOS = {
    # AI capital spending pauses in years 3-5, prices fall toward the oilfield level,
    # equipment stays expensive, debt is scarce.
    "Downside": dict(
        compute_mw=[30, 80, 150, 150, 150, 220, 280, 320, 350, 370],
        price_k=[42, 42, 38, 32, 30, 30, 30, 30, 30, 30],
        capex_per_mw=2.6, acq_price_per_mw=2.3, opex_k=240,
        debt_share=0.40, rate=0.12, ev_multiple=6.5, promote=0.10,
    ),
    # Panel clearing prices, panel entrant costs, supply catches up from year 4.
    "Base": dict(
        compute_mw=[50, 140, 300, 550, 850, 1150, 1450, 1750, 2000, 2200],
        price_k=[46, 46, 46, 44, 42, 40, 39, 38, 38, 38],
        capex_per_mw=2.1, acq_price_per_mw=2.0, opex_k=220,
        debt_share=0.45, rate=0.10, ev_multiple=9.0, promote=0.12,
    ),
    # Shortage persists, the company reaches incumbent-like cost and borrowing terms.
    "Upside": dict(
        compute_mw=[80, 250, 600, 1200, 2000, 3000, 4000, 5000, 6000, 7000],
        price_k=[48, 48, 48, 47, 46, 45, 44, 43, 42, 42],
        capex_per_mw=1.75, acq_price_per_mw=1.8, opex_k=200,
        debt_share=0.55, rate=0.085, ev_multiple=11.0, promote=0.15,
    ),
}

ACQ_MW = 100             # sellable MW in the fleet bought in year 1
OILFIELD_PRICE_K = 16    # $000 per MW-month on acquired units not yet moved to compute
OILFIELD_UTIL = 0.75
OILFIELD_OPEX_K = 110    # lighter duty than prime power
SGA_FIXED = 14.0         # $M a year
SGA_VAR = 0.02           # share of revenue
DEP_YEARS = 15
TAX = 0.21
STAFF_PER_MW = 0.45      # field crews, per MW sold (panel: 8-12 people per 25 MW block)
STAFF_HQ = 45
AVG_SITE_MW = 75


def run(p, shock=None):
    shock = shock or {}
    rows, net_debt, equity_in, invested, prev_mw, owned = [], 0.0, 0.0, 0.0, 0.0, 0.0
    for y in range(YEARS):
        mw = p["compute_mw"][y] * shock.get("mw_mult", 1.0)
        if y in shock.get("freeze", []):
            mw = prev_mw
        price = p["price_k"][y] * (shock.get("price_mult", 1.0) if y >= shock.get("price_from", 0) else 1.0)
        capex = 0.0
        if y == 0:
            capex += ACQ_MW * p["acq_price_per_mw"]
            owned = ACQ_MW
        build = max(0.0, mw - owned)
        capex += build * p["capex_per_mw"] * shock.get("capex_mult", 1.0)
        owned += build
        idle = max(0.0, owned - mw)
        avg_mw = (mw + prev_mw) / 2
        rev = avg_mw * price * 12 / 1000 * (1 - shock.get("lost_share", 0.0))
        rev += idle * OILFIELD_UTIL * OILFIELD_PRICE_K * 12 / 1000
        opex = avg_mw * p["opex_k"] / 1000 + idle * OILFIELD_UTIL * OILFIELD_OPEX_K / 1000
        sga = SGA_FIXED + SGA_VAR * rev
        ebitda = rev - opex - sga - shock.get("one_off", {}).get(y, 0.0)
        invested += capex
        ebit = ebitda - invested / DEP_YEARS
        interest = net_debt * p["rate"]
        tax = max(0.0, (ebit - interest) * TAX)
        free = ebitda - interest - tax
        new_debt = capex * p["debt_share"]
        gap = capex - new_debt - max(0.0, free)
        if gap > 0:
            equity_in += gap
        else:
            net_debt += gap                  # surplus cash repays debt
        if free < 0:
            equity_in += -free               # losses are funded with equity
        net_debt += new_debt
        ev = max(ebitda, 0.0) * p["ev_multiple"]
        eq = max(ev - net_debt, 0.0)
        gain = max(0.0, eq - equity_in)
        rows.append(dict(
            year=y + 1, mw=mw, sites=max(1, round(mw / AVG_SITE_MW)), price=price, rev=rev,
            ebitda=ebitda, ebit=ebit, capex=capex, invested=invested, net_debt=net_debt,
            equity_in=equity_in, eq=eq, moic=(eq / equity_in if equity_in else 0.0),
            founder=p["promote"] * gain,
            roic=ebit * (1 - TAX) / invested if invested else 0.0,
            staff=round(STAFF_HQ + owned * STAFF_PER_MW),
        ))
        prev_mw = mw
    return rows


def table(rows):
    head = ("| Year | MW sold | Sites | Price $000/MW-month | Revenue | EBITDA | EBITDA margin | Operating margin | "
            "Capex | Capital invested | Net debt | Equity paid in | Staff | ROIC | Equity value | "
            "Value / equity paid in | Founder promote value |")
    out = [head, "|" + "---|" * 17]
    for r in rows:
        m = r["ebitda"] / r["rev"] if r["rev"] else 0
        e = r["ebit"] / r["rev"] if r["rev"] else 0
        out.append(
            f"| {r['year']} | {r['mw']:,.0f} | {r['sites']} | {r['price']:.0f} | {r['rev']:,.0f} | {r['ebitda']:,.0f} | "
            f"{m:.0%} | {e:.0%} | {r['capex']:,.0f} | {r['invested']:,.0f} | {r['net_debt']:,.0f} | "
            f"{r['equity_in']:,.0f} | {r['staff']:,} | {r['roic']:.1%} | {r['eq']:,.0f} | {r['moic']:.1f}x | {r['founder']:,.0f} |")
    return "\n".join(out)


def main():
    print("# Model output: contracted onsite power for compute (C1 v3)\n")
    print("Inputs are assumptions from the research notes and the simulation panels. "
          "Dollar figures are in millions unless stated. Revenue is recognized capacity fees. "
          "Fuel is passed through at cost and excluded. Backlog and contract value are not revenue.\n")
    print("## Inputs\n")
    print("| Input | Downside | Base | Upside |\n|---|---|---|---|")
    labels = [("capex_per_mw", "New-build cost per MW sold, $M"), ("acq_price_per_mw", "Purchase price of acquired fleet per MW, $M"),
              ("opex_k", "Operating cost per MW-year, $000"), ("debt_share", "Debt share of capital spending"),
              ("rate", "Interest rate"), ("ev_multiple", "Enterprise value / EBITDA"), ("promote", "Founder share of gains above equity paid in")]
    for k, lab in labels:
        vals = [SCENARIOS[s][k] for s in ("Downside", "Base", "Upside")]
        fmt = (lambda v: f"{v:.0%}") if k in ("debt_share", "promote") else ((lambda v: f"{v:.1%}") if k == "rate" else (lambda v: f"{v:g}"))
        print(f"| {lab} | " + " | ".join(fmt(v) for v in vals) + " |")
    print(f"| Fleet acquired in year 1, MW | {ACQ_MW} | {ACQ_MW} | {ACQ_MW} |")
    print()
    for name, p in SCENARIOS.items():
        print(f"## {name} case\n")
        print(table(run(p)))
        print()

    base = SCENARIOS["Base"]
    shocks = [
        ("Base case, no shock", {}),
        ("Selling price falls 50% from year 3", dict(price_mult=0.5, price_from=2)),
        ("Equipment prices rise 30%", dict(capex_mult=1.3)),
        ("Largest customer (35% of revenue) lost and not replaced", dict(lost_share=0.35)),
        ("Industry growth halves", dict(mw_mult=0.5)),
        ("Capital markets shut in years 3 and 4", dict(freeze=[2, 3])),
        ("Major deployment fails in year 3 ($60M of damages and rework)", dict(one_off={2: 60.0})),
        ("Permits delayed a year (growth frozen in year 2)", dict(freeze=[1])),
    ]
    print("## Stress tests on the base case\n")
    print("| Shock | Year-5 revenue | Year-5 EBITDA | Year-10 revenue | Year-10 equity value | Year-10 equity paid in | Year-10 net debt / EBITDA |")
    print("|---|---|---|---|---|---|---|")
    for label, s in shocks:
        rows = run(base, s)
        y5, y10 = rows[4], rows[9]
        lev = f"{y10['net_debt'] / y10['ebitda']:.1f}x" if y10["ebitda"] > 0 else "not meaningful"
        print(f"| {label} | {y5['rev']:,.0f} | {y5['ebitda']:,.0f} | {y10['rev']:,.0f} | {y10['eq']:,.0f} | {y10['equity_in']:,.0f} | {lev} |")
    print()

    print("## Revenue stages at base-case unit economics\n")
    print("Price $42,000 per MW-month, operating cost $220,000 per MW-year, new-build cost $2.1M per MW sold, 45% debt.\n")
    print("| Stage | MW sold | Sites at 75 MW | Units delivered (25 MW blocks) | Revenue $M | EBITDA margin | Capital invested $bn | Equity needed $bn | Staff |")
    print("|---|---|---|---|---|---|---|---|---|")
    for label, rev in [("First customer (25 MW)", 12.6), ("$10M", 10.0), ("$100M", 100.0), ("$1bn", 1000.0), ("$10bn", 10000.0), ("$100bn", 100000.0)]:
        mw = rev / (42 * 12 / 1000)
        ebitda = rev - mw * 0.22 - (SGA_FIXED + SGA_VAR * rev)
        cap = mw * 2.1 / 1000
        print(f"| {label} | {mw:,.0f} | {max(1, round(mw / AVG_SITE_MW)):,} | {max(1, round(mw / 25)):,} | {rev:,.0f} | {ebitda / rev:.0%} | "
              f"{cap:,.2f} | {cap * 0.55:,.2f} | {round(STAFF_HQ + mw * STAFF_PER_MW):,} |")


if __name__ == "__main__":
    main()
