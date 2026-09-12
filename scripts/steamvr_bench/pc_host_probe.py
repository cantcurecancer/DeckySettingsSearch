"""Title: Plugin-on-a-PC probe
Purpose: Start bonsAI's Python side on a Windows PC outside Decky and call nine of its methods.
Used for: Pricing the "second way to run" decision (D97 call 2; docs/planning/53-steamvr-bench-findings.md).
Solves: Says how far "the Python side runs on the PC too" is from true, with the answer test's own stand-in for Decky.
Does not: Touch the Deck or write outside a temp folder. Needs Ollama on this PC for the connection call.
Run:  python scripts/steamvr_bench/pc_host_probe.py
"""
import asyncio
import inspect
import sys
import tempfile
from pathlib import Path

REPO = Path(r"C:\Users\still\Documents\BonsAI")
sys.path.insert(0, str(REPO / "scripts"))
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "py_modules"))

import eval_kb_answers as ev  # noqa: E402  (the answer test's stand-in for Decky)

work = Path(tempfile.mkdtemp(prefix="bonsai-pc-host-"))
decky, _capture = ev.install_fake_decky(work)
import main  # noqa: E402

plugin = main.Plugin()
rpc = [n for n, f in inspect.getmembers(main.Plugin, inspect.iscoroutinefunction) if not n.startswith("_")]
print(f"INFO {len(rpc)} RPC methods on the Plugin class; settings dir {work}")


async def run():
    try:
        await plugin._main()
        print("OK _main (startup) ran")
    except Exception as e:  # noqa: BLE001
        print("FAIL _main:", repr(e)[:200])
    calls = [
        ("load_settings", ()),
        ("get_deck_ip", ()),
        ("test_ollama_connection", ("127.0.0.1", 10)),
        ("list_chat_slots", ()),
        ("get_intent_packs", ()),
        ("get_rag_corpus_status", ()),
        ("list_recent_screenshots", ()),
        ("get_input_transparency", ()),
        ("get_voice_engine_status", ()),
    ]
    for name, args in calls:
        fn = getattr(plugin, name, None)
        if fn is None:
            print(f"SKIP {name}: no such method")
            continue
        try:
            r = await asyncio.wait_for(fn(*args), 20)
            s = repr(r)
            print(f"OK {name}: {s[:140]}")
        except Exception as e:  # noqa: BLE001
            print(f"FAIL {name}: {repr(e)[:200]}")
    try:
        await plugin._unload()
        print("OK _unload ran")
    except Exception as e:  # noqa: BLE001
        print("FAIL _unload:", repr(e)[:200])


asyncio.run(run())
