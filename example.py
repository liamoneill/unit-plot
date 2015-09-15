import time
import numpy as np
import unitplot as up

@up.graph('graph_1')
def graph_1(fig):
	t = np.arange(0.0, 1.0 + 0.01, 0.01)
	s = np.cos(4 * np.pi * t) + 2

	ax = fig.add_subplot(111)
	ax.plot(t, s)

	ax.set_xlabel(r'\textbf{time} (s)')
	ax.set_ylabel(r'\textit{voltage} (mV)',fontsize=16)
	ax.set_title(r"\TeX\ is Number "
		      r"$\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!",
				fontsize=16, color='gray')

	# Make room for the ridiculously large title.
	fig.subplots_adjust(top=0.8)


@up.graph('graph_2')
def graph_2(graph):
	x = np.linspace(0, 10, 1000)
	y1 = np.sin(x)
	y2 = np.cos(x)
	ax1 = graph.add_subplot(111)
	#ax2 = graph.add_subplot(111)
	ax1.plot(x, y1)
	ax1.plot(x, y2)
