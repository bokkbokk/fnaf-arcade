my_sprite = sprites.create(assets.image("""
    myImage
"""), SpriteKind.player)
controller.move_sprite(None)
controller.move_sprite(my_sprite)
characterAnimations.loop_frames(my_Sprite, [], 500, 0)