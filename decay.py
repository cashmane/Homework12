import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    Bi = 10000 #number of Bi213 atoms initially
    timestep = 1 #second
    tmax = 20000 #max time to calculate
    tau_Bi = 46*60 #Bi213 half life in seconds
    tau_Tl = 2.2*60 #Tl half life in seconds
    tau_Pb = 3.3*60 #Pb half life in seconds
    Tl = 0 #initial number of Tl atoms
    Pb = 0 #initial number of Pb atoms
    Bi_final = 0 #initial number of Bi209 atoms
    p_Bi_decay = 1-2**(-timestep/tau_Bi) #probability of decay for Bi213 in one second
    p_Tl_decay = 1-2**(-timestep/tau_Tl) #probability of decay for Tl in one second
    p_Pb_decay = 1-2**(-timestep/tau_Pb) #probability of decay for Pb in one second

    ts = np.arange(0, tmax, timestep)
    
    #initialize lists to keep track of the number of atoms of each type for each timestep
    BiList = []
    TlList = []
    PbList = []
    BiFinalList = []
    
    #Loop which calculates how many atoms decay, and adds them to appropriate counts
    for t in ts:
        BiList.append(Bi)
        TlList.append(Tl)
        PbList.append(Pb)
        BiFinalList.append(Bi_final)
        for i in range(Bi):
            if np.random.random() < p_Bi_decay:
                if np.random.random() < .0209:
                    Bi -= 1
                    Tl += 1
                else:
                    Bi -= 1
                    Pb += 1
        for i in range(Tl):
            if np.random.random() < p_Tl_decay:
                Tl -= 1
                Pb += 1
        for i in range(Pb):
            if np.random.random() < p_Pb_decay:
                Bi_final += 1
                Pb -= 1

    #plot the results, with time on x axis and number of atoms on y axis
    plt.scatter(ts, BiList, color='blue', label='Bi213', marker='.', s=0.5)
    plt.scatter(ts, TlList, color='red', label='Tl209', marker='.', s=0.5)
    plt.scatter(ts, PbList, color='green', label='PB209', marker='.', s=0.5)
    plt.scatter(ts, BiFinalList, color='magenta', label='Bi209', marker='.', s=0.5)
    plt.xlabel('Time [s]')
    plt.ylabel('Number of Atoms')
    plt.yscale('log')
    plt.title('Decay of Bi213 Over Time')
    #plt.xscale('log')
    plt.legend()
    plt.show()
                
            
        
        
    
