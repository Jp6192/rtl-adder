import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_addition(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    await RisingEdge(dut.clk)
    dut.a.value = 5
    dut.b.value = 3
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert int(dut.sum.value) == 8, f"Expected 8, got {int(dut.sum.value)}"

# Pytest wrapper required by guide
def test_simple_adder_hidden_runner():
    import os
    from pathlib import Path
    from cocotb_tools.runner import get_runner

    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent.parent

    sources = [proj_path / "sources/simple_adder.sv"]

    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="simple_adder",
        always=True,
    )
    runner.test(
        hdl_toplevel="simple_adder",
        test_module="test_simple_adder_hidden"
    )
