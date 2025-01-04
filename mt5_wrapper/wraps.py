import MetaTrader5 as mt5  # type: ignore
from typing import Optional, Tuple, Dict, List
from .data_structures import *
from datetime import datetime
from numpy.typing import NDArray
import numpy as np


def initialize(
    path: Optional[str] = None,
    *,
    login: Optional[int] = None,
    password: Optional[str] = None,
    server: Optional[str] = None,
    timeout: Optional[int] = None,
    portable: bool = False,
) -> bool:

    args: Dict[str, Optional[int | str]] = {
        "path": path,
        "login": login,
        "password": password,
        "server": server,
        "timeout": timeout,
        "portable": portable,
    }

    filtered_args = {key: value for key, value in args.items() if value is not None}

    return mt5.initialize(**filtered_args)  # type: ignore


def login(
    login: int,
    password: Optional[str] = None,
    server: Optional[str] = None,
    timeout: Optional[int] = None,
) -> bool:

    args: Dict[str, Optional[int | str]] = {
        "login": login,
        "password": password,
        "server": server,
        "timeout": timeout,
    }

    filtered_args = {key: value for key, value in args.items() if value is not None}

    return mt5.login(**filtered_args)  # type: ignore


def shutdown() -> None:
    return mt5.shutdown()  # type: ignore


def version() -> Tuple[int, int, str]:
    return mt5.version()  # type: ignore


def last_error() -> Optional[Tuple[int, str]]:
    return mt5.last_error()  # type: ignore


def account_info() -> Optional[AccountInfo]:
    return mt5.account_info()  # type: ignore


def terminal_info() -> Optional[TerminalInfo]:
    return mt5.terminal_info()  # type: ignore


def symbols_total() -> int:
    return mt5.symbols_total()  # type: ignore


def symbol_info(symbol: str) -> Optional[SymbolInfo]:
    return mt5.symbol_info(symbol)  # type: ignore


def symbols_get(group: Optional[str] = None) -> Tuple[SymbolInfo]:

    args = {
        "group": group,
    }

    filtered_args = {key: value for key, value in args.items() if value is not None}

    return mt5.symbols_get(**filtered_args)  # type: ignore


def symbol_info_tick(symbol: str) -> Optional[Tick]:
    return mt5.symbol_info_tick(symbol)  # type: ignore


def symbol_select(symbol: str, enabled: Optional[bool] = None) -> bool:

    args: List[str | Optional[bool]] = [symbol, enabled]

    filtered_args = [arg for arg in args if arg is not None]

    return mt5.symbol_select(*filtered_args)  # type: ignore


def market_book_add(symbol: str) -> bool:
    return mt5.market_book_add(symbol)  # type: ignore


def market_book_release(symbol: str) -> bool:
    return mt5.market_book_release(symbol)  # type: ignore


def market_book_get(symbol: str) -> Optional[Tuple[BookInfo]]:
    return mt5.market_book_add(symbol)  # type: ignore


def copy_rates_from(
    symbol: str, timeframe: int, date_from: int | float | datetime, count: int
) -> Optional[NDArray[np.void]]:
    return mt5.copy_rates_from(symbol, timeframe, date_from, count)  # type: ignore


def copy_rates_from_pos(
    symbol: str, timeframe: int, start_pos: int, count: int
) -> Optional[NDArray[np.void]]:
    return mt5.copy_rates_from_pos(symbol, timeframe, start_pos, count)  # type: ignore


def copy_rates_range(
    symbol: str,
    timeframe: int,
    date_from: int | float | datetime,
    date_to: int | float | datetime,
) -> Optional[NDArray[np.void]]:
    return mt5.copy_rates_range(symbol, timeframe, date_from, date_to)  # type: ignore


def copy_ticks_from(
    symbol: str, date_from: int | float | datetime, count: int, flags: int
) -> Optional[NDArray[np.void]]:
    return mt5.copy_ticks_from(symbol, date_from, count, flags)  # type: ignore


def copy_ticks_range(
    symbol: str,
    date_from: int | float | datetime,
    date_to: int | float | datetime,
    flags: int,
) -> Optional[NDArray[np.void]]:
    return mt5.copy_ticks_range(symbol, date_from, date_to, flags)  # type: ignore


def orders_total() -> Optional[int]:
    return mt5.orders_total()  # type: ignore


def orders_get(
    symbol: Optional[str] = None,
    group: Optional[str] = None,
    ticket: Optional[int] = None,
) -> Optional[Tuple[TradeOrder]]:

    args: Dict[str, Optional[int | str]] = {
        "symbol": symbol,
        "group": group,
        "ticket": ticket,
    }

    filtered_args = {key: value for key, value in args.items() if value is not None}

    return mt5.orders_get(**filtered_args)  # type: ignore


def order_calc_margin(
    action: int, symbol: str, volume: float, price: float
) -> Optional[int]:
    return mt5.order_calc_margin(action, symbol, volume, price)  # type: ignore


def order_calc_profit(
    action: int, symbol: str, volume: float, price_open: float, price_close: float
) -> Optional[int]:
    return mt5.order_calc_profit(action, symbol, volume, price_open, price_close)  # type: ignore


def order_check(
    request: Dict[str, Optional[str | int | float]]
) -> Optional[OrderCheckResult]:
    return mt5.order_check(request)  # type: ignore


def order_send(
    request: Dict[str, Optional[str | int | float]]
) -> Optional[OrderSendResult]:
    return mt5.order_send(request)  # type: ignore


def positions_total() -> Optional[int]:
    return mt5.positions_total()  # type: ignore


def positions_get(
    symbol: Optional[str] = None,
    group: Optional[str] = None,
    ticket: Optional[int] = None,
) -> Optional[Tuple[TradePosition]]:

    args: Dict[str, Optional[int | str]] = {
        "symbol": symbol,
        "group": group,
        "ticket": ticket,
    }

    filtered_args = {key: value for key, value in args.items() if value is not None}

    return mt5.positions_get(**filtered_args)  # type: ignore


def history_orders_total(
    date_from: int | float | datetime,
    date_to: int | float | datetime,
) -> Optional[int]:
    return mt5.history_orders_total(date_from, date_to)  # type: ignore


def history_orders_get(
    date_from: int | float | datetime,
    date_to: int | float | datetime,
    group: Optional[str] = None,
    ticket: Optional[int] = None,
    position: Optional[int] = None,
) -> Optional[Tuple[TradeOrder]]:

    args: Dict[str, Optional[int | str]] = {
        "position": position,
        "group": group,
        "ticket": ticket,
    }

    filtered_args = {key: value for key, value in args.items() if value is not None}

    return mt5.history_orders_get(date_from, date_to, **filtered_args)  # type: ignore


def history_deals_total(
    date_from: int | float | datetime,
    date_to: int | float | datetime,
) -> Optional[int]:
    return mt5.history_deals_total(date_from, date_to)  # type: ignore


def history_deals_get(
    date_from: int | float | datetime,
    date_to: int | float | datetime,
    group: Optional[str] = None,
    ticket: Optional[int] = None,
    position: Optional[int] = None,
) -> Optional[Tuple[TradeDeal]]:

    args: Dict[str, Optional[int | str]] = {
        "position": position,
        "group": group,
        "ticket": ticket,
    }

    filtered_args = {key: value for key, value in args.items() if value is not None}

    return mt5.history_deals_get(date_from, date_to, **filtered_args)  # type: ignore
