# standard library imports
from time import sleep
from datetime import datetime
import logging

# third party imports
import coloredlogs

# project imports
from constants import *
from functions import *

log = logging.getLogger('main')
coloredlogs.install(level='INFO', fmt='[%(asctime)s] %(levelname)s %(message)s', datefmt='%d/%b/%Y %I:%M:%S')


def main(FIELD, CENTERFIELD, TOWERS, AMPLIFIERS, LANTERNS, PYLONS, WALLS, NEWWAVEINTERVAL=1, NEWWAVENUMBER=2, run=1):
    BUILDINGS = TOWERS + AMPLIFIERS
    log.info('starting run %s at %s' % (run, datetime.now()))

    startField(FIELD, CENTERFIELD, run)

    # build walls
    log.info('building %s walls' % len(WALLS))
    for wall in WALLS:
        buildWall(wall)

    # build amps
    log.info('building %s amplifier' % len(AMPLIFIERS))
    for amp in AMPLIFIERS:
        buildAmplifier(amp)

    # build towers
    log.info('building %s towers' % len(TOWERS))
    for tower in TOWERS:
        buildTower(tower)

    # create yellow gems in all buildings
    log.info('creating and placing %s gems' % (len(BUILDINGS)))
    for building in BUILDINGS:
        createGem('yellow')
        placeDefaultGemInBuilding(building)

    log.info('setting all priorities to "flying"')
    for tower in TOWERS:
        setPriority(tower, 'flying')

    # start he game
    log.info('starting the game')
    startTime(fast=True)

    # loop: keep upgrading everything
    upgradeCounter = 0
    while True:
        upgradeCounter += 1
        log.info('upgrade round %s' % upgradeCounter)
        for building in BUILDINGS:
            upgradeGem(building)
            if building in TOWERS:
                addRandomEnhancement(building)
            sleep(1)

        if NEWWAVEINTERVAL is not None:
            if upgradeCounter % NEWWAVEINTERVAL == 0:
                callNextWave(NEWWAVENUMBER)

        if not isRunning():
            log.info('game over?')
            backToTheMap()
            sleep(10)
            break
        log.info('game is still on')


def a1_xp():
    FIELD = (803, 277)
    CENTERFIELD = (961, 567)

    TOWERS = [(255, 193), (495, 593), (441, 647),
              (491, 645), (547, 647), (493, 701)]

    AMPLIFIERS = [(439, 591), (541, 591), (441, 699), (547, 699)]

    # after how many gem upgrade cycles should another wave be called early?
    # set to None to disable
    NEWWAVEINTERVAL = 1

    # how many waves should be called each time?
    NEWWAVENUMBER = 2
    run = 0
    while True:
        run += 1
        main(FIELD, CENTERFIELD, TOWERS, AMPLIFIERS, [], [], [], NEWWAVEINTERVAL, NEWWAVENUMBER, run)


def a1_fragments():
    FIELD = (803, 277)
    CENTERFIELD = (961, 567)

    TOWERS = [(255, 193), (495, 593), (441, 647),
              (491, 645), (547, 647), (493, 701)]

    AMPLIFIERS = [(439, 591), (541, 591), (441, 699), (547, 699)]

    # after how many gem upgrade cycles should another wave be called early?
    # set to None to disable
    NEWWAVEINTERVAL = 1

    # how many waves should be called each time?
    NEWWAVENUMBER = 2
    run = 0
    while True:
        run += 1
        main(FIELD, CENTERFIELD, TOWERS, AMPLIFIERS, NEWWAVEINTERVAL, NEWWAVENUMBER, run)


if __name__ == '__main__':
    a1_xp()
