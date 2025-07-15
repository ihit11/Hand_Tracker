import cv2
import mediapipe as mp
import threading
import sys
sys.path.append('/home/ihit2011/EspioProjects/EspioHandTrack')
from gui import *
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils


cam = cv2.VideoCapture(0)

TopLeft = False
TopRight = False
LowLeft = False
LowRight = False
Coardinates  = [0,0,0,0,0,0,0,0]
CalComplete = False
cvText = "Start Calibrating by pressing C"
pinching = False
tix, tiy = None, None
killWin = False
Moving = ""
_Moving = ""

def Calibrate(ix, iy):
    global TopLeft, TopRight, LowLeft, LowRight, CalComplete, cvText
    print(f"Calibrate called with ix={ix}, iy={iy}")
    if TopLeft == False:
        print("Setting TopLeft")
        Coardinates[0] = ix
        Coardinates[1] = iy
        TopLeft = True
        print(f"TopLeft set to: {ix}, {iy}")
        cvText = f"TopLeft set to: {ix}, {iy}"
    elif TopLeft == True and TopRight == False:
        print("Setting TopRight")
        Coardinates[2] = ix
        Coardinates[3] = iy   
        TopRight = True
        print(f"TopRight set to: {ix}, {iy}")
        cvText = f"TopRight set to: {ix}, {iy}"
    elif TopLeft == True and TopRight == True and LowLeft == False:
        print("Setting LowLeft")
        Coardinates[4] = ix
        Coardinates[5] = iy
        LowLeft = True
        print(f"LowLeft set to: {ix}, {iy}")
        cvText = f"LowLeft set to: {ix}, {iy}"
    elif TopLeft == True and TopRight == True and LowLeft == True and LowRight == False:
        print("Setting LowRight")
        Coardinates[6] = ix
        Coardinates[7] = iy
        LowRight = True
        print(f"LowRight set to: {ix}, {iy}")
        cvText = f"LowRight set to: {ix}, {iy}"
    if TopLeft and TopRight and LowLeft and LowRight and not CalComplete:
        print("Calibration Complete")
        cvText = f"LowRight set to: {ix}, {iy}"
        CalComplete = True

def CamDetect():
    global cvText, tix, tiy, pinching, killWin, Moving, _Moving
    print("Start Calibrating by pressing C wherever your index is")
    print("The order of calibration is Top left to right then Lower left to right")
    pix, piy = None, None
    
    while True:
        ret, vid = cam.read()
        vidrgb = cv2.cvtColor(vid, cv2.COLOR_BGR2RGB)
        r = hands.process(vidrgb)
        ix, iy = None, None
        tx, ty = None, None
        mx, my = None, None
        rx, ry = None, None
        lx, ly = None, None
        if r.multi_hand_landmarks:
            for hand_landmarks in r.multi_hand_landmarks:
                h, w, _ = vid.shape
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                little_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
                ix = int(index_finger_tip.x * w)
                iy = int(index_finger_tip.y * h)
                tx = int(thumb_tip.x * w)
                ty = int(thumb_tip.y * h)
                mx = int(middle_finger_tip.x * w)
                my = int(middle_finger_tip.y * h)
                rx = int(ring_finger_tip.x * w)
                ry = int(ring_finger_tip.y * h)
                lx = int(little_tip.x * w)
                ly = int(little_tip.y * h)
                mp_draw.draw_landmarks(vid, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.putText(vid, cvText, (0,20), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255,85,0), thickness=2)
        cv2.putText(vid, f"x: {ix} y: {iy}", (480,20), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255,85,0), thickness=2)
        if CalComplete:
            cvText="Calibration Complete"
            _TL = (Coardinates[0], Coardinates[1])
            _TR = (Coardinates[2], Coardinates[3])
            _LL = (Coardinates[4], Coardinates[5])
            _LR = (Coardinates[6], Coardinates[7])
            min_x = min(_TL[0], _TR[0], _LL[0], _LR[0])
            max_x = max(_TL[0], _TR[0], _LL[0], _LR[0])
            min_y = min(_TL[1], _TR[1], _LL[1], _LR[1])
            max_y = max(_TL[1], _TR[1], _LL[1], _LR[1])
            
            #index movement detection
            if ix is not None and iy is not None:
                tix = round(((ix - min_x) / (max_x - min_x)) * 1920) + 200
                tiy = round(((iy - min_y) / (max_y - min_y)) * 1080) + 180
                G3label.config(text=f"x: {tix} y: {tiy}")
                if min_x <= ix <= max_x and min_y <= iy <= max_y:
                    cv2.line(vid, _TL, _TR, (0,255,0), 2)
                    cv2.line(vid, _TR, _LR, (0,255,0), 2)
                    cv2.line(vid, _LR, _LL, (0,255,0), 2)
                    cv2.line(vid, _LL, _TL, (0,255,0), 2)
                    if pix is not None:
                        if ix > pix: 
                            print("Moving Right")
                            Moving="Right"
                            Glabel.config(text="Moving Right")
                        if ix < pix: 
                            print("Moving Left")
                            Moving="Left"
                            Glabel.config(text="Moving Left")
                    pix = ix
                    if piy is not None:
                        if iy > piy: 
                            print("Moving Down")
                            _Moving="Down"
                            G1label.config(text="Moving Down")
                        if iy < piy: 
                            print("Moving Up")
                            _Moving="Up"
                            G1label.config(text="Moving Up")
                    piy = iy
                    Mlabel.config(text=(f"x: {ix} and y: {iy}"))
            if ix is not None and iy is not None and tx is not None and ty is not None:
                distance = ((ix - tx) ** 2 + (iy - ty) ** 2) ** 0.5
                if distance < 27 and pinching == False:
                    print("Pinching: True")
                    G2label.config(text="Pinching True")
                    pinching = True
                if distance > 27 and pinching == True:
                    G2label.config(text="Pinching False")
                    pinching = False

        cv2.imshow("Espio Hand Track", vid)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            root.quit()
            cv2.destroyAllWindows()
            killWin = True
            break
        elif key == ord('c') and ix is not None and iy is not None:
            Calibrate(ix, iy)

def GestureCon():
    global Moving, _Moving
    while True:
        time.sleep(0.01)
        #Gesture controling
        if pinching:
            #Example Object
            egx, egy = EgObj.winfo_x(), EgObj.winfo_y()
            G4label.config(text=f"egx: {egx} egy: {egy}")
            if Moving == "Right":
                if (tix >= egx):
                    EgObj.place(x=tix, y=tiy)
            if Moving == "Left":
                if (tix <= egx):
                    EgObj.place(x=tix, y=tiy)


if __name__ == "__main__":
    camthr = threading.Thread(target=CamDetect, daemon=True)
    camthr.start()
    gesthr = threading.Thread(target=GestureCon, daemon=True)
    gesthr.start()
    while not CalComplete and not killWin:
        time.sleep(0.01)
        pass
    if killWin: print("Stopping program")
    else: gloop()
    camthr.join()
