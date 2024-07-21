# opencv-pcb-fiducials
Python project using OpenCV to detect fiducials and rotate to the correct angle and crop. To be applicated in combination with visual inspection projects.

# how to use it ?

First config all constants to adapt to your use case. Can be used with fiducials marks and also any kind of pattern like holes. Foe instance in this use case 

EXTERNAL_DIAMETER = 160<br>
INTERNAL_DIAMETER = 88<br>
EXTERNAL_COLOR = 100<br>
INTERNAL_COLOR = 240<br>
MAX_MATCHS = 3<br>
ANGLE_BETWEEN_MOST_SEPARATED_POINTS = 42.95<br>
DISTANCE_TOP_LEFT_CORNER = (1260,490)<br>
DISTANCE_BOTTOM_RIGHT_CORNER = (970,318)<br>

![alt text](https://github.com/archocron/opencv-pcb-fiducials/blob/main/images/rpi_parameters.jpg?raw=true)

Introducing an image like this ...

![alt text](https://github.com/archocron/opencv-pcb-fiducials/blob/main/images/rpi_raw.jpg?raw=true)

You can get through all steps, the rotated and cropped image, this is valid to perform after this transformation a visual inspection for example.

![alt text](https://github.com/archocron/opencv-pcb-fiducials/blob/main/images/rpi_result.jpg?raw=true)

## Image Attribution

The image used in this project, "Raspberry Pi B+ bottom.jpg", is a work by Lucasbosch and is licensed under the Creative Commons Attribution-Share Alike 3.0 Unported license.

### Image Details
- **Description**: Bottom face of the Raspberry Pi model B+
- **Date**: July 24, 2014
- **Author**: [Lucasbosch](https://commons.wikimedia.org/wiki/User:Lucasbosch)
- **Source**: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Raspberry_Pi_B%2B_bottom.jpg)
- **License**: [Creative Commons Attribution-Share Alike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/)
