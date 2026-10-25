import plotly.express as px

students = ["S1", "S2", "S3", "S4", "S5",
            "S6", "S7", "S8", "S9", "S10"]

marks = [78, 85, 67, 90, 73, 81, 69, 94, 76, 88]

fig = px.bar(
    x=students,
    y=marks,
    labels={"x": "Students", "y": "Mathematics Marks"},
    title="Students' Mathematics Marks"
)

fig.show()