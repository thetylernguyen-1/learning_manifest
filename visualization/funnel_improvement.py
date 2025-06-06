from plotly import graph_objects as go

def create_leadership_funnel_chart(y=None, x=None):
    if y is None:
        y = ['Vision', 'Integrity', 'Influence', 'Accountability', 'Decision-Making']
    if x is None:
        x = [40, 20, 20, 10, 10]
    
    soft_colors = ["#badcf9", "#ccf0bf", "#d5c9a5", "#efc497", "#eb9e4b"]

    fig = go.Figure(go.Funnel(
        y=y,
        x=x,
        textinfo="value+percent previous",
        marker=dict(color = soft_colors)
    ))

    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(l=40, r=40, t=60, b=40),
        height=500,
         yaxis=dict(
        tickfont=dict(family="Arial Black", size=14, color="black")
    ),
        width=700
    )

    return fig