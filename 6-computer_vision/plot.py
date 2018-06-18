from motion_detector import data_frame
from bokeh.plotting import figure,show,output_file

p=(figure(x_axis_type="datetime",height=100,width=100,title="Motion Detection"))

q=p.quad(left=data_frame["Start"],right=data_frame["End"],bottom=0,top=1,color="green")

output_file("detection_graph.html")
show(p)
