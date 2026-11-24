"""
URL Shortener CLI
Shorten lengthy URLs instantly using the TinyURL service via pyshorteners.
"""
import sys

try:
    import pyshorteners
except ImportError:
    print("Error: 'pyshorteners' is not installed. Install it via: pip install pyshorteners")
    sys.exit(1)


def shorten_url(url: str) -> str:
    """Shortens a URL using TinyURL."""
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)


def main():
    print("=" * 45)
    print("            URL Shortener CLI")
    print("=" * 45)

    if len(sys.argv) > 1:
        target_url = sys.argv[1]
        try:
            shortened = shorten_url(target_url)
            print(f"Original : {target_url}")
            print(f"Shortened: {shortened}")
        except Exception as e:
            print(f"Error shortening URL: {e}")
        return

    while True:
        url_input = input("\nEnter URL to shorten (or 'exit' to quit): ").strip()
        if not url_input:
            continue
        if url_input.lower() in ("exit", "quit", "q"):
            print("Exiting URL Shortener. Goodbye!")
            break

        try:
            shortened = shorten_url(url_input)
            print(f"  --> Shortened URL: {shortened}")
        except Exception as e:
            print(f"  [!] Failed to shorten URL: {e}")


if __name__ == "__main__":
    main()
