import cv2

print "Put your picture in the same folder as this program."

picture_file = input("Enter the name of your picture file, including the "
                                 "extension, and then press 'enter': ")
# Read picture_file
picture = cv2.imread(picture)

meme_text = input("Type your text and press enter. Stay under 23 characters. ")
print("Click on the picture. Press t to add your text to the top, or m to "
      "add it to the middle, or Escape to quit.")

cv2.imshow("My Meme", picture)

keypressed = cv2.waitKey(0)

# loop until user presses escape
while keypressed != 27:
    if keypressed == ord('t'):
        print("T Pressed!")
        cv2.putText(picture, meme_text, (20, 0), cv2.FONT_HERSHEY_SIMPLEX,
                1.8, (0,0,255), 4)
        
    elif keypressed == ord('m'):
        print("M Pressed!")
        cv2.putText(picture, meme_text, (20, 200), cv2.FONT_HERSHEY_SIMPLEX,
                1.8, (0,0,255), 4)
        
    elif keypressed == ord('s'):
        cv2.imwrite("new_meme.jpg", picture);
    else:
        print ("Invalid input, please try again.")
    keypressed = cv2.waitkey(0)
    
# These functions close the image window
cv2.destroyAllWindows()
cv2.waitKey(1) 

