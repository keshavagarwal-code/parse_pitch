Task at hand is to parse CBOE PITCH messages to calculate the total volume. 

[Detailed PITCH Specification](http://cdn.cboe.com/resources/membership/Cboe_US_Equities_TCP_PITCH_Specification.pdf)
 
There are 3 types of messages that we are concerned with to calculate the volume 
 
a> AddOrder(A,d) 
b> OrdersExecuted(E) 
c> TradeMessage(P) 
  
  
TradeMessages are straightforward they have both the long/short stock symbol and the quantity 
OrdersExecuted have the quantity but do not have the stock symbol, so need to be looked up with the previous AddOrders using OrderId 
The volume of the trade is total orders executed for a symbol irrespective of order side. 