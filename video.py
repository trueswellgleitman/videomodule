#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.79.01), Tue Oct  6 06:48:07 2015
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'try'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(2560, 1700), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1 ,-1, -1], colorSpace='rgb')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
image_2 = visual.ImageStim(win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('test.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    movie = visual.MovieStim(win=win, name='movie',
        filename="videos/"+actor+"_"+reciever+"_"+verb+".avi",
        ori=0, pos=[675, 0], opacity=1,
        depth=-2.0,
        )
    movie_2 = visual.MovieStim(win=win, name='movie_2',
        filename="videos/"+actor+"_"+reciever+"_"+verb+".avi",
        ori=0, pos=[-675, 0], opacity=1,
        depth=-3.0,
        )
    movie_2.setFlipHoriz(newVal=True, log=None)    
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(key_resp_2)
    trialComponents.append(movie)
    trialComponents.append(movie_2)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            event.clearEvents()
        if key_resp_2.status == STARTED:
            leftKey = event.getKeys(keyList=['left'])
            rightKey = event.getKeys(keyList=['right'])
            if len(leftKey) > 0:  # at least one key was pressed
                key_resp_2.keys = leftKey[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
                sound.SoundPyo(value='bad.wav')
            if len(rightKey) > 0:
                key_resp_2.keys = rightKey[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
                sound.SoundPyo(value='button.wav')
        
        # *movie* updates
        if t >= 0.0 and movie.status == NOT_STARTED:
            # keep track of start time/frame for later
            movie.tStart = t  # underestimates by a little under one frame
            movie.frameNStart = frameN  # exact frame index
            movie.setAutoDraw(True)
        elif movie.status == STARTED and t >= (0.0 + 2.0):
            movie.setAutoDraw(False)
        if movie.status == FINISHED:  # force-end the routine
            continueRoutine = False
        
        # *movie_2* updates
        if t >= 0.0 and movie_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            movie_2.tStart = t  # underestimates by a little under one frame
            movie_2.frameNStart = frameN  # exact frame index
            movie_2.setAutoDraw(True)
        elif movie_2.status == STARTED and t >= (0.0 + 2.0):
            movie_2.setAutoDraw(False)
        if movie_2.status == FINISHED:  # force-end the routine
            continueRoutine = False
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(5.0)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
    # store data for trials (TrialHandler)
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    thisExp.nextEntry()
    
# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'images.csv'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    #------Prepare to start Routine "trial2"-------
    t = 0
    trial2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image_2.setImage("images/" + names + verb + color + object + ".png")
    # setup some python lists for storing info about the mouse_2
    # keep track of which components have finished
    trial2Components = []
    trial2Components.append(image_2)
    trial2Components.append(mouse_2)
    for thisComponent in trial2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trial2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t  # underestimates by a little under one frame
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        # *mouse_2* updates
        if t >= 0.0 and mouse_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse_2.tStart = t  # underestimates by a little under one frame
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouse_2.status == STARTED:  # only update if started and not stopped!
            buttons = mouse_2.getPressed()
            if sum(buttons) > 0:  # ie if any button is pressed
                # abort routine on response
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trial2"-------
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # get info about the mouse_2
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    trials_2.addData('mouse_2.x', x)
    trials_2.addData('mouse_2.y', y)
    trials_2.addData('mouse_2.leftButton', buttons[0])
    trials_2.addData('mouse_2.midButton', buttons[1])
    trials_2.addData('mouse_2.rightButton', buttons[2])
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'

win.close()
core.quit()

