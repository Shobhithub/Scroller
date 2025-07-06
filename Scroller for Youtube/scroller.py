import cv2
import mediapipe as mp
import pyautogui
import time

# Mediapipe setup
mp_hands=mp.solutions.hands
hands =mp_hands.Hands(max_num_hands=1)
mp_draw=mp.solutions.drawing_utils

#webcam
cap=cv2.VideoCapture(0)

#Time delay between actions
last_action_time=0
action_delay=1 #seconds

#Tip landmarks for fingers (excluding thumb)
finger_tips=[8,12]  #index amd middle fingers

def count_fingers(hand_landmarks):
    count=0
    for tip_id in finger_tips:
        if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y:
            count+=1
    return count

while True:
    success, img =cap.read()
    if not success:
        break

    img =cv2.flip(img,1)
    img_rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results=hands.process(img_rgb)

    current_time= time.time()
    if current_time - last_action_time < action_delay:
         cv2.imshow("Finger Detection", img)
         if cv2.waitKey(1) & 0xFF==27:
             break
         continue

    if  results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img,hand_landmarks, mp_hands.HAND_CONNECTIONS)

            fingers_up= count_fingers(hand_landmarks)

            if fingers_up==1:
                print("One Finger detected - Pressing Up")
                pyautogui.press('up')
                last_action_time=current_time

            if fingers_up==2:
                print("Two finger detected - Pressing Down")
                pyautogui.press('down')
                last_action_time = current_time


    cv2.imshow("Finger Detection", img)
    if cv2.waitKey(1)& 0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()



