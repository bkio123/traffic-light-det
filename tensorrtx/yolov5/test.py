
import cv2
image_path_batch = ['01.jpg']

def get_raw_image(image_path_batch):
  """
  description: Read an image from image path
  """
  for img_path in image_path_batch:
      yield cv2.imread(img_path)

out = get_raw_image(image_path_batch)

rtn = next(out)

print(type(rtn), rtn.shape)
