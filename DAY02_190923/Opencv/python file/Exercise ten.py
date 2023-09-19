import cv2

# Load the video
video_path = 'test.mp4'
video = cv2.VideoCapture(video_path)

# Load the logo image with transparency (PNG format is recommended)
logo_path = 'logoh.png'
logo = cv2.imread(logo_path)

rows, cols, channels = logo.shape

# Create a VideoWriter object to save the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for output video
output_path = 'output_video_with_logo.mp4'
output_video = cv2.VideoWriter(output_path, fourcc, 30, (int(video.get(3)), int(video.get(4))))

# Process each frame in the input video
while True:
    ret, frame = video.read()
    if not ret:
        break

    # Extract the region of interest for the logo
    logoArea = frame[0:rows, 0:cols]

    # Create a mask for the logo
    img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # Apply the mask to the logo and the frame
    forground_with_mask = cv2.bitwise_and(logo, logo, mask=mask)
    backgrond_with_mask = cv2.bitwise_and(logoArea, logoArea, mask=mask_inv)
    final_img = cv2.add(forground_with_mask, backgrond_with_mask)
    frame[0:rows, 0:cols] = final_img

    # Write the frame to the output video
    output_video.write(frame)

    cv2.imshow("Logo in Video", frame)
    
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video objects
video.release()
output_video.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

# Display a message when the process is complete
print("Video with logo added saved as", output_path)
