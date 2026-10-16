# 📋 Phase-VIII: Statistical Hypothesis Testing, P-Values & Multi-Objective Pareto Frontier

## 📌 Phase Overview
In top-tier peer-reviewed research (NeurIPS, ICLR, CVPR), raw numbers are insufficient without rigorous **inferential statistics** and **ablation analysis**. Phase-VIII performs statistical hypothesis testing across $N=100$ independent trials to formally reject the null hypothesis ($H_0$), compute exact $p$-values, degrees of freedom, confidence intervals, Cohen's $d$ effect sizes, and map the multi-objective **Pareto Optimal Frontier** across Accuracy, Latency, and Cost.

---

## 🎯 Research Tasks & Objectives

### Task 8.1: Statistical Hypothesis Testing & Welch's T-Test
- **Script**: `step1_statistical_hypothesis_testing.py`
- **Objective**: Conduct $N=100$ randomized benchmark trials. Formulate:
  - $H_0: \mu_{\text{Surget}} = \mu_{\text{Baseline}}$ (No difference in latency or accuracy)
  - $H_1: \mu_{\text{Surget}} < \mu_{\text{Baseline}}$ (Surget.AI is statistically faster and more accurate)
- **Computations**: Compute Welch's $t$-statistic, Welch-Satterthwaite degrees of freedom $\nu$, two-tailed $p$-value, $95\%$ Confidence Intervals (CI), and Cohen's $d$ effect size.

### Task 8.2: Multi-Objective Pareto Frontier Optimization
- **Script**: `step2_pareto_frontier_optimizer.py`
- **Objective**: Formulate the multi-objective optimization problem:
  $$\max_{\pi} \left( \mathcal{J}_{\text{accuracy}}(\pi), \; -\mathcal{J}_{\text{latency}}(\pi), \; -\mathcal{J}_{\text{cost}}(\pi) \right)$$
- **Validation**: Prove Pareto dominance ($\pi_{\text{Surget}} \succ \pi_{\text{Baseline}}$) and trace the non-dominated Pareto front.

### Task 8.3: Systematic Ablation Matrix (Component Isolation)
- **Script**: `step3_systematic_ablation_matrix.py`
- **Objective**: Isolate each subsystem to quantify its exact marginal contribution:
  1. Config A: Pure Vision VLM (No UIA, No Memory)
  2. Config B: Vision + Memory (No UIA)
  3. Config C: UIA + Stateless (No Memory)
  4. Config D: Full Surget.AI Stack (UIA + Vision + Memory)
