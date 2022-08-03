import sys
from .scraper import (
    Scraper, TAG_LINK,
    HTMLSession, AsyncHTMLSession, HTML, HTMLResponse, Element, user_agent
)
from .user_agents import UserAgent
from .url import URL, remove_urls, replace_urls
from .proxy import ProxyManager, PROXY, ProxyRotate
from .logging import LogConfig, LOG_LEVEL
from .versions import __VERSION__

# Sanity checking.
try:
    assert sys.version_info.major == 3
    assert sys.version_info.minor > 7
except AssertionError:
    raise RuntimeError('Requests-HTML requires Python 3.8+!')

__all__ = [
    "Scraper",
    "TAG_LINK",
    "HTMLSession",
    "AsyncHTMLSession",
    "HTML",
    "HTMLResponse",
    "Element",
    "user_agent",
    "UserAgent",
    "URL",
    "remove_urls",
    "replace_urls",
    "ProxyManager",
    "ProxyRotate",
    "PROXY",
    "LogConfig",
    "LOG_LEVEL",
    "__VERSION__",
]
