from excelbird import *
red, green, orange = colors.theme.red3, colors.theme.green3, colors.theme.orange3


Book(
    Sheet(
        Stack(
            VFrame(
                Row(1,2,3,4),
                Row(1, Gap(2)),
                Row(1,2),
                fill_empty=True,
                fill_color=orange,
                background_color=red,
            ),
            VFrame(
                Row(1,2,3),
                Row(1, Gap(6)),
                Row(1,2),
                background_color=green,
            ),
        )
    ),
    auto_open=True,
).write("/Users/Ryan.Young3/Desktop/test.xlsx")


quit()

Book(
    Sheet(
        VStack(
            Stack(
                Frame(Col(1,2,Gap(), 3), Gap(), Col(4,5,6, header='hi'), border=True, fill_empty=True, background_color=False),
                # margin=2,
                # padding_top=1,
                padding=2,
                # background_color=green,
                # margin=1,
                id='main',
            ),
            Gap(1),
            # Expr("[main].ref(inherit_style=True)"),
            background_color=colors.mono.gray1,
            padding=1,
        ),
        end_gap=dict(col_width=4),
        center=True,
        # background_color=colors.mono.white,
    ),
    auto_open=True,
    zoom=250,
).write("/Users/Ryan.Young3/Desktop/test.xlsx")

"""
Give all layout elements below Stack a background_color attribute and resolve background_color
"""
