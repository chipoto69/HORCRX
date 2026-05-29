"""Provider-level defaults for Z.AI / GLM profiles."""

from __future__ import annotations

from typing import Any, Dict


_TRUE_STRINGS = {"1", "true", "yes", "on"}


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        return value.strip().lower() in _TRUE_STRINGS
    return bool(value)


def _provider_is_zai(config: Dict[str, object]) -> bool:
    model_cfg = config.get("model")
    if not isinstance(model_cfg, dict):
        return False
    return str(model_cfg.get("provider") or "").strip().lower() == "zai"


def apply_zai_provider_defaults(config: Dict[str, object]) -> set[str]:
    """Enable streaming-friendly defaults for Z.AI / GLM profiles.

    Z.AI exposes incremental content and reasoning deltas over streaming chat
    completions.  When Hermes is using the ``zai`` provider, turn on the CLI
    and gateway streaming surfaces by default so GLM profiles behave like live
    streaming models instead of buffered dead air.
    """

    if not _provider_is_zai(config):
        return set()

    changed: set[str] = set()

    display_cfg = config.get("display")
    if not isinstance(display_cfg, dict):
        display_cfg = {}
        config["display"] = display_cfg

    if not _truthy(display_cfg.get("streaming")):
        display_cfg["streaming"] = True
        changed.add("display.streaming")

    if not _truthy(display_cfg.get("show_reasoning")):
        display_cfg["show_reasoning"] = True
        changed.add("display.show_reasoning")

    gateway_cfg = config.get("gateway")
    if not isinstance(gateway_cfg, dict):
        gateway_cfg = {}
        config["gateway"] = gateway_cfg

    streaming_cfg = gateway_cfg.get("streaming")
    if not isinstance(streaming_cfg, dict):
        streaming_cfg = {}
        gateway_cfg["streaming"] = streaming_cfg

    if not _truthy(streaming_cfg.get("enabled")):
        streaming_cfg["enabled"] = True
        changed.add("gateway.streaming.enabled")

    return changed
