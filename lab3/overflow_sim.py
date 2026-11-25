import sys

def simulate_overflow(size=80):
    buffer = [0] * 64
    payload = "A" * size

    print(f"Buffer capacity: {len(buffer)}")
    print(f"Payload size: {len(payload)}")

    if len(payload) > len(buffer):
        print("WARNING: Potential buffer overflow detected!")
    else:
        print("SAFE: Payload is within buffer capacity.")

if __name__ == "__main__":
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 80
    simulate_overflow(size)
