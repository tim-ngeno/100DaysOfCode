import requests
import tkinter as tk


def get_quote():
    """Retrieves quotes from the Kanye API at `api.kanye.rest`"""
    endpoint = "https://api.kanye.rest"
    res = requests.get(url=endpoint)
    quote = res.json()["quote"]

    print(quote)
    canvas.itemconfig(quote_text, text=quote)


window = tk.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=300, height=414)
background_img = tk.PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

kanye_img = tk.PhotoImage(file="kanye.png")
kanye_button = tk.Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
