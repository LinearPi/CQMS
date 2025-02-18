import cv2

# RTSP流的URL
rtsp_url = "rtsp://admin:Admin1234@10.199.136.1:554/stream/live?channel=1&type=0"
# rtsp_url = 0

# 创建一个VideoCapture对象
cap = cv2.VideoCapture(rtsp_url)

# 检查是否成功打开视频流
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# 循环读取视频流中的帧
while True:
    # 读取一帧
    ret, frame = cap.read()

    # 如果正确读取帧，ret为True
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break

    # 显示帧
    cv2.imshow('RTSP Stream', frame)

    # 按'q'退出循环
    if cv2.waitKey(1) == ord('q'):
        break

# 释放VideoCapture对象
cap.release()
# 关闭所有OpenCV窗口
cv2.destroyAllWindows()