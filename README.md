# CS396 Artificial Life Final Project

This is my submission for the Scientific Hypothesis Final Project for CS 396 Artificial Life

It is heavily based on the ludobots MOOC, particularly the parallel hill climber, on https://www.reddit.com/r/ludobots/ created by Professor Josh Bongard

Code from Professor Bongard's pyrosim, at the link https://github.com/jbongard/pyrosim, was also used

Credit to Raed Mughaus on StackExchange for helping to write confidence interval grapher code, https://stackoverflow.com/a/70949996

Scientific Method:
    Hypothesis: Having synapses be able to evolve alongside bodies improves locomotion distance, with multiple synaptic pairings between motors and sensors further improving locomotion distance

    To test this I ran 500 Generations of 10 robots per population, with 5 different random seeds, for each of these 4 scenarios

    NO EVOLUTION SYNAPSES(CONTROL):
        Scenario 1: Every sensor to every motor, immutable connections except for sensor/motor addition or deletion
        Scenario 2: One sensor to one motor if possible, from the first sensor and motor added to minimize mutation impact, immutable pairings not changed by mutation, unless a sensor or motor is deleted physically

    EVOLVED SYNAPSES:
        Scenario 3: Sensors can only connect to one motor and vice versa, flexible pairings
        Scenario 4: Sensors that can connect to multiple motors, flexible pairings
        
    Here is a diagram of the hypothetical neural makeups of each of these scenarios:



    Accounting for Evolution in Shape:
        Limit # of blocks for both, 1.5 * the starting length, which is randomly decided between 6-12 for all robots
        Sensor Likelihoods are equal in both control and evolution
        Run several times with different random seeds, to see if evolution takes truly different path

    Accounting for Synaptic Weights:
        Weights are randomly decided at start (between either -1 or 1) and can not be changed through mutation, evolution does not affect synaptic weights except when a sensor or motor is added/removed

### Observations and Conclusion
    Observations:
        What I observed was rather different than what I expected for the most part. 



### Technical Specifications:

    Body: The evolution of the body is done through 



    Fitness: The fitness of the robots is decided by a simple check of the final x coordinate position of the robots base block at the end of its lifespan
    

    Mutation: Mutations are handled by a call to the Mutate() function inside of each Solution Class 
    In the mutate function
    
    Independently of that, for the Hypothesis tests, each mutation call has 


### Known Issue:
    The system only checks for overlaps when making the body before simulation starts, so occasionally a motor can cause two blocks to go into eachother and overlap after simulation starts
    
### To Run Simulations:
    Set the simulationsettings variable in constants.py to 0,1,2, or 3 depending on which scenario you wish to test
    
        0 is control all connected, 1 is control only single synapse pairs, 2 is evolve single synapse pairs, 3 is evolve multiple pairs
    Then, run python3 runsnakemake.py with two parameters, the name of your simulation and the random seed you wish to use
        eg. `python3 runsnakemake.py readmedemonstration 123456789`
        
        Note: random seeds can only be in the format of unsigned 32 bit ints due to numpy constraints. No negative numbers!
        
### To Run Saved Simulations:
    Set the simulationsettings variable in constants.py to 0,1,2, or 3 depending on which scenario your file is. Incorrect settings may cause issues.
    Then, run python3 picklerunner with one parameter, your file name
        eg. `python3 picklerunner.py readmedemonstration`
            or
            `python3 picklerunner.py pickles/readmedemonstration/generation0`
    
        
    
    
    
    

