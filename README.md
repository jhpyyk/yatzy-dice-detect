# yatzy-dice-detect

**Work in progress**.

A quick project to test training a YOLOv5 model with a custom dataset. Detects Yatzy dice rolls and calculates the probabilities of getting each set after the remaining rolls. A video showcasing the application:

<iframe width="560" height="315" src="https://www.youtube.com/embed/RzZcJA58j4Y" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The probabilities are calculated using Markov chains. The application makes some assumptions on what dice will be selected to re-roll. A very helpful paper about the subject is found at: https://issuu.com/milliemince/docs/using_markov_chains_and_probabilistic_modeling_to_

The dataset used to train the model is 33 pictures taken by the author. Roboflow was used to annotate the data and to generate a larger augmented dataset with rotated pictures and different brightnesses. The model was then trained for 300 epochs in Google Colab. The detection confidence is about 0.88 on average.

Link to the dataset: https://universe.roboflow.com/juuso-pyykknen/dice-detect2

**NOTE**: This is for *Yatzy* and not *Yahtzee*. They are very similar but there are some differences in the rules.

**TODO**: Calculate Full House probabilities, make UI prettier.