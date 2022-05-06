import math
import random
import pygame
import colorsys

kolor_tla = (0,0,0)

def init_figury(bok_kwadratu_opisanego, ilosc_katow):
    delta_kat = 360 / ilosc_katow
    offset = bok_kwadratu_opisanego / 2 - 10
    figura = []

    for i in range(0, ilosc_katow):
        kat = (180 + i * delta_kat) * math.pi / 180
        color = colorsys.hsv_to_rgb((i * delta_kat) / 360, 0.8, 1)
        figura.append(((bok_kwadratu_opisanego / 2 + offset * math.sin(kat),
                         bok_kwadratu_opisanego / 2 + offset * math.cos(kat)),
                        (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))))
    return figura

def random_point(figura):
    global index
    index = random.randint(0, len(figura)-1)
    return index

def mark_pix(powieszchnia, pozycja, kolol_pixela):
    color = powieszchnia.get_at(pozycja)
    powieszchnia.set_at(pozycja, (min(color[0] + kolol_pixela[0] / 10, 255),
                              min(color[1] + kolol_pixela[1] / 10, 255),
                              min(color[2] + kolol_pixela[2] / 10, 255)))   

def main(bok, ilosc_katow):
    if ((ilosc_katow > 2) and (ilosc_katow < 5)):
        odsuniecie = 0.5
    if ilosc_katow >= 5:
        odsuniecie = 0.62
    pygame.init()
    przestrzen_wyswietlania = pygame.display.set_mode((bok, bok))
    przestrzen_wyswietlania.fill(kolor_tla)
    pygame.display.set_caption('Sierpiński')
    figura = init_figury(bok, ilosc_katow)

    while True:
        x, y = (0, 0)
        for i in range(0, bok^2):
            i = random_point(figura)
            x += (figura[i][0][0] - x) * odsuniecie
            y += (figura[i][0][1] - y) * odsuniecie
            
            mark_pix(przestrzen_wyswietlania, (int(x), int(y)), figura[i][1])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
        pygame.quit

if __name__ == "__main__":
    main(500, 3)

