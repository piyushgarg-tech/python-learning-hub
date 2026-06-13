import cv2
import time

# Reading Video From Webcam
video = cv2.VideoCapture(0)

# Writing Video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter("Output.mp4", fourcc, 25.0, (640,480))
font = cv2.FONT_HERSHEY_DUPLEX
color = (0,255,0)

while video.isOpened():
    ret,frame = video.read()

    if ret:
        output.write(frame)
        # Adding Shapes
        # Left Upper Corner
        cv2.line(frame, (15, 15), (15, 155), color=color, thickness=2)
        cv2.line(frame, (15, 15), (155, 15), color=color, thickness=2)
        # Right Upper Corner
        cv2.line(frame, (625, 15), (625, 155), color=color, thickness=2)
        cv2.line(frame, (625, 15), (485, 15), color=color, thickness=2)
        # Left Lower Corner
        cv2.line(frame, (15, 465), (15, 325), color=color, thickness=2)
        cv2.line(frame, (15, 465), (155, 465), color=color, thickness=2)
        # Right Lower Corner
        cv2.line(frame, (625, 465), (625, 325), color=color, thickness=2)
        cv2.line(frame, (625, 465), (475, 465), color=color, thickness=2)
        # Adding Text
        # Text Middle
        cv2.putText(frame, "Recording..... Press 'q' to Stop.", (140,440), font, 0.7, color=(255,255,255), thickness=1, lineType=cv2.LINE_AA)
        # Webcam Display
        cv2.imshow("Webcam Live", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

video.release()
output.release()
cv2.destroyAllWindows()
time.sleep(3)

# Reading Video
result = cv2.VideoCapture("Output.mp4")

while result.isOpened():
    ret1,frame1 = result.read()

    if not ret1:
        print("Reached end of video")
        break

    # Saved Video Display
    cv2.imshow("Saved Video", frame1)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()