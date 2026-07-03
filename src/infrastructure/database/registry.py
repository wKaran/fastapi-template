"""Automatically import all SQLAlchemy models."""

from importlib import import_module
from pkgutil import iter_modules

import src.modules


def _safe_import(module: str) -> None:
    try:
        import_module(module)
    except ModuleNotFoundError:
        pass


def load_models() -> None:
    for _, feature_name, is_pkg in iter_modules(src.modules.__path__):
        if not is_pkg or feature_name == "relations":
            continue
        _safe_import(f"src.modules.{feature_name}.models")

    try:
        import src.modules.relations as relations

        for _, relation_name, _ in iter_modules(relations.__path__):
            _safe_import(f"src.modules.relations.{relation_name}")
    except ModuleNotFoundError:
        pass


load_models()
