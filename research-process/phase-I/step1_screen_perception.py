"""
Surget.AI Research Process - Phase I: Task 1.1
Script: step1_screen_perception.py
Objective: Benchmark screen capture speed & examine the screen as a NumPy tensor.
"""

import sys
import time
import numpy as np
import mss
import cv2
import os

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def benchmark_screen_capture():
    print("=" * 60)
    print("🔬 SURGET.AI PHASE-I: SENSORY PERCEPTION EXPERIMENT")
    print("=" * 60)
    
    with mss.mss() as sct:
        # Get primary monitor specification
        monitor = sct.monitors[1]
        width, height = monitor["width"], monitor["height"]
        print(f"\n[+] Primary Monitor Detected: {width} x {height} pixels")
        
        # Benchmark 20 consecutive screen captures
        latencies = []
        frames = []
        for i in range(20):
            t0 = time.perf_counter()
            sct_img = sct.grab(monitor)
            # Convert raw BGRA buffer to NumPy array (H, W, 3)
            img_np = np.array(sct_img)[:, :, :3]
            t1 = time.perf_counter()
            latencies.append((t1 - t0) * 1000) # milliseconds
            if i == 0:
                frames.append(img_np)
                
        latencies = np.array(latencies)
        mean_lat = np.mean(latencies)
        p95_lat = np.percentile(latencies, 95)
        min_lat = np.min(latencies)
        
        sample_frame = frames[0]
        mem_mb = sample_frame.nbytes / (1024 * 1024)
        
        print("\n📊 MATHEMATICAL & PERFORMANCE METRICS:")
        print(f"  • Tensor Shape: {sample_frame.shape} (Height x Width x Channels)")
        print(f"  • Data Type: {sample_frame.dtype} (Unsigned 8-bit Integer [0, 255])")
        print(f"  • Memory Footprint: {mem_mb:.2f} MB per uncompressed frame")
        print(f"  • Mean Latency: {mean_lat:.2f} ms")
        print(f"  • Min Latency: {min_lat:.2f} ms")
        print(f"  • P95 Latency: {p95_lat:.2f} ms")
        print(f"  • Equivalent Frame Rate: {1000 / mean_lat:.1f} FPS")
        
        # Color distribution statistics
        b_mean = np.mean(sample_frame[:, :, 0])
        g_mean = np.mean(sample_frame[:, :, 1])
        r_mean = np.mean(sample_frame[:, :, 2])
        print(f"  • Channel Means: Blue={b_mean:.1f}, Green={g_mean:.1f}, Red={r_mean:.1f}")
        
        # Save a compressed diagnostic thumbnail
        out_path = os.path.join(os.path.dirname(__file__), "screen_sample.jpg")
        cv2.imwrite(out_path, sample_frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        print(f"\n[✓] Diagnostic snapshot saved: {out_path}")
        print("=" * 60)
        
        return {
            "resolution": f"{width}x{height}",
            "mean_latency_ms": round(float(mean_lat), 2),
            "p95_latency_ms": round(float(p95_lat), 2),
            "fps": round(float(1000 / mean_lat), 1)
        }

if __name__ == "__main__":
    benchmark_screen_capture()
