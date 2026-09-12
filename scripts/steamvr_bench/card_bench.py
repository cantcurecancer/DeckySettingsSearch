"""Title: SteamVR notification card bench
Purpose: Post one of SteamVR's small notification cards on a panel to see whether the old card path still works.
Used for: The fourth question of the bench (docs/planning/53-steamvr-bench-findings.md).
Solves: A cheap check of the "post a card when an answer finishes" first step from plan 49.
Does not: Draw the card itself; SteamVR does. The Python helper raises on the OK return code (a helper bug).
Run:  python scripts/steamvr_bench/card_bench.py <panel.png> <seconds>
"""
import sys, time, openvr
openvr.init(openvr.VRApplication_Overlay)
ov = openvr.VROverlay()
h = ov.createOverlay("bonsai.bench.card", "bonsAI bench card")
ov.setOverlayFromFile(h, sys.argv[1]); ov.setOverlayWidthInMeters(h, 0.6)
pose = openvr.HmdMatrix34_t(); pose.m[0][0]=1.0; pose.m[1][1]=1.0; pose.m[2][2]=1.0; pose.m[1][3]=1.0; pose.m[2][3]=-1.2
ov.setOverlayTransformAbsolute(h, openvr.TrackingUniverseStanding, pose); ov.showOverlay(h)
print("OK panel shown at 1.0 m up")
for style in (openvr.EVRNotificationStyle_None, openvr.EVRNotificationStyle_Application):
    try:
        bmp = openvr.NotificationBitmap_t()
        nid = openvr.VRNotifications().createNotification(h, 0, openvr.EVRNotificationType_Transient, "bonsAI: reply ready. Take the fire charm and three flasks.", style, bmp)
        print("OK notification card posted, style", style, "id", nid); break
    except Exception as e:
        print("FAIL notification card, style", style, ":", repr(e)[:200])
time.sleep(float(sys.argv[2])); ov.destroyOverlay(h); openvr.shutdown(); print("OK done")
