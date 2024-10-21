import cv2

print ("This program will eventually make a meme with text on top of the picture")

print ("Put your picture in the same folder as this program.")

#take keyboard input from the user to retrieve a picture from their computer
picture_file = input("Enter the name of your picture file, including the "
                     "extension, and then press 'enter': ")

#take the data from a picture and store in variable
picture = cv2.imread(picture_file)

#take keyboard input from the user and save into new variable
meme_text = input("Type your text and press enter. Stay under 23 characters. ")

#pick color for the text
color = input("Type a color you would like the text to be. white, red, blue, pink.")
if color == "white" :
    colornumber = (255,255,255)
    
if color == "red" :
        colornumber = (0,0,255)
        
if color == "blue" :
        colornumber = (255,0,1)
        
if color == "pink" :
        colornumber = (171,48,242)
    
#add text on the picture
cv2.putText(picture, meme_text, (100,100) ,
            cv2.FONT_HERSHEY_SIMPLEX, 2.6, (colornumber), 5)

#the user must make the picture window active first by clicking on it
print ("Click on the picture, then press the Escape key to quit the program")

#show the picture
cv2.imshow("Meme", picture)
#if user presses a key, record that key in new variable
keypressed = cv2.waitKey(0)

print (keypressed)

#if user presses escape key, close the window and end
while keypressed != 27:
    
    #if user presses r make text red
    if keypressed == ord('r'):
        #put new picture
        picture = cv2.imread(picture_file)
        #add text on top of the picture using text from users imput
        cv2.putText(picture, meme_text, (100,100), cv2.FONT_HERSHEY_SIMPLEX,
                    2.6, (0,0,255), 4)
        #show picture(needs waitkey)
        cv2.imshow("Meme", picture)
    
    #if user presses b make text blue
    elif keypressed == ord('b'):
        #put new picture
        picture = cv2.imread(picture_file)
        #add text on top of picture from users imput
        cv2.putText(picture, meme_text, (100,100), cv2.FONT_HERSHEY_SIMPLEX,
                    2.6, (255,0,1), 4)
        #show picture(needs waitkey)
        cv2.imshow("Meme", picture)
    
    #if user presses p make text pink
    elif keypressed == ord('p'):
        #put new picture
        picture = cv2.imread(picture_file)
        #add text on top of picture from users imput
        cv2.putText(picture, meme_text, (100,100), cv2.FONT_HERSHEY_SIMPLEX,
                    2.6, (171,48,242), 4)
        #show picture(needs waitkey)
        cv2.imshow("Meme", picture)
    
    #if user presses s save it in a new picture
    elif keypressed == ord('s'):
        #create new jpeg in the same folder as the program
        cv2.imwrite('meme_dog/cat1.jpeg',picture)
        
    #if user presses d change font    
    elif keypressed == ord('f'):
        #put new picture
        picture = cv2.imread(picture_file)
        #add text on picture
        cv2.putText(picture, meme_text, (100,100), cv2.FONT_HERSHEY_DUPLEX,
                    2.6, (colornumber), 4)
        #show picture(needs waitkey)
        cv2.imshow("Meme", picture)
        
    else:
        #if user presses any other key then esc then give print statement
        print ("Invalid input, please try again.")
    keypressed = cv2.waitKey(0)

cv2.destroyAllWindows()
    
#needed on mac to work destroyAllWindows
cv2.waitKey(1)
