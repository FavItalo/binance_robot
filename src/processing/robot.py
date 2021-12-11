import asyncio
import websockets

import pandas as pd

from json import loads

from src.functions.bot_utils import set_dataframe


async def bot(websocket:str, database:pd.DataFrame):

    stream = websockets.connect(websocket)

    async with stream as request_btc:
        data_btc = await request_btc.recv()
        _data = set_dataframe(loads(data_btc)["data"])
        database.append(_data)
        database = database.append(set_dataframe(loads(data_btc)["data"]))
        return database

async def main():

    database = pd.DataFrame(columns=["symbol", "Time", "Price", "Quantity"])
    database.to_csv()

    while True:
        for new_row in asyncio.as_completed({bot("wss://stream.binance.com:9443/stream?streams=btcusdt@trade", database), bot("wss://stream.binance.com:9443/stream?streams=ethusdt@trade", database)}):
            database = await new_row
        
        print(database)

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())