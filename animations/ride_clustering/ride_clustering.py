import os
import re
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class CropSelector:
    def __init__(self, image_path):
        self.image_path = image_path
        self.crop_coords = None
        self.rect = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

    def select_crop(self):
        img = Image.open(self.image_path)
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.set_title("Click and drag to select crop area. Close window when done.")

        def on_press(event):
            self.start_x, self.start_y = event.xdata, event.ydata
            self.rect = Rectangle((self.start_x, self.start_y), 0, 0,
                                  edgecolor='red', facecolor='none', lw=2)
            ax.add_patch(self.rect)

        def on_drag(event):
            if self.rect and event.xdata and event.ydata:
                width = event.xdata - self.start_x
                height = event.ydata - self.start_y
                self.rect.set_width(width)
                self.rect.set_height(height)
                fig.canvas.draw_idle()

        def on_release(event):
            self.end_x, self.end_y = event.xdata, event.ydata
            plt.close(fig)

        fig.canvas.mpl_connect('button_press_event', on_press)
        fig.canvas.mpl_connect('motion_notify_event', on_drag)
        fig.canvas.mpl_connect('button_release_event', on_release)
        plt.show()

        if self.start_x and self.start_y and self.end_x and self.end_y:
            x_min = int(min(self.start_x, self.end_x))
            y_min = int(min(self.start_y, self.end_y))
            x_max = int(max(self.start_x, self.end_x))
            y_max = int(max(self.start_y, self.end_y))
            self.crop_coords = (x_min, y_min, x_max, y_max)

        return self.crop_coords

def crop_images_and_create_gif(folder_path, crop_box, output_path, interval):
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

    # Sort files numerically by padding the numbers in the filenames
    image_files.sort(key=lambda x: int(re.search(r'(\d+)', x).group().zfill(5)))  # Pad numbers for consistent sorting

    cropped_images = []

    for image_file in image_files:
        img_path = os.path.join(folder_path, image_file)
        img = Image.open(img_path)
        cropped_img = img.crop(crop_box)
        cropped_images.append(cropped_img)

    cropped_images[0].save(
        output_path,
        save_all=True,
        append_images=cropped_images[1:],
        loop=0,
        duration=interval
    )
    print(f"GIF created at {output_path}")

if __name__ == "__main__":
    # Hardcoded values
    folder_path = r"C:\Users\cyberwitch\Documents\portfolio\ALTR_PROJECT\animations\ride_clustering\img"  # Replace with your folder path
    output_path = r"C:\Users\cyberwitch\Documents\portfolio\ALTR_PROJECT\animations\ride_clustering\ride_clustering.gif"  # Replace with your output GIF path
    interval = 3000  # Interval in milliseconds between frames

    if os.path.isdir(folder_path):
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
        if not image_files:
            print("No valid image files found in the folder.")
        else:
            first_image_path = os.path.join(folder_path, image_files[0])
            cropper = CropSelector(first_image_path)
            crop_box = cropper.select_crop()
            if crop_box:
                crop_images_and_create_gif(folder_path, crop_box, output_path, interval)
            else:
                print("Cropping cancelled or invalid crop area.")
    else:
        print("Invalid folder path. Exiting.")
