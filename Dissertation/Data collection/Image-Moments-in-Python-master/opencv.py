import cv2

def planogram():
  im = cv2.imread(r'C:\Users\Michiel.VanderMerwe\Desktop\Image-Moments-in-Python-master\image\download.jpg',cv2.IMREAD_GRAYSCALE)
  # Threshold image
  _,im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)
  # Calculate Moments
  moments = cv2.moments(im)
  # Calculate Hu Moments
  planogram.huMoments = cv2.HuMoments(moments)


def realogram():
  im = cv2.imread(r'C:\Users\Michiel.VanderMerwe\Desktop\Image-Moments-in-Python-master\image\download  (1) .jpg',cv2.IMREAD_GRAYSCALE)
  # Threshold image
  _,im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)
  # Calculate Moments
  moments = cv2.moments(im)
  # Calculate Hu Moments
  realogram.huMoments2 = cv2.HuMoments(moments)


def diff():
  planogram()
  realogram()
  diffs =  planogram.huMoments -  realogram.huMoments2
  print(diffs)
