# 📘 Phase-I: Sensory Perception & Deterministic GUI Grounding (आँखें और हाथ)

---

## 🎯 Phase-I Ka Objective
Is phase me hum AI agent ka **Foundation (Pehla Kadam)** bana rahe hain. 
Bina kisi mehenge AI model ko call kiye, agent ko:
1. **Screen ko dekhna aana chahiye (Perception)**: Screen ko ek fast NumPy array / tensor me convert karna.
2. **Screen par elements dhoondhna aana chahiye (Grounding)**: Windows OS ke Accessibility Tree (UIA) se button aur input fields ke exact pixel coordinates nikaalna ($<10$ ms me).
3. **Action execute karna aana chahiye (Actuation)**: Coordinates par click karna ya keyboard inputs bhejna.
4. **Action verify karna aana chahiye (State Verification)**: Click ke baad screen par badlaav (motion/visual diff) calculate karna.

---

## 📐 Mathematical & Algorithmic Foundation

### 1. Screen as a 3D Tensor
Screen resolution $W \times H$ (e.g., $1920 \times 1080$) ko RGB color space me represent kiya jata hai:
$$I \in \mathbb{R}^{H \times W \times C}, \quad C \in \{R, G, B\}, \quad I(y, x, c) \in [0, 255]$$

### 2. Coordinate Normalization
Alag-alag screens (1080p, 2K, 4K) par agent confuse na ho, iske liye standard $[0, 1000]$ normalized space use hota hai:
$$x_{\text{norm}} = \frac{x_{\text{pixel}}}{W} \times 1000, \qquad y_{\text{norm}} = \frac{y_{\text{pixel}}}{H} \times 1000$$

### 3. Bounding Box Centroid (Target Vector)
Jab OS element ka bounding box deta hai $\mathcal{B} = [x_{\min}, y_{\min}, x_{\max}, y_{\max}]$, tab click target centroid formula:
$$\mathbf{c} = \left[ \frac{x_{\min} + x_{\max}}{2}, \; \frac{y_{\min} + y_{\max}}{2} \right]$$

### 4. Visual State Change Difference ($\Delta I$)
Action verify karne ke liye dono frames ka Mean Absolute Difference compute hota hai:
$$\Delta I = \frac{1}{H \cdot W} \sum_{y=1}^{H} \sum_{x=1}^{W} |I_{t}(y, x) - I_{t-1}(y, x)|$$
Agar $\Delta I > \tau$ (threshold), to state change confirm ho gaya!

---

## 📋 Phase-I Tasks Checklist

- [x] **Task 1.1:** Screen Grabber Script (`step1_screen_perception.py`) — Screen capture latency benchmark.
- [x] **Task 1.2:** Windows UIA Grounding (`step2_windows_uia_grounding.py`) — Calculator UI elements scan & instant click.
- [x] **Task 1.3:** Frame Differencing Verification (`step3_state_verification_diff.py`) — Visual difference check without LLM.
- [ ] **Task 1.4:** Results & Mathematical Benchmark Analysis (`02_PHASE_I_CONCLUSION_AND_FINDINGS.md`).
