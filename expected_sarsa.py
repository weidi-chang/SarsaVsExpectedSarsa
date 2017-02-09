import numpy as np

def expected_sarsa(mdp, max_episode, alpha = 0.1, gamma = 0.9):
    # Initialization
    Q = [[0.0 for i in range(mdp.A)] for j in range(mdp.S)]
    old_Q = Q
    n_episode = 0
    epsilon = 0.1
    total_reward = 0
    while n_episode < max_episode: # TODO: Pick a finish condition for episode
        s = 0 # Initialize s, starting state

        # With prob epsilon, pick a random action
        if np.random.random_sample() <= epsilon:
            a = np.random.random_integers(0, mdp.A-1)
        else:
            a = np.argmax(Q[s][:])
        r = 0
        while not mdp.is_terminal(s): # TODO: Finish episode/trajectory on terminal state
            # Observe S and R
            s_new = np.argmax(mdp.T[s, a, :]) # TODO: Change to stochastic ?
            r = mdp.R[s_new]
            T_new = np.zeros((mdp.S, mdp.S))

            # Pick new action A' from S'
            if np.random.random_sample() <= epsilon:
                a_new = np.random.random_integers(0, mdp.A-1)
            else:
                a_new = np.argmax(Q[s_new][:])

            best_action = np.argmax(Q[s_new][:])
            Q[s][a] = Q[s][a] + alpha*(r + gamma*((1-epsilon)*Q[s_new][best_action]+(epsilon/mdp.A)*sum(Q[s_new][act] for act in range(mdp.A))) - Q[s][a])

            s = s_new
            a = a_new
            total_reward += r

        n_episode += 1
    return Q, total_reward/max_episode