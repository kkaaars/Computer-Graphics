import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import gc


class ImageProcessor:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Processing Application")
        self.master.configure(background="#f0f0f0")

        self.image_path = None
        self.original_image = None
        self.processed_image = None

        # Frame for controls
        self.control_frame = Frame(master, background="#f0f0f0")
        self.control_frame.pack(side=LEFT, padx=5, pady=5)

        button_width = 30
        font_size = 10

        self.load_button = Button(self.control_frame, text="Загрузить изображение", command=self.load_image,
                                  bg="#4CAF50", fg="white", font=("Arial", font_size), width=button_width)
        self.load_button.grid(row=0, column=0, padx=3, pady=3)

        self.contrast_button = Button(self.control_frame, text="Линейное контрастирование",
                                      command=self.linear_contrast,
                                      bg="#2196F3", fg="white", font=("Arial", font_size), width=button_width)
        self.contrast_button.grid(row=1, column=0, padx=3, pady=3)

        self.simple_threshold_button = Button(self.control_frame, text="Простая пороговая обработка",
                                              command=self.simple_threshold,
                                              bg="#2196F3", fg="white", font=("Arial", font_size), width=button_width)
        self.simple_threshold_button.grid(row=2, column=0, padx=3, pady=3)

        self.adaptive_threshold_button = Button(self.control_frame, text="Адаптивная пороговая обработка",
                                                command=self.adaptive_threshold,
                                                bg="#2196F3", fg="white", font=("Arial", font_size), width=button_width)
        self.adaptive_threshold_button.grid(row=3, column=0, padx=3, pady=3)

        # Labels and input fields for pixel values
        self.pixel_value_label_add_sub = Label(self.control_frame, text="Введите значение (сложение/вычитание):",
                                               bg="#f0f0f0",
                                               font=("Arial", font_size))
        self.pixel_value_label_add_sub.grid(row=4, column=0, padx=3, pady=3)

        self.pixel_value_entry_add_sub = Entry(self.control_frame, font=("Arial", font_size), width=7)
        self.pixel_value_entry_add_sub.grid(row=5, column=0, padx=3, pady=3)

        self.pixel_value_label_mul_div = Label(self.control_frame, text="Введите значение (умножение/деление):",
                                               bg="#f0f0f0",
                                               font=("Arial", font_size))
        self.pixel_value_label_mul_div.grid(row=6, column=0, padx=3, pady=3)

        self.pixel_value_entry_mul_div = Entry(self.control_frame, font=("Arial", font_size), width=7)
        self.pixel_value_entry_mul_div.grid(row=7, column=0, padx=3, pady=3)

        self.jpeg_quality_label = Label(self.control_frame, text="Качество JPEG (0-200):", bg="#f0f0f0",
                                        font=("Arial", font_size))
        self.jpeg_quality_label.grid(row=8, column=0, padx=3, pady=3)

        self.jpeg_quality_entry = Entry(self.control_frame, font=("Arial", font_size), width=7)
        self.jpeg_quality_entry.grid(row=9, column=0, padx=3, pady=3)

        self.add_button = Button(self.control_frame, text="Поэлементное сложение", command=self.elementwise_add,
                                 bg="#FFC107", fg="black", font=("Arial", font_size), width=button_width)
        self.add_button.grid(row=10, column=0, padx=3, pady=3)

        self.subtract_button = Button(self.control_frame, text="Поэлементное вычитание",
                                      command=self.elementwise_subtract,
                                      bg="#FFC107", fg="black", font=("Arial", font_size), width=button_width)
        self.subtract_button.grid(row=11, column=0, padx=3, pady=3)

        self.multiply_button = Button(self.control_frame, text="Поэлементное умножение",
                                      command=self.elementwise_multiply,
                                      bg="#FFC107", fg="black", font=("Arial", font_size), width=button_width)
        self.multiply_button.grid(row=12, column=0, padx=3, pady=3)

        self.divide_button = Button(self.control_frame, text="Поэлементное деление", command=self.elementwise_divide,
                                    bg="#FFC107", fg="black", font=("Arial", font_size), width=button_width)
        self.divide_button.grid(row=13, column=0, padx=3, pady=3)

        self.jpeg_button = Button(self.control_frame, text="Сжать в JPEG", command=self.jpeg_compression,
                                  bg="#FF5722", fg="white", font=("Arial", font_size), width=button_width)
        self.jpeg_button.grid(row=14, column=0, padx=3, pady=3)

        self.save_uncompressed_button = Button(self.control_frame, text="Сохранить изображение",
                                               command=self.save_uncompressed_image,
                                               bg="#FF5722", fg="white", font=("Arial", font_size), width=button_width)
        self.save_uncompressed_button.grid(row=15, column=0, padx=3, pady=3)

        self.canvas = Canvas(master, width=600, height=600, bg="#ffffff", highlightbackground="#ffffff")
        self.canvas.pack(side=RIGHT, padx=10, pady=10)

    def load_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.original_image = cv2.imread(self.image_path)
            self.processed_image = self.original_image
            self.show_image(self.original_image)

    def show_image(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.canvas.create_image(300, 300, image=img)
        self.canvas.img = img

    def linear_contrast(self):
        if self.original_image is None:
            messagebox.showerror("Ошибка", "Сначала загрузите изображение")
            return

        contrast_image = cv2.convertScaleAbs(self.original_image, alpha=1.5, beta=0)
        self.processed_image = contrast_image
        self.show_image(contrast_image)
        gc.collect()

    def simple_threshold(self):
        if self.original_image is None:
            messagebox.showerror("Ошибка", "Сначала загрузите изображение")
            return

        gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        _, binary_threshold = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
        self.processed_image = binary_threshold
        self.show_image(binary_threshold)
        gc.collect()

    def adaptive_threshold(self):
        if self.original_image is None:
            messagebox.showerror("Ошибка", "Сначала загрузите изображение")
            return

        gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        adaptive_threshold = cv2.adaptiveThreshold(gray_image, 255,
                                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                   cv2.THRESH_BINARY, 11, 2)
        self.processed_image = adaptive_threshold
        self.show_image(adaptive_threshold)
        gc.collect()

    def get_pixel_value_add_sub(self):
        try:
            value = int(self.pixel_value_entry_add_sub.get())
            return value
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное целое число")
            return None

    def get_pixel_value_mul_div(self):
        try:
            value = int(self.pixel_value_entry_mul_div.get())
            return value
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное целое число")
            return None

    def get_jpeg_quality(self):
        try:
            quality = int(self.jpeg_quality_entry.get())
            if 0 <= quality <= 200:
                return quality
            else:
                messagebox.showerror("Ошибка", "Качество должно быть в диапазоне от 0 до 200.")
                return None
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное целое число для качества.")
            return None

    def elementwise_add(self):
        if self.original_image is None:
            messagebox.showerror("Ошибка", "Сначала загрузите изображение")
            return

        value = self.get_pixel_value_add_sub()
        if value is None:
            return

        added_image = cv2.add(self.original_image, np.full(self.original_image.shape, value, dtype=np.uint8))
        self.processed_image = added_image
        self.show_image(added_image)
        gc.collect()

    def elementwise_subtract(self):
        if self.original_image is None:
            messagebox.showerror("Ошибка", "Сначала загрузите изображение")
            return

        value = self.get_pixel_value_add_sub()
        if value is None:
            return

        subtracted_image = cv2.subtract(self.original_image,
                                        np.full(self.original_image.shape, value, dtype=np.uint8))
        self.processed_image = subtracted_image
        self.show_image(subtracted_image)
        gc.collect()

    def elementwise_multiply(self):
        if self.original_image is None:
            messagebox.showerror("Ошибка", "Сначала загрузите изображение")
            return

        value = self.get_pixel_value_mul_div()
        if value is None:
            return

        multiplied_image = cv2.multiply(self.original_image,
                                        np.full(self.original_image.shape, value, dtype=np.uint8))
        self.processed_image = multiplied_image
        self.show_image(multiplied_image)
        gc.collect()

    def elementwise_divide(self):
        if self.original_image is None:
            messagebox.showerror("Ошибка", "Сначала загрузите изображение")
            return

        value = self.get_pixel_value_mul_div()
        if value is None:
            return

        if value == 0:
            messagebox.showerror("Ошибка", "Деление на ноль не допускается")
            return

        divided_image = cv2.divide(self.original_image,
                                   np.full(self.original_image.shape, value, dtype=np.uint8))
        self.processed_image = divided_image
        self.show_image(divided_image)
        gc.collect()

    def jpeg_compression(self):
        if self.processed_image is None:
            messagebox.showerror("Ошибка", "Сначала выполните обработку изображения")
            return

        quality = self.get_jpeg_quality()
        if quality is None:
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                 filetypes=[("JPEG files", "*.jpg;*.jpeg"),
                                                            ("Все файлы", "*.*")])
        if save_path:
            cv2.imwrite(save_path, self.processed_image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
            messagebox.showinfo("Сжатие JPEG", "Изображение сжато и сохранено успешно.")

        gc.collect()

    def save_uncompressed_image(self):
        if self.processed_image is None:
            messagebox.showerror("Ошибка", "Сначала выполните обработку изображения.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"),
                                                            ("JPEG files", "*.jpg;*.jpeg"),
                                                            ("Все файлы", "*.*")])
        if save_path:
            cv2.imwrite(save_path, self.processed_image)
            messagebox.showinfo("Сохранение", "Изображение сохранено успешно.")

        gc.collect()


if __name__ == "__main__":
    root = Tk()
    app = ImageProcessor(root)
    root.mainloop()
