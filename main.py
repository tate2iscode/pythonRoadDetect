from ProcessingImage import *

def onChange(pos):
    pass

def main():

    src = cv2.imread("datas/highway.jpeg")

    print(src.shape)
    cv2.namedWindow("Trackbar Windows")
    cv2.createTrackbar("threshold", "Trackbar Windows", 0, 255, onChange)
    cv2.createTrackbar("maxValue", "Trackbar Windows", 0, 255, lambda x: x)

    cv2.setTrackbarPos("threshold", "Trackbar Windows", 127)
    cv2.setTrackbarPos("maxValue", "Trackbar Windows", 255)


    while True:
        #p_src = src[240:480, 0:640].copy()
        #cv2.imshow("a",p_src)
        #threshold = cv2.getTrackbarPos("threshold", "Trackbar Windows") #threshold = 125
        #maxValue = cv2.getTrackbarPos("maxValue", "Trackbar Windows")

        #print(threshold)
        img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

        img = cv2.GaussianBlur(img, (5, 5), 0)
        cv2.imshow("test", perspectiveTransform(img))
        #BEVDProcess(perspectiveTransform(img))
        _, img = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        high = img.shape[0]
        high = int(round(high/2))
        img = process(img)
        #img = perspectiveTransform(img)
        #img = cv2.rectangle(img, (0, 0), (img.shape[1], high), (0, 0, 0), -1)
        #proc = img[240:480, 0:640].copy()
        #print(proc.shape)
        contours, h = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
        #result = cv2.drawContours(p_src, contours, -1, (0, 255, 0), 3)
        #print(contours[0])

        #print(len(contours))

        cv2.imshow("Trackbar Windows", img)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    #plt.plot(histographic)
    #plt.show()




if __name__ == "__main__":
    main()