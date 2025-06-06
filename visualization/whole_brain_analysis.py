import plotly.graph_objects as go

def create_quadrant_pie_chart(labels=None, values=None):
    if labels is None:
        labels = ['A-quadrant', 'B-quadrant', 'C-quadrant', 'D-quadrant']
    if values is None:
        values = [40, 30, 20, 10]

    colors = ["#90adc5", "#c1ddb6", "#c9be9b", "#dfc5a9"]

    fig = go.Figure(data=[
        go.Pie(labels=labels, values=values, hole=0.3, marker=dict(colors=colors))
    ])

    fig.update_layout(
        height=500,
        width=500
    )

    return fig