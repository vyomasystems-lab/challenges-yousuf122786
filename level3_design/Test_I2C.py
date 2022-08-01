# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.rst.value = 1
    dut.addr.value = 0b0010110
    dut.data_in.value = 0b10101010
    dut.enable.value = 1
    dut.rw.value = 1

    await FallingEdge(dut.clk)  
    dut.rst.value = 0
    await FallingEdge(dut.clk)
    for i in range(18):
        await FallingEdge(dut.i2c_scl)
        cocotb.log.info(f'i2c_sda = {dut.i2c_sda.value}')
    if dut.i2c_scl.value == 1:
        assert True
    else:
        assert False



