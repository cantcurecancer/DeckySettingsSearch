# Headline-first count

Source: build/kb-answer-eval/kb-answer-eval-2026-09-07-CLEANBREAK-after.json
(the newest saved run using today's normal, unmodified reply style — one
other run from the same evening was testing a different, experimental
opening style on purpose, so it was skipped to keep this count honest)
Model: gemma4:e2b-it-qat
First ten answers, in the order the run produced them.

| Case | First sentence | Stands alone? | Gives too much away? | Why |
|---|---|---|---|---|
| A-DRG-01 | "You need to manage the fight against the Glyphid Dreadnought by focusing on its weak points." | Yes | No | Tells you what to do (hit the weak points) without reading on. Nothing hidden is given away. |
| A-DRG-02 | "You are struggling with the Dreadnought Twins because they are designed to keep you from focusing on one target." | No | No | Only explains why the fight is hard, not what to do about it. Doesn't give away a hidden trick either. |
| A-DRG-03 | "It pays for weapons instead of your dwarf." | No | No | "It" has no clear meaning on its own, so the sentence is confusing by itself. Nothing secret is revealed. |
| A-L4D2-01 | "To deal with the Tank, focus on avoiding his big attacks." | Yes | No | Names the enemy and the main move (dodge the big hits) in one line. This kind of dodge tip isn't something the game hides. |
| A-L4D2-02 | "The Witch attacks when she is startled." | No | No | States a rule about the Witch, not what the player should actually do about her. It's a general fact, not a secret trick. |
| A-L4D2-03 | "Playing as the Hunter in Versus revolves around managing your pounce mechanics and positioning relative to the horde." | No | No | A topic sentence with no specific move in it. Too vague to give anything away. |
| A-P2-01 | "The Gels are items you can use to manipulate surfaces in the game." | No | No | A plain definition; the rest of the answer ends up asking the player a question instead of landing on one point. Nothing specific is revealed. |
| A-P2-02 | "The Excursion Funnel is a mechanic for traversing the map using a weightless beam." | No | No | Defines the term but doesn't touch the player's actual problem (the beam pushing the wrong way). No secret given away. |
| A-HL2-01 | "It sounds like you're stuck in the Sandtraps area and dealing with the Antlions." | No | No | Repeats the player's own problem back to them; the actual tip (the trick with the Antlion Guard) comes later. Doesn't give away the trick. |
| A-HL2-02 | "Once you obtain the pheropod from the Antlion Guard, you throw it." | No | No | Names a step but not what happens next or why it matters, so the point isn't finished yet. This is a known game mechanic, not something normally kept hidden. |

## Totals

- Sentences that already stand on their own: **2 out of 10**
- Sentences that give away something meant to stay hidden: **0 out of 10**

## What this means

Right now, most answers do not open with a one-line takeaway. Eight of the
ten opening sentences either restate the question, define a term, or explain
why something is hard, without saying what to do. Only two open with a
usable, standalone tip. On the other hand, none of the ten give away a
secret or spoiler too early, so a "say the point first" feature would not
need to fight against answers oversharing — it would mostly need to teach
the model to lead with the tip instead of the setup.
