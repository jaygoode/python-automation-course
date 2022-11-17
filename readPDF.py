import camelot
import cv2

hackathoncert = camelot.read_pdf('hackathoncert.pdf')

print(hackathoncert, pages='1')
