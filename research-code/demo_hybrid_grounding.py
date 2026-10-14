"""
Proof of Concept Demo: Hybrid UI Grounding & Workflow Memory
-------------------------------------------------------------
This script demonstrates the two core concepts of our research:
1. Tier-0 Deterministic Grounding: Finding UI elements directly through OS
   Accessibility APIs (pywinauto) with ZERO neural network latency.
2. Fast Dirty-Region Detection: Detecting only changed parts of the screen
   using OpenCV in ~10 milliseconds (avoiding full-screen VLM re-parsing).
3. Workflow Memory Cache: Saving element signatures for instant deterministic replay.
"""

import time
import mss
import numpy as np
import cv2
from pywinauto import Desktop

def test_tier0_grounding():
    print("=" * 60)
    print("TEST 1: TIER-0 DETERMINISTIC OS GROUNDING (ZERO-LLM)")
    print("=" * 60)
    start_time = time.time()
    
    desktop = Desktop(backend="uia")
    windows = desktop.windows()
    
    elapsed_ms = (time.time() - start_time) * 1000
    print(f"[OK] Discovered {len(windows)} active desktop windows in {elapsed_ms:.2f} ms!")
    
    # Print top 5 visible windows with their process and bounds
    print("\nSample Active Windows discovered with 100% exact coordinates:")
    count = 0
    for w in windows:
        try:
            title = w.window_text()
            if title.strip():
                rect = w.rectangle()
                print(f"  - Window: '{title[:40]}' | Bounds: (L:{rect.left}, T:{rect.top}, R:{rect.right}, B:{rect.bottom})")
                count += 1
                if count >= 5:
                    break
        except Exception:
            continue
    print(f"\n>> Advantage: 100% exact coordinates, no VLM hallucination, <{elapsed_ms:.1f}ms latency.")

def test_screen_grab_and_dirty_region():
    print("\n" + "=" * 60)
    print("TEST 2: FAST SCREEN CAPTURE & DIRTY REGION DETECTION")
    print("=" * 60)
    
    try:
        with mss.MSS() as sct:
            monitor = sct.monitors[1] if len(sct.monitors) > 1 else sct.monitors[0]
            t0 = time.time()
            frame1 = np.array(sct.grab(monitor))
            grab_time_ms = (time.time() - t0) * 1000
            print(f"[OK] Full screen captured in {grab_time_ms:.2f} ms via mss!")
            time.sleep(0.05)
            frame2 = np.array(sct.grab(monitor))
    except Exception as e:
        print(f"[NOTE] Headless/background session detected ({e}). Using simulated high-res frames for benchmarking:")
        t0 = time.time()
        frame1 = np.zeros((1080, 1920, 3), dtype=np.uint8)
        frame2 = frame1.copy()
        # simulate a dirty region (e.g. a dropdown menu appearing at 400,200)
        cv2.rectangle(frame2, (400, 200), (600, 450), (255, 255, 255), -1)
        grab_time_ms = (time.time() - t0) * 1000
        print(f"[OK] 1080p frame buffer initialized in {grab_time_ms:.2f} ms.")

    # Compute pixel difference (Dirty Region)
    t_diff = time.time()
    if len(frame1.shape) == 3 and frame1.shape[2] == 4:
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGRA2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGRA2GRAY)
    elif len(frame1.shape) == 3:
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    else:
        gray1, gray2 = frame1, frame2

    diff = cv2.absdiff(gray1, gray2)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    non_zero_count = np.count_nonzero(thresh)
    diff_time_ms = (time.time() - t_diff) * 1000

    print(f"[OK] Frame differencing completed in {diff_time_ms:.2f} ms.")
    print(f"     Changed pixels detected: {non_zero_count}")
    print(">> Advantage: If screen has not changed or only changed by 5%, we avoid expensive VLM calls completely!")

def test_workflow_memory():
    print("\n" + "=" * 60)
    print("TEST 3: WORKFLOW MEMORY LOOKUP (O(1) CACHED REPLAY)")
    print("=" * 60)
    
    # Mock Workflow Memory Store
    memory_store = {
        "export_pdf_workflow": [
            {
                "step": 1,
                "target_element": "FileMenu",
                "action": "click",
                "verified_anchor": {"uia_id": "FileTab", "fallback_coords": [45, 70]},
                "assertion": {"expected_window": "BackstageView"}
            },
            {
                "step": 2,
                "target_element": "ExportButton",
                "action": "click",
                "verified_anchor": {"uia_id": "ExportTab", "fallback_coords": [45, 210]},
                "assertion": {"expected_window": "ExportOptions"}
            }
        ]
    }
    
    t_lookup = time.time()
    steps = memory_store.get("export_pdf_workflow", [])
    lookup_time_ms = (time.time() - t_lookup) * 1000
    
    print(f"[OK] Retrieved cached execution DAG ({len(steps)} steps) in {lookup_time_ms:.3f} ms!")
    for s in steps:
        print(f"  Step {s['step']}: Action='{s['action']}' on target='{s['target_element']}' -> UIA ID='{s['verified_anchor']['uia_id']}'")
    print("\n>> Result: Zero VLM calls required on repeated workflows. Real-time deterministic execution!")

if __name__ == "__main__":
    test_tier0_grounding()
    test_screen_grab_and_dirty_region()
    test_workflow_memory()
