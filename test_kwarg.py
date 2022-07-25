
def kw_arg(**kwargs):
    color = kwargs["color"]
    xy = kwargs["xy"]
    print(xy, color)

kw_arg(xy=[0,0],color="red")