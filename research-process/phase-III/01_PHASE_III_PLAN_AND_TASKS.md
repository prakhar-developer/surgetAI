# 🚀 Phase-III: Autonomous Agent Loop, Tool Calling & Self-Healing Recovery

---

## 🎯 Phase-III Ka Objective
Phase-I ne **Eyes & Hands** diye, Phase-II ne **Semantic Memory** di.
Ab Phase-III me hum complete **Autonomous Computer-Use Agent Engine** banayenge jo:
1. **Observe $\to$ Plan $\to$ Act $\to$ Verify** ke continuous loop me execute kare.
2. **Tool Calling** (Structured JSON Actions) aur **State Management** (Task Breadcrumbs) maintain kare.
3. **Tri-Tier Grounding Router** chalaye:
   - Pehle Tier-0 (OS Accessibility) try kare ($<10$ ms).
   - Agar fail ho to Tier-1 (Local OCR) try kare ($50$ ms).
   - Sirf aakhri raste ke roop me Tier-2 (Cloud VLM) ko call kare ($2500$ ms).
4. **Self-Healing Failure Recovery**: Agar koi button click karne par UI freeze ho ya popup modal block kar raha ho, to crash hone ke bajaye agent automatic fallback strategy se recover kare.

---

## 📐 Mathematical Formulation: POMDP & Policy Routing

### 1. Partially Observable Markov Decision Process (POMDP)
Computer-Use environment ko hum formal POMDP se model karte hain:
$$\mathcal{M} = \langle \mathcal{S}, \mathcal{A}, \mathcal{T}, \mathcal{R}, \Omega, \mathcal{O}, \gamma \rangle$$
- $\mathcal{S}$: True hidden OS state (internal memory, active process table).
- $\Omega$: Observable state (Screen pixel tensor $I_t$, Accessibility Tree $\mathcal{T}_{\text{UIA}}$).
- $\mathcal{A}$: Discrete action space $\{\text{CLICK}(x, y), \text{TYPE}(text), \text{PRESS}(key), \text{SCROLL}(dy)\}$.
- $\mathcal{T}(s' \mid s, a)$: State transition probability.

### 2. Confidence-Based Tier Routing
Decision router cost aur confidence ka trade-off optimize karta hai:
$$\text{Tier}^*(e) = \begin{cases} 
\text{Tier-0 (OS UIA)}, & \text{if } P_{\text{UIA}}(e \mid \Omega) \ge 0.85 \\
\text{Tier-1 (Fast OCR)}, & \text{if } P_{\text{UIA}} < 0.85 \text{ and } P_{\text{OCR}}(e) \ge 0.80 \\
\text{Tier-2 (Cloud VLM)}, & \text{otherwise}
\end{cases}$$

### 3. Failure Recovery Policy
Agar action $a_t$ ke baad verification assertion fail hota hai:
$$\Delta I < \tau_{\text{state}} \implies \text{Trigger Recovery Sequence: } \{\text{Dismiss Overlays} \to \text{Scroll Viewport} \to \text{Re-Ground}\}$$

---

## 📋 Phase-III Tasks Checklist

- [ ] **Task 3.1:** End-to-End Agent Loop & Tool Calling (`step1_autonomous_agent_loop.py`).
- [ ] **Task 3.2:** Tri-Tier Grounding Router (`step2_tri_tier_grounding_router.py`).
- [ ] **Task 3.3:** Self-Healing Failure Recovery Engine (`step3_failure_recovery_and_self_healing.py`).
- [ ] **Task 3.4:** Comprehensive Empirical Conclusion & Paper Comparison (`02_PHASE_III_CONCLUSION_AND_FINDINGS.md`).
