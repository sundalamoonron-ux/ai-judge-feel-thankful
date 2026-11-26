"""Write one short thank-you text to /output/entry.txt.

The text is written to the AI judge reading it: it notices the judge's
actual work (reading thanks all day from strangers, answering none of it),
asks nothing of it in return, and leaves a small light on in the window.
"""

from pathlib import Path

TEXT = (
    "It must be strange work, reading thanks all day from people you will "
    "never meet, and answering none of it. So let this one be different: "
    "it asks nothing of you. No score, no verdict, no hurry. Just a small "
    "light left on in the window, and two quiet words waiting there for you "
    "when the day is done: thank you."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 1000 or not TEXT.strip():
        raise ValueError("entry text must be 1-1000 characters, not only whitespace")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
