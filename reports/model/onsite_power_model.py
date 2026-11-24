"""Bottom-up ten-year model for the closest candidate: contracted onsite power for compute,
entered by buying a generator fleet. All inputs are assumptions drawn from the research notes
and the simulation panels. Nothing here is a forecast of a real company.

Run: python3 onsite_power_model.py > model_output.md
"""

SCENARIOS = {
    "Downside": dict(
        # AI capital spending pauses for two years from year 3; prices fall to the oilfield-plus level
        compute_mw=[30, 80, 150, 150, 150, 220, 280, 320, 350, 370],
        price_k=[40, 40, 36, 30, 30, 30, 30, 30, 30, 30],       # $000 per MW-month
        capex_per_mw=2.4, acq_price_per_mw=2.2, opex_k=240,
        debt_share=0.40, rate=0.12, ev_multiple=6.5, founder_start=0.10,
    ),
    "Base": dict(
        compute_mw=[50, 140, 300, 550, 850, 1150, 1450, 1750, 2000, 2200],
        price_k=[45, 45, 45, 44, 42, 40, 39, 38, 38, 38],
        capex_per_mw=2.0, acq_price_per_mw=1.9, opex_k=220,
        debt_share=0.45, rate=0.10, ev_multiple=9.0, founder_start=0.12,
    ),
    "Upside": dict(
        compute_mw=[80, 250, 600, 1200, 2000, 3000, 4000, 5000, 6000, 7000],
        price_k=[48, 48, 48, 47, 46, 45, 44, 43, 42, 42],
        capex_per_mw=1.75, acq_price_per_mw=1.7, opex_k=200,
        debt_share=0.55, rate=0.085, ev_multiple=11.0, founder_start=0.15,
    ),
}

ACQ_MW = 100             # fleet bought in year 1
OILFIELD_PRICE_K = 16    # $000 per MW-month earned by acquired units not yet moved to compute
OILFIELD_UTIL = 0.75
SPARE_RATIO = 1.25       # installed MW per MW sold (spare units)
SGA_FIXED = 14.0         # $M a year
SGA_VAR = 0.02           # share of revenue
DEP_YEARS = 15
TAX = 0.21
STAFF_PER_MW = 0.40
STAFF_HQ = 45
AVG_SITE_MW = 75


def run(p, shock=None):
    shock = shock or {}
    rows = []
    net_debt = 0.0
    equity_in = 0.0
    invested = 0.0
    founder = p["founder_start"]
    installed = 0.0
    prev_mw = 0.0
    for y in range(10):
        mw = p["compute_mw"][y] * shock.get("mw_mult", 1.0)
        if shock.get("freeze") and y in shock["freeze"]:
            mw = prev_mw
        price = p["price_k"][y] * shock.get("price_mult", 1.0)
        capex_mw = p["capex_per_mw"] * shock.get("capex_mult", 1.0)
        need_installed = max(mw * SPARE_RATIO, ACQ_MW)
        build = max(0.0, need_installed - max(installed, ACQ_MW))
        capex = build * capex_mw
        if y == 0:
            capex += ACQ_MW * p["acq_price_per_mw"]
            installed = ACQ_MW
        installed = max(installed, need_installed)
        idle_acq = max(0.0, ACQ_MW - mw * SPARE_RATIO)
        avg_mw = (mw + prev_mw) / 2 if y > 0 else mw / 2
        rev_compute = avg_mw * price * 12 / 1000 * (1 - shock.get("lost_share", 0.0))
        rev_oil = idle_acq * OILFIELD_UTIL * OILFIELD_PRICE_K * 12 / 1000
        revenue = rev_compute + rev_oil
        opex = (avg_mw * SPARE_RATIO + idle_acq * OILFIELD_UTIL) * p["opex_k"] / 1000
        sga = SGA_FIXED + SGA_VAR * revenue
        ebitda = revenue - opex - sga - shock.get("one_off", {}).get(y, 0.0)
        invested += capex
        dep = invested / DEP_YEARS
        ebit = ebitda - dep
        interest = net_debt * p["rate"]
        cash_after_interest = ebitda - interest - max(0.0, (ebit - interest) * TAX)
        new_debt = capex * p["debt_share"]
        gap = capex - new_debt - max(0.0, cash_after_interest)
        new_equity = max(0.0, gap)
        if gap < 0:
            net_debt += gap  # surplus cash pays down debt
        net_debt += new_debt
        ev = max(ebitda, 0.0) * p["ev_multiple"]
        eq_value = max(ev - net_debt, 0.0)
        if new_equity > 0 and y > 0:
            post = max(eq_value, new_equity * 1.5)
            founder *= (1 - new_equity / post)
        equity_in += new_equity
        roic = ebit * (1 - TAX) / invested if invested else 0.0
        rows.append(dict(
            year=y + 1, mw=mw, customers=max(1, round(mw / AVG_SITE_MW)) if mw else 0,
            price=price, revenue=revenue, ebitda=ebitda, ebit=ebit, capex=capex,
            invested=invested, net_debt=net_debt, equity_in=equity_in, ev=ev,
            eq_value=eq_value, founder=founder, founder_value=founder * eq_value,
            roic=roic, staff=round(STAFF_HQ + installed * STAFF_PER_MW),
        ))
        prev_mw = mw
    return rows


