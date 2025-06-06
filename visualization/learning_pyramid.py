import plotly.graph_objects as go

def create_capability_pyramid():
    fig = go.Figure()

    # Define background pyramid blocks (grid cells)
    for i in range(3):  # rows
        for j in range(5):  # columns
            x0, x1 = j, j + 1
            y0, y1 = i, i + 1
            is_active_cell = (j, i) in [(2, 0), (2, 1)]
            fig.add_shape(
                type="rect",
                x0=x0, x1=x1, y0=y0, y1=y1,
                line=dict(color="lightgray", width=1),
                fillcolor="#f9f9f9" if not is_active_cell else "#d6eaf8"
            )

    # Pyramid outline
    fig.add_shape(
        type="path",
        path="M 0 0 L 2.5 3 L 5 0 Z",
        line=dict(color="black", width=2),
        fillcolor='rgba(0,0,0,0)'
    )

    # Numbered learning blocks with soft pastel fill
    pastel_fill = "#a2c4c9"  # soft teal
    number_positions = {
        "1": (2, 1),
        "2": (1, 1),
        "3": (4, 0),
        "4": (0, 0),
        "5": (2, 2)
    }

    for num, (x, y) in number_positions.items():
        fig.add_shape(
            type="rect",
            x0=x + 0.2, x1=x + 0.8,
            y0=y + 0.2, y1=y + 0.8,
            fillcolor=pastel_fill,
            line=dict(color="black", width=1)
        )
        fig.add_annotation(
            x=x + 0.5, y=y + 0.5,
            text=num,
            showarrow=False,
            font=dict(size=20, color="black", family="Arial")
        )

    # Bottom labels
    labels = ["ACCOUNTABILITY", "DECISION-MAKING", "VISION", "INTEGRITY", "INFLUENCE"]
    for i, label in enumerate(labels):
     fig.add_annotation(
        x=i + 0.5,
        y=-0.25,
        text=f"<b>{label}</b>",
        showarrow=False,
        font=dict(size=15, color=" dimgrey", family="Arial"),
        textangle=0
    )

    # Legend entry for soft learning boxes
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=15, color=pastel_fill),
        name="Learning Journey (most important to least)"
    ))

    # Layout updates
    fig.update_layout(
        showlegend=True,
        legend=dict(
            x=0.7,
            y=1,
            bgcolor='rgba(255,255,255,0)',
            bordercolor='lightgray'
        ),
        xaxis=dict(range=[0, 5], showticklabels=False, showgrid=False, zeroline=False),
        yaxis=dict(range=[-0.5, 3.5], showticklabels=False, showgrid=False, zeroline=False),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=600,
        width=800,
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig