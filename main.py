import flet as ft
import pyqrcode
import base64
from io import BytesIO


def main(page: ft.Page):
    page.title = "QR Code Generator"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def generate_qr_code(event_control):
        qr = pyqrcode.create(f"{user_input.value}", version=6 if len(user_input.value) < 60 else 12)
        # Converting qrcode into base64 string
        buf = BytesIO()
        qr.svg(buf, scale=7)

        # Append generated QR Code to flow and delete the last created
        if len(page.controls) > 2:
            page.controls.pop(-2)
        page.controls.append(
            ft.Image(src_base64=base64.b64encode(buf.getvalue()).decode('utf-8'))
        )

        # Append information bar
        page.controls.append(
            ft.SnackBar(ft.Text(f"QR Code for is generated!"), open=True)
        )
        page.update()

    user_input = ft.TextField(
        label="Type/Paste your text here"
    )
    generate_button = ft.ElevatedButton(
        text="Generate QR Code",
        on_click=generate_qr_code
    )

    page.add(
        user_input,
        generate_button
    )


ft.app(target=main)
