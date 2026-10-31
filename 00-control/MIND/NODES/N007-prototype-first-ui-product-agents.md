# N007: Prototype-First Multi-Agent Architecture (Product + UI Designer)
*Captured: 2026-09-24 | Type: INSIGHT | Status: ACTIONABLE*
*Tags: agents, product-management, ui-ux, prototyping, hermes, paperclip, systems*

---

## 1. Raw Core Insight
Coding directly on a live production web dashboard without upfront UI research and functional specs causes endless churn, small font bugs, broken layouts, and misalignment with actual agent platforms.
The system needs a clear separation of concerns before code is touched:
1. **UI Designer Agent:** Researches what real-world interfaces (Nous Research Hermes Web Dashboard, Paperclip AI company orchestrator) actually look like, what capabilities and toggles they expose, and produces high-fidelity interactive visual prototypes.
2. **Product Agent (Product Architect):** Bridges the founder's unique polymathic use case (orchestrating ThinkLate YouTube, Off Script, ThinkLate SaaS/utilities, LifeOS routines, PaisaVault) with those agent capabilities into structured functional specs.
3. **Review & Approval Gate:** The founder iterates and approves the prototype *before* any production frontend/backend engineering begins.

---

## 2. Connections to Existing Graph
- **Connects to N005 (Proactive AI Director):** The director shouldn't just push code; it must orchestrate specialized agents (Product → Designer → Engineer) so the founder only reviews tangible prototypes.
- **Connects to N001 (Interconnected System):** Paperclip's company/org model maps directly to the user's multi-repo portfolio (each repo is a venture department).
- **Connects to N006 (Polymath Identity):** A polymath needs a cockpit tailored to multi-venture switching, requiring a deliberate Product Agent to design the unified view.

---

## 3. Immediate Action Items
- Formalize the **Product Agent** (`product-architect`) and **UI Designer Agent** (`ui-designer`).
- Conduct deep teardown of Hermes Web Dashboard and Paperclip UI options.
- Build an interactive, self-contained prototype preview for founder sign-off before making any further edits to `agent-os`.
