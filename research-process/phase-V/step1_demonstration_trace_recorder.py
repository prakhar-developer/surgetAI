"""
Surget.AI Research Process - Phase V: Task 5.1
Script: step1_demonstration_trace_recorder.py
Objective: Ingest & Record Raw Human Demonstration Trajectory Telemetry
"""

import sys
import os
import time
import json

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def generate_raw_human_demonstration():
    """
    Simulates raw recorded events from a human demonstrating 'Create New Vendor':
    Includes human noise (cursor hover jitter, long idle pauses, character-by-character typing).
    """
    t_base = time.time()
    raw_events = [
        {"id": 1, "t": t_base + 0.05, "type": "mouse_move", "coords": [100, 150], "dwell_ms": 20},
        {"id": 2, "t": t_base + 0.12, "type": "mouse_move", "coords": [102, 153], "dwell_ms": 15},
        {"id": 3, "t": t_base + 0.35, "type": "mouse_hover", "coords": [105, 155], "dwell_ms": 120},
        {"id": 4, "t": t_base + 0.50, "type": "click", "coords": [110, 160], "target": "VendorsTab", "element_type": "TabItem"},
        {"id": 5, "t": t_base + 2.80, "type": "idle_pause", "coords": [110, 160], "dwell_ms": 2300}, # 2.3s human hesitation
        {"id": 6, "t": t_base + 3.05, "type": "mouse_move", "coords": [250, 210], "dwell_ms": 30},
        {"id": 7, "t": t_base + 3.20, "type": "click", "coords": [260, 220], "target": "NewVendorButton", "element_type": "Button"},
        {"id": 8, "t": t_base + 3.60, "type": "click", "coords": [350, 310], "target": "VendorNameInput", "element_type": "Edit"},
        # Human typing "Global Corp" character by character
        {"id": 9, "t": t_base + 3.80, "type": "keypress", "key": "G", "field": "VendorNameInput"},
        {"id": 10, "t": t_base + 3.92, "type": "keypress", "key": "l", "field": "VendorNameInput"},
        {"id": 11, "t": t_base + 4.05, "type": "keypress", "key": "o", "field": "VendorNameInput"},
        {"id": 12, "t": t_base + 4.18, "type": "keypress", "key": "b", "field": "VendorNameInput"},
        {"id": 13, "t": t_base + 4.30, "type": "keypress", "key": "a", "field": "VendorNameInput"},
        {"id": 14, "t": t_base + 4.42, "type": "keypress", "key": "l", "field": "VendorNameInput"},
        {"id": 15, "t": t_base + 4.55, "type": "keypress", "key": " ", "field": "VendorNameInput"},
        {"id": 16, "t": t_base + 4.68, "type": "keypress", "key": "C", "field": "VendorNameInput"},
        {"id": 17, "t": t_base + 4.80, "type": "keypress", "key": "o", "field": "VendorNameInput"},
        {"id": 18, "t": t_base + 4.92, "type": "keypress", "key": "r", "field": "VendorNameInput"},
        {"id": 19, "t": t_base + 5.05, "type": "keypress", "key": "p", "field": "VendorNameInput"},
        {"id": 20, "t": t_base + 5.50, "type": "mouse_hover", "coords": [500, 600], "dwell_ms": 250},
        {"id": 21, "t": t_base + 5.80, "type": "click", "coords": [520, 620], "target": "SaveVendorButton", "element_type": "Button"}
    ]
    return raw_events

def run_recorder_benchmark():
    print("=" * 65)
    print("🔬 SURGET.AI PHASE-V: DEMONSTRATION TRACE RECORDER")
    print("=" * 65)
    
    t0 = time.perf_counter()
    raw_trace = generate_raw_human_demonstration()
    recording_time = (time.perf_counter() - t0) * 1000
    
    print(f"\n[+] Raw Human Demonstration Ingested in {recording_time:.2f} ms")
    print(f"[+] Total Raw Telemetry Events: {len(raw_trace)}")
    
    # Event breakdown
    event_counts = {}
    for ev in raw_trace:
        event_counts[ev["type"]] = event_counts.get(ev["type"], 0) + 1
        
    print("\n📊 RAW EVENT DISTRIBUTION:")
    for ev_type, count in event_counts.items():
        print(f"  • {ev_type:<15}: {count} events ({count/len(raw_trace)*100:.1f}%)")
        
    # Save raw trace artifact
    out_file = os.path.join(os.path.dirname(__file__), "raw_demonstration_trace.json")
    with open(out_file, "w") as f:
        json.dump(raw_trace, f, indent=2)
    print(f"\n[✓] Raw Trace Artifact Saved: {out_file}")
    print("=" * 65)
    
    return {
        "total_events": len(raw_trace),
        "event_distribution": event_counts
    }

if __name__ == "__main__":
    run_recorder_benchmark()
