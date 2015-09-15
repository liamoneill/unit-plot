# unit-plot
Simple GUI to manage functions which create graphs using matplotlib.

This is my first python project. I created it to help making graphs through matplotlib. This program is useful for experiments which output graphs as the GUI provides the user with the choice of which graphs to generate, avoiding unnecessary rerunning of time intensive experiments.

The instantiation of matplotlib and the saving of the graphs is separated from the code creating the graphs. To achieve this, functions which configure a graph should be decorated by @graph from the unitplot module. A figure object will be injected into the function when it’s invoked, this object will be saved to a pdf file on disk automatically. A simple GUI exists to allow the user to choose which functions to run. It also displays the amount of time it took to render a graph.
