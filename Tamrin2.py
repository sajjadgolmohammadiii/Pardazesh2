import cv2
import numpy as np

def zoom_image(image_path, zoom_factor):
    # Load the image
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # Calculate the center of the image
    center_x, center_y = width // 2, height // 2

    # Calculate the new size
    new_width = int(width / zoom_factor)
    new_height = int(height / zoom_factor)

    # Define the cropping area
    x1 = max(center_x - new_width // 2, 0)
    y1 = max(center_y - new_height // 2, 0)
    x2 = min(center_x + new_width // 2, width)
    y2 = min(center_y + new_height // 2, height)

    # Crop the image
    cropped_image = image[y1:y2, x1:x2]

    # Resize the final image to the new size
    if zoom_factor > 1:
        final_image = cv2.resize(cropped_image, (512, 512), interpolation=cv2.INTER_LINEAR)
    else:
        # If the zoom is less than 1, zoom out the image to a larger size
        final_image = cv2.resize(cropped_image, (int(512 * zoom_factor), int(512 * zoom_factor)), interpolation=cv2.INTER_LINEAR)

    # Create a black background
    black_background = np.zeros((512, 512, 3), dtype=np.uint8)

    # Place the zoomed image in the center of the black background
    x_offset = (512 - final_image.shape[1]) // 2
    y_offset = (512 - final_image.shape[0]) // 2

    black_background[y_offset:y_offset + final_image.shape[0], x_offset:x_offset + final_image.shape[1]] = final_image

    cv2.imshow("Zoomed Image", black_background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_zoom_factor():
    while True:
            zoom_factor = float(input("Please enter the zoom factor: "))
            if zoom_factor <= 0:
                print("The zoom factor must be greater than zero.")
            else:
                return zoom_factor

# Get the zoom factor from the user
zoom_factor = get_zoom_factor()
zoom_image("image.jpg", zoom_factor)
