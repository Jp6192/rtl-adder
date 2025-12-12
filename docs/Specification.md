The simple_adder module is an 8-bit synchronous adder. It samples inputs `a` and `b` on
the rising edge of `clk` and updates the registered output `sum` with the lower 8 bits
of the sum (i.e. arithmetic is modulo 256).

Interface:
- `clk`: clock input
- `a[7:0]`: operand A
- `b[7:0]`: operand B
- `sum[7:0]`: registered sum output

Behavior:
On each rising edge of `clk`, compute `sum <= a + b` (lower 8 bits kept).
