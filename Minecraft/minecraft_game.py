from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
grass = load_texture('texture\grass_block')
stone = load_texture('texture\stone_block.png')
brick = load_texture('brick_block.png')
dirt = load_texture('texture\dirt_block.png')
block_pick = 1
sky = load_texture('texture\skybox.png')
arm = load_texture('arm_texture.png')
punch_sound = Audio('texture\punch_sound.wav', loop = False, autoplay= False)
hud_1 = load_texture('brick_block.png')
window.exit_button.visible = False
h = hud_1


def update():
    global block_pick, h


    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
        
    if held_keys['1']:
        block_pick = 1
        h = Entity(parent = camera.ui, model = 'quad', texture = hud_1,scale = 0.5, position= (0,-0.4,1))
    if held_keys['2']:
        block_pick = 2
        h.visible = False
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4

    if held_keys['esc']: exit()

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass):
        super().__init__(
            parent = scene,
            position = position,
            model = 'block',
            origin_y = 0.5,
            texture = texture,
            color = color.white,
            highlight_color = color.lime,
            scale = 0.5 # mouse != block
        )

    def input(self, key):
        
        if self.hovered:
            if key == 'escape':
                quit()
                
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position= self.position + mouse.normal, texture= grass)
                if block_pick == 2: voxel = Voxel(position= self.position + mouse.normal, texture= stone)
                if block_pick == 3: voxel = Voxel(position= self.position + mouse.normal, texture= brick)
                if block_pick == 4: voxel = Voxel(position= self.position + mouse.normal, texture= dirt)

            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)
            
            

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky,
            scale = 150,
            double_sided = True)

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'texture/arm',
            texture = arm,
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.6,-0.6))
        
    def active(self):
        self.rotation = Vec3(150, -10, 0),
        self.position = Vec2(0.5,-0.5)

    def passive(self):
        self.position = Vec2(0.6,-0.6)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position= (x,0,z))


firstperson = FirstPersonController()
sky = Sky()
hand = Hand()
app.run()