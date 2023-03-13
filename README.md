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
        Sensor Likelihoods are equal in both control and evolution, cap # of sensors
        Run several times, to see if evolution takes truly different path

    Accounting for Synaptic Weights:
        Weights are randomly decided at start and can not be changed through mutation, evolution does not affect synaptic weights

Technical Specifications:

    Program: Uses python library multiprocessing to improve performance for parallel

    Fitness:

    Mutation:




