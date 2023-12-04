## Protagonist Sprites

## Alban Sprites
image alban_default = "sprites/alban/default.png"
image alban_smile = "sprites/alban/smile.png"
image alban_concerned = "sprites/alban/concerned.png"
image alban_serious = "sprites/alban/serious.png"
image alban_upset = "sprites/alban/upset.png"
image alban_messed_up = "sprites/alban/messed_up.png"

## Fulgur Sprites
image fulgur_default = "sprites/fulgur/default.png"
image fulgur_smile = "sprites/fulgur/smile.png"
image fulgur_concerned = "sprites/fulgur/concerned.png"
image fulgur_serious = "sprites/fulgur/serious.png"
image fulgur_upset = "sprites/fulgur/upset.png"
image fulgur_corrupted = "sprites/fulgur/corrupted.png"

## Sonny Sprites
image sonny_default = "sprites/sonny/default.png"
image sonny_smile = "sprites/sonny/smile.png"
image sonny_concerned = "sprites/sonny/concerned.png"
image sonny_serious = "sprites/sonny/serious.png"
image sonny_upset = "sprites/sonny/upset.png"
image sonny_corrupted = "sprites/sonny/corrupted.png"

## Uki Sprites
default uki_hair_index = 0
default uki_eyewear_index = 0
default uki_top_index = 0
default uki_outerwear_index = 0
default uki_bottom_index = 0
default uki_shoes_index = 0
default uki_expression = "default"

image uki_hair = "sprites/uki/hair[uki_hair_index].png"
image uki_eyewear = "sprites/uki/eyewear[uki_eyewear_index].png"
image uki_top = "sprites/uki/top[uki_top_index].png"
image uki_outerwear = "sprites/uki/outerwear[uki_outerwear_index].png"
image uki_bottom = "sprites/uki/bottom[uki_bottom_index].png"
image uki_shoes = "sprites/uki/shoes[uki_shoes_index].png"
image uki_face = "sprites/uki/[uki_expression].png"

# Placeholder sprite size and component position
define sprite_size = (276, 1080)
define placeholder_pos = (0, 0)

image uki_sprite = Composite(
    sprite_size,
    placeholder_pos, "uki_shoes",
    placeholder_pos, "uki_bottom",
    placeholder_pos, "uki_top",
    placeholder_pos, "uki_outerwear",
    placeholder_pos, "uki_face",
    placeholder_pos, "uki_eyewear",
    placeholder_pos, "uki_hair",
)

label show_uki_sprite(expression):
    $ uki_expression = expression
    show uki_sprite

## Mascot/Animal Sprites

## Enemy Sprites
