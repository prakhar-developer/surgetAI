# 🧠 Phase-II: Semantic Memory, Embeddings & Fast Workflow Retrieval (दिमाग और याददाश्त)

---

## 🎯 Phase-II Ka Objective
Phase-I me agent ko aankhein (Screen Perception) aur hath (Centroid Actuation) mil gaye.
Lekin agar har bar user bole: *"Rahul ko invoice bhejo"*, aur agent har bar sochne ke liye GPT-4o / Claude ko $3500\text{ ms}$ aur paise de, to agent slow aur mehenga ban jayega.

**Phase-II ka mission:**
Agent ko ek **Semantic Workflow Memory** dena jo:
1. Natural language commands ko **384-dimensional dense vectors (Embeddings)** me badal sake.
2. **Cosine Similarity** se user ke bolne ke tarike aur purane saved workflow ke beech ka semantic match calculate kare.
3. Agar match $\ge 0.85$ ho, to **$0.5\text{ ms}$ me instant cached workflow execute** kar de bina LLM ko call kiye!
4. **FAISS Vector Index** ka use karke $10,000+$ workflows me microsecond lookup achieve kare.

---

## 📐 Mathematical & Algorithmic Formulations

### 1. Dense Semantic Embedding Vector
Kisi bhi text prompt $T$ ko ek embedding function $f_\theta$ ke through continuous dense vector space me map karte hain:
$$\mathbf{v} = f_\theta(T) \in \mathbb{R}^d, \quad d = 384$$

### 2. Cosine Similarity & Angular Distance
Do prompts $A$ (user input) aur $B$ (cached workflow) ke beech ka cosine angle:
$$\cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \cdot \|\mathbf{v}\|_2} = \frac{\sum_{i=1}^d u_i v_i}{\sqrt{\sum_{i=1}^d u_i^2} \sqrt{\sum_{i=1}^d v_i^2}}$$

### 3. Metric Learning: Experiment A (Retrieval Quality)
- **Precision@1:**
  $$\text{P@1} = \frac{\sum_{i=1}^N \mathbb{I}(\text{Top-1 retrieved workflow is ground truth})}{N}$$
- **Mean Reciprocal Rank (MRR):**
  $$\text{MRR} = \frac{1}{|Q|} \sum_{i=1}^{|Q|} \frac{1}{\text{rank}_i}$$

### 4. Memory Scaling: Experiment B (Latency vs Enterprise Size)
Comparing brute-force linear search $O(N \cdot d)$ vs FAISS inverted file index (IVF) $O(\sqrt{N} \cdot d)$ across $N = 10,000$ workflows.

---

## 📋 Phase-II Tasks Checklist

- [ ] **Task 2.1:** Semantic Text Embeddings & Cosine Engine (`step1_embedding_and_cosine_similarity.py`).
- [ ] **Task 2.2:** Semantic Workflow Retrieval & Experiment A Quality Benchmark (`step2_semantic_workflow_retrieval.py`).
- [ ] **Task 2.3:** FAISS Vector Index Scaling & Experiment B Latency Benchmark (`step3_faiss_vector_index_benchmark.py`).
- [ ] **Task 2.4:** Empirical Findings & Mathematical Conclusion (`02_PHASE_II_CONCLUSION_AND_FINDINGS.md`).
