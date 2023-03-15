# CS396 Artificial Life Final Project

This is my submission for the Scientific Hypothesis Final Project for CS 396 Artificial Life

It is heavily based on the ludobots MOOC, particularly the parallel hill climber, on https://www.reddit.com/r/ludobots/ created by Professor Josh Bongard

Code from Professor Bongard's pyrosim, at the link https://github.com/jbongard/pyrosim, was also used

Credit to Raed Mughaus on StackExchange for helping to write the mathplotlib confidence interval grapher code, https://stackoverflow.com/a/70949996


## Description
    This is a simulator 


### Scientific Method:
    Hypothesis: Having synapses be able to evolve alongside bodies improves locomotion distance for my parallel hill climber, with multiple synaptic pairings between motors and sensors further improving locomotion distance

    To test this I ran 500 Generations of 10 robots per population, with 5 different random seeds, for each of these 4 scenarios

    NO EVOLUTION SYNAPSES(CONTROL):
        Scenario 1: Every sensor to every motor, immutable connections except for sensor/motor addition or deletion
        Scenario 2: One sensor to one motor if possible, from the first sensor and motor added to minimize mutation impact, immutable pairings not changed by mutation, unless a sensor or motor is deleted physically

    EVOLVED SYNAPSES:
        Scenario 3: Sensors can only connect to one motor and vice versa, flexible pairings
        Scenario 4: Sensors that can connect to multiple motors, flexible pairings
        
    Here is a diagram of the hypothetical neural makeups of each of these scenarios:
        4 scenarios brains jpeg


    Accounting for Evolution in Shape:
        Limited # of blocks for both, 1.5 * the starting length, which is randomly decided between 6-12 for all robots
        Sensor Likelihoods are equal in both control and evolution
        Run several times with different random seeds, to see if evolution takes truly different path

    Accounting for Synaptic Weights:
        Weights are randomly decided at start (between either -1 or 1) and can not be changed through mutation, evolution does not affect synaptic weights except when a sensor or motor is added/removed

### Observations and Conclusion
    Observations:
        What I observed was rather different than what I expected for the most part. While the Control scenario with one sensor for each motor did end up performing much worse than the other three, as I expected, the Control with every sensor connected to every motor performing the best on average was quite a suprise. I was also suprised to find that there wasnt a large difference in the averages for the two Hypothesis Scenarios, with them performing approximately equally.

        Graphs of the four scenarios best fitness charts, seperate and then combined:
            4 scenario pics
            all combined pic
        The confidence interval:
            ci figure.png

        One thing I noticed from observing the simulations in action, was that many of the final robots optimized to essentially vibrate their way across the world, with small rapid movements, something which I believe takes fewer actuating motors than actual leg movement. Some potential solutions to this could be to increase the values of synaptic weights possible, to evolutionarily incentivize robots with more movement, or to perhaps increase the range of motor movement.


    Conclusion:
        From the data observed, I can not say that evolving synapses leads to further locomotion, with the data observed seeming to suggest the opposite, that having every motor connected to every sensor leads to greater distance traveled. Furthermore, there is no yet apparent difference between having synapses be able to evolve one to one or unrestricted between motors and sensors.

    Future Inquiry:
        Run more simulations to see if a pattern becomes apparent with more accurate confidence intervals
        Alter the way bodies are generated so that vibration movement is less likely
        Potentially see if better brains can evolve given different weight values, or with more generations
        Change the types of joints, potentially add a ball and socket joint like discussed in class, or change axis of rotation
        See how having a fixed body impacts neural evolution and whether it reveals a difference between these scenarios



   



### Technical Specifications:

    Body: The evolution of the body is done through building a database of blocks before starting, with each block having three qualities(sensor/not, random dimensions, random directions of connection). The simulation then starts by adding the base block no matter what, and then reading to see how many connections the base block then has. For each direction of connection, a block is then added, and then these blocks undergo the same process, to see how many connections they then have, whether they are sensor blocks or not, and then these blocks are added to the blocks connected to the base block, and so on until the maximum number of blocks is reached. 
    
   This diagram is a theoretical diagram to show how this happens, each arrow is theoretical, the base block is guaranteed to have a connection but the rest are not:
   
   ![theoretical geneprint](https://user-images.githubusercontent.com/23564433/225198933-1be1eb12-be7e-423e-8cdf-15a0533296c5.png)
   
   Here is another diagram showing the blueprint for a block fully evolved side by side with the block itself:


    Brain: See the above Hypothesis section for a diagram of how the brains are created/evolved depending on the scenario 

    Fitness: The fitness of the robots is decided by a simple check of the final x coordinate position of the robots base block at the end of its lifespan, a larger fitness is considered better, incentivizing movement along the positive x axis


    Mutation: Mutations are handled by a call to the Mutate() function inside of each Solution Class(the class for each robot) 
        In the mutate function there is a 
            40% chance that a blocks size and connection directions are randomly changed
            40% chance that the number of blocks is either increased or decreased by 1, so 20% chance each
            20% chance that the number of blocks is increased or decreased by 2, 10% chance each
        
        Furthermore, for scenarios in which the brain is allowed to evolve, there is a seperate and independent:
            20% chance that a sensor motor pairing is removed 
            20% chance that a sensor motor pairing is added, if one exists that does not violate the conditions of the scenario

        Here is a diagram of such mutations:



            For the hypothesis, where brains can evolve:
            mutate brains.jpg
            

    Environment: The environment is a simple plain flat world with a floor without any defining characteristics. Creatures face no obstacles in movement.
        Here is a simple diagram covering the essentials:



### Known Issue:
    The system only checks for overlaps when making the body before simulation starts, so a motor joint can cause two blocks to go into eachother and overlap after simulation starts

### Requirements
    The program requires pybullet to be installed and has only been tested on Mac. If running on Windows, any rm, mkdir, or cp commands must be changed to their Windows equivalents.

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
    
        
    
    
    
    

