# Written by Kyle Fricke & Vincent O'Sullivan, Engineer Your World
# Created in 2017, last updated in January 2020 (for Python 3)
# Use trackbars to filter the original video for a single color. 
# Display the original video and the filtered videos.
# Trackbars allow adjustment of the filters as the filtered videos display.
# Close windows when the Escape key is pressed.
# You will need to add code for the other 3 colors.

# Import OpenCV library for image processing, NumPy for digital image arrays.
import cv2
import numpy

# Create an object from the VideoCapture class that will capture images and
# video from the external webcam.
cap = cv2.VideoCapture(0)

# Create windows in which to display images and track bars.
cv2.namedWindow("Original")
cv2.namedWindow("Filtered C1")
# NOTE - For this part, I'll give you the code for C2.
# cv2.namedWindow("Filtered C2")
# NOTE - Get C2 to work first, then add code for C3/C4


cv2.namedWindow("Combined") 
cv2.namedWindow("C1 Controls")
# NOTE - Here's the code for C2, what's needed for C3 and C4?
# cv2.namedWindow("C2 Controls")


# Resize trackbar windows if trackbars do not display correctly.
cv2.resizeWindow("C1 Controls", 300, 300)
# NOTE - From now on, adding the code for C2, C3, and C4 is up to you


# Create trackbars to adjust the color min and max values.
cv2.createTrackbar("C1 Blu Min", "C1 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C1 Blu Max", "C1 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C1 Grn Min", "C1 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C1 Grn Max", "C1 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C1 Red Min", "C1 Controls", 0, 255, lambda x:None)
cv2.createTrackbar("C1 Red Max", "C1 Controls", 0, 255, lambda x:None)



# Initialize while loop control variable.
key_pressed = 1

# In a loop, use trackbars to adjust the filter.
# Loop ends once the Escape key is pressed.
while key_pressed != 27:

    # Capture one frame (image) of video, save the data in two variables.
    # The second variable, frame, contains the image data.
    ret, frame = cap.read()
    # NOTE - The commented line of code below "flips" the video,
    #        use it if your left and right side are flipped
    # frame = cv2.flip(frame, 1)

    # Create and update a variable with the current position of the trackbar. 
    C1b_min = cv2.getTrackbarPos("C1 Blu Min", "C1 Controls") 
    C1b_max = cv2.getTrackbarPos("C1 Blu Max", "C1 Controls")
    C1g_min = cv2.getTrackbarPos("C1 Grn Min", "C1 Controls") 
    C1g_max = cv2.getTrackbarPos("C1 Grn Max", "C1 Controls")
    C1r_min = cv2.getTrackbarPos("C1 Red Min", "C1 Controls") 
    C1r_max = cv2.getTrackbarPos("C1 Red Max", "C1 Controls")
    

    # Create variable with a list of filter boundaries.
    lower_C1 = [C1b_min, C1g_min, C1r_min]
    upper_C1 = [C1b_max, C1g_max, C1r_max]
    
    
    # Assign the proper data type to each of these new lists (arrays).
    lower_C1 = numpy.array(lower_C1, dtype = "uint8")
    upper_C1 = numpy.array(upper_C1, dtype = "uint8")
    

    # Create the masks to identify the colored regions.
    C1_mask = cv2.inRange(frame, lower_C1, upper_C1)
    

    # Apply the mask to create the filtered image.
    filtered_C1 = cv2.bitwise_or(frame, frame, mask = C1_mask)
    

    # Combine the filtered images to see the "big picture".
    # NOTE - Uncomment these lines as you do the code for each color
    # combined = cv2.bitwise_or(filtered_C1, filtered_C2)
    # combined = cv2.bitwise_or(combined, filtered_C3)
    # combined = cv2.bitwise_or(combined, filtered_C4)

    # Display the image data in the windows. Must be followed by waitKey().
    cv2.imshow("Original", frame)
    cv2.imshow("Filtered C1", filtered_C1)
    
    
    # NOTE - Uncomment this once you think your C2 filter works
    # Show each color filter combined together in one video
    # cv2.imshow("Combined", combined)
    
    # Wait 40 milliseconds for a key to be pressed.
    # You might increase/decrease this number for performance
    key_pressed = cv2.waitKey(40)
                
# Close the image file and close all windows.
cap.release()
cv2.destroyAllWindows()


