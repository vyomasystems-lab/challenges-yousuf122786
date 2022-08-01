# I2C Master and Slave(Level3_Design)

## Test Scenario *(Important)*
- Test Inputs:
    rst = 1
    addr = 0b0010110
    data_in = 0b10101010
    enable = 1
    rw = 1 for read operation

- Expected Output: Master should read the data from the slave as read signal is given by the master.
- Observed Output: Master could not read the correct data as there is a bug in the verilog code.



## Design Bug
Based on the above test input and analysing the design, we see the following test fail due to some bug
![](https://github.com/vyomasystems-lab/challenges-yousuf122786/blob/master/Images/Screenshot_6.jpg)

      
## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://github.com/vyomasystems-lab/challenges-yousuf122786/blob/master/Images/Screenshot_7.jpg)



## Verification Strategy
By assigning the address to a respective slave and read signal is given by the master and the respective data should be read by the master as given and compare that with what actually master should read given by the slave.
As there is a bug the test case failed. 

## Is the verification complete ?
- Yes Verification is complete.