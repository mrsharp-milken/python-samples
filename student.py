import random
import cv2

thememenum = (random.choice([1,2,3,4,5,6,7,8]))

if thememenum == 1 :
   picture_file = "cat.jpeg"
elif thememenum == 2 :
   picture_file = "trump.jpeg"
elif thememenum == 3 :
   picture_file = "biden.jpg"
elif thememenum == 4 :
   picture_file = "mrsharp.jpeg"
elif thememenum == 5:
   picture_file = "mrsharp2.jpeg"
elif thememenum == 6:
   picture_file = "mrsharp3.jpeg"
elif thememenum == 7:
   picture_file = "mrsharp4.jpeg"
elif thememenum == 8:
   picture_file = "mrsharp5.jpg"

picture_file = "cat.jpeg"


print("This program makes absolutley amazing memes")
print("The following are your instructions:")
print("1. You well get asigned a meme")
print("2. Once you have your meme and you look at it come back to this window")
print("3. Follow the instructions")




gowait = input("Write go to begin: ")




while gowait != "go" :
   dont = 1
   #cv2.destroyAllWindows()
   #cv2.waitkey(1)


#print("Put your picture in the same folder as this program")


#picture_file = input("Enter the name of your picture file, including the "+"extension, and then press 'enter': ")
#Rememebrs what the image is using the variable picture


#fontthickness = input("Enter the number of fontthickness you would like between 1-10")
picture = cv2.imread(picture_file)




cv2.imshow("YOUR MEME",picture)
keypressed = cv2.waitKey(10)
cv2.destroyAllWindows()


#Color=input("What color would you like, Red, Green, or Blue")


#if color=="red"
#Red=100,0,0
Textoverpicture = input("What shoud the meme say: ")
color = input("pick a color, red, green, or blue: ")
if color == ("red") :
   newcolor = (0, 0, 255)
if color == ("blue") :
   newcolor = (255, 0, 0)
if color == ("green"):
   newcolor = (0, 255, 0)


print("Press the spcae key if you would like to change the color to black")
print("Press the escape key to quit")
cv2.putText(picture, Textoverpicture, (100,100),
   cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.8, newcolor, 4)
# Shows image with title "Meme"
cv2.imshow("YOUR MEME",picture)
keypressed = cv2.waitKey(0)


#all this happens when escape is not pressed, can change color to black
while keypressed != 27:
   if keypressed == ord(' '):
       newcolor = (0, 0, 0)
       cv2.putText(picture, Textoverpicture, (100, 100),
                   cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.8, newcolor, 4)
       cv2.imshow("meme", picture)
   elif keypressed == ord('s') :
       cv2.imwrite('new_meme.jpg',picture)
   else:
       print("Invalid input")
   keypressed = cv2.waitKey(0)


cv2.destroyAllWindows()
cv2.waitkey(1)
