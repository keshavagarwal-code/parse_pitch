Task at hand is to parse CBOE PITCH messages to calculate the total volume. 

[Detailed PITCH Specification](http://cdn.cboe.com/resources/membership/Cboe_US_Equities_TCP_PITCH_Specification.pdf)
 
There are 3 types of messages that we are concerned with to calculate the volume 
 
a> AddOrder(A,d)  
b> OrdersExecuted(E)  
c> TradeMessage(P,r)  
  
  
TradeMessages are straightforward they have both the long/short stock symbol and the quantity 
OrdersExecuted have the quantity but do not have the stock symbol, so need to be looked up with the previous AddOrders using OrderId 
The volume of the trade is total orders executed for a symbol irrespective of order side. 
  
To run the code  
  
```
1> if the input type is a file pass the file path as an argument

   for e.g.

   $ python3.8 message_parser.py "/tmp/pitch_example_data.txt"
   
2> if the input is from stdin, run it without filename argument
    I have used some special inputs for e.g. use PRINT/print in between to check the current highest volume
    use Q/CTRL-C to quit

    $ python3.8 message_parser.py

    use PRINT to get current max Volume or Q/CTRL-C to quit
    S28807199A5K27GA00000SB000100FXP   0000654100Y
    S28807216E5K27GA00000S00010000005AQ00002
    print
        SYMBOL     VOLUME
        ------     ------
        FXP        100

```
  
