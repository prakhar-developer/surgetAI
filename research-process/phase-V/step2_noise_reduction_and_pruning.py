"""
Surget.AI Research Process - Phase V: Task 5.2
Script: step2_noise_reduction_and_pruning.py
Objective: Clean & Prune Raw Telemetry Trajectory via Algorithmic Heuristics
Formula: Filter(T_raw) -> T_clean: Discard Hover/Move, Compress Keypress Streams
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

def prune_and_denoise_trace(raw_events):
    """
    Applies the Surget.AI Denoising Filter:
    1. Discard non-actuating events (mouse_move, mouse_hover, idle_pause).
    2. Fuse sequential keypress events targeting the same input field into one atomic string typing step.
    3. Retain intentful clicks and window changes.
    """
    clean_steps = []
    current_text_buffer = ""
    current_field = None
    
    for ev in raw_events:
        ev_type = ev["type"]
        
        # Rule 1: Keypress Aggregator
        if ev_type == "keypress":
            field = ev.get("field", "ActiveInput")
            if current_field is None:
                current_field = field
                current_text_buffer = ev["key"]
            elif current_field == field:
                current_text_buffer += ev["key"]
            else:
                # Field changed, flush old buffer
                clean_steps.append({
                    "action": "type_text",
                    "target": current_field,
                    "value": current_text_buffer
                })
                current_field = field
                current_text_buffer = ev["key"]
            continue
        else:
            # If we were accumulating text and hit a non-keypress, flush it
            if current_text_buffer:
                clean_steps.append({
                    "action": "type_text",
                    "target": current_field,
                    "value": current_text_buffer
                })
                current_text_buffer = ""
                current_field = None
                
        # Rule 2: Prune Hovers, Movements & Pauses
        if ev_type in ["mouse_move", "mouse_hover", "idle_pause"]:
            continue
            
        # Rule 3: Retain Intentful Clicks
        if ev_type == "click":
            clean_steps.append({
                "action": "click",
                "target": ev.get("target"),
                "coords": ev.get("coords"),
                "element_type": ev.get("element_type")
            })
            
    # Flush remaining text if any
    if current_text_buffer:
        clean_steps.append({
            "action": "type_text",
            "target": current_field,
            "value": current_text_buffer
        })
        
    return clean_steps

def run_denoising_benchmark():
    print("=" * 65)
    print("🔬 SURGET.AI PHASE-V: TRAJECTORY DENOISING & PRUNING")
    print("=" * 65)
    
    # Load raw demonstration trace from task 5.1
    in_file = os.path.join(os.path.dirname(__file__), "raw_demonstration_trace.json")
    with open(in_file, "r") as f:
        raw_trace = json.load(f)
        
    t0 = time.perf_counter()
    clean_steps = prune_and_denoise_trace(raw_trace)
    filtering_time_ms = (time.perf_counter() - t0) * 1000
    
    compression_ratio = (1 - len(clean_steps) / len(raw_trace)) * 100
    
    print(f"\n[+] Denoising Filter Executed in {filtering_time_ms:.3f} ms")
    print(f"[+] Raw Input Events:     {len(raw_trace)} events")
    print(f"[+] Pruned Output Steps:  {len(clean_steps)} atomic steps")
    print(f"[+] Noise Reduction Rate: {compression_ratio:.1f}% of telemetry eliminated")
    
    print("\n📋 EXTRACTED CLEAN WORKFLOW STEPS:")
    print("-" * 65)
    for i, s in enumerate(clean_steps, 1):
        if s["action"] == "click":
            print(f"Step {i}: CLICK on '{s['target']}' at coords {s['coords']} (Type: {s['element_type']})")
        elif s["action"] == "type_text":
            print(f"Step {i}: TYPE text \"{s['value']}\" into field '{s['target']}'")
    print("-" * 65)
    
    # Save clean steps artifact
    out_file = os.path.join(os.path.dirname(__file__), "clean_workflow_steps.json")
    with open(out_file, "w") as f:
        json.dump(clean_steps, f, indent=2)
    print(f"\n[✓] Clean Steps Artifact Written: {out_file}")
    print("=" * 65)
    
    return {
        "raw_count": len(raw_trace),
        "clean_count": len(clean_steps),
        "noise_reduction_pct": round(float(compression_ratio), 1)
    }

if __name__ == "__main__":
    run_denoising_benchmark()
