#CS396 Artificial Life Final Project

This is my submission for the Scientific Hypothesis Final Project 

It is heavily based on the ludobots MOOC on https://www.reddit.com/r/ludobots/ created by Professor Josh Bongard

Scientific Method:
    hypothesis: having synapses evolve, and further allowing them to connect to multiple motors improves locomotion evolution, potentially even playing a role in the shape evolution

    sensors can evolve synaptic connections as random


    NO EVOLUTION SYNAPSES(CONTROL):
        Scenario 1: every sensor to every motor, immutable, DONE
        Scenario 2: one sensor to one motor if possible, from the first motor added to minimize mutation impact, immutable pairings not changed by mutation, unless a sensor or motor is deleted physically

    EVOLVED SYNAPSES:
        Scenario 1: Sensors that can connect to multiple motors, flexible pairings
        Scenario 2: Sensors can only connect to one motor, flexible pairings


    Accounting for Evolution in Shape:
        Limit # of blocks for both
        Limit # of motors for both
        Sensor Likelihoods are equal in both control and evolution
        Run several times, to see if evolution takes truly different path

    Accounting for Synaptic Weights:
        Weights are randomly decided at start (-1 or 1) and can not be changed through mutation, evolution does not affect synaptic weights

Technical Specifications:

    Program: Uses python library multiprocessing to improve performance for parallel

    Fitness:

    Mutation:


###Known Issue:
    The system only checks for overlaps when making the body before simulation starts, so occasionally a motor can cause two blocks to go into eachother and overlap after simulation starts
    
###To Run Simulations:
    Set the simulationsettings variable in constants.py to 0,1,2, or 3 depending on which scenario you wish to test
    
        0 is control all connected, 1 is control only single synapse pairs, 2 is evolve single synapse pairs, 3 is evolve multiple pairs
    Then, run python3 runsnakemake.py with two parameters, the name of your simulation and the random seed you wish to use
        eg. `python3 runsnakemake.py readmedemonstration 123456789`
        
        Note: random seeds can only be in the format of unsigned 32 bit ints due to numpy constraints. No negative numbers!
        
###To Run Saved Simulations:
    Set the simulationsettings variable in constants.py to 0,1,2, or 3 depending on which scenario your file is. Incorrect settings may cause issues.
    Then, run python3 picklerunner with one parameter, your file name
        eg. `python3 picklerunner.py readmedemonstration`
            or
            `python3 picklerunner.py pickles/readmedemonstration/generation0`
    
        
    
    
    
    

