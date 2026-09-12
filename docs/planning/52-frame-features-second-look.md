# 52 — Frame features, second look: the three small ones, the anti-cheat rule, and the second way to run

Written 2026-09-11 from the maintainer's read of [49-steam-frame-features.md](49-steam-frame-features.md).
Plan 49 gave each of the nine features a paragraph. That is enough to rank them and not enough to
build them. This document goes deeper on the three the maintainer asked about, records two rules they
gave in the same chat, and opens the one gap plan 49 underplayed. The calls are filed as D97 in the
decisions file. The four Frame tips shipped the same day, so they are not repeated here.

Read first: plan 49; [50-steamvr-pc-setup.md](50-steamvr-pc-setup.md) for the PC bench;
[42-read-aloud-feasibility.md](42-read-aloud-feasibility.md) for the spoken answer these features hang off.

**One sentence:** Headline first should be counted before it is built, Voice follow-ups is a sound cue plus
a short listening window on top of the mic code we already have, the floating panel must go through
SteamVR's own door and never touch a game, and the panel cannot exist until we decide where its brain runs.

---

## 1. What the maintainer said on 2026-09-11

- Go on the tips. Done the same day.
- Headline first is probably the weakest of the nine. Asked for a view on it. § 2.
- Voice follow-ups: a subtle "mic back on" sound is enough as feedback. Keep it simple. After the spoken
  answer, a period of listening; if words are coming in, keep listening. It must be obvious to the person
  that the mic is open, which is why the sound matters. Cost unknown. § 3.
- The floating panel could set off anti-cheat. Follow Steam's way of doing things so nobody gets in
  trouble playing online with bonsAI open. Best effort. § 4.
- The pretend-headset switches go in a settings file that survives updates. § 7.
- This PC is the test PC. Steam is signed in and can install games. No headset in the house.

## 2. Headline first: the weakest one, and what to do instead

**Agreed, it is the weakest.** Five reasons.

1. **It changes every answer for everyone to serve surfaces that mostly do not exist yet.** The popup
   slice waits on a Deck measurement, reading aloud is planned and not built, and the headset card is
   two decisions away. On the Deck today the answer box shows the whole answer, so nobody would notice
   the change, except when it makes an answer worse.
2. **The model probably does this already, most of the time.** A good answer opens with the point. We
   have never counted how often. If it is most of the time, there is nothing to build.
3. **"Carries the point and gives nothing away" fights itself.** For a boss fight or a puzzle, the
   sentence that carries the point is the spoiler. A headline that must not spoil becomes a throat-clear
   like "Here is how to get past this part", which is a worse opener than the natural one and exactly the
   filler the popup and the spoken answer would then show first.
4. **It is hard to judge.** "Stands alone" is a matter of taste. The spoiler check planned for the
   thinking display can judge leaks; it cannot judge whether a sentence is a good headline.
5. **The same benefit is available without touching the prompt.** The popup and the spoken answer can
   take the first sentence as it is and cut it to a length. Headset mode already asks the model to
   "answer for the ear", which is where a shaped opening belongs, and only for people who turned it on.

**What to do: count first, then decide.** The answer test already produces a set of answers on the PC.
Read the first sentence of each and mark two things: does it stand on its own as a summary, and does it
give away something the rest of the answer hides. Two numbers come out: how many of ten first sentences
stand alone, and how many leak. If at least seven in ten stand alone and none leak, drop the entry and
let Headset mode carry the shaped opening. If fewer, build the prompt change and re-run the same count
to prove it helped. No code is written before the count. The count is a morning's work for one worker
on the cheap model, since the answers already exist.

**Roadmap change.** The entry stays at two stars and gains one line: counted first, built only if the
count is poor. Filed as D97 call 4.

