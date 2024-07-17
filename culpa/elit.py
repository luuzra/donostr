import numpy as np
import scipy.stats as stats

def parse_normal_distribution(params):
    try:
        mean = params.get('mean', 0)
        stddev = params.get('stddev', 1)
        
        if stddev <= 0:
            raise ValueError("Standard deviation must be positive")
        
        distribution = stats.norm(loc=mean, scale=stddev)
        return distribution
    except Exception as e:
        print(f"Error parsing normal distribution parameters: {e}")
        return None

# Example usage
params = {
    'mean': 10,
    'stddev': 2
}

normal_dist = parse_normal_distribution(params)

if normal_dist:
    print("Distribution created successfully")
    print(f"Mean: {normal_dist.mean()}, StdDev: {normal_dist.std()}")
    samples = normal_dist.rvs(size=10)
    print("Random samples:", samples)
else:
    print("Failed to create distribution")
