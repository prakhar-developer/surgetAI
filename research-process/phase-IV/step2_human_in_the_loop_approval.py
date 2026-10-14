"""
Surget.AI Research Process - Phase IV: Task 4.2
Script: step2_human_in_the_loop_approval.py
Objective: Human-in-the-Loop (HITL) Dynamic Pause, Elevation Request & Resumption Architecture
"""

import sys
import os
import time
import json
import hashlib

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class HumanInTheLoopGate:
    """Manages asynchronous elevation requests for high-risk autonomous actions."""
    def __init__(self):
        self.pending_requests = {}
        self.approval_tokens = {}
        
    def create_elevation_request(self, agent_id, proposed_action, risk_score):
        req_id = f"REQ_{hashlib.md5(f'{time.time()}_{proposed_action}'.encode()).hexdigest()[:8]}"
        payload = {
            "request_id": req_id,
            "agent_id": agent_id,
            "timestamp": time.time(),
            "proposed_action": proposed_action,
            "risk_score": risk_score,
            "status": "AWAITING_SUPERVISOR_SIGNATURE"
        }
        self.pending_requests[req_id] = payload
        return payload

    def submit_supervisor_decision(self, request_id, approved=True, supervisor_id="MANAGER_ALICE"):
        if request_id not in self.pending_requests:
            return False, "Request ID not found"
            
        req = self.pending_requests[request_id]
        if approved:
            # Generate cryptographic approval token
            raw_token = f"{request_id}_{supervisor_id}_APPROVED"
            token = hashlib.sha256(raw_token.encode()).hexdigest()[:16]
            req["status"] = "APPROVED"
            req["token"] = token
            req["supervisor"] = supervisor_id
            self.approval_tokens[token] = req
            return True, token
        else:
            req["status"] = "REJECTED"
            req["supervisor"] = supervisor_id
            return False, "Action denied by supervisor"

    def verify_and_execute(self, token):
        if token in self.approval_tokens:
            req = self.approval_tokens[token]
            return True, f"Action authorized: Executed {req['proposed_action']['target']}"
        return False, "Invalid or expired authorization token"

def run_hitl_benchmark():
    print("=" * 65)
    print("🔬 SURGET.AI PHASE-IV: HUMAN-IN-THE-LOOP (HITL) GATING")
    print("=" * 65)
    
    gate = HumanInTheLoopGate()
    
    # High-Risk Scenario: Financial wire transfer
    sensitive_action = {
        "tool": "click",
        "target": "ApproveWireTransfer_$50000",
        "recipient": "Vendor Global Logistics Ltd",
        "amount_usd": 50000
    }
    risk_score = 0.78 # High Risk (>0.30)
    
    print(f"\n[!] High-Risk Action Detected: {sensitive_action['target']} (Risk = {risk_score*100:.1f}%)")
    print("  • Rule: Direct autonomous execution prohibited.")
    print("  • Triggering HITL elevation pause...")
    
    # Step 1: Create Elevation Request
    t0 = time.perf_counter()
    req = gate.create_elevation_request("AGENT_WORKFORCE_07", sensitive_action, risk_score)
    elevation_lat_ms = (time.perf_counter() - t0) * 1000
    
    print(f"\n[+] Elevation Request Created in {elevation_lat_ms:.2f} ms:")
    print(f"    Request ID: {req['request_id']}")
    print(f"    Status:     {req['status']}")
    
    # Step 2: Supervisor Reviews and Approves
    print("\n[+] Human Supervisor (Alice) reviews telemetry context on dashboard...")
    approved, token = gate.submit_supervisor_decision(req["request_id"], approved=True, supervisor_id="DIR_FINANCE_ALICE")
    print(f"  • Supervisor Decision: APPROVED")
    print(f"  • Authorization Token: {token}")
    
    # Step 3: Agent Verifies Token & Safely Executes
    t_exec = time.perf_counter()
    executed, status_msg = gate.verify_and_execute(token)
    exec_lat_ms = (time.perf_counter() - t_exec) * 1000
    
    print(f"\n[+] Token Verification:  {status_msg} (in {exec_lat_ms:.3f} ms)")
    print(f"[+] Cryptographic Proof: Stored in session authorization table")
    print("=" * 65)
    
    return {
        "elevation_latency_ms": round(float(elevation_lat_ms), 3),
        "authorized": bool(executed)
    }

if __name__ == "__main__":
    run_hitl_benchmark()
