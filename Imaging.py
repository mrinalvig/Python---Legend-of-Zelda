from pygame_functions import *
import random

screen = pygame.display.set_mode((800, 600))
enemy_list = pygame.sprite.Group()
platform_list = pygame.sprite.Group()

screenSize(1000, 750)
setBackgroundImage(["mapping.png", "mapping2.png"])
sprite = makeSprite("link.gif", 32)
enemy = makeSprite("link.gif", 32)

# Collision sprites
collision = makeSprite("blank.png")
collision2 = makeSprite("blank.png")
collision3 = makeSprite("blank2.png")
collision4 = makeSprite("cube.png")
collision5 = makeSprite("blank3.png")
collision6 = makeSprite("blank3.png")
collision7 = makeSprite("cube.png")
collision8 = makeSprite("blank4.png")
collision9 = makeSprite("cube.png")
collision10 = makeSprite("cube.png")
collision11 = makeSprite("cube.png")
collision12 = makeSprite("blank5.png")
collision13 = makeSprite("blank4.png")
collision14 = makeSprite("blank2.png")
collision15 = makeSprite("blank5.png")
collision16 = makeSprite("water.png")


xPos = 0
yPos = 180
xPos2 = 1920
yPos2 = 180
xPos3 = 1170
yPos3 = 120
xPos4 = 617
yPos4 = 165
xPos5 = 450
yPos5 = 75
xPos6 = 354
yPos6 = 75
xPos7 = 185
yPos7 = 165
xPos8 = 180
yPos8 = 120
xPos9 = 988
yPos9 = 165
xPos10 = 1360
yPos10 = 165
xPos11 = 1734
yPos11 = 165
xPos12 = 0
yPos12 = 905
xPos13 = 187
yPos13 = 1060
xPos14 = 1170
yPos14 = 1060
xPos15 = 1920
yPos15 = 905
xPos16 = -947
yPos16 = 450

# Putting Sprite in proper place
moveSprite(sprite, 500, 375, True)
moveSprite(collision2, xPos2, yPos2, True)
moveSprite(collision3, xPos3, yPos3, True)
moveSprite(collision4, xPos4, yPos4, True)
moveSprite(collision5, xPos5, yPos5, True)
moveSprite(collision6, xPos6, yPos6, True)
moveSprite(collision7, xPos7, yPos7, True)
moveSprite(collision8, xPos8, yPos8, True)
moveSprite(collision9, xPos9, yPos9, True)
moveSprite(collision10, xPos10, yPos10, True)
moveSprite(collision11, xPos11, yPos11, True)
moveSprite(collision12, xPos12, yPos12, True)
moveSprite(collision13, xPos13, yPos13, True)
moveSprite(collision14, xPos14, yPos14, True)
moveSprite(collision15, xPos15, yPos15, True)
moveSprite(collision16, xPos16, yPos16, True)
showSprite(sprite)
showSprite([collision, collision2, collision3, collision4, collision5, collision6, collision7, collision8])
showSprite([collision9, collision10, collision11, collision12, collision13, collision14, collision15, collision16])


moveSprite(sprite, 500, 375, True)
showSprite(enemy)
showSprite(sprite)

nextFrame = clock()
frame = 0

while True:
    y = random.randint(1, 1001)
    z = random.randint(1, 1001)

    a = random.randint(1, 5)
    if a == 1:
        y -= 1
        z -= 1
    if a == 2:
        y += 1
        z += 1
    if a == 3:
        y -= 1
        z += 1
    if a == 4:
        y += 1
        z -= 1
    # moveSprite(enemy, y, z, True)

    if clock() > nextFrame:  # We only animate our character every 80ms.
        frame = (frame + 1) % 8  # There are 8 frames of animation in each direction
        nextFrame += 80  # so the modulus 8 allows it to loop

    if keyPressed("right") or keyPressed("d"):

        if touching(sprite, collision) or touching(sprite, collision2) or touching(sprite, collision3)\
                or touching(sprite, collision4) or touching(sprite, collision5) or touching(sprite, collision6)\
                or touching(sprite, collision7) or touching(sprite, collision8) or touching(sprite, collision9)\
                or touching(sprite, collision10) or touching(sprite, collision11)or touching(sprite, collision12)\
                or touching(sprite, collision13) or touching(sprite, collision14) or touching(sprite, collision15)\
                or touching(sprite, collision16):
            x = 1
            while x == 1:
                scrollBackground(0, 0)
                if keyPressed("left") or keyPressed("a"):
                    x = 2

        changeSpriteImage(sprite, 0 * 8 + frame)  # 0*8 because right animations are the 0th set in the sprite sheet
        scrollBackground(-3, 0)
        xPos -= 5
        xPos2 -= 5
        xPos3 -= 5
        xPos4 -= 5
        xPos5 -= 5
        xPos6 -= 5
        xPos7 -= 5
        xPos8 -= 5
        xPos9 -= 5
        xPos10 -= 5
        xPos11 -= 5
        xPos12 -= 5
        xPos13 -= 5
        xPos14 -= 5
        xPos15 -= 5
        xPos16 -= 5

        moveSprite(collision, xPos, yPos, True)
        moveSprite(collision2, xPos2, yPos2, True)
        moveSprite(collision3, xPos3, yPos3, True)
        moveSprite(collision4, xPos4, yPos4, True)
        moveSprite(collision5, xPos5, yPos5, True)
        moveSprite(collision6, xPos6, yPos6, True)
        moveSprite(collision7, xPos7, yPos7, True)
        moveSprite(collision8, xPos8, yPos8, True)
        moveSprite(collision9, xPos9, yPos9, True)
        moveSprite(collision10, xPos10, yPos10, True)
        moveSprite(collision11, xPos11, yPos11, True)
        moveSprite(collision12, xPos12, yPos12, True)
        moveSprite(collision13, xPos13, yPos13, True)
        moveSprite(collision14, xPos14, yPos14, True)
        moveSprite(collision15, xPos15, yPos15, True)
        moveSprite(collision16, xPos16, yPos16, True)

    elif keyPressed("down") or keyPressed("s"):

        if touching(sprite, collision) or touching(sprite, collision2) or touching(sprite, collision3) \
                or touching(sprite, collision4) or touching(sprite, collision5) or touching(sprite, collision6) \
                or touching(sprite, collision7) or touching(sprite, collision8) or touching(sprite, collision9) \
                or touching(sprite, collision10) or touching(sprite, collision11) or touching(sprite, collision12) \
                or touching(sprite, collision13) or touching(sprite, collision14) or touching(sprite, collision15)\
                or touching(sprite, collision16):
            x = 1
            while x == 1:
                scrollBackground(0, 0)
                if keyPressed("up") or keyPressed("w"):
                    x = 2

        changeSpriteImage(sprite, 1 * 8 + frame)  # down facing animations are the 1st set
        scrollBackground(0, -3)
        yPos -= 5
        yPos2 -= 5
        yPos3 -= 5
        yPos4 -= 5
        yPos5 -= 5
        yPos6 -= 5
        yPos7 -= 5
        yPos8 -= 5
        yPos9 -= 5
        yPos10 -= 5
        yPos11 -= 5
        yPos12 -= 5
        yPos13 -= 5
        yPos14 -= 5
        yPos15 -= 5
        yPos16 -= 5

        moveSprite(collision, xPos, yPos, True)
        moveSprite(collision2, xPos2, yPos2, True)
        moveSprite(collision3, xPos3, yPos3, True)
        moveSprite(collision4, xPos4, yPos4, True)
        moveSprite(collision5, xPos5, yPos5, True)
        moveSprite(collision5, xPos5, yPos5, True)
        moveSprite(collision6, xPos6, yPos6, True)
        moveSprite(collision7, xPos7, yPos7, True)
        moveSprite(collision8, xPos8, yPos8, True)
        moveSprite(collision9, xPos9, yPos9, True)
        moveSprite(collision10, xPos10, yPos10, True)
        moveSprite(collision11, xPos11, yPos11, True)
        moveSprite(collision12, xPos12, yPos12, True)
        moveSprite(collision13, xPos13, yPos13, True)
        moveSprite(collision14, xPos14, yPos14, True)
        moveSprite(collision15, xPos15, yPos15, True)
        moveSprite(collision16, xPos16, yPos16, True)

    elif keyPressed("left") or keyPressed("a"):

        if touching(sprite, collision) or touching(sprite, collision2) or touching(sprite, collision3) \
                or touching(sprite, collision4) or touching(sprite, collision5) or touching(sprite, collision6) \
                or touching(sprite, collision7) or touching(sprite, collision8) or touching(sprite, collision9) \
                or touching(sprite, collision10) or touching(sprite, collision11) or touching(sprite, collision12) \
                or touching(sprite, collision13) or touching(sprite, collision14) or touching(sprite, collision15)\
                or touching(sprite, collision16):
            x = 1
            while x == 1:
                scrollBackground(0, 0)
                if keyPressed("right") or keyPressed("d"):
                    x = 2

        changeSpriteImage(sprite, 2 * 8 + frame)  # and so on
        scrollBackground(3, 0)
        xPos += 5
        xPos2 += 5
        xPos3 += 5
        xPos4 += 5
        xPos5 += 5
        xPos6 += 5
        xPos7 += 5
        xPos8 += 5
        xPos9 += 5
        xPos10 += 5
        xPos11 += 5
        xPos12 += 5
        xPos13 += 5
        xPos14 += 5
        xPos15 += 5
        xPos16 += 5

        moveSprite(collision, xPos, yPos, True)
        moveSprite(collision2, xPos2, yPos2, True)
        moveSprite(collision3, xPos3, yPos3, True)
        moveSprite(collision4, xPos4, yPos4, True)
        moveSprite(collision5, xPos5, yPos5, True)
        moveSprite(collision5, xPos5, yPos5, True)
        moveSprite(collision6, xPos6, yPos6, True)
        moveSprite(collision7, xPos7, yPos7, True)
        moveSprite(collision8, xPos8, yPos8, True)
        moveSprite(collision9, xPos9, yPos9, True)
        moveSprite(collision10, xPos10, yPos10, True)
        moveSprite(collision11, xPos11, yPos11, True)
        moveSprite(collision12, xPos12, yPos12, True)
        moveSprite(collision13, xPos13, yPos13, True)
        moveSprite(collision14, xPos14, yPos14, True)
        moveSprite(collision15, xPos15, yPos15, True)
        moveSprite(collision16, xPos16, yPos16, True)

    elif keyPressed("up") or keyPressed("w"):

        if touching(sprite, collision) or touching(sprite, collision2) or touching(sprite, collision3) \
                or touching(sprite, collision4) or touching(sprite, collision5) or touching(sprite, collision6) \
                or touching(sprite, collision7) or touching(sprite, collision8) or touching(sprite, collision9) \
                or touching(sprite, collision10) or touching(sprite, collision11) or touching(sprite, collision12) \
                or touching(sprite, collision13) or touching(sprite, collision14) or touching(sprite, collision15)\
                or touching(sprite, collision16):
            x = 1
            while x == 1:
                scrollBackground(0, 0)
                if keyPressed("down") or keyPressed("s"):
                    x = 2

        changeSpriteImage(sprite, 3 * 8 + frame)
        scrollBackground(0, 3)
        yPos += 5
        yPos2 += 5
        yPos3 += 5
        yPos4 += 5
        yPos5 += 5
        yPos6 += 5
        yPos7 += 5
        yPos8 += 5
        yPos9 += 5
        yPos10 += 5
        yPos11 += 5
        yPos12 += 5
        yPos13 += 5
        yPos14 += 5
        yPos15 += 5
        yPos16 += 5

        moveSprite(collision, xPos, yPos, True)
        moveSprite(collision2, xPos2, yPos2, True)
        moveSprite(collision3, xPos3, yPos3, True)
        moveSprite(collision4, xPos4, yPos4, True)
        moveSprite(collision5, xPos5, yPos5, True)
        moveSprite(collision5, xPos5, yPos5, True)
        moveSprite(collision6, xPos6, yPos6, True)
        moveSprite(collision7, xPos7, yPos7, True)
        moveSprite(collision8, xPos8, yPos8, True)
        moveSprite(collision9, xPos9, yPos9, True)
        moveSprite(collision10, xPos10, yPos10, True)
        moveSprite(collision11, xPos11, yPos11, True)
        moveSprite(collision12, xPos12, yPos12, True)
        moveSprite(collision13, xPos13, yPos13, True)
        moveSprite(collision14, xPos14, yPos14, True)
        moveSprite(collision15, xPos15, yPos15, True)
        moveSprite(collision16, xPos16, yPos16, True)

    else:
        changeSpriteImage(sprite, 1 * 8 + 5)  # the static facing front look

    tick(120)

endWait()
