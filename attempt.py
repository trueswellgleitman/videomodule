#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.79.01), Tue Oct 13 06:17:22 2015
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
import random as choose
# Store info about the experiment session
expName = 'attempt'  # from the Builder filename that created this script
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
win = visual.Window(size=(800, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
mouse = event.Mouse(win=win)
mouse2 = event.Mouse(win=win)
x, y = [None, None]

text = visual.TextStim(win=win, ori=0, name='text',
    text=u'Welcome to the Trueswell Gleitman Lab!',    font=u'Arial',
    pos=[0.25, 0.5], height=0.05, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
image = visual.ImageStim(win=win, name='image',
    image=u'alien_new.png', mask=None,
    ori=0, pos=[-.7, 0], size=[0.8, 0.8],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
image_2 = visual.ImageStim(win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace=u'rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=0.0)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

def doVideo(resourceFile):
    i = 0
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method=u'sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(resourceFile),
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
        if i == 0:
            #------Prepare to start Routine "trial"-------
            t = 0
            text.setText(welcometext)
            i = i+1
            trialClock.reset()  # clock 
            frameN = -1
            routineTimer.add(100000000.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            trialComponents = []
            trialComponents.append(ISI)
            trialComponents.append(text)
            trialComponents.append(image)
            trialComponents.append(mouse2)
            for thisComponent in trialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "trial"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text* updates
                if t >= 0.0 and text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text.tStart = t  # underestimates by a little under one frame
                    text.frameNStart = frameN  # exact frame index
                    text.setAutoDraw(True)
                elif text.status == STARTED and t >= (0.0 + 100000000):
                    text.setAutoDraw(False)
                
                # *image* updates
                if t >= 0.0 and image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image.tStart = t  # underestimates by a little under one frame
                    image.frameNStart = frameN  # exact frame index
                    image.setAutoDraw(True)
                elif image.status == STARTED and t >= (0.0 + 100000000):
                    image.setAutoDraw(False)
                # *mouse* updates
                if t >= 0.0 and mouse2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    mouse2.tStart = t  # underestimates by a little under one frame
                    mouse2.frameNStart = frameN  # exact frame index
                    mouse2.status = STARTED
                    event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
                elif mouse2.status == STARTED and t >= (0.0 + 100000000):
                    mouse2.status = STOPPED
                if mouse2.status == STARTED:  # only update if started and not stopped!
                    buttons = mouse2.getPressed()
                    if sum(buttons) > 0:  # ie if any button is pressed
                        # abort routine on response
                        continueRoutine = False
                        mouse2.status = FINISHED
                        print mouse2.status
                                            
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                                    

                # *ISI* period
                if t >= 0.0 and ISI.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ISI.tStart = t  # underestimates by a little under one frame
                    ISI.frameNStart = frameN  # exact frame index
                    ISI.start(0.5)
                elif ISI.status == STARTED: #one frame should pass before updating params and completing
                    ISI.complete() #finish the static period
                

                # check for quit (the [Esc] key)
                if event.getKeys(["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "trial"-------
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
        
        #------Prepare to start Routine "trial2"-------
        t = 0
        trial2Clock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        x = choose.choice([675, -675])
        movie = visual.MovieStim(win=win, name='movie',
            filename="videos/"  + actor + "_" + receiver + "_" + verb + ".avi",
            ori=0, pos=[x, 0], opacity=1,
            depth=-2.0,
            )
        movie_2 = visual.MovieStim(win=win, name='movie',
            filename="videos/"  + actortwo + "_" + receivertwo + "_" + verbtwo + ".avi",
            ori=0, pos=[-x, 0], opacity=1,
            depth=-2.0,
            )    
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(ISI)
        trialComponents.append(mouse)
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
            # *mouse* updates
            if t >= 0.0 and mouse.status == NOT_STARTED:
                # keep track of start time/frame for later
                mouse.tStart = t  # underestimates by a little under one frame
                mouse.frameNStart = frameN  # exact frame index
                mouse.status = STARTED
                event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
            elif mouse.status == STARTED and t >= (0.0 + 10000000000):
                mouse.status = STOPPED
            if mouse.status == STARTED:  # only update if started and not stopped!
                buttons = mouse.getPressed()
                if sum(buttons) > 0:  # ie if any button is pressed
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    if ((mouse.x > 0)):
                        correctPress = "yes"
                        sound.SoundPyo(value='button.wav')
                    if (mouse.x < 0) :
                        correctPress = "yes"
                        sound.SoundPyo(value='button.wav')
                    else:
                        correctPress = "no"
                        sound.SoundPyo(value='bad.wav')
                    mouse.y.append(y)
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(trialClock.getTime())
                    # abort routine on response
                    continueRoutine = False
            
            # *movie* updates
            valueSound="soundfiles/" + soundactor + "_" + soundreceiver + "_" + soundverb + ".wav"
            theSound = sound.SoundPygame(valueSound)
            theSound.play()
            if t >= 0.0 and movie.status == NOT_STARTED:
                # keep track of start time/frame for later
                movie.tStart = t  # underestimates by a little under one frame
                movie.frameNStart = frameN  # exact frame index
                movie.setAutoDraw(True)
            if movie.status == FINISHED:
                movie.pause()      
            #elif movie.status == STARTED and t >= (0.0 + 2.0):
            #    movie.setAutoDraw(False)    
            # *ISI* period
            if t >= 0.0 and ISI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI.tStart = t  # underestimates by a little under one frame
                ISI.frameNStart = frameN  # exact frame index
                ISI.start(0.5)
 
            elif ISI.status == STARTED: #one frame should pass before updating params and completing
                ISI.complete() #finish the static period
                
            if t >= 0.0 and movie_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                movie_2.tStart = t  # underestimates by a little under one frame
                movie_2.frameNStart = frameN  # exact frame index
                movie_2.setAutoDraw(True)
            if movie_2.status == FINISHED:
                movie_2.pause()   
            #elif movie_2.status == STARTED and t >= (0.0 + 2.0):
            #    movie_2.setAutoDraw(False)
    
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
        # save mouse data
        trials.addData('correct', correctPress)
        trials.addData('Type', type)
        #trials.addData('mouse.x', mouse.x[0])
        #trials.addData('mouse.x', mouse.x[0])
        #trials.addData('mouse.y', mouse.y[0])
        #trials.addData('mouse.leftButton', mouse.leftButton[0])
        #trials.addData('mouse.midButton', mouse.midButton[0])
        #trials.addData('mouse.rightButton', mouse.rightButton[0])
        trials.addData('mouse.time', mouse.time[0])
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
def doImage(resourceFile):
    i = 0
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1, method=u'sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(resourceFile),
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
                
        if i == 0:
            #------Prepare to start Routine "trial"-------
            t = 0
            text.setText(welcometext)
            i = i+1
            trialClock.reset()  # clock 
            frameN = -1
            routineTimer.add(100000000.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            trialComponents = []
            trialComponents.append(ISI)
            trialComponents.append(text)
            trialComponents.append(image)
            trialComponents.append(mouse2)
            for thisComponent in trialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "trial"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text* updates
                if t >= 0.0 and text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text.tStart = t  # underestimates by a little under one frame
                    text.frameNStart = frameN  # exact frame index
                    text.setAutoDraw(True)
                elif text.status == STARTED and t >= (0.0 + 100000000):
                    text.setAutoDraw(False)
                
                # *image* updates
                if t >= 0.0 and image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image.tStart = t  # underestimates by a little under one frame
                    image.frameNStart = frameN  # exact frame index
                    image.setAutoDraw(True)
                elif image.status == STARTED and t >= (0.0 + 100000000):
                    image.setAutoDraw(False)
                # *mouse* updates
                if t >= 0.0 and mouse2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    mouse2.tStart = t  # underestimates by a little under one frame
                    mouse2.frameNStart = frameN  # exact frame index
                    mouse2.status = STARTED
                    event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
                elif mouse2.status == STARTED and t >= (0.0 + 100000000):
                    mouse2.status = STOPPED
                if mouse2.status == STARTED:  # only update if started and not stopped!
                    buttons = mouse2.getPressed()
                    if sum(buttons) > 0:  # ie if any button is pressed
                        # abort routine on response
                        continueRoutine = False
                        mouse2.status = FINISHED
                        print mouse2.status
                                            
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                                    

                # *ISI* period
                if t >= 0.0 and ISI.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ISI.tStart = t  # underestimates by a little under one frame
                    ISI.frameNStart = frameN  # exact frame index
                    ISI.start(0.5)
                elif ISI.status == STARTED: #one frame should pass before updating params and completing
                    ISI.complete() #finish the static period
                

                # check for quit (the [Esc] key)
                if event.getKeys(["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "trial"-------
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)                
        
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
        trials_2.addData('Type', type)        
        #x, y = mouse_2.getPos()
        #buttons = mouse_2.getPressed()
        #trials_2.addData('mouse_2.x', x)
        #trials_2.addData('mouse_2.y', y)
        #trials_2.addData('mouse_2.leftButton', buttons[0])
        #trials_2.addData('mouse_2.midButton', buttons[1])
        #trials_2.addData('mouse_2.rightButton', buttons[2])
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
myFuncs = [doVideo,doImage]
myFuncs[0]('test.csv')
print "yes"
myFuncs[1]('images.csv')
print "reached"
myFuncs[1]('images2.csv')

win.close()
core.quit()

