# Camera로 부터 영상 재생
import cv2

# cap 이 정상적으로 open이 되었는지 확인하기 위해서 cap.isOpen() 으로 확인가능
cap = cv2.VideoCapture(0)
print(cap.isOpened())

# cap.get(prodId)/cap.set(propId, value)을 통해서 속성 변경이 가능.
# 3은 width, 4는 heigh

print ('width: {0}, height: {1}'.format(cap.get(3),cap.get(4)))

#cap.set(3,320)
#cap.set(4,240)

while(True):
    # ret : frame capture결과(boolean)
    # frame : Capture한 frame
    ret, frame = cap.read()

    if(ret):
        # image를 Grayscale로 Convert함.
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(frame, 0)

        cv2.imshow('frame', gray)
        # waitKey(1) : 1ms
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

