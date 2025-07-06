✅ Purpose:
This Python program uses your webcam to detect hand gestures (1 or 2 raised fingers) and simulate keyboard key presses like up and down. It's useful for controlling things like YouTube Shorts or scrolling through web pages without touching your keyboard.

⚙️ How It Works:
Webcam Access (cv2.VideoCapture)
Captures real-time video from your webcam.

Hand Detection (mediapipe.solutions.hands)
Detects your hand and tracks landmarks (key finger joint positions) in each video frame.

Gesture Recognition

Focuses on index (tip 8) and middle (tip 12) fingers

If the tip of a finger is above its lower joint, it's considered “raised”.

Action Trigger with Delay

If 1 finger is raised → pyautogui.press('up') is called

If 2 fingers are raised → pyautogui.press('down') is called

A 1-second delay between actions avoids multiple triggers too quickly.

Visualization

The video feed is shown with hand landmarks drawn in real time (cv2.imshow).

🧠 Example Use Case:
Show 1 finger → Scroll up

Show 2 fingers → Scroll down

Great for hands-free control of web apps, slideshows, or media players
