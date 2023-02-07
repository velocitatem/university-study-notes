import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
mu = 106
variance = 244
sigma = np.sqrt(variance)
og_population = {
    80: 0.2,
    100: 0.3,
    120: 0.5
}
samples = np.arange(10, 110, 30)
fig, axes = plt.subplots(1, len(samples), figsize=(15, 5))
for sampleSize in samples:
    sample_means = []
    for i in range(1000):
        sample = np.random.choice(list(og_population.keys()), size=sampleSize, p=list(og_population.values()))
        sample_mean = np.mean(sample)
        sample_means.append(sample_mean)
    sns.distplot(sample_means, ax=axes[samples.tolist().index(sampleSize)])
    axes[samples.tolist().index(sampleSize)].set_title('Sample Size: {}'.format(sampleSize))
    axes[samples.tolist().index(sampleSize)].set_xlabel('Sample Mean')
    axes[samples.tolist().index(sampleSize)].set_ylabel('Probability')
plt.show()