**The count came back 2026-09-12, and it is poor.** Of ten answers, only 2 opened with a sentence that
stands alone, and 0 gave anything away. By the rule above, that means this gets built. Before writing a
new prompt, one more count is owed: an answer-first opening was already tried on purpose the same
evening, on the same set of questions, and that run may already be the change being asked for here — so
it gets counted the same way before anything new is written. Full count in
[plan 53 § 4](53-steamvr-bench-findings.md#4-the-headline-first-count-run-the-same-morning).

## 3. Voice follow-ups: a sound, a short listen, a few words

### 3.1 What a person notices

The Deck finishes reading an answer aloud. A short rising tone plays. For the next few seconds the
Deck is listening. Say "again" and it reads the answer once more. Say "go on" and it reads the next
part, or unhides the spoiler it just stopped at. Say "stop" and it stops. Say "next" and it asks the
next suggestion in the row. Say nothing and, after a few seconds, a short falling tone plays and the
mic is off. If the menu happens to be open, a small mic mark shows beside the answer while the mic is
open, and goes away with the falling tone. There is no wake word and nothing is always listening.

### 3.2 What we already have

The mic code for the Ask box already does most of this. It records from the Deck's own mic, it tells
sound from quiet by a loudness line tuned for the Deck's mic in Gaming Mode, it waits two seconds of
quiet before it treats speech as finished, it throws away the filler words the small speech model
invents on noise, and there is a warm speech server that answers in a fraction of a second once it is
up, so the listening window does not start with a spin-up. The speech model is the small English one.
None of that is new work. What is new is a second way to use it: a short, bounded listen that ends by
itself and hands back a word, instead of a recording the person starts and stops.

### 3.3 The shape

| Step | What happens | How long |
|---|---|---|
| The spoken answer ends | The warm speech server was started when the reading began, so it is ready | 0 |
| Rising tone | Two notes up, about a fifth of a second, quiet | 0.2 s |
| Listening, quiet room | The mic is open. Nothing above the loudness line | up to 5 s, then close |
| Listening, someone speaks | Sound above the line keeps the window open until two seconds of quiet | at most 12 s from the tone |
| Match | The clip goes to the speech server; the words come back; matched against the short list | under a second, to measure |
| Act | Again, go on, stop, next | 0 |
| Falling tone | Two notes down, quieter than the rising one | 0.2 s |

**The word list.** Four words, chosen to sound unlike each other and unlike the filler the small
model invents on noise: **again**, **go on**, **stop**, **next**. "Next tip" from plan 49 becomes
"next" so a short clip is enough. Anything else, or nothing, closes the mic with the falling tone and
does nothing. A word is accepted only if the clip was clearly louder than the room was in the moment
after the tone, so a game's own sound does not get turned into a word.

**Where the sounds come from.** Two tiny sound files, shipped with the plugin, played by the Python
side through the Deck's sound system the same way the spoken answer is, so they play whether the menu
is open or closed. Generated once by a script, not recorded. Quiet by design: they sit under the game.

**The switch.** One setting, off by default, under the Read aloud setting: *Listen for a word after
reading*. On is the whole feature. There is no separate switch for the tones.

### 3.4 What it costs

Two stars, as plan 49 said, with one warning. The listening code is a small second entry into the
mic service, perhaps a hundred and fifty lines with its test. The tones are two files and one play
call. The wiring is: when the reading ends, start the listen; when a word comes back, do the thing.
The expensive part is the setting itself: this repo has measured one on-off setting at about
eighteen files and thirty edit points, and that is the honest size of the switch. One worker on the
mid-priced model for the build, as the two-star and three-star features this year were. The real
cost is the Deck evening after: the two tests below cannot be done anywhere else.

### 3.5 Waits on, and what can be done before that

Waits on Read answers aloud, which is planned under D74 and not yet built. The listen and the tones
do not need it: for testing, the window can open after a typed answer finishes, from a Developer
switch, so the recognition test below can run before the voice exists.

### 3.6 The two Deck tests

1. **Can it hear the four words over a game.** A game playing at normal volume through the speakers,
   the Deck at arm's length. Say each word five times. Count the hits, the misses and the wrong words.
   The number that matters: how many of twenty are right. Below fifteen the loudness rule needs work.
2. **Does the tone read as "listening".** Someone who has not seen the feature hears the answer end
   and the tone. Ask what they think the tone means. If they do not say "it is listening", the tone is
   wrong, not the person.

### 3.7 Open questions

- What "go on" means when there is no hidden spoiler and the answer was read to the end. Proposed:
  nothing, and the falling tone.
- Whether the falling tone is wanted at all. Proposed: yes, but quieter; a phone's convention.
- Whether the mic mark should show on the popup as well as in the menu. Proposed: yes, once the
  popup exists.

## 4. The floating panel and anti-cheat

**The maintainer's rule.** Follow Steam's way of doing things so a person playing online with bonsAI
open never gets in trouble. Best effort. Filed as locked in D97.

**Why the risk is real.** Anti-cheat programs watch for anything that gets inside the game: a file
loaded into it, a hook on how it draws, a read of its memory, fake input, a copy of its picture. Tools
that do those things get people banned, whatever their purpose.

**Why SteamVR's own door avoids it.** A SteamVR panel is a separate program. It hands SteamVR a
picture and a position; SteamVR draws it into the headset on top of the game. The game never sees the
panel and the panel never touches the game. This is how the desktop-mirror tool in plan 50 works, and
how the well-known VR toolbox and frame-counter panels have worked for years beside online VR games.
It is also the same position bonsAI holds on the Deck, where it lives inside Steam's own menu and
never inside a game.

**The rules the panel follows, in full.**

1. Panels go only through SteamVR's official panel door. No other way of drawing over a game.
2. Nothing of ours is ever loaded into a game.
3. No hooks on a game's drawing, sound or input.
4. No reading a game's memory, files in use, or saved state while it runs.
5. No sending input to a game. bonsAI's panel takes its own pointer events from SteamVR and nothing
   else.
6. No copying the game's picture. bonsAI has no need to see the game.
7. If any future feature would need one of the above, it is a maintainer decision first, not a
   worker's shortcut.

**What we cannot promise, and say so.** Each game's anti-cheat sets its own policy, and a few forbid
any overlay at all. When the panel ships, the README says which door it uses and that a game may still
object. That is the honest limit of best effort.

## 5. The second way to run: the gap plan 49 underplayed

Plan 49 said the panel needs "its own way to reach the Python side" and moved on. It is bigger than
that. **Today the only way anything talks to bonsAI's Python side is through Decky on the Deck.** There
is no network door, no web address, nothing a program on another machine can ask. A panel on the PC
would have a screen and no brain.

Three ways to give it one:

| Option | What it is | For | Against |
|---|---|---|---|
| (a) The PC program carries its own brain | The panel talks to Ollama itself and re-does the prompt building, the knowledge base search, the spoiler rules | No Deck needed | A second copy of everything that makes bonsAI bonsAI; it drifts from the first within weeks |
| (b) A network door on the Deck | The Deck's bonsAI listens on the home network; the PC program asks it | One brain, no new code on the PC beyond the panel | The Deck must be on and awake; a listening port on the Deck is a new thing to secure; two devices for one feature |
| (c) The Python side runs on the PC too | The same Python code, unchanged, started by the panel program on the PC; the panel is its front | One code base, two hosts; the PC is where the model runs anyway | Unknown how much of the Python side assumes the Deck: settings folder, sound system, Steam paths |

**Recommendation: find out how far (c) is from true before choosing.** One fact already in hand: the
Python tests run and pass on the maintainer's Windows PC, every day. So the Python side is not welded
to the Deck. What is unknown is the edge: the parts that reach the sound system, the settings folder
Decky provides, the Steam paths, the game-detection. Those are the parts a PC host would have to
supply differently.

**What to check on the PC, during the same bench session as the panel test.** Start the Python side
on the PC by hand, outside Decky, with a folder of its own for settings, and ask it one question the
way the frontend would. Note what breaks. That list is the cost of (c). It is a half-day for one
worker and it turns the six-star decision into a priced one.

**Not reopened: llama.cpp.** The study said do not reopen it because of the Frame, and nothing here
changes that. The PC runs Ollama. The Frame's own chip is a Deck-shaped question for another day.

**The check passed, 2026-09-12.** The plugin's Python side started outside Decky on the maintainer's
PC with the fifty-line stand-in, answered nine calls the frontend normally makes, and reached Ollama.
The decision is now priced rather than guessed at. See
[plan 53 § 3](53-steamvr-bench-findings.md#3-the-plugins-python-side-on-this-pc-it-runs).

## 6. Glance view: the brief and the mockup

**Shelved 2026-09-12 by the maintainer.** Their own words: "shelve the glanceable view for now. It's too much UI
change and we're not ready for it yet." This section stays as the record for when it comes back.

**The mockup:** [Glance View on the design canvas](https://claude.ai/code/artifact/c48fb3e2-38ef-4c91-997c-c515353eec96),
drawn 2026-09-11. The working files are in [docs/design/handoffs/glance-view/](../design/handoffs/glance-view/),
so the canvas can be rebuilt after a change. Five boards at true size, 300 px wide and 700 px tall: the
Main tab as built today, then three ways to show only the answer. Every measurement in the drawing is
a value from the stylesheet, cited in § 6.2; the only assumed value is the dark ground behind the panel,
which is Steam's and not ours.

### 6.1 What a person notices

The Deck shows the *Reply ready* popup over the game. They open the menu. Instead of the full panel
(tab bar, chat row, the answer, two chips, the question box, the Ask button) they see only the answer,
one third bigger than usual, filling the column top to bottom. Down walks the paragraphs as it does
today. A reads the answer aloud, once that exists. B puts the full panel back. Nothing else is on
screen.

### 6.2 What the drawing is built from

| Thing drawn | Value used | Where it comes from |
|---|---|---|
| Column | 300 px wide | the design language, rule 1 |
| Tab bar | 20 px tall, then a 4 px gap; dashes 14 by 3 px, 4 px apart; name 11 px, LB and RB 9 px | the tab bar constants and stylesheet |
| Dock at the bottom | 157 px measured; chips 30 px tall two across with a 4 px gap; question box 66 px empty; Ask button 36 px | the chip row layout, the Ask bar constants, the plan 29 and plan 45 measurements |
| Reading space today | 412 px, a measured number, never set in code | plan 30 and plan 45 |
| Answer text today | 12 px on a 1.4 line, colour #d4dde6, bubble 92 % wide, padding 8 by 10, green border and wash | the Main tab stylesheet, section 6 |
| A paragraph as a D-pad stop | 2 px left border, 6 px left padding, radius 4; ring colour rgba(150,187,223,0.9) with a faint blue fill | section 6 |
| Hidden spoiler | padding 10 by 12, radius 8, two lines at 12 px bold and 11 px | the markdown chunk renderer |
| Glance text | 16 px on a 1.5 line, so one third bigger; option B 20 px | chosen for the drawing, not from code |

### 6.3 The three options, and the axis each explores

- **Leading candidate, bare.** Only the answer, edge to edge, plus one 24 px line at the bottom
  naming what B, A and Down do. Keeps the most reading space: 676 px against 412 today. The
  paragraph ring, the spoiler block and the copy control are the ones already built, only larger.
- **Option B, one paragraph at a time.** Text at 20 px, one paragraph fills the screen, dots say
  where you are, Down moves on. Best across a room; worst for a checklist, because two steps are
  never visible together.
- **Option C, the tab bar stays.** LB and RB still switch tabs, so nobody is ever lost, and the
  planned Read aloud button takes the Ask button's place. Costs 92 px of reading space against the
  bare option.

**Recommendation: the bare option**, with option C's Read aloud button added only once reading aloud
exists. The tab bar can be brought back by B in one press; keeping it costs a row for the case where
someone forgets what B does, and the bottom line already tells them.

### 6.4 What it waits on, and the cost

- **A Deck measurement first**, as every Main tab change does: the drawing says 676 px of reading
  space; the device says what it really is over a running game (the body measured 736 px there, so
  the number may be better, not worse).
- **The entry point.** Today, tapping the popup only opens Decky's tab and sets a flag; it does not
  open bonsAI or land on the answer. Glance view needs that flag to mean "open bonsAI on the Main tab
  in glance mode", which is the same wiring plan 38's popup work needs. Build them together.
- **Text size.** The scaling hook exists and every size goes through it, so the one-third-bigger text
  is a profile, not new plumbing. The adjustable-text-size setting on the roadmap would ride the same
  hook later.
- **Focus.** Down through the paragraphs and the spoiler stop already work; B needs a new handler
  that restores the panel and lands the ring where it was. A focus-graph entry, as every new control.
- **Cost: two stars**, as plan 49 said. One worker on the mid-priced model, plus the Deck evening for
  the measurement and the free-play sweep it owes.

### 6.5 Open questions for the maintainer, on the canvas

1. Bare, B or C. The drawing exists so this is a look, not a read.
2. Should glance open on its own from the popup, or should the menu open as today and glance be one
   press away? The drawing assumes the popup opens straight into glance.
3. Should the chat row's LB and RB (next and previous chat) work inside glance? The drawing says no.
4. When a new answer arrives while glance is open: stay in glance and show it, or bring the full
   panel back? Both are drawn (second row of the canvas). Recommended: stay.

### 6.6 Settled with the maintainer on 2026-09-12

**The position rail.** The maintainer asked for a large, obvious sign of where you are in the
answer. The drawing now has a rail down the right edge of every glance board: an arrow up, the stop
you are on out of how many, one tall block per paragraph with the current one lit, an arrow down.
The hidden spoiler counts as a stop, as it does for the D-pad today. The rail takes 32 px of width,
so the text gets 250 px instead of 276. Up and Down move the ring and the rail together.

**What each press does.** Glance is a lid on the panel. Reading presses work inside it; any other
press lifts it.

| Press | In glance |
|---|---|
| Up, Down | Move between paragraphs; the ring and the rail follow |
| A on the hidden spoiler | Opens it, as today |
| A anywhere else | Read aloud, once that exists; nothing until then |
| B | The full panel comes back |
| X, Y, Steam button | The full panel comes back, then the press does what it does today |
| LB, RB | The full panel comes back on the tab you asked for |
| A tap on the answer | What A does |
| A tap on the bottom line | What B does |

**Coming back is not a morph, and must not snap either.** The full panel appears with the same
paragraph at the top and the ring still on it, so the eye lands where it was. The bars around the
answer fade in over about a sixth of a second instead of appearing at once. The text drops from the
big size to the normal size in that moment; that reflow is the whole change. The fade is measured on
the Deck before it ships, as every Main tab change is, and dropped if the panel's own frame rate
suffers.

**The bottom line may wrap.** A second line costs 14 px out of 676 px of reading space, about two
per cent. The drawing's leading board shows the long version on two lines so the cost is visible.
The rule: the line is never cut off at the edge; if it does not fit, it wraps.

## 7. The PC bench, three additions to plan 50

1. **The pretend-headset switches go in the settings file that survives updates.** Steam keeps a
   personal SteamVR settings file in its own config folder, and updates do not touch it. The three
   lines for the pretend headset, and the line that turns the pretend driver on, go there. Plan 50's
   two-file edit stays as the fallback if SteamVR ignores the driver line in the personal file, which
   is possible and will be known within a minute of trying. The exact contents are in § 7.1. **Worked
   on the first start, 2026-09-12** — the two-file edit was never needed.
2. **A fourth thing to find out: do SteamVR's small pop-up cards still work.** Plan 49's cheapest
   first step is to post one card when an answer finishes. That part of SteamVR is old and Valve has
   not looked after it in years. Before betting the first step on it, post one card from the bench and
   see whether the current SteamVR shows it. If not, the first step is the panel itself.
3. **A fifth: can a panel take input at all.** The three questions in plan 50 are about reading. A
   headset version needs a way to ask as well. With the desktop-mirror tool open, click a text box in
   it and type. Whether typing reaches the panel, and whether a laser can press a button in it, decide
   how much of the Ask box a headset version can have.

**Where results go: one file.** `docs/planning/53-steamvr-bench-findings.md`, created by the session
that runs the bench, linked from the roadmap's floating-panel entry. Not the study, not a spikes
folder.

### 7.1 The personal settings file

Path: the `config` folder inside the Steam folder, file `steamvr.vrsettings`. On this PC that is
`C:\Program Files (x86)\Steam\config\steamvr.vrsettings`. It does not exist yet on this PC (checked
2026-09-11); SteamVR creates it on first run, and it may be created empty by hand before that.

```
{
  "steamvr": {
    "requireHmd": false,
    "forcedDriver": "null",
    "activateMultipleDrivers": true
  },
  "driver_null": {
    "enable": true
  }
}
```

To go back to a real headset later, remove the `forcedDriver` line and set `requireHmd` back to
`true`, or delete the file.

## 8. Order, revised

1. Tips and README line. Done 2026-09-11.
2. The Headline first count. A morning, no code. **Started 2026-09-12.**
3. Glance view: the mockup goes to Claude Design, then the Deck measurement, then the build. **Shelved
   2026-09-12 by the maintainer — too much UI change, not ready for it yet.**
4. The PC bench: SteamVR, the pretend headset, the desktop-mirror tool, the five questions, and the
   "run the Python side on the PC" check from § 5. One session. Findings to plan 53. **Done 2026-09-12.**
5. Read answers aloud (D74), then Voice follow-ups with the tones, then Spoilers by voice.
6. The second-way-to-run decision, now priced by step 4.
7. Everything above four stars, after 6.
