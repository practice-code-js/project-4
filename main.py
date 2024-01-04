from kivy import Config
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.fitimage import FitImage
from pip  import structural_similarity
import cv2
Config.set('graphics', 'resizable', True)
first = cv2.imread('IMG1.jpg')
second = cv2.imread('IMG2.jpg')

first1 = cv2.resize(first, (800, 800))
second1 = cv2.resize(second, (800, 800))

# Convert images to grayscale
first_gray = cv2.cvtColor(first1, cv2.COLOR_BGR2GRAY)
second_gray = cv2.cvtColor(second1, cv2.COLOR_BGR2GRAY)

# Compute SSIM between two images
score, diff = structural_similarity(first_gray, second_gray, full=True)

KV = '''
MDScreen:

    MDBoxLayout:
        id: box
        orientation: "horizontal"
        spacing: "6dp"
        pos_hint: {"top": 1}
        adaptive_height: True
'''


class ImageSimilarity(MDApp):
    info = ''
    dialog = ''

    def build(self):
        self.theme_cls.material_style = "M3"
        screen = Builder.load_string(KV)

        screen.add_widget(FitImage(
                        source="IMG1.jpg",
                        size_hint=(.5, 0.2),
                        pos_hint={'center_x': 0.5, 'center_y': 0.7},

                    ))
        screen.add_widget(FitImage(
                        source="IMG2.jpg",
                        size_hint=(.5, 0.2),
                        pos_hint={'center_x': 0.5, 'center_y': 0.4},

                    ))
        btn1 = MDRaisedButton(text='Check_Similarity', pos_hint={'center_x': 0.5, 'center_y': 0.170}, md_bg_color="green", text_color="white", on_release=self.show_similarity)
        screen.add_widget(btn1)

        return screen

    def on_start(self):
        for type_height in ["small"]:
            self.theme_cls.primary_palette = 'LightGreen'
            self.root.ids.box.add_widget(
                MDTopAppBar(
                    type_height=type_height,
                    title=f"Image Similarity",
                    md_bg_color="#00ff9e"
                )
            )

    def show_similarity(self, obj):
        if (score*100) < 50:
            self.info = "[color=#00cc00]Similarity score: {:.3f}%[/color]\n\n\n[color=#00cc00]Safe to use this straw[/color]".format(score * 100)
        else:
            self.info = "[color=#ff3300]Similarity score: {:.3f}%[/color]\n\n\n[color=#ff3300]Avoid this semen straw use another straw!!!..[/color]".format(score * 100)
        self.dialog = MDDialog(title='Similarity of images',
                               text=self.info, size_hint=(0.8, 1), shadow_radius=1000,elevation=0.1,
                               buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


if __name__ == '__main__':
    ImageSimilarity().run()
