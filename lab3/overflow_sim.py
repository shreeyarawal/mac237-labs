import sys

def simulate_overflow():
    print("[*] Starting MAC237 Buffer Overflow Simulation...")
    buffer = [0] * 64
    print(f"[*] Allocated safe stack buffer of {len(buffer)} bytes.")
    
    # Simulate data input
    payload = "A" * 80
    print(f"[*] Attempting to write payload of size {len(payload)} bytes...")
    
    if len(payload) > len(buffer):
        print("[!] Warning: Potential stack overflow detected in simulation!")
        print("[+] Boundary check triggered safely. Simulation successful.")

if __name__ == "__main__":
    simulate_overflow()
