import time
import asyncio
import logging
from threading import Lock

logger = logging.getLogger(__name__)


class TTLCache:
    """简单的内存 TTL 缓存，线程安全"""

    def __init__(self, default_ttl: int = 300):
        self._store: dict[str, tuple[float, any]] = {}
        self._lock = Lock()
        self._default_ttl = default_ttl

    def get(self, key: str):
        with self._lock:
            entry = self._store.get(key)
            if entry is None:
                return None
            expires_at, value = entry
            if time.time() > expires_at:
                del self._store[key]
                return None
            return value

    def set(self, key: str, value, ttl: int | None = None):
        ttl = ttl if ttl is not None else self._default_ttl
        with self._lock:
            self._store[key] = (time.time() + ttl, value)

    def clear(self):
        with self._lock:
            self._store.clear()
            logger.info("Cache cleared")

    @property
    def size(self) -> int:
        with self._lock:
            return len(self._store)

    def _cleanup_expired(self):
        """清理过期条目（可周期调用）"""
        now = time.time()
        with self._lock:
            expired = [k for k, (exp, _) in self._store.items() if now > exp]
            for k in expired:
                del self._store[k]
        if expired:
            logger.info(f"Cleaned up {len(expired)} expired cache entries")


# 全局缓存实例（在 main.py 中初始化 TTL）
_cache: TTLCache | None = None


def get_cache() -> TTLCache | None:
    return _cache


def init_cache(ttl: int) -> TTLCache:
    global _cache
    _cache = TTLCache(default_ttl=ttl)
    logger.info(f"Cache initialized with TTL={ttl}s")
    return _cache
