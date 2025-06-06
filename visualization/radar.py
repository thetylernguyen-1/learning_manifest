import plotly.graph_objects as go

def create_radar_chart(categories, current_values, desired_values, title):
    fig = go.Figure()

    # Current state
    fig.add_trace(go.Scatterpolar(
        r=current_values,
        theta=categories,
        fill='toself',
        name='Current Vision',
        line=dict(color='rgba(135, 206, 250, 1)')  # soft blue
    ))

    # Desired state
    fig.add_trace(go.Scatterpolar(
        r=desired_values,
        theta=categories,
        fill='toself',
        name='Desired Vision',
        line=dict(color='rgba(255, 192, 203, 1)')  # soft pink
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 10])
        ),
        showlegend=True,
        height=500,
        width=500,
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    return fig