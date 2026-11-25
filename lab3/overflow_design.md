Program: overflow_sim.py
Date: November 25, 2026

Security Design:
1. The simulated buffer has a capacity of 64 elements.
2. Input is treated as untrusted data.
3. The input length is checked against the buffer capacity.
4. Oversized input triggers an overflow warning.
5. Validation occurs before any attempted write.
