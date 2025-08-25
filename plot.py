import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('penguins.csv')  # error

sns.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g', hue='species')
plt.title('Flipper vs Mass')
plt.savefig('figures/fig-NEW.png')
