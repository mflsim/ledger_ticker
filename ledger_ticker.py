from yahooquery import Ticker

def write_ticker(ticker_name, symb1, symb2):
    ticker = Ticker(ticker_name)
    output = ticker.price

    if not(output.get(ticker_name)):
        print('Cannot get ticker:', ticker_name)

    price = output.get(ticker_name).get('regularMarketPrice')
    datetime = output.get(ticker_name).get('regularMarketTime')
        
    out_line = 'P\t' + datetime + '\t' + symb1 + '\t' + format(price, '.8f').rstrip('0') + '\t' + symb2
    db_file = open("prices.ledger", "a")
    db_file.write(out_line + '\n')
    print('Ticker added: ', out_line)


file_set = open("symbols.txt","r")
file_set_lines = file_set.readlines()
file_set.close()

for line in file_set_lines:
    if line[0] != ';':
        data_list = line.split()
        write_ticker(data_list[0], data_list[1], data_list[2])