from pygame import*


class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed   
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (200, 255, 255)
win_width = 600
win_height = 500 
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('roma10.jpg'), (win_width, win_height))


game = True
finish = False
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('roma5.mp3')
mixer.music.play()
lose_sound = mixer.Sound('roma6.mp3')

racket1 = Player('roma5.png', 30, 200, 4, 50, 150)
racket2 = Player('roma6.png', 520, 200, 4, 50, 150)
ball = GameSprite('roma3.png', 200, 200, 4, 50, 50)

font.init()
font = font.SysFont('Arial', 35)
lose1 = font.render('ТИ ВИГРАВ!!!', True, (180, 0, 0))
lose2 = font.render('ТИ ПРОГРАВ!!!', True, (180, 0, 0))
speed_x = 5 
speed_y = 5
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        keys = key.get_pressed()
        window.blit(background, (0, 0))
        racket1.update_l()
        racket2.update_r()  
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1


        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1


        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            if keys[K_r]:
                ball.rect.x = 300
                ball.rect.y = 250
            lose_sound.play()
            mixer.music.stop()

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            finish = False
            if keys[K_r]:
                ball.rect.x = 300
                ball.rect.y = 250
            lose_sound.play()
            mixer.music.stop() 

            

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)                 