import cv2

def sojyak():
    img = cv2.imread('slicing.png')
    if img.shape[1] > img.shape[0]:
        overlay = cv2.cvtColor(cv2.imread('soyjak.png'), cv2.COLOR_RGB2RGBA)
    else:
        overlay = cv2.cvtColor(cv2.imread('soyjak_vertical.png'), cv2.COLOR_RGB2RGBA)
    background = cv2.resize(cv2.cvtColor(img, cv2.COLOR_RGB2RGBA), tuple(reversed(overlay.shape[:2])), interpolation = cv2.INTER_AREA)

    mask = overlay[:, :, 0] != 0
    background[mask] = overlay[mask]

    cv2.imwrite('combined.png', background)
