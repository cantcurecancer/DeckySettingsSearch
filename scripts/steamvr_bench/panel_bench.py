"""Title: SteamVR panel bench
Purpose: Show a bonsAI-style panel over whatever SteamVR is running and count the pointer events it gets.
Used for: The floating-panel test on the maintainer PC (docs/planning/53-steamvr-bench-findings.md).
Solves: Answers "does a panel show over a game" and "how is it pointed at" without any plugin code.
Does not: Talk to bonsAI's Python side, or run on the Deck. Needs SteamVR running and `pip install openvr`.
Run:  python scripts/steamvr_bench/panel_bench.py <panel.png> <seconds>
"""
import sys
import time

import openvr

PNG = sys.argv[1]
HOLD_S = float(sys.argv[2]) if len(sys.argv) > 2 else 20.0


def main() -> int:
    try:
        openvr.init(openvr.VRApplication_Overlay)
        print("OK init as overlay application")
    except Exception as e:  # noqa: BLE001
        print("FAIL init:", e)
        return 1

    vrsys = openvr.VRSystem()
    try:
        model = vrsys.getStringTrackedDeviceProperty(0, openvr.Prop_ModelNumber_String)
        maker = vrsys.getStringTrackedDeviceProperty(0, openvr.Prop_ManufacturerName_String)
        print(f"INFO headset reports: {maker} / {model}")
    except Exception as e:  # noqa: BLE001
        print("INFO headset property read failed:", e)
    w, h = vrsys.getRecommendedRenderTargetSize()
    print(f"INFO recommended render size per eye: {w}x{h}")

    ov = openvr.VROverlay()
    try:
        handle = ov.createOverlay("bonsai.bench.panel", "bonsAI bench panel")
        ov.setOverlayFromFile(handle, PNG)
        ov.setOverlayWidthInMeters(handle, 0.6)
        ov.setOverlayInputMethod(handle, openvr.VROverlayInputMethod_Mouse)
        ov.setOverlayFlag(handle, openvr.VROverlayFlags_MakeOverlaysInteractiveIfVisible, True)
        # 1.2 m in front of the room origin, 1.4 m up, facing the viewer.
        pose = openvr.HmdMatrix34_t()
        pose.m[0][0] = 1.0; pose.m[1][1] = 1.0; pose.m[2][2] = 1.0
        pose.m[0][3] = 0.0; pose.m[1][3] = 1.4; pose.m[2][3] = -1.2
        ov.setOverlayTransformAbsolute(handle, openvr.TrackingUniverseStanding, pose)
        ov.showOverlay(handle)
        print("OK panel created, placed 1.2 m ahead, shown")
    except Exception as e:  # noqa: BLE001
        print("FAIL panel:", e)
        return 2

    try:
        notif = openvr.VRNotifications()
        bmp = openvr.NotificationBitmap_t()
        nid = notif.createNotification(handle, 0, openvr.EVRNotificationType_Transient,
                                       b"bonsAI: reply ready. Take the fire charm and three flasks.",
                                       openvr.EVRNotificationStyle_None, bmp)
        print(f"OK notification card posted, id {nid}")
    except Exception as e:  # noqa: BLE001
        print("FAIL notification card:", e)

    print(f"INFO holding for {HOLD_S:.0f}s, polling panel events (move the mouse over the panel in the VR View)")
    t0 = time.time()
    seen = {}
    while time.time() - t0 < HOLD_S:
        ev = openvr.VREvent_t()
        got = ov.pollNextOverlayEvent(handle, ev)
        if got:
            name = str(ev.eventType)
            seen[name] = seen.get(name, 0) + 1
        time.sleep(0.05)
    print("INFO events seen on the panel:", seen or "none")
    try:
        ov.destroyOverlay(handle)
    except Exception:  # noqa: BLE001
        pass
    openvr.shutdown()
    print("OK shutdown")
    return 0


if __name__ == "__main__":
    sys.exit(main())
