# Multiplexer (Level1_design1)

## Test Scenario *(Important)*
- Test Inputs: 5'b11110,5'b01100
- Expected Output: Multiplexer should give the output based upon the resepective select line given in input
- Observed Output in the DUT dut.out = bug is detected

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following test fail due to some bug
![](https://github.com/vyomasystems-lab/challenges-yousuf122786/blob/master/Images/Screenshot_1.jpg)

      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;    <== Bug
        else


      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;     <== BUG


    SEQ_1011:
        next_state = IDLE;    <== BUG


So assigning ``next_state = SEQ_1;`` in else of SEQ_1 state, assigning ``next_state = SEQ_10;`` in else of SEQ_101 state and putting if condition ``if(inp_bit == 1)
        next_state = SEQ_1;
      else
        next_state = SEQ_10;
      end`` in SEQ_1011 state fixed the bug.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://github.com/vyomasystems-lab/challenges-yousuf122786/blob/master/Images/Screenshot_2.jpg)

The updated design is checked in as seq_detect_1011_Fix.v

## Verification Strategy
By drawing the FSM of the overlapping sequence(1011) and checking all possible overlapping sequences as test vectors. 

## Is the verification complete ?
- Yes Verification is complete