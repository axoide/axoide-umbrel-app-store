# Minimal sample strategy for Freqtrade
# Compatible with freqtrade strategy interface (basic EMA crossover)

from pandas import DataFrame
import talib
from freqtrade.strategy.interface import IStrategy


class SampleStrategy(IStrategy):
    """Simple EMA crossover strategy.

    - Buys when EMA(10) crosses above EMA(50)
    - Sells when EMA(10) crosses below EMA(50)

    This is a minimal example for testing. Use at your own risk.
    """

    # Strategy minimal configuration
    timeframe = '5m'
    stoploss = -0.10  # 10% stoploss
    minimal_roi = {"0": 0.02}
    startup_candle_count = 50

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Calculate EMA indicators
        dataframe['ema10'] = talib.EMA(dataframe['close'], timeperiod=10)
        dataframe['ema50'] = talib.EMA(dataframe['close'], timeperiod=50)
        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                dataframe['ema10'] > dataframe['ema50']) &
                (dataframe['ema10'].shift(1) <= dataframe['ema50'].shift(1))
            , 'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                dataframe['ema10'] < dataframe['ema50']) &
                (dataframe['ema10'].shift(1) >= dataframe['ema50'].shift(1))
            , 'sell'] = 1
        return dataframe
