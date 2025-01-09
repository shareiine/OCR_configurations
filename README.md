Testing of different OCR configurations using OpenCV and tesseract/EasyOCR <br>
Test both for image and real-time video feed

# Tesseract OCR Outputs
## Normal application of OCR with bounding boxes
![pytess_with_box](https://github.com/user-attachments/assets/38e81304-1b9a-4523-9df5-6806c8e97789)

## Application of OCR on a Video Feed (90% confidence level)
![pytess_vid](https://github.com/user-attachments/assets/ead5ea21-d2d1-4f89-bee6-07593e11ce69)

# EasyOCR Outputs
## Normal Application of OCR with bounding boxes
![easyocr](https://github.com/user-attachments/assets/f381aa26-b793-4a89-a108-1bbf5c1d2d8e)

## Application of OCR on a Video Feed (no set probability level; continuous reading)
![easyocr_video](https://github.com/user-attachments/assets/ab90f5ae-9bf8-48be-9c33-9ffbb747077d)


### Findings:
Both libraries can detect English and Tagalog. However, using image_to_data function in pytesseract enabled to "filter" those that did not reach a certain threshold.
On the other hand, EasyOCR can also be filtered depending on the probability set by the programmer. Still, it is noticed that it takes more time when processing image/video.

The use of CNN might provide a better output and increase confidence/probability levels.
