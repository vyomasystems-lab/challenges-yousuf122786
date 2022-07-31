# Sequence Detector(Level1_Design2)

## Test Scenario *(Important)*
- Test Inputs: 111011 and 1011011 (overlaping Sequence)
- Expected Output: FSM should detect sequence produce output 1 for overlapping sequence
- Observed Output in the DUT dut.out = Sequence not detected for overlapping sequence 

Output mismatches for the above inputs proving that there is a bug in the design

## Design Bug
Based on the above test input and analysing the design, we see the following test fail due to some bug
![](https://github.com/vyomasystems-lab/challenges-yousuf122786/blob/master/Images/Screenshot_3.jpg)

      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;    <== Bug
        else
          next_state = SEQ_10;


      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;     <== BUG


    SEQ_1011:
        next_state = IDLE;    <== BUG


Assigning ``next_state = SEQ_1;`` in  SEQ_1 state for inp_bit=1, assigning ``next_state = SEQ_10;`` in else of SEQ_101 state and assigning in final state as
    ``if(inp_bit == 1)
        next_state = SEQ_1;
      else
        next_state = SEQ_10;
      end`` in SEQ_1011 state will fix the bug.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://github.com/vyomasystems-lab/challenges-yousuf122786/blob/master/Images/Screenshot_4.jpg)

The updated design is checked in as seq_detect_1011_Fix.v

## Verification Strategy
By drawing the FSM of the overlapping sequence(1011) and checking all possible overlapping sequences as test vectors. 

## Is the verification complete ?
- Yes Verification is complete