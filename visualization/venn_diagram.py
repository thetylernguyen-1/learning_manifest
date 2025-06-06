import matplotlib.pyplot as plt
from matplotlib_venn import venn2

def create_who_how_venn():
    fig, ax = plt.subplots()
    venn = venn2(
        subsets=(4, 4, 2),
        set_labels=("WHO", "HOW")
    )
    
    ax.set_title("Venn Diagram: Bridging WHO and HOW in Learning", fontsize=14)
    
    venn.get_label_by_id('10').set_text("Intentional\nC-quadrant\npractice")
    venn.get_label_by_id('01').set_text("- active listening\n- reflective journaling\n- feedback\n- peer coaching")
    venn.get_label_by_id('11').set_text("Bridging\nthe gaps")
    
    return fig