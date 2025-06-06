import plotly.graph_objects as go

def create_saboteur_bar_chart(labels=None, values=None, title="SABOTEURS"):
    if labels is None:
        labels = ["Restless", "Hyper-Rational", "Stickler",
                  "Controller", "Hyper-Achiever", "Avoider",
                  "Hyper-Vigilant", "Victim", "Pleaser"]
    if values is None:
        values = [10, 10, 9.4, 8.8, 8.1, 5.6, 4.4, 1.3, 1.3]

    fig = go.Figure(data=[
        go.Bar(
            x=labels,
            y=values,
            marker_color='lightblue',
            marker_line_width=1,
            marker_line_color='gray',
            width=0.6
        )
    ])

    fig.update_layout(
        title=title,
        title_font_size=20,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Arial", size=14, color="gray"),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            tickangle=-30
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='lightgray',
            title="Score"
        ),
        margin=dict(l=40, r=20, t=60, b=80),
        height=500,
        width=800
    )

    return fig