from matplotlib import rc
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

__DIR = './'

registry = {}

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

def graph(fname):
	fname = (fname if fname.endswith('.pdf') else fname + '.pdf')
	def wrapper(func):
		def new_func():
			print('Running function %s' % func.__name__)
			fig = Figure()
			canvas = FigureCanvas(fig)
			func(fig)
			print('Saving graph: %s' % fname)
			__save(fig, fname)
		registry[func.__name__] = new_func
		return new_func
	return wrapper

def __save(graph, fname):
	path = (__DIR if __DIR.endswith('/') else __DIR + '/') + fname
	graph.savefig(path, format='pdf')