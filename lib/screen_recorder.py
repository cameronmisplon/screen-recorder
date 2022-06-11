import cv2
import numpy as np
import pyautogui


SCREEN_SIZE = tuple(pyautogui.size())

fourcc = cv2.VideoWriter_fourcc(*"DIVX")
fps = 19

output = cv2.VideoWriter("..\\outputs\\test.mp4", fourcc, fps, (SCREEN_SIZE))
record_seconds = 15

## capture screenshots

for i in range(fps*record_seconds):
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
output.release()