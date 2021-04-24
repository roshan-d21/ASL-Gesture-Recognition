import numpy as np
import cv2
from fastai.vision import *

# defaults.device = torch.device('cpu')
learn = load_learner(Path('./model/v4'))

cap = cv2.VideoCapture(0)
s = ' '
i = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # ret, frame = cv2.flip(frame, 1)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('z'):
        s = ' '

    if i % 50 == 0:
        t = torch.tensor(np.ascontiguousarray(np.flip(frame[50:400, 230:450], 2)).transpose(2,0,1)).float()/255
        # t = torch.tensor(np.ascontiguousarray(np.flip(frame, 2)).transpose(2,0,1)).float()/255
        # print(t, t.shape)

        img = Image(t) # fastai.vision.Image, not PIL.Image
        # img.show()

        pred, pred_idx, _ = learn.predict(img)
        print(pred)
        s1 = str(pred)

        if s1 == 'nothing':
            pass
        elif s1 == 'space':
            if s[-1] != ' ':
                s += ' '
        elif s1 == 'del':
            s = s[:-1]
        else:
            s += s1
            # s += s1 if st1 != s[-1] else ''
    i += 1

    frame = cv2.flip(frame, 1)
    frame = cv2.rectangle(frame, (200, 50), (500, 400), (80, 80, 80), 1)
    frame = cv2.putText(frame, s, (25, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('frame', frame)

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
