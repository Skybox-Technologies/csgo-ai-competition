#!/usr/bin/env python3
import os
import sys
import random
import pandas as pd
from collections import defaultdict

# Don't print "Hello from pygame" on stdout
with open(os.devnull, 'w') as f:
    # disable stdout
    oldstdout = sys.stdout
    sys.stdout = f

    import pygame
    from pygame.locals import *

    # enable stdout
    sys.stdout = oldstdout


def display_text(msg, pos):
    text = font.render(msg, True, (255, 255, 255))
    screen.blit(text, pos)


# Load one of the datasets
if len(sys.argv) < 2:
    print("Usage: render.py <path/to/dataset_xx.json>")
    sys.exit(1)

dataset = pd.read_json(sys.argv[1])
round_snapshot_index = 0
round_snapshot = dataset.loc[round_snapshot_index]
num_snapshots = len(dataset)

# Init map data
game_map_coords = {
    "de_cache":    (-2000, 3250),
    "de_dust2":    (-2476, 3239),
    "de_inferno":  (-2087, 3870),
    "de_mirage":   (-3230, 1713),
    "de_nuke":     (-3453, 2887),
    "de_overpass": (-4831, 1781),
    "de_train":    (-2477, 2392),
    "de_vertigo":  (-3168, 1762),
}
game_map_scales = {
    "de_cache":    5.5,
    "de_dust2":    4.4,
    "de_inferno":  4.9,
    "de_mirage":   5.0,
    "de_nuke":     7.0,
    "de_overpass": 5.2,
    "de_train":    4.7,
    "de_vertigo":  4.0,
}
map_name = None
game_map = None
game_map_lower = None
game_map_scale = None
game_map_coord = None


def coord(x, y):
    '''Calculate radar coordinates from game coordinates for the chosen map'''
    res = (int(round((x-game_map_coord[0]) / game_map_scale)),
           int(abs(round((y-game_map_coord[1]) / game_map_scale))))
    return res


def load_snapshot(index):
    '''Load round snapshot `index` from the dataset and select the map it was played on'''
    global round_snapshot, map_name, game_map, game_map_lower, game_map_scale, game_map_coord
    round_snapshot = dataset.loc[index]
    map_name = round_snapshot['map']
    game_map = pygame.image.load(
        'resources/overview/{}_radar.png'.format(map_name))
    game_map_lower = pygame.image.load('resources/overview/{}_lower_radar.png'.format(
        map_name)) if map_name in ["de_nuke"] else game_map
    game_map_scale = game_map_scales[map_name]
    game_map_coord = game_map_coords[map_name]


load_snapshot(round_snapshot_index)

# Init pygame
pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 12)

# Screen
screen_width = 1024
screen_height = 1024
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()

# Colors
ct_color = (0, 0, 255)
t_color = (255, 200, 0)
tooltip = ''


def render_player(player):
    pos = player['position_history'][-1]
    color = ct_color if player['team'] == 'CT' else t_color
    pygame.draw.circle(
        screen, color, coord(pos['x'], pos['y']), 7
    )

def render_smoke(smoke):
    pos = smoke['position']
    pygame.draw.circle(
        screen, (127, 127, 127), coord(pos['x'], pos['y']), 20
    )

def render_molotov(molotov):
    pos = molotov['position']
    pygame.draw.circle(
        screen, (255, 69, 0), coord(pos['x'], pos['y']), 20
    )

def render_bomb(pos):
    pygame.draw.rect(
        screen, (255, 0, 0), pygame.Rect(coord(pos['x'], pos['y']), (5, 8))
    )


def render_frame():
    for molotov in round_snapshot['active_molotovs']:
        render_molotov(molotov)
    for smoke in round_snapshot['active_smokes']:
        render_smoke(smoke)
    for player in round_snapshot['alive_players']:
        render_player(player)
    if round_snapshot['planted_bomb']:
        render_bomb(round_snapshot['planted_bomb']['position'])


# Render loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            if event.key == pygame.K_LEFT:
                # Previous index
                round_snapshot_index = max(0, round_snapshot_index - 1)
                load_snapshot(round_snapshot_index)
            if event.key == pygame.K_RIGHT:
                # Next index
                round_snapshot_index = min(
                    num_snapshots, round_snapshot_index + 1)
                load_snapshot(round_snapshot_index)
            if event.key == pygame.K_r:
                # Random index
                round_snapshot_index = random.randint(0, num_snapshots)
                load_snapshot(round_snapshot_index)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_l]:
        game_map, game_map_lower = game_map_lower, game_map
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(game_map, (0, 0))
    render_frame()
    if tooltip:
        display_text(tooltip, (800, 950))
        tooltip = ''

    pygame.display.update()
    clock.tick(16)
