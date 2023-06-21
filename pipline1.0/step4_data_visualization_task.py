import os
import argparse
import sys
sys.path.append(
    os.path.dirname(
         os.path.dirname(
             os.path.abspath(__file__)
         )
    )
)
import logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(os.path.basename(__file__))
from typing import Any
from pyecharts.charts import Bar, Calendar, Funnel, Line, Page, Tab, Timeline
from pyecharts.charts.three_axis_charts.surface3D import Surface3D
from pyecharts.charts.three_axis_charts.bar3D import Bar3D
from pyecharts import options as opts
from pyecharts.render import make_snapshot
# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/npm/echarts@latest/dist/"


class echarts(object):
    
    def __init__(self, data) -> None:
        self.data = data

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.case()

    '''***************************TODO:2D region***************************'''

    def line(self):
        line = (
            Line()
            .add_xaxis(["A", "B", "C", "D", "E"])
            .add_yaxis("Series 2", [5, 4, 3, 2, 1])
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="line",
                    pos_left="center",
                ),
                legend_opts=opts.LegendOpts(
                    is_show=False,
                )
            )
        )
        return line
    
    def bar(self):
        bar = (
            Bar()
            .add_xaxis(["A", "B", "C", "D", "E"])
            .add_yaxis("Series 1", [1, 3, 2, 5, 4])
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="bar",
                    pos_left="center",
                ),
                legend_opts=opts.LegendOpts(
                    is_show=False,
                )
            )
        )
        return bar
    
    def funnel(self):
        funnel = (
            Funnel()
            .add(
                series_name="funnel",
                data_pair=self.data,
                color="red",
                gap=2,
                label_opts=opts.LabelOpts(
                    is_show=False,
                    font_size=14,
                )
            )
            .set_global_opts(
                legend_opts=opts.LegendOpts(
                    is_show=False,
                    border_width=2,
                    border_color="black",
                    border_radius=2,
                    orient="horizontal", 
                    pos_bottom=0,
                ),
                title_opts=opts.TitleOpts(
                    title="funnel",
                    pos_left="center",
                    title_textstyle_opts=opts.TextStyleOpts(
                        font_size=30,
                        color="red",
                        border_color="black",
                        border_radius=2,
                        border_width=2,
                    )
                ),
                visualmap_opts=opts.VisualMapOpts(
                    max_=max([i[1] for i in self.data]), 
                    min_=0, 
                    orient="horizontal",
                    pos_bottom=0,
                    pos_left=0,
                )
            )
        )
        return funnel

    def calendar(self):
        calendar = (
            Calendar()
            .add(
                series_name="日历图",
                yaxis_data=self.data,
                calendar_opts=opts.CalendarOpts(
                    range_=[sorted([i[0] for i in self.data])[0], sorted([i[0] for i in self.data])[-1]],
                    pos_top="30%",
                    cell_size=[15, 20]
                ),
            )
            .set_global_opts(
                legend_opts=opts.LegendOpts(
                    is_show=False,
                ),
                title_opts=opts.TitleOpts(
                    title="calendar",
                    pos_left="center",
                    padding=10,
                    title_textstyle_opts=opts.TextStyleOpts(
                        font_size=35,
                        color="red",
                    )
                ),
                visualmap_opts=opts.VisualMapOpts(
                    max_=max([i[1] for i in self.data]), 
                    min_=0, 
                    orient="horizontal", 
                    pos_bottom=0,
                    pos_left=0,
                ),
            )
        )
        return calendar

    '''***************************TODO:3D region***************************'''

    def surface3D(self):
        data = []
        for i in range(-10, 11):
            for j in range(-10, 11):
                x = i
                y = j
                z = i ** 2 + j ** 2
                data.append([x, y, z])
        surface3D = (
            Surface3D(
                init_opts=opts.InitOpts(
                    width="auto"
                )
            )
            .add(
                "",
                data=data,
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="Surface3D chart",
                    pos_left="center",
                    title_textstyle_opts=opts.TextStyleOpts(
                        font_size=30,
                        color="red",
                    )
                )
            )
        )
        return surface3D

    '''***************************TODO:Multi Graph***************************'''

    #TAB multiple chart
    def tab(self):
        tab = (
            Tab()
            .add(self.calendar(), 'calendar')
            .add(self.bar(), 'bar')
            .add(self.line(), 'line')
            .add(self.funnel(), 'funnel')
            .add(self.surface3D(), 'surface3D')
        )
        tab.render()

    #Sequential multigraph
    def page(self):
        page = Page(
            layout=Page.DraggablePageLayout,
        )
        page.add(
            self.funnel(),
            self.bar(), 
            self.line(), 
            self.calendar(), 
            self.surface3D(),
        )
        page.width = "auto"
        page.height = "auto"
        page.render()

    def time_line(self):
        timeline = (
            Timeline(
                init_opts=opts.InitOpts(
                    width="auto"
                )
            )
            .add(self.bar(), 'bar')
            .add(self.line(), 'line')
            .add(self.funnel(), 'funnel')
            .add(self.calendar(), 'calendar')
            .add_schema(
                symbol="circle",
                is_auto_play=True,
                is_loop_play=True,
            )
        )
        timeline.render()

    #save to png
    def make_snapshot(self):
        make_snapshot(snapshot, self.calendar().render(), "calendar.png")

    #test case
    def case(self):
        line = (
            Line(
                init_opts=opts.InitOpts(
                    width="100%",
                )
            )
            .add_xaxis(["A", "B", "C", "D", "E"])
            .add_yaxis("Series 2", [5, 4, 3, 2, 1])
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    pos_left="center",
                ),
                legend_opts=opts.LegendOpts(
                    is_show=False,
                )
            )
        )
        line.render()
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate video for current pipline")
    parser.add_argument("--data_path", default="C:/Users/weidong.he/Desktop/1/bigsize_V2", help="img location original path")
    parser.add_argument("--save_path", default="C:/Users/weidong.he/Desktop", help="video location save path")
    args = parser.parse_args()
    data = [
        ("2023-01-01", 100),
        ("2023-02-01", 200),
        ("2023-02-10", 900),
        ("2023-03-15", 300),
        ("2023-04-15", 400),
        ("2023-05-15", 500),
    ]
    echart = echarts(data)
    echart.time_line()