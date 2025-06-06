import plotly.graph_objects as go

def create_who_how_venn():
    labels = {
        "A": "WHO",
        "B": "HOW",
        "A & B": "Bridging the Gaps"
    }

    values = [4, 4, 2]

    region_text = [
        "Intentional\nC-quadrant\npractice",
        "- active listening\n- reflective journaling\n- feedback\n- peer coaching",
        "Bridging\nthe gaps"
    ]

    fig = go.Figure(data=go.Venn(
        labels=labels,
        values=values,
        text=region_text,
        textposition="middle center"
    ))

    fig.update_layout(
        title_text="Venn Diagram: Bridging WHO and HOW in Learning",
        height=600,
        width=800
    )

    return fig