from collections import Counter
import sys
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
log.addHandler(handler)

orderid_book = {}
trades_executed = {}

def print_current_vol():
    c = Counter(trades_executed)
    log_str = "{0:>10} {1:>10}"
    log.info(log_str.format("SYMBOL", "VOLUME"))
    log.info(log_str.format("------", "------"))
    for cm in c.most_common():
        log.info(log_str.format(cm[0], cm[1]))

def parse_trade_message(order, msg_type):
    orderQty = order[23:29]
    if msg_type == 'P':
        trade_symbol = order[29:35].strip()
    else:
        trade_symbol = order[29:37].strip()
    if trade_symbol in trades_executed:
        trades_executed[trade_symbol] += int(orderQty)
    else:
        trades_executed[trade_symbol] = int(orderQty)
    
    
def parse_executed_order(order, msg_type):
    orderid = order[10:22]
    order_from_book = orderid_book.get(orderid, None)
    if not order_from_book:
        log.error("Received an executed order for id {} but the trade has no add order request".format(orderid))
        return
    trade_symbol = order_from_book.get('orderSymbol')
    if trade_symbol in trades_executed:
        trades_executed[trade_symbol] += int(order[22:28])
    else:
        trades_executed[trade_symbol] = int(order[22:28])

def parse_add_order(order, msg_type):
    orderid = order[10:22]
    orderQty = order[23:29]
    if msg_type == 'A':
        orderSymbol = order[29:35].strip()
    else:
        orderSymbol = order[29:37].strip()
    orderid_book[orderid] = {
                                'orderQty':orderQty,
                                'orderSymbol':orderSymbol
                            }

def main_parser(input_line):
    parse_methods = {
        "P" : parse_trade_message,
        "r" : parse_trade_message,
        "A" : parse_add_order,
        "d" : parse_add_order,
        "E" : parse_executed_order,
        
    }

    try:
        msg_type = input_line[9]
        messageParser = parse_methods.get(msg_type)
        if messageParser:
            messageParser(input_line, msg_type)
    except IndexError as e:
        log.error("ERROR on {} with message {}".format(input_line, e))
    

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            f = open(filename)
                
            for lines in f.readlines():
                main_parser(lines)
            
            f.close()
        except Exception as e:
            log.error("reading filename {} failed with error {}".format(filename, e))
    else:
        log.info("\nuse PRINT to get current max Volume or Q/CTRL-C to quit")
        for line in sys.stdin:
            if line.strip().lower() == 'print':
                print_current_vol()
            elif line.strip().lower() == 'q':
                break
            else:
                main_parser(line.strip())

    print_current_vol()

    

if __name__ == '__main__':
    main()

