# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    dut.inp0.value =2
    dut.inp1.value =2
    dut.inp2.value =2
    dut.inp3.value =2
    dut.inp4.value =2
    dut.inp5.value =2
    dut.inp6.value =2
    dut.inp7.value =2
    dut.inp8.value =2
    dut.inp9.value =2
    dut.inp10.value =2
    dut.inp11.value =2
    dut.inp12.value =2
    dut.inp13.value =2
    dut.inp14.value =2
    dut.inp15.value =2
    dut.inp16.value =2
    dut.inp17.value =2
    dut.inp18.value =2
    dut.inp19.value =2
    dut.inp20.value =2
    dut.inp21.value =2
    dut.inp22.value =2
    dut.inp23.value =2
    dut.inp24.value =2
    dut.inp25.value =2
    dut.inp26.value =2
    dut.inp27.value =2
    dut.inp28.value =2
    dut.inp29.value =2
    dut.inp30.value =2
    i=0
    while i<31:
        dut.sel.value = i
        await Timer(1,units='ns')
        if dut.out.value != 2:
            assert False
        i=i+1    

    assert True

@cocotb.test()
async def test_mux1(dut):
    c=12
    d=1
    dut.sel.value = c
    dut.inp12.value =d
    
    await Timer(2,units="ns")
    #cocotb.log.info('##### CTB: Develop your test here ########')
    assert dut.out.value == d


