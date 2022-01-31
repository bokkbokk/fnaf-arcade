my_sprite = sprites.create(assets.image("""
    myImage
"""), SpriteKind.player)
controller.move_sprite(my_sprite)

def on_forever():
    pass
forever(on_forever)
