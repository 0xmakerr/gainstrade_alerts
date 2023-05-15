from web3feeperblock_oi import fundingfeeperblock, rolloverfeeperblock, oi_long, oi_short, long_or_short, blocks_per_hour

collateral = int(input("Collateral?: "))
leverage = int(input("Leverage?: "))
rollover = round((rolloverfeeperblock * blocks_per_hour) / 10000000000, 4)
position_size = collateral * leverage
loop_break = False

def funding_calc(funding, position_size, rollover_leverage):
    funding_positive = abs(funding)
    funding_apr = round(funding_positive * 24 * 365, 2)
    funding_per_day = round((position_size / 100) * funding_positive * 24, 2)
    funding_hourly = round((position_size / 100) * funding_positive, 2)

    funding_rollover = round(funding_positive - rollover_leverage, 4)
    funding_rollover_positive = abs(funding_rollover)
    funding_rollover_apr = round(funding_rollover_positive * 24 * 365, 2)
    funding_rollover_per_day = round((position_size / 100) * funding_rollover_positive * 24, 2)
    funding_rollover_hourly = round((position_size / 100) * funding_rollover_positive, 2)
    return funding_positive, funding_apr, funding_per_day, funding_hourly, funding_rollover_positive, funding_rollover_apr, funding_rollover_per_day, funding_rollover_hourly

if long_or_short == "L" or long_or_short == "LA":
    while loop_break == False:
        rollover_leverage = rollover / leverage
        oi_long += position_size

        funding = round(((oi_long - oi_short) * blocks_per_hour * fundingfeeperblock) / oi_long / 10000000000, 4)
        funding_positive, funding_apr, funding_per_day, funding_hourly, funding_rollover_positive, funding_rollover_apr, funding_rollover_per_day, funding_rollover_hourly = funding_calc(funding, position_size, rollover_leverage)

        if funding > 0:
            print(f"Paying: {funding}% / {funding_apr}% per year / {funding_per_day}$ per day")
        else:
            print(f"Earning: {funding_positive}% / {funding_apr}% per year / {funding_per_day}$ per day / {funding_hourly}$ per hour")
            print(f"Earning - Rollover: {funding_rollover_positive}% / {funding_rollover_apr}% per year / {funding_rollover_per_day}$ per day / {funding_rollover_hourly}$ per hour")

        continue_stop = input("ENTER for new position size")
        if continue_stop == "":
            oi_long -= position_size
            collateral = int(input("Collateral?: "))
            leverage = int(input("Leverage?: "))
            position_size = collateral * leverage
        else:
            loop_break = True

elif long_or_short == "S" or long_or_short == "SA":
    while loop_break == False:
        rollover_leverage = rollover / leverage
        oi_short += position_size

        funding = round(((oi_short - oi_long) * blocks_per_hour * fundingfeeperblock) / oi_short / 10000000000, 4)
        funding_positive, funding_apr, funding_per_day, funding_hourly, funding_rollover_positive, funding_rollover_apr, funding_rollover_per_day, funding_rollover_hourly = funding_calc(funding, position_size, rollover_leverage)

        if funding > 0:
            print(f"Paying: {funding}% / {funding_apr}% per year / {funding_per_day}$ per day")
        else:
            print(f"Earning: {funding_positive}% / {funding_apr}% per year / {funding_per_day}$ per day / {funding_hourly}$ per hour")
            print(f"Earning - Rollover: {funding_rollover_positive}% / {funding_rollover_apr}% per year / {funding_rollover_per_day}$ per day / {funding_rollover_hourly}$ per hour")

        continue_stop = input("ENTER for new position size")
        if continue_stop == "":
            oi_short -= position_size
            collateral = int(input("Collateral?: "))
            leverage = int(input("Leverage?: "))
            position_size = collateral * leverage
        else:
            loop_break = True

# Fees

gtrade_fees = (position_size / 100) * 0.08
binance_fees_busd = (position_size / 100) * 0.04
total_fees = round(gtrade_fees + binance_fees_busd,2)
print(f"Open fees: {total_fees}$ \nOpen and Close fees: {total_fees * 2}$")

# SPREAD

gtrade_entry = float(input("GainsTrade Entry Price: "))
gtrade_exit = float(input("GainsTrade Exit Price: "))
binance_entry = float(input("Binance Entry Price: "))
binance_exit = float(input("Binance Exit Price: "))

if long_or_short == "L" or long_or_short == "LA":
    gtrade_pnl = (gtrade_exit - gtrade_entry) * (position_size / gtrade_entry)
    binance_pnl = (binance_entry - binance_exit) * (position_size / binance_entry)
elif long_or_short == "S" or long_or_short == "SA":
    gtrade_pnl = (gtrade_entry - gtrade_exit) * (position_size / gtrade_entry)
    binance_pnl = (binance_exit - binance_entry) * (position_size / binance_entry)

total_pnl = round(gtrade_pnl + binance_pnl, 2)
print(f"PNL on spread: {total_pnl}$")