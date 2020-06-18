

def draw_demo():
    from PIL import Image, ImageDraw

    width = 500
    height = 500

    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)


    
    half_width = width / 2
    third_width_left = width / 3
    third_width_right = (width/3)*2
    quarter_width_left = width / 4
    quarter_width_right = (width/4)*3
    half_height = height / 2
    top_third_height = height / 3
    bottom_third_height = (height/3)*2
    arm_start_height = (top_third_height+bottom_third_height)/2

    # draw head
    draw.ellipse((third_width_left, 0, third_width_right, top_third_height), fill=250)

    # draw body
    draw.line([(half_width, top_third_height), (half_width, bottom_third_height)])

    # draw right arm
    draw.line([(half_width, arm_start_height), (third_width_right, top_third_height)])

    # draw left arm
    draw.line([(half_width, arm_start_height),(third_width_left, top_third_height)])

    # draw right leg
    draw.line([(half_width, bottom_third_height),(quarter_width_right, height)])

    # draw left leg
    draw.line([(half_width, bottom_third_height),(quarter_width_left, height)])

    img.show()

draw_demo()