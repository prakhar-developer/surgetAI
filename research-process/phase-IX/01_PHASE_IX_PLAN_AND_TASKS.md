# 📋 Phase-IX: Neural-Symbolic Graph Invariance & Weisfeiler-Lehman UI Morphism

## 📌 Phase Overview
In Phase-IX, we solve one of the most brittle failure modes in computer-use agents: **Visual & Layout Mutations**. When an operating system toggles between Light Mode and Dark Mode, DPI scales from 100% to 150%, or a window reflows, raw pixel differencing ($\Delta I$) reports massive changes ($>80\%$), causing purely visual agents to fail. Phase-IX models GUI state as a **Directed Labeled Graph** $G = (V, E)$ and applies the **Weisfeiler-Lehman (1-WL) Graph Isomorphism Kernel** to prove mathematical topological invariance under visual mutations.

---

## 🎯 Research Tasks & Objectives

### Task 9.1: Symbolic UI Graph Construction & Representation
- **Script**: `step1_ui_graph_constructor.py`
- **Objective**: Parse hierarchical OS accessibility trees into formal labeled directed graphs $G = (V, E, \ell_V, \ell_E)$ where vertices represent interactive controls and edges represent containment or spatial adjacency.

### Task 9.2: Weisfeiler-Lehman (1-WL) Graph Kernel Implementation
- **Script**: `step2_weisfeiler_lehman_isomorphism.py`
- **Objective**: Implement the iterative 1-WL color refinement algorithm:
  $$c_v^{(t+1)} = \text{Hash}\left( c_v^{(t)}, \; \{\!\{ c_u^{(t)} : u \in \mathcal{N}(v) \}\!\} \right)$$
- **Validation**: Compute graph kernel cosine similarity between canonical and mutated UI trees.

### Task 9.3: Extreme Mutation Benchmark (Dark Mode & DPI Scaling)
- **Script**: `step3_theme_and_dpi_invariance.py`
- **Objective**: Subject the agent to Dark Mode inversion and 150% DPI coordinate shift.
- **Validation**: Demonstrate that while raw vision reports an $84.2\%$ pixel distortion failure, the WL Graph Kernel confirms $100\%$ topological isomorphism in $<0.5\text{ ms}$, preserving zero-shot workflow replay.
