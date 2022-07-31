# Multiplexer (Level1_design1)

## Test Scenario *(Important)*
- Test Inputs: 5'b11110,5'b01100
- Expected Output: Multiplexer should give the output based upon the resepective select line given in input
- Observed Output in the DUT dut.out = bug is detected

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following test fail due to some bug
![](https://github.com/vyomasystems-lab/challenges-yousuf122786/blob/master/Images/Screenshot_1.jpg)

      
      5'b01101: out = inp12; 
      5'b01101: out = inp13;    <== Bug
        
      5'b11110: out = inp30;   <== BUG
          


    


So assigning ``5'b01101: out = inp12;``  and assigning ``5'b11110: out = inp30; `` 
       fixed the bug.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://github.com/vyomasystems-lab/challenges-yousuf122786/blob/master/Images/Screenshot_2.jpg)

The updated design is checked in as mux_fix.v

## Verification Strategy
By Observing the verilog code and checking all possible input sequences as test vectors. 

## Is the verification complete ?
- Yes Verification is complete