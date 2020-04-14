# standard library imports
from time import sleep
from datetime import datetime
import logging

# third party imports
import coloredlogs

# project imports
from constants import *
from functions import *


FIELD = (803, 277)
CENTERFIELD = (961, 567)

TOWERS = [(255, 193), (495, 593), (441, 647),
          (491, 645), (547, 647), (493, 701)]

AMPLIFIERS = [(439, 591), (541, 591), (441, 699), (547, 699)]

BUILDINGS = TOWERS + AMPLIFIERS


log = logging.getLogger('main')
coloredlogs.install(
    level='INFO', fmt='[%(asctime)s] %(levelname)s %(message)s', datefmt='%d/%b/%Y %I:%M:%S')


def main(run):
    log.info('starting run %s at %s' % (run, datetime.now()))

    startField(FIELD, CENTERFIELD, run)

    # build 4 amps
    log.info('building %s amplifier' % len(AMPLIFIERS))
    for amp in AMPLIFIERS:
        buildAmplifier(amp)

    # build 5 + 1 towers
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

        if not isRunning():
            log.info('game over?')
            backToTheMap()
            sleep(10)
            break
        log.info('game is still on')


if __name__ == '__main__':
    run = 0
    while True:
        run += 1
        main(run)
