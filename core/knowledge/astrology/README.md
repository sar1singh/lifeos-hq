# Vedic Astrology Knowledge Module: LifeOS Core

A permanent, deterministic knowledge engine integrating classical Vedic astrology (Parashari & Jaimini principles) with systems engineering, operational strategy, and real-world executive decision-making.

---

## 1. Core Birth Parameters (Lagna & Panchanga Index)

| Parameter | Value | Technical Context |
| :--- | :--- | :--- |
| **Native Name** | Sharwan Singh | Verified against primary birth record |
| **Date of Birth** | September 17, 1990 (17.09.1990) | Monday |
| **Time of Birth** | 13:12:00 IST (UTC +05:30) | Local Mean Time: 12:51:40 LMT |
| **Place of Birth** | Ghaziabad, Uttar Pradesh, India | 28°40' N, 77°25' E (28.6692° N, 77.4538° E) |
| **Ayanamsha** | Lahiri (Chitra Paksha) | 23°43'36" (AstroSage) / 23°43'38" (Swiss Ephemeris) |
| **Ascendant (Lagna)** | **Sagittarius (Dhanu) 01°53'39"** | Mula Nakshatra, Pada 1 (Ketu Lord) |
| **Lagna Lord (Lagnesha)** | **Jupiter (Guru) — EXALTED** | Cancer 12°12'19", 8th House (Pushya 3) |
| **Moon Sign (Rashi)** | **Leo (Simha) 09°47'34"** | Magha Nakshatra, Pada 3 (Ketu Lord) |
| **Sun Sign (Saur Rashi)** | **Virgo (Kanya) 00°26'28"** | Uttaraphalguni Nakshatra, Pada 2 (Sun Lord) |
| **Active Mahadasha** | **Moon (Chandra)** | 2018-07-27 to 2028-07-27 (10 Years) |
| **Active Antardasha** | **Venus (Shukra)** | 2026-05-27 to 2028-01-27 (20 Months) |

---

## 2. Planetary Placements & Harmonic Matrix

| Celestial Body | D1 Sign | Sign Degrees | Absolute Longitude | Nakshatra & Pada | Dignity / Special Status | Bhava Chalit Position | Navamsha (D9) Sign |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Ascendant** | Sagittarius | 01°53'39" | 241.894167° | Mula - 1 | Agni Lagna | House 1 | Aries (Mesh) |
| **Sun** | Virgo | 00°26'28" | 150.441111° | Uttaraphalguni - 2 | Digbala (Directional Strength) | House 10 | Capricorn (Makar) |
| **Moon** | Leo | 09°47'34" | 129.792778° | Magha - 3 | Pitri Throne / Royal Sign | House 9 | Gemini (Mithuna) |
| **Mars** | Taurus | 13°43'28" | 43.724444° | Rohini - 2 | **Vargottama** (Fixed Stamina) | House 6 | Taurus (Vrishabha) |
| **Mercury [R]** | Leo | 15°51'36" | 135.860000° | Purvaphalgini - 1 | **Vargottama** / Retrograde Power | House 9 | Leo (Simha) |
| **Jupiter** | Cancer | 12°12'19" | 102.205278° | Pushya - 3 | **Exalted (Uccha)** in 8th House | House 8 | Libra (Tula) |
| **Venus** | Leo | 18°37'43" | 138.628611° | Purvaphalgini - 2 | Swa-Nakshatra / Aesthetic Triad | House 9 | Virgo (Kanya) - Neecha |
| **Saturn [R]** | Sagittarius | 24°59'04" | 264.984444° | Purvashadha - 4 | Retrograde / Chesta Bala | **House 2 (Dhāna Bhava)** | Scorpio (Vrishchika) |
| **Rahu [R]** | Capricorn | 10°59'43" | 280.995278° | Shravana - 1 | Earth Sign Focus | House 2 | Aries (Mesh) |
| **Ketu [R]** | Cancer | 10°59'43" | 100.995278° | Pushya - 3 | Deep Esoteric Insight | House 8 | Libra (Tula) |

---

## 3. Directory Map & Architecture Index

```text
core/knowledge/astrology/
├── assets/
│   └── SARWAN_SINGH_original_kundli.pdf    <── Original 3-page birth chart PDF
├── data/
│   ├── pdf_parsed_kundli.json              <── 100% Raw OCR & table extraction
│   ├── ai_computed_kundli.json             <── Swiss Ephemeris astronomical calculation
│   └── chart_reconciliation_audit.md       <── Comparative delta & tolerance audit
├── reports/
│   ├── foundation_chart_analysis.md        <── Comprehensive life blueprint & yogas
│   ├── yearly/
│   │   ├── 2026_yearly_overview.md         <── Transition to Moon-Venus & age 36 milestone
│   │   └── 2027_yearly_overview.md         <── Peak Moon-Venus & matrimonial gateway
│   └── monthly/
│       ├── 2026-11_monthly_report.md       <── Mars ingress, direct motion, tactical checklist
│       └── 2026-12_monthly_report.md       <── Solar return to Lagna, Q4 wrap-up, salary push
├── inquiries_and_logs.md                   <── Living Q&A table & tactical decision ledger
└── README.md                               <── This master module specification
```

### Direct Document Links
- **Primary Source Asset:** <a href="assets/SARWAN_SINGH_original_kundli.pdf" target="_blank">SARWAN_SINGH_original_kundli.pdf ↗</a>
- **Raw Parsed Data:** [pdf_parsed_kundli.json](data/pdf_parsed_kundli.json)
- **Swiss Ephemeris Dataset:** [ai_computed_kundli.json](data/ai_computed_kundli.json)
- **Astronomical Audit:** [chart_reconciliation_audit.md](data/chart_reconciliation_audit.md)
- **Foundational Blueprint:** [foundation_chart_analysis.md](reports/foundation_chart_analysis.md)
- **2026 Strategy:** [2026_yearly_overview.md](reports/yearly/2026_yearly_overview.md)
- **2027 Strategy:** [2027_yearly_overview.md](reports/yearly/2027_yearly_overview.md)
- **November 2026 Operations:** [2026-11_monthly_report.md](reports/monthly/2026-11_monthly_report.md)
- **December 2026 Operations:** [2026-12_monthly_report.md](reports/monthly/2026-12_monthly_report.md)
- **Inquiry & Strategy Ledger:** [inquiries_and_logs.md](inquiries_and_logs.md)

---

## 4. How to Log New Inquiries & Maintain Reports

### Logging a New Decision / Strategy Inquiry
1. Open [inquiries_and_logs.md](inquiries_and_logs.md).
2. Append a new row to the table in Section 1 following the schema:
   ```markdown
   | YYYY-MM-DD | Domain | Specific Question | Planetary Timing / Analysis | Actionable Verdict / Strategy | Status |
   ```
3. If the decision requires multi-step analysis, add a numbered sub-section under Section 2 ("In-Depth Operational Case Studies").

### Monthly Report Workflow
At the beginning of each calendar month:
1. Create `reports/monthly/YYYY-MM_monthly_report.md`.
2. Compute planetary transits (*Gochar*) against the native's natal coordinates:
   - Check Mars, Mercury, and Venus motion states (direct vs. retrograde).
   - Check Sun ingress date (shifts every ~30 days around the 14th–16th).
   - Track Jupiter (Leo) and Saturn (Pisces) aspects.
3. Outline a 2-phase operational calendar with clear behavioral Dos and Don'ts.
