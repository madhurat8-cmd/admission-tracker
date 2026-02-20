import gradio as gr

INTAKE = 60

branches = {
    "Computer Engineering": 0,
    "Computer Science and Engineering": 0,
    "Information Technology": 0,
    "CSE (AIML)": 0
}

def format_display():
    output = "# 🎓 Real-Time Admission Tracker\n"
    output += "### Sanctioned Intake per Branch: 60 Students\n\n"

    for branch, admitted in branches.items():
        percent = (admitted / INTAKE) * 100
        output += f"""
## {branch}
Admitted: **{admitted} / {INTAKE}**

Progress: {percent:.1f}%  
{'🟩' * int(percent // 5)}{'⬜' * (20 - int(percent // 5))}

---
"""
    return output

def add_seat(branch):
    if branches[branch] < INTAKE:
        branches[branch] += 1
    return format_display()

def cancel_seat(branch):
    if branches[branch] > 0:
        branches[branch] -= 1
    return format_display()

with gr.Blocks(theme=gr.themes.Soft()) as app:
    display = gr.Markdown(format_display())

    branch_selector = gr.Dropdown(
        list(branches.keys()), 
        label="Select Branch"
    )

    with gr.Row():
        add_btn = gr.Button("➕ Add Seat", variant="primary")
        cancel_btn = gr.Button("❌ Cancel Seat", variant="stop")

    add_btn.click(add_seat, inputs=branch_selector, outputs=display)
    cancel_btn.click(cancel_seat, inputs=branch_selector, outputs=display)

app.launch()
