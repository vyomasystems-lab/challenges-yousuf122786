# Co-Processor(Level2_Design)

## Test Scenario *(Important)*
- Test Inputs: mav_putvalue_src1 = 0x015
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x101010B3
    Here i have assigned values to the instruction code of the processor as an array to perform multiple operations using while loop  in the testbench.
- Expected Output: The respective output should be produced based upon the instruction code.
- Observed Output in the DUT dut.output = output is mismatched 

Output mismatches for the above inputs proving that there is a bug in the design.

## Design Bug
Based on the above test input and analysing the design, we see the following test fail due to some bug
![](https://github.com/vyomasystems-lab/challenges-yousuf122786/blob/master/Images/Screenshot_5.jpg)


## Design Fix
Tried to fix the bug but i was unable to fix it at the end. It is out of my scope.



## Verification Strategy
By driving the all possible instruction codes as test vectors, observe the output based upon the respective operation it should be perform and compare that with what exactly it should perform.
As there are bugs in the code test failed.

## Is the verification complete ?
- Yes Verification is complete