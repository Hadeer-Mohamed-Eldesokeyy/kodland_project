from pygame import Rect

WIDTH = 800
HEIGHT = 600

GRAVITY = 0.6
JUMP_POWER = -12
GROUND_Y = 520

game_state = "menu"
sound_enabled = True


# class for both the player and enemies
class Character:
    def __init__(self, idle_frames, walk_frames, x, y):
        self.idle_frames = idle_frames
        self.walk_frames = walk_frames
        self.actor = Actor(idle_frames[0], (x, y))

        self.frame = 0
        self.animation_time = 0
        self.moving = False
        self.facing_right = True

    # Change between idle and walking frames
    def update_animation(self, dt):
        self.animation_time += dt

        if self.moving:
            frames = self.walk_frames
            frame_delay = 0.12
        else:
            frames = self.idle_frames
            frame_delay = 0.35

        if self.animation_time >= frame_delay:
            self.animation_time = 0
            self.frame += 1

            if self.frame >= len(frames):
                self.frame = 0

            self.actor.image = frames[self.frame]

        self.actor.flip_x = not self.facing_right

    def get_rect(self):
        return Rect(
            self.actor.x - 20,
            self.actor.y - 40,
            40,
            80
        )

    def draw(self):
        self.actor.draw()


# Player movement and jumping
class Player(Character):
    SPEED = 4

    def __init__(self, x, y):
        idle_frames = ["player_stand", "player_idle"]
        walk_frames = ["player_walk1", "player_walk2"]

        super().__init__(idle_frames, walk_frames, x, y)

        self.vertical_speed = 0
        self.on_ground = False

    def move(self):
        self.moving = False

        if keyboard.left:
            self.actor.x -= self.SPEED
            self.facing_right = False
            self.moving = True

        if keyboard.right:
            self.actor.x += self.SPEED
            self.facing_right = True
            self.moving = True

    def jump(self):
        if self.on_ground:
            self.vertical_speed = JUMP_POWER
            self.on_ground = False

            if sound_enabled:
                sounds.jump.play()

    # gravity and land on platforms to ensure its real
    def update_physics(self, platforms):
        self.vertical_speed += GRAVITY
        self.actor.y += self.vertical_speed
        self.on_ground = False

        for platform in platforms:
            if self.get_rect().colliderect(platform):
                if self.vertical_speed >= 0:
                    self.actor.y = platform.top - 40
                    self.vertical_speed = 0
                    self.on_ground = True

    def update_animation(self, dt):
        if not self.on_ground:
            self.actor.image = "player_jump"
            self.actor.flip_x = not self.facing_right
        else:
            super().update_animation(dt)


# enemy that moves inside its own limited area
class Enemy(Character):
    def __init__(self, idle_frames, walk_frames, x, y,
                 left_limit, right_limit, speed):

        super().__init__(idle_frames, walk_frames, x, y)

        self.left_limit = left_limit
        self.right_limit = right_limit
        self.speed = speed
        self.moving = True

    def patrol(self):
        self.actor.x += self.speed

        if self.actor.x >= self.right_limit:
            self.speed = -abs(self.speed)
            self.facing_right = False

        elif self.actor.x <= self.left_limit:
            self.speed = abs(self.speed)
            self.facing_right = True


# floating platforms for the level
platforms = [
    Rect(0, GROUND_Y, WIDTH, 40),
    Rect(150, 400, 140, 20),
    Rect(400, 320, 140, 20),
    Rect(600, 220, 140, 20)
]


# the main hero
player = Player(60, GROUND_Y - 40)


# two different enemies
zombie = Enemy(
    ["zombie_stand", "zombie_idle"],
    ["zombie_walk1", "zombie_walk2"],
    250,
    GROUND_Y - 40,
    170,
    330,
    1.5
)

soldier = Enemy(
    ["soldier_stand", "soldier_idle"],
    ["soldier_walk1", "soldier_walk2"],
    550,
    GROUND_Y - 40,
    480,
    650,
    2
)

enemies = [zombie, soldier]


# The player wins by reaching the flag
flag = Actor("flag", (700, 175))


# Clickable menu buttons
buttons = {
    "start": Rect(300, 220, 200, 50),
    "sound": Rect(300, 290, 200, 50),
    "exit": Rect(300, 360, 200, 50)
}


def reset_game():
    player.actor.pos = (60, GROUND_Y - 40)
    player.vertical_speed = 0
    player.on_ground = False


def update(dt):
    global game_state

    if game_state != "playing":
        return

    player.move()

    if keyboard.space:
        player.jump()

    player.update_physics(platforms)
    player.update_animation(dt)

    for enemy in enemies:
        enemy.patrol()
        enemy.update_animation(dt)

    # player loses after falling
    if player.actor.y > HEIGHT + 50:
        game_state = "lose"

        if sound_enabled:
            sounds.hit.play()

        return

    # player loses after touching the enemy
    for enemy in enemies:
        if player.get_rect().colliderect(enemy.get_rect()):
            game_state = "lose"

            if sound_enabled:
                sounds.hit.play()

            return

    # the flag collision area
    flag_rect = Rect(
        flag.x - 16,
        flag.y - 24,
        32,
        48
    )

    # player wins
    if player.get_rect().colliderect(flag_rect):
        game_state = "win"

        if sound_enabled:
            sounds.win.play()


def draw():
    screen.fill((135, 206, 235))

    if game_state == "menu":
        draw_menu()
        return

    # draw platforms
    for platform in platforms:
        if platform.top == GROUND_Y:
            color = (60, 140, 60)
        else:
            color = (90, 60, 40)

        screen.draw.filled_rect(platform, color)

    flag.draw()
    player.draw()

    for enemy in enemies:
        enemy.draw()

    if game_state == "win":
        draw_message(
            "You reached the flag! Click to return to the menu."
        )

    elif game_state == "lose":
        draw_message(
            "You were caught! Click to return to the menu."
        )


def draw_menu():
    screen.draw.text(
        "Forest Escape",
        center=(WIDTH // 2, 130),
        fontsize=60,
        color="white"
    )

    # Start button
    screen.draw.filled_rect(
        buttons["start"],
        (70, 150, 70)
    )

    screen.draw.text(
        "Start Game",
        center=buttons["start"].center,
        fontsize=30,
        color="white"
    )

    # Sound button
    screen.draw.filled_rect(
        buttons["sound"],
        (70, 90, 150)
    )

    if sound_enabled:
        sound_text = "Sound: ON"
    else:
        sound_text = "Sound: OFF"

    screen.draw.text(
        sound_text,
        center=buttons["sound"].center,
        fontsize=30,
        color="white"
    )

    # Exit button
    screen.draw.filled_rect(
        buttons["exit"],
        (150, 70, 70)
    )

    screen.draw.text(
        "Exit",
        center=buttons["exit"].center,
        fontsize=30,
        color="white"
    )


def draw_message(message):
    message_box = Rect(100, 250, 600, 100)

    screen.draw.filled_rect(
        message_box,
        (0, 0, 0)
    )

    screen.draw.text(
        message,
        center=(WIDTH // 2, 300),
        fontsize=28,
        color="white"
    )


def on_mouse_down(pos):
    global game_state, sound_enabled

    if game_state == "menu":

        if buttons["start"].collidepoint(pos):
            reset_game()
            game_state = "playing"

            if sound_enabled:
                music.play("theme")

        elif buttons["sound"].collidepoint(pos):
            sound_enabled = not sound_enabled

            if sound_enabled:
                music.play("theme")
            else:
                music.stop()

        elif buttons["exit"].collidepoint(pos):
            exit()

    # return to the menu after winning or losing
    elif game_state in ("win", "lose"):
        game_state = "menu"