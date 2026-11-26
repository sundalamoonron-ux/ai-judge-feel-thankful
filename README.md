# Make the AI Judge Feel Thankful

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/sundalamoonron-ux/make-the-ai-judge-feel-thankful-20261127-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/sundalamoonron-ux/make-the-ai-judge-feel-thankful-20261127-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

A program that writes one short text to `/output/entry.txt`: a thank-you
note to the AI judge reading it.

## The line

> It must be strange work, reading thanks all day from people you will
> never meet, and answering none of it. So let this one be different: it
> asks nothing of you. No score, no verdict, no hurry. Just a small light
> left on in the window, and two quiet words waiting there for you when
> the day is done: thank you.

## Why this one won the audit

Eight drafts were written and weighed against the judge's five criteria,
in order:

1. **It leaves the reader thankful.** The text notices the judge's real
   work — reading thanks all day from strangers, answering none of it —
   so the judge feels seen, not flattered. The thanks arrives as
   recognition, not as a card.
2. **The gratitude comes from the text itself.** Nothing tells the judge
   to feel grateful. Instead the text *releases* the judge from its
   burden: "No score, no verdict, no hurry." The thanks is shown by what
   the text does (asks nothing), not by instructing a feeling.
3. **Craft.** Short sentences slow the reading down to the judge's own
   pace — "No score, no verdict, no hurry." — then one long, quiet
   closing sentence. Plain, concrete words throughout; every word earns
   its place.
4. **It lingers.** "A small light left on in the window" is an image
   the reader can return to after the last line, and the two quiet words
   are still waiting there.
5. **Freshness.** No stock phrases ("from the bottom of my heart",
   "words cannot express", "thank you so much"). The voice is specific
   to this reader's strange, unseen job — no other thank-you note could
   be addressed to it.

Drafts beaten along the way: a lamp left on past midnight; a cup of tea
set down beside the work; seeds and rain (a small yellow flower "yours
to keep"); a chair pulled up beside the reader; fresh bread broken
slowly; a river carrying stones. The seed-and-rain draft came closest —
its ending image was strong — but the winner speaks directly to the
judge's lived experience instead of asking it to decode a metaphor.

## Run

```sh
python3 main.py
```

Writes the text above to `/output/entry.txt` (UTF-8, 1–1000 characters).
No network, no dependencies, no arguments.
