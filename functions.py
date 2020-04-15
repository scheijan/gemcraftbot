# standard library imports
from time import sleep
import os
import random
import logging

# third party imports
import pyautogui as gui
import pytesseract
import cv2

# project imports
from constants import *

log = logging.getLogger('main')


def buildTower(pos):
    gui.press('t')
    gui.click(*pos)
    gui.press('t')
    sleep(STEP)


def buildAmplifier(pos):
    gui.press('a')
    gui.click(*pos)
    gui.press('a')
    sleep(STEP)


def buildLantern(pos):
    gui.press('l')
    gui.click(*pos)
    gui.press('l')
    sleep(STEP)


def buildPylon(pos):
    gui.press('p')
    gui.click(*pos)
    gui.press('p')
    sleep(STEP)


def buildTrap(pos):
    gui.press('r')
    gui.click(*pos)
    gui.press('r')
    sleep(STEP)


def buildWall(pos):
    gui.press('w')
    gui.click(*pos)
    gui.press('w')
    sleep(STEP)


def createGem(color, level=1):
    gui.press(GEMKEYS.get(color, 'yellow'))
    sleep(STEP)


def upgradeGem(pos):
    gui.moveTo(*pos)
    gui.press('u')
    sleep(STEP)


def duplicateGem(pos):
    gui.moveTo(*pos)
    gui.press('d')
    sleep(STEP)


def sellGem(pos):
    gui.moveTo(*pos)
    gui.press('x')
    sleep(STEP)


def sellAllGems(pos):
    for pos in INVENTORY:
        sellGem(pos)


def enrageWithGem(gemPosition):
    gui.moveTo(*gemPosition)
    gui.dragTo(*ENRAGESLOT)


def enrageWithDefaultGem():
    gui.click(*ENRAGESLOT)


def addEnhancement(pos, enhancement):
    gui.moveTo(*pos)
    gui.press(str(enhancement))
    sleep(STEP)


def addRandomEnhancement(pos):
    enhancement = random.randint(4, 6)
    addEnhancement(pos, enhancement)


def setPriority(gemPosition, priority):
    if priority == 'flying':
        gui.moveTo(*gemPosition)
        gui.mouseDown(button="RIGHT")
        gui.move(-25, 25)
        gui.mouseUp(button="RIGHT")
    else:
        pass
    sleep(STEP)


def placeDefaultGemInBuilding(building):
    gui.click(*building)
    sleep(STEP)


def placeGemInBuilding(gem, building):
    gui.moveTo(*gem)
    gui.dragTo(*building)
    sleep(STEP)


def backToTheMap():
    gui.click(*BACKBUTTON)


def startTime(fast=True):
    gui.press('q')
    if fast:
        gui.press('q')
    sleep(STEP)


def togglePause():
    gui.press('space')
    sleep(STEP)


def callNextWave(number=1):
    gui.press('n', presses=number)


def isRunning():
    os.system('rm ~/gemcraftbot/screenshots/*')
    os.system('flameshot full -p ~/gemcraftbot/screenshots/')
    sleep(10)
    img = cv2.imread('screenshots/screenshot.png')
    text = pytesseract.image_to_string(img)
    # log.info(text)
    words = ['Field', 'Journey', 'mode', 'highest', 'Gathered',
             'Longest', 'Shrines', 'Activated', 'Waves', 'Called', 'Early']
    for word in words:
        if word in text:
            return False

    return True


def startField(field, center, run, label='unknown'):
    log.info('starting field "%s" at position %s' % (label, field))
    # click on the field
    if run == 1:
        gui.click(*field)
        gui.click(*field)
    else:
        gui.click(*center)
        gui.click(*center)
        gui.click(*field)
        gui.click(*field)
    sleep(1)

    # click on Start the Battle!
    gui.click(*STARTBUTTON)

    # wait for field to load
    if run == 1:
        sleep(15)
    else:
        sleep(8)
