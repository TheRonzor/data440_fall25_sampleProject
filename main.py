from src.analysis import make_data, save_data, load_data
from src.viz import make_figure

data = make_data()
make_figure(data, 'test.svg')
