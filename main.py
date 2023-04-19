import flet as ft
import pyqrcode
import base64
from io import BytesIO


def main(page: ft.Page):
    page.title = "QR Code Generator"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def generate_qr_code(event_control):
        """
        Generate the QR Code by using pyqrcode lib and append it's image to the program flow.
        """
        qr = pyqrcode.create(f"{user_input.value}", version=8 if len(
            user_input.value) < 70 else 14)

        # Converting qrcode into base64 string
        buf = BytesIO()
        qr.svg(buf, scale=6)

        # Append generated QR Code to flow and delete the last created
        if len(page.controls) > 2:
            page.controls.pop(-1)
        page.add(
            ft.Image(src_base64=base64.b64encode(
                buf.getvalue()).decode('utf-8'))
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
