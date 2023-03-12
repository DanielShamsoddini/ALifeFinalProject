#CS396 Artificial Life Final Project

Scientific Method:
    hypothesis: having synapses evolve, and further allowing them to connect to multiple motors improves locomotion evolution, potentially even playing a role in the shape evolution

    sensors can evolve synaptic connections as random


    NO EVOLUTION SYNAPSES(CONTROL):
        Scenario 1: every sensor to every motor, immutable
        Scenario 2: one sensor to one motor, immutable pairings not changed by mutation

    EVOLVED SYNAPSES:
        Scenario 1: Sensors that can connect to multiple motors, flexible pairings
        Scenario 2: Sensors can only connect to one motor, flexible pairings


    Accounting for Evolution in Shape:
        Limit # of blocks for both
        Limit # of motors for both
        Sensor Likelihoods are equal in both control and evolution, also set a potential cap on # of sensors per bot in both
        Run several times, to see if evolution takes truly different path

    Accounting for Synaptic Weights:
        Either fixed weight for synapses or random discrete weight numbers from a list, ex. (-1,-0.5,0.5,1)
            Fixed Weight of 1 in both control and evolved

Technical Specifications:

    Program: Uses python library multiprocessing to improve performance for parallel

    Fitness:

    Mutation:




