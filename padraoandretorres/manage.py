#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    if os.environ.get("ENV") == "local":
        attach_debugpy()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "padraoandretorres.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def attach_debugpy():
    """
    Attach debugpy
    """
    try:
        print("Attaching debugpy")
        import debugpy

        debugpy.listen(("0.0.0.0", 3011))
        print("Attached debugpy!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
