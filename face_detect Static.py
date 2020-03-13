import cv2
def detect():
    img_path=input("enter image name")


# Create the haar cascade
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

# Read the image
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=6)

# Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    print("Found {0} faces!".format(len(faces)))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect()
