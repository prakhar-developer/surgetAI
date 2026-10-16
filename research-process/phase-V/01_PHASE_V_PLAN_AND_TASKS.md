# 🎓 Phase-V: Workflow Demonstration Learning & DAG Synthesis (सीखने की क्षमता)

---

## 🎯 Phase-V Ka Objective
Surget.AI ka sabse bada product proposition ye hai:
> *"An AI workforce that learns how a company operates its software by watching an employee do it once."*

Is phase me hum agent ka **Learning Engine (Process Mining & Program Synthesis)** banayenge:
1. **Demonstration Trace Ingestion:** Employee jab mouse ghumata hai aur buttons click karta hai, to OS events (clicks, keystrokes, UIA element trees) record karna.
2. **Noise Filtering & Trajectory Pruning:** Insaan beech me pauses leta hai, cursor hilaata hai, ya galti se misclick karta hai. Denoising algorithm in faltu events ko prune karke clean optimal sequence banata hai.
3. **Parameter Abstraction:** Hardcoded inputs (jaise `"Prakhar"`, `"INV-9902"`, `"₹45,000"`) ko generic variables me abstract karna (`{{customer_name}}`, `{{invoice_id}}`, `{{amount}}`).
4. **DAG Compilation:** Linear clicks ko ek robust, executable **Directed Acyclic Graph (DAG)** me compile karna jisme parallel branches aur verification assertions embedded hon.

---

## 📐 Mathematical & Algorithmic Formulations

### 1. Raw Demonstration Trajectory
$$\mathcal{T}_{\text{raw}} = \left\{ (t_i, a_i, \mathbf{c}_i, \omega_i, \Delta t_i) \right\}_{i=1}^M$$
Where $t_i$ is timestamp, $a_i$ is action type, $\mathbf{c}_i = [x_i, y_i]$ screen coordinates, $\omega_i$ is active window context, and $\Delta t_i$ is dwell time.

### 2. Trajectory Denoising Filter
$$\mathcal{T}_{\text{clean}} = \text{Filter}(\mathcal{T}_{\text{raw}}): \quad \begin{cases}
\text{Prune}, & \text{if } a_i = \text{HOVER} \lor \Delta t_i < 50\text{ ms} \\
\text{Fuse}, & \text{if } a_i = \text{KEYPRESS} \land a_{i-1} = \text{KEYPRESS} \implies \text{TYPE}(\text{string}) \\
\text{Retain}, & \text{if } a_i \in \{\text{CLICK}, \text{SCROLL}, \text{HOTKEY}\}
\end{cases}$$

### 3. Workflow Directed Acyclic Graph (DAG)
$$G = (\mathcal{V}, \mathcal{E})$$
- $\mathcal{V}$: Discrete execution nodes $v_k = \langle \text{Action}, \text{TargetAnchor}, \text{Parameters}, \text{Assertion} \rangle$.
- $\mathcal{E}$: Causal dependency edges $(v_j \to v_k)$ indicating preconditions required before node $v_k$ can fire.

---

## 📋 Phase-V Tasks Checklist

- [ ] **Task 5.1:** Demonstration Trace Recorder (`step1_demonstration_trace_recorder.py`).
- [ ] **Task 5.2:** Trajectory Denoising & Redundancy Pruning (`step2_noise_reduction_and_pruning.py`).
- [ ] **Task 5.3:** DAG Compiler & Parameter Generalization (`step3_dag_compiler_and_parameterization.py`).
- [ ] **Task 5.4:** Empirical Findings & Workflow Synthesis Conclusion (`02_PHASE_V_CONCLUSION_AND_FINDINGS.md`).