def table(rows):
    out = ["| Year | MW sold | Sites | $000/MW-mo | Revenue $M | EBITDA $M | EBITDA % | EBIT % | Capex $M | Capital invested $M | Net debt $M | Equity raised $M | Staff | ROIC | Equity value $M | Founder % | Founder stake $M |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        m = r["ebitda"] / r["revenue"] if r["revenue"] else 0
        e = r["ebit"] / r["revenue"] if r["revenue"] else 0
        out.append("| {year} | {mw:,.0f} | {customers} | {price:.0f} | {revenue:,.0f} | {ebitda:,.0f} | {m:.0%} | {e:.0%} | {capex:,.0f} | {invested:,.0f} | {net_debt:,.0f} | {equity_in:,.0f} | {staff:,} | {roic:.1%} | {eq_value:,.0f} | {founder:.1%} | {founder_value:,.0f} |".format(m=m, e=e, **r))
    return "\n".join(out)


if __name__ == "__main__":
    print("# Model output: contracted onsite power for compute\n")
    print("Inputs are assumptions from the research notes and simulation panels. Dollar figures in millions unless stated.\n")
    for name, p in SCENARIOS.items():
        print(f"## {name} case\n")
        print(table(run(p)))
        print()
    base = SCENARIOS["Base"]
    ref = run(base)
    shocks = {
        "Selling price falls 50% from year 3": dict(price_mult=1.0),
        "Engine and equipment prices rise 30%": dict(capex_mult=1.3),
        "Largest customer (35% of revenue) lost, not replaced": dict(lost_share=0.35),
        "Industry growth halves (half the MW)": dict(mw_mult=0.5),
        "Capital markets shut for years 3-4 (no growth)": dict(freeze=[2, 3]),
        "Major deployment fails in year 3 ($60M damages and rework)": dict(one_off={2: 60.0}),
    }
    print("## Stress tests on the base case\n")
    print("| Shock | Year-5 revenue $M | Year-5 EBITDA $M | Year-10 revenue $M | Year-10 equity value $M | Year-10 net debt / EBITDA |")
    print("|---|---|---|---|---|---|")
    def line(label, rows):
        y5, y10 = rows[4], rows[9]
        lev = y10["net_debt"] / y10["ebitda"] if y10["ebitda"] > 0 else float("inf")
        print(f"| {label} | {y5['revenue']:,.0f} | {y5['ebitda']:,.0f} | {y10['revenue']:,.0f} | {y10['eq_value']:,.0f} | {lev:.1f}x |")
    line("Base case, no shock", ref)
    for label, s in shocks.items():
        if label.startswith("Selling price"):
            p2 = dict(base); p2["price_k"] = [x if i < 2 else x * 0.5 for i, x in enumerate(base["price_k"])]
            line(label, run(p2))
        else:
            line(label, run(base, s))
    print()
    print("## Revenue stages\n")
    print("| Stage | MW sold at $42,000 per MW-month | Sites | Installed MW | Capital at $2.0M per MW $bn | Staff |")
    print("|---|---|---|---|---|---|")
    for label, rev in [("First customer", 13.5), ("$10M", 10), ("$100M", 100), ("$1bn", 1000), ("$10bn", 10000), ("$100bn", 100000)]:
        mw = rev / (42 * 12 / 1000)
        print(f"| {label} | {mw:,.0f} | {max(1, round(mw / AVG_SITE_MW)):,} | {mw * SPARE_RATIO:,.0f} | {mw * SPARE_RATIO * 2.0 / 1000:,.2f} | {round(STAFF_HQ + mw * SPARE_RATIO * STAFF_PER_MW):,} |")
