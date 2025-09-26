import unittest
import pandas as pd
from sea_level_predictor import draw_plot

class SeaLevelPredictorTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = draw_plot()
        self.lines = self.ax.get_lines()

    def test_plot_title(self):
        self.assertEqual(self.ax.get_title(), "Rise in Sea Level", "Title should be 'Rise in Sea Level'")

    def test_plot_x_label(self):
        self.assertEqual(self.ax.get_xlabel(), "Year", "x-axis label should be 'Year'")

    def test_plot_y_label(self):
        self.assertEqual(self.ax.get_ylabel(), "Sea Level (inches)", "y-axis label should be 'Sea Level (inches)'")

    def test_prediction_line_1_goes_to_2050(self):
        x_data = self.lines[0].get_xdata()
        self.assertEqual(x_data[-1], 2050, "First prediction line should extend to the year 2050.")

    def test_prediction_line_2_goes_to_2050(self):
        x_data = self.lines[1].get_xdata()
        self.assertEqual(x_data[-1], 2050, "Second prediction line should extend to the year 2050.")

if __name__ == "__main__":
    unittest.main()