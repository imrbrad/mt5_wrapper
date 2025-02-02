import numpy as np
from typing import Dict, Optional, Tuple
from .data_structures import *
from datetime import datetime
from numpy.typing import NDArray

def initialize(path: Optional[str] = ..., *, login: Optional[int] = ..., password: Optional[str] = ..., server: Optional[str] = ..., timeout: Optional[int] = ..., portable: bool = ...) -> bool:
    ...

def login(login: int, password: Optional[str] = ..., server: Optional[str] = ..., timeout: Optional[int] = ...) -> bool:
    ...

def shutdown() -> None:
    ...

def version() -> Tuple[int, int, str]:
    ...

def last_error() -> Optional[Tuple[int, str]]:
    ...

def account_info() -> Optional[AccountInfo]:
    ...

def terminal_info() -> Optional[TerminalInfo]:
    ...

def symbols_total() -> int:
    ...

def symbol_info(symbol: str) -> Optional[SymbolInfo]:
    ...

def symbols_get(group: Optional[str] = ...) -> Tuple[SymbolInfo]:
    ...

def symbol_info_tick(symbol: str) -> Optional[Tick]:
    ...

def symbol_select(symbol: str, enabled: Optional[bool] = ...) -> bool:
    ...

def market_book_add(symbol: str) -> bool:
    ...

def market_book_release(symbol: str) -> bool:
    ...

def market_book_get(symbol: str) -> Optional[Tuple[BookInfo]]:
    ...

def copy_rates_from(symbol: str, timeframe: int, date_from: int | float | datetime, count: int) -> Optional[NDArray[np.void]]:
    ...

def copy_rates_from_pos(symbol: str, timeframe: int, start_pos: int, count: int) -> Optional[NDArray[np.void]]:
    ...

def copy_rates_range(symbol: str, timeframe: int, date_from: int | float | datetime, date_to: int | float | datetime) -> Optional[NDArray[np.void]]:
    ...

def copy_ticks_from(symbol: str, date_from: int | float | datetime, count: int, flags: int) -> Optional[NDArray[np.void]]:
    ...

def copy_ticks_range(symbol: str, date_from: int | float | datetime, date_to: int | float | datetime, flags: int) -> Optional[NDArray[np.void]]:
    ...

def orders_total() -> Optional[int]:
    ...

def orders_get(symbol: Optional[str] = ..., group: Optional[str] = ..., ticket: Optional[int] = ...) -> Optional[Tuple[TradeOrder]]:
    ...

def order_calc_margin(action: int, symbol: str, volume: float, price: float) -> Optional[int]:
    ...

def order_calc_profit(action: int, symbol: str, volume: float, price_open: float, price_close: float) -> Optional[int]:
    ...

def order_check(request: Dict[str, Optional[str | int | float]]) -> Optional[OrderCheckResult]:
    ...

def order_send(request: Dict[str, Optional[str | int | float]]) -> Optional[OrderSendResult]:
    ...

def positions_total() -> Optional[int]:
    ...

def positions_get(symbol: Optional[str] = ..., group: Optional[str] = ..., ticket: Optional[int] = ...) -> Optional[Tuple[TradePosition]]:
    ...

def history_orders_total(date_from: int | float | datetime, date_to: int | float | datetime) -> Optional[int]:
    ...

def history_orders_get(date_from: int | float | datetime, date_to: int | float | datetime, group: Optional[str] = ..., ticket: Optional[int] = ..., position: Optional[int] = ...) -> Optional[Tuple[TradeOrder]]:
    ...

def history_deals_total(date_from: int | float | datetime, date_to: int | float | datetime) -> Optional[int]:
    ...

def history_deals_get(date_from: int | float | datetime, date_to: int | float | datetime, group: Optional[str] = ..., ticket: Optional[int] = ..., position: Optional[int] = ...) -> Optional[Tuple[TradeDeal]]:
    ...

