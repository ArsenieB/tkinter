import tkinter as tk
from tkinter import messagebox, filedialog
import webbrowser 
import os


def load_links():

    links_path = os.path.join(os.path.expanduser("~"), "Desktop", "Proiecte", "vscodium", "Geografie", "ResorcePack", "Links.txt")

    try:
        with open(links_path, 'r', encoding='utf-8') as file:
            links = []
            for line in file:
                line = line.strip()
                if line: # Ignorati spatiile libere si liniile goale
                    # Elimina numerele de la inceput dac exista
                    parts = line.split()
                    if parts[0].isdigit():
                        usl = ''.join(parts[1:])
                    else:
                        url = line

                    links.append(url)

        # Verificam daca avem destule link-uri
        if len(links) < 10:
            raise ValueError("NU sunt destule link-uri in fisier (necesar 10)")
        return links[:10] # Returnam primele 10 link-uri

    except Exception as e:
        # Link-uri de rezerva daca apare o eroare
        backup_links = [
            "https://en.wikipedia.org/wiki/Geography",
            "https://en.wikipedia.org/wiki/Physical_geography",
            "https://en.wikipedia.org/wiki/Human_geography",
            "https://en.wikipedia.org/wiki/Enviromental_geography",
            "https://en.wikipedia.org/wiki/GEographic_information_system",
            "https://en.wikipedia.org/wiki/Cartography",
            "https://en.wikipedia.org/wiki/Geomorphology",
            "https://en.wikipedia.org/wiki/Climatology",
            "https://en.wikipedia.org/wiki/Biogeography",
            "https://en.wikipedia.org/wiki/CUltural_geography"
        ]
        messagebox.showwarning("Avertisment", f"Eroare la incarcarea link_urilor: {str(e)}\n" f"Se folosesc link-uri implicite.")
        return backup_links

# Incarca ink-urile la inceput 
button_links = load_links()


"""
# Functia pentru deschiderea si citirea unui fisier text
 def open_text_file(button_number):
    # Deschide dialogul pentru selectarea fisierului
    file_path = filedialog.askopenfilename(
        title=f"Selecteaza fisierul pentru Butonul {button_number}",
        filetypes=[("Fisierul text", "*text.txt.txt"), ("Toate fisierele", "*.*")]
    )

    if file_path:  # Daca utilizatorul a selectat um fisier
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            messagemox.showinfo(
                f"Continut fisier - Buton {button_number}",
                f"Fisier: {file_path}\n\nContinut:\n{content[:500]}..."   # Afiseaza doar primele 500 caractere
            )

        except Exception as e:
            messagebox.showerror("Eroare", f"Nu am putut citi fisierul:\n{e}")
"""
# Functia pentru butoane 
def open_link(button_number):
    try:
        webbrowser.open_new(button_links[button_number-1])
    except Exception as e:
        messagebox.showerror("Eroare", f"Nu am putut deschide link-ul:\n {e}")


# Creaza fereastra principala
root = tk.Tk()
root.title("Geografie")

# Dimensiunea ferestrei 
root.geometry("1200x600")

# Culori pentru butoane
colors = ["#FF5733", "#33FF57", "#3357FF", "#F033FF", "#FF33A8",
          "#33FFF5", "#FF8C33", "#8C33FF", "#33FF8C", "#FF3333"]

# creaza si plaseaza 10 butoane
for i in range(10):
    button = tk.Button(
        root,
        text=str(i+1),
        font=("Arial", 14, "bold"),
        bg=colors[i],
        fg="grey",
        width=15,
        height=3,
        command=lambda num=i+1: open_link(num)
    ) 

    # Aranjarea butoanelor in coloane ( 2 randuri 5 coloane)

    row = i // 5 # 0 pentru primele 2 randuri x 5 coloane
    column = i % 5 # 0-4 pentru fiecare rand 
    button.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    # Configurarea gridului sa le extinda
    root.grid_columnconfigure(column, weight=1)
    root.grid_rowconfigure(row, weight=1)

# Butonul se amestecare
lucky_button = tk.Button(
    root,
    text="Amesteca",
    font=("Arial", 18, "bold"),
    bg="black",
    fg="gray",
    width=20,
    height=3,
    command=lambda: messagebox.showinfo("INFO", "Amestecul a avut succes!")
)
lucky_button.grid(row=2, column=0, columnspan=5, pady=20, sticky="nsew") 

root.mainloop()