import tkinter as tk

MAX_PRODUCTS_IN_LATEST_LIST = 10

products_to_buy: list = []
latest_products_bought: list = []

root = tk.Tk()
root.title("ListaDellaSpesa")
root.config(pady=20, padx=20)

frame = tk.Frame(root)


def remove_entry_text(*args):
    entry.delete(0, "end")
    entry.bind("<Return>", add_product_to_current_list)


def add_product_to_current_list(*args):
    product = entry.get()
    if product != "":
        new_products_listbox.insert("end", product)
        entry.delete(0, "end")

        products_to_buy.append(product)
        update_lists()


def switch_product_list(*args):
    selected_listbox = args[0].widget
    other_listbox: tk.Listbox

    selected_indices = selected_listbox.curselection()
    if selected_indices == ():
        return

    product: str = selected_listbox.get(selected_indices)

    if selected_listbox == new_products_listbox:
        products_to_buy.remove(product)
        if len(latest_products_bought) >= MAX_PRODUCTS_IN_LATEST_LIST:
            del latest_products_bought[0]
        latest_products_bought.append(product)
    else:
        products_to_buy.append(product)
        latest_products_bought.remove(product)

    update_lists()


def update_lists():
    new_products_listbox.delete(0, "end")
    old_products_listbox.delete(0, "end")
    products_to_buy.sort()

    for item in products_to_buy:
        new_products_listbox.insert("end", item)

    for item in latest_products_bought:
        old_products_listbox.insert("end", item)


def expose_research_listbox():
    research_listbox.grid(column=0, row=6, columnspan=2)
    contextual_research_button.config(text="Chiudi ricerca contestuale", command=close_research_listbox)


def close_research_listbox():
    research_listbox.grid_forget()
    contextual_research_button.config(text="Apri ricerca contestuale", command=expose_research_listbox)


new_products_label = tk.Label(frame, text="Lista della spesa.")
quantity_label = tk.Label(frame, text="Quantità")
new_products_listbox = tk.Listbox(frame, height=5)
new_products_listbox.bind('<<ListboxSelect>>', switch_product_list)
quantity_listbox = tk.Listbox(frame, height=5, width=8)

old_products_label = tk.Label(frame, text="Gli ultimi 10 prodotti.")
old_products_listbox = tk.Listbox(frame, height=10, width=30)
old_products_listbox.bind('<<ListboxSelect>>', switch_product_list)

entry = tk.Entry(frame)
entry.insert(0, "Mi serve...")
entry.bind("<Button>", remove_entry_text)

research_listbox = tk.Listbox(frame, height=5, width=30)

insert_button = tk.Button(frame, text="Inserisci", command=add_product_to_current_list)
contextual_research_button = tk.Button(frame, text="Apri ricerca contestuale", width=25, command=expose_research_listbox)


frame.grid(column=0, row=0)

new_products_label.grid(column=0, row=0)
new_products_listbox.grid(column=0, row=1, pady=5)
quantity_label.grid(column=1, row=0)
quantity_listbox.grid(column=1, row=1, pady=5)
old_products_label.grid(column=0, row=2, pady=5)
old_products_listbox.grid(column=0, row=3, columnspan=2)
entry.grid(column=0, row=4, pady=5)
insert_button.grid(column=1, row=4)
contextual_research_button.grid(column=0, row=5, columnspan=2)
root.mainloop()


