import pygame, os
    # sound/crunch.ogg
    #     Apple Bite by AntumDeluge -- https://freesound.org/s/584290/ -- License: Creative Commons 0
    #     apple bite by sonicmariobrotha -- https://freesound.org/s/333825/ -- License: Creative Commons 0

    # sound/collision.wav
    #     Hit 2 by NearTheAtmoshphere -- https://freesound.org/s/676462/ -- License: Creative Commons 0
    
    # background
    # sound/bckgrnd sirius-by-sascha-ende-from-filmmusic-io.mp3
    #     https://filmmusic.io/uk/song/3233-sirius
    #     Sirius by Sascha Ende
    #         мрійливі, пливучі синтезаторні підкладки та заводний ритм. ідеально підходить для космічних тем!
    
    # sound/bckgrnd Space Jazz.mp3
    # "Space Jazz"
    # https://incompetech.com/music/royalty-free/music.html
    #     Instruments: Synths
    #     Feel: Bright, Grooving, Relaxed
    #     While working on a video game, the script called for "Space Jazz". I don't know if that is a thing, but this is what I made. Sounds like Space Jazz to me!
    #     ISRC: USUAN2100030
    #     Uploaded: 2021-09-29
    
    # Credit this piece by copying the following to your credits section:
    #     "Space Jazz" Kevin MacLeod (incompetech.com)
    #     Licensed under Creative Commons: By Attribution 4.0 License
    #     http://creativecommons.org/licenses/by/4.0/

def init_sound():
    pygame.mixer.init()
    dir_for_sound_files = os.path.join(os.path.dirname(__file__), 'sound')
    crunch = pygame.mixer.Sound(os.path.join(dir_for_sound_files, 'crunch.ogg'))
    collision = pygame.mixer.Sound(os.path.join(dir_for_sound_files, 'collision.wav'))
    pygame.mixer.Sound.play(collision) # Під час програвання зіткнення
    
    # Додавання та запуск фонової музики:
    # !!! Потім розкоментуй!
    # bckgrnd_music = pygame.mixer.music.load(os.path.join(dir_for_sound_files, 'bckgrnd Space Jazz.mp3'))
    # pygame.mixer.music.play(-1)
    return crunch, collision