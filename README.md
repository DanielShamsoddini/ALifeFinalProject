# CS396 Artificial Life Final Project

This is my submission for the Scientific Hypothesis Final Project for CS 396 Artificial Life

It is heavily based on the ludobots MOOC, particularly the parallel hill climber, on https://www.reddit.com/r/ludobots/ created by Professor Josh Bongard

Code from Professor Bongard's pyrosim, at the link https://github.com/jbongard/pyrosim, was also used

Credit to Raed Mughaus on StackExchange for helping to write the mathplotlib confidence interval grapher code, https://stackoverflow.com/a/70949996


## Description
   This is a parallel hill climber simulator designed to move as far as possible in the positive x-axis
   
   Trailer Video: https://youtu.be/uiFjitC-cHE
   
   Two Minute Full Video: https://youtu.be/JKTDE07n8ak


### Scientific Method:
   After doing all of our assignments I realized even though the bodies are all evolving throughout our generations, what about the brains? Surely there must be a better way to evolve brains, more akin to how humans evolved, through building or removing synapses? This then led me to my hypothesis...
    
   Hypothesis: Having synapses be able to evolve alongside bodies improves locomotion distance for my parallel hill climber, with multiple synaptic pairings between motors and sensors further improving locomotion distance

   To test this I ran 500 Generations of 10 robots per population, with 5 different random seeds, for each of these 4 scenarios

   NO EVOLUTION SYNAPSES(CONTROL):
   
        Scenario 1: Every sensor to every motor, immutable connections except for sensor/motor addition or deletion
        
        Scenario 2: One sensor to one motor if possible, from the first sensor and motor added to minimize mutation impact, immutable pairings not changed by mutation, unless a sensor or motor is deleted physically

   EVOLVED SYNAPSES:
   
        Scenario 3: Sensors can only connect to one motor and vice versa, flexible pairings
        
        Scenario 4: Sensors that can connect to multiple motors, flexible pairings
        
   Here is a diagram of the hypothetical neural makeups of each of these scenarios:
   ![imgonline-com-ua-twotoone-jC7ss93zwG6hVZCr](https://user-images.githubusercontent.com/23564433/225202408-7f8b6e89-b9d5-4ae3-8ae3-a522e80facb9.jpg)
![imgonline-com-ua-twotoone-6PD5Zjgq0BX](https://user-images.githubusercontent.com/23564433/225202515-50cc17f9-a3e5-4dce-951b-111fe940906f.jpg)



   Accounting for Evolution in Shape:
   
      Limited # of blocks for both, 1.5 * the starting length, which is randomly decided between 6-12 for all robots
        
      Sensor Likelihoods are equal in both control and evolution
        
      Run several times with different random seeds, to see if evolution takes truly different path

   Accounting for Synaptic Weights:
   
        Weights are randomly decided at start (either -1 or 1) and can not be changed through mutation, evolution does not affect synaptic weights except when a sensor or motor is added/removed

### Observations and Conclusion
   Observations:
   What I observed was rather different than what I expected for the most part. While the Control scenario with one sensor for each motor did end up performing much worse than the other three, as I expected, the Control with every sensor connected to every motor performing the best on average was quite a suprise. I was also suprised to find that there wasnt a large difference in the averages for the two Hypothesis Scenarios, with them performing approximately equally.

   Graphs of the four scenarios best fitness charts, seperate and then combined:
   
   ![control all](https://user-images.githubusercontent.com/23564433/225202824-443ef9e5-dd52-4c3d-8456-170a75cbd14e.png)
   ![control one](https://user-images.githubusercontent.com/23564433/225202822-c7a79e4a-c38e-4839-a3e3-38cd26313cf2.png)
   ![hyp one](https://user-images.githubusercontent.com/23564433/225202819-8e03dd7b-87c0-4526-aa7c-a1499d22fb90.png)
   ![hyp mult](https://user-images.githubusercontent.com/23564433/225202817-dc765c1f-c9f2-4c10-877d-efe6aff9b1a4.png)
   ![all sims](https://user-images.githubusercontent.com/23564433/225202776-ee962e82-a2fa-486e-86c1-cee11e5b0546.png)

   The confidence interval:
   
   ![CI FIGURE](https://user-images.githubusercontent.com/23564433/225202917-b968e83f-93ee-4bb7-b8ac-9e165fae1b1a.png)


   One thing I noticed from observing the simulations in action, was that many of the final robots optimized to essentially vibrate their way across the world, with small rapid movements, something which I believe takes more actuating motors than actual leg movement. I believe that evolution incentivizes robots to develop so that many motors are making constant rapid small movements, something that the control scenario with all synapses connected provides, due to its maximal sensor to motor input relative to the others
   
   Here is a gif of this behavior in action:
   ![Screen Recording 2023-03-14 at 11 42 30 PM](https://user-images.githubusercontent.com/23564433/225209516-8aba6e07-8b50-4091-a5ac-1e15140c6a15.gif)

   
   Some potential solutions to this could be to increase the values of synaptic weights possible, to evolutionarily disincentivize robots that exhibit this kind of movement, or to perhaps increase the range of motor movement.


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

![jumper side by side](https://user-images.githubusercontent.com/23564433/225201038-0d36e063-e4e0-4a64-a154-50987365185e.jpeg)

   Brain: See the above Hypothesis section for a diagram of how the brains are created/evolved depending on the scenario 

   Fitness: 
      The fitness of the robots is decided by a simple check of the final x coordinate position of the robots base block at the end of its lifespan, a larger fitness is considered better, incentivizing movement along the positive x axis

   Evolution: 
      The system handles evolution through the parallelhillclimber.py class created as a part of Ludobots, albeit with a few modifications. It pickles in a folder the new best fitness, whenever a fitness score beats the previous recordholder. The parallelhillclibmer.py class in general works through running a Solution.py file, which is responsible for creating bodies and brains, for each member of the population. It then runs a simulation for each of these Solution classes and afterwards copies them to create children. These children are then mutated through Solution.py's Mutate() function and then run a simulation of their own. Afterwards, they are compared to their parents by their fitness scores and if theirs are greater, they replace their parents for the next cycle of the parallel hill climber. This is done until the number of generations is reached and then at the end, the robot with the best fitness is pickled. 
      
      Here are diagrams conveying how this functions:
      
![newparallel](https://user-images.githubusercontent.com/23564433/225207593-11417592-b8bb-41b2-a54b-c482fba1018f.png)

![imgonline-com-ua-twotoone-1jfPedzmbb](https://user-images.githubusercontent.com/23564433/225207732-af8c00ad-dbd2-4902-a9ff-365cbd16dae6.jpg)


   Mutation: 
   Mutations are handled by a call to the Mutate() function inside of each Solution Class(the class for each robot) 
        
        In the mutate function there is a:
        
            40% chance that a blocks size and connection directions are randomly changed
            
            40% chance that the number of blocks is either increased or decreased by 1, so 20% chance each
            
            20% chance that the number of blocks is increased or decreased by 2, 10% chance each
        
   Furthermore, for scenarios in which the brain is allowed to evolve, there is a seperate and independent:
            
            20% chance that a sensor motor pairing is removed 
            
            20% chance that a sensor motor pairing is added, if one exists that does not violate the conditions of the scenario

   Here is a diagram of such mutations:
   
      In this scenario, the 20% chance to remove a link has transpired
      
      Parent Generation:
  
  ![jumper blueprint](https://user-images.githubusercontent.com/23564433/225207901-34dea606-b536-4748-a8e8-bc4e06c62c51.png)

      Child Generation:
  ![jumper final](https://user-images.githubusercontent.com/23564433/225208056-1ac64b2c-abf0-4dba-a8b5-b18bf0168e46.png)


   For the hypothesis, where brains can evolve:
   
      Parent Generation
   ![parentgen mutated brains](https://user-images.githubusercontent.com/23564433/225204241-42e0403d-3da3-4ff8-b1ed-03586fc56914.png)
   
      Child Generation
![childgeneration mutated brains](https://user-images.githubusercontent.com/23564433/225204262-fbaca871-6d17-4d8a-a1fa-8ad1d69c1b40.png)

            

   Environment: The environment is a simple plain flat world with a floor without any defining characteristics. Creatures face no obstacles in movement.



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
    
        
    
    
    
    

