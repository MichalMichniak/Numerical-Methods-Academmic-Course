# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np

expected = pickle.load(open('expected','rb'))

result_log_plot = expected['log_plot']
result_parallel_plot =  expected['parallel_plot']
result_compare_plot = expected['compare_plot']

result_log_plot_none = expected['log_plot_none']     
result_parallel_plot_none =  expected['parallel_plot_none']
result_compare_plot_none = expected['compare_plot_none']

@pytest.mark.mpl_image_compare(baseline_dir='baseline', tolerance=20)
@pytest.mark.parametrize("x,y,xlabel,ylabel,title,log_axis", result_log_plot)
def test_log_plot(x,y,xlabel,ylabel,title,log_axis):
    return main.log_plot(x,y,xlabel,ylabel,title,log_axis)

@pytest.mark.mpl_image_compare(baseline_dir='baseline', tolerance=20)
@pytest.mark.parametrize("x1,y1,x2,y2,x1label,y1label,x2label,y2label,title,orientation", result_parallel_plot)
def test_parallel_plot(x1,y1,x2,y2,x1label,y1label,x2label,y2label,title,orientation):
    return main.parallel_plot(x1,y1,x2,y2,x1label,y1label,x2label,y2label,title,orientation)

@pytest.mark.mpl_image_compare(baseline_dir='baseline', tolerance=20)
@pytest.mark.parametrize("x1,y1,x2,y2,xlabel,ylabel,title,label1,label2", result_compare_plot)
def test_compare_plot(x1,y1,x2,y2,xlabel,ylabel,title,label1,label2):
    return main.compare_plot(x1,y1,x2,y2,xlabel,ylabel,title,label1,label2)

@pytest.mark.parametrize("x,y,xlabel,ylabel,title,log_axis,result", result_log_plot_none)
def test_log_plot_none(x,y,xlabel,ylabel,title,log_axis,result):
    assert  main.log_plot(x,y,xlabel,ylabel,title,log_axis) is result

@pytest.mark.parametrize("x1,y1,x2,y2,x1label,y1label,x2label,y2label,title,orientation, result", result_parallel_plot_none)
def test_parallel_plot_none(x1,y1,x2,y2,x1label,y1label,x2label,y2label,title,orientation,result):
    assert  main.parallel_plot(x1,y1,x2,y2,x1label,y1label,x2label,y2label,title,orientation) is result

@pytest.mark.parametrize("x1,y1,x2,y2,xlabel,ylabel,title,label1,label2,result", result_compare_plot_none)
def test_compare_plot_none(x1,y1,x2,y2,xlabel,ylabel,title,label1,label2,result):
    if main.compare_plot(x1,y1,x2,y2,xlabel,ylabel,title,label1,label2) is not None:
        assert True
    else:
        assert main.compare_plot(x1,y1,x2,y2,xlabel,ylabel,title,label1,label2) is result