import numpy as np

def main():
    print(gaussian_distribution(1, 1, 10))

def gaussian_distribution(x, mean, sigma):
    
    # TODO
    gd = (1/(sigma*np.sqrt(2*np.pi))) * (np.exp(-(x-mean)**2/(2*sigma**2)))
    return gd

if __name__ == "__main__":
    main()