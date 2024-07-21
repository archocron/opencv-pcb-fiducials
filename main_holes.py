import cv2
from utils.image_utils import *

EXTERNAL_DIAMETER = 355 
INTERNAL_DIAMETER = 155
EXTERNAL_COLOR = 200
INTERNAL_COLOR = 240
MAX_MATCHS = 4
ANGLE_BETWEEN_MOST_SEPARATED_POINTS = 40
DISTANCE_TOP_LEFT_CORNER = (1500,241)
DISTANCE_BOTTOM_RIGHT_CORNER = (233,350)

image = cv2.imread('images/rpi_holes.jpg')

pattern = create_pattern(EXTERNAL_DIAMETER, INTERNAL_DIAMETER, EXTERNAL_COLOR,INTERNAL_COLOR)
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

match_img = cv2.matchTemplate(grey_image, pattern, cv2.TM_CCOEFF_NORMED)
found_points = find_points(match_img, MAX_MATCHS)

image, found_points_rotated= align_image(image,ANGLE_BETWEEN_MOST_SEPARATED_POINTS, found_points, EXTERNAL_DIAMETER)
paint_matched_points(image, found_points_rotated, EXTERNAL_DIAMETER)

image = paint_cutout_border(image, found_points_rotated, EXTERNAL_DIAMETER, DISTANCE_TOP_LEFT_CORNER, DISTANCE_BOTTOM_RIGHT_CORNER)
image = crop_image(image, found_points_rotated, EXTERNAL_DIAMETER, DISTANCE_TOP_LEFT_CORNER, DISTANCE_BOTTOM_RIGHT_CORNER)

cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
cv2.imshow('Result', image)

cv2.waitKey(0)
cv2.destroyAllWindows()