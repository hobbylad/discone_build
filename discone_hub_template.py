from PIL import Image, ImageDraw
import math

dpcm = 150

def pos_to_pix(pos, offset = (0, 0)):
    return (int(round((pos[0] + offset[0]) * dpcm)), int(round((pos[1] + offset[1]) * dpcm)))

def draw_drill_hole(imd, pos, r, drill_mark = True):
    imd.ellipse(pos_to_pix(pos, (-r, -r)) + pos_to_pix(pos, (r, r)), outline = 0)
    if drill_mark:
        imd.line(pos_to_pix(pos, (-1.3 * r, 0)) + pos_to_pix(pos, (1.3 * r, 0)), fill = 0)
        imd.line(pos_to_pix(pos, (0, -1.3 * r)) + pos_to_pix(pos, (0, 1.3 * r)), fill = 0)
    del imd

if __name__ == '__main__':
    washer_r_cm = 2.5 / 2
    washer_hole_r_cm = 0.5 / 2
    radial_hole_r_cm = 0.25 / 2
    number_of_radials = 8

    centre = washer_r_cm;
    im = Image.new("RGB", pos_to_pix((2 * centre, 2 * centre)), (255, 255, 255))
    imd = ImageDraw.Draw(im)

    draw_drill_hole(imd, (centre, centre), washer_r_cm, False)
    draw_drill_hole(imd, (centre, centre), washer_hole_r_cm)

    for i in range(0, number_of_radials):
        angle = 2 * i * math.pi / number_of_radials
        draw_drill_hole(imd, (centre + 0.9 * math.cos(angle), centre + 0.9 * math.sin(angle)), radial_hole_r_cm)

    for i in range(0, number_of_radials):
        angle = 2 * i * math.pi / number_of_radials
        draw_drill_hole(imd, (centre + 0.9 * math.cos(angle), centre + 0.9 * math.sin(angle)), radial_hole_r_cm)

    im.show()

