from __future__ import annotations

from tifa.settings import settings

# pytest no need to check
if not settings.ENV == "TEST":
    use_console_exporter = True
