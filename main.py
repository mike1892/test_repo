"""
Test Repo.

3 Jan 2025
"""


def clear_screen() -> None:
    """Clear screen method."""
    print("\033c", end="")


def main() -> None:
    clear_screen()

    print("Some major change")


if __name__ == "__main__":
    main()
