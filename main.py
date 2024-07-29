import tkinter as tk

root = tk.Tk()
root.title("ListaDellaSpesa")
root.config(pady=20, padx=20)

products_to_buy: list = []
latest_products_bought: list = []


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
        latest_products_bought.append(product)
    else:
        products_to_buy.append(product)
        latest_products_bought.remove(product)

    update_lists()


def update_lists():
    new_products_listbox.delete(0, "end")
    old_products_listbox.delete(0, "end")
    products_to_buy.sort()
    latest_products_bought.sort()

    for item in products_to_buy:
        new_products_listbox.insert("end", item)

    for item in latest_products_bought:
        old_products_listbox.insert("end", item)


new_products_label = tk.Label(text="Prodotti da comprare.")
new_products_label.pack()
new_products_listbox = tk.Listbox(height=5)
new_products_listbox.bind('<<ListboxSelect>>', switch_product_list)
new_products_listbox.pack()

old_products_label = tk.Label(text="Gli ultimi prodotti.")
old_products_label.pack()
old_products_listbox = tk.Listbox(height=10)
old_products_listbox.bind('<<ListboxSelect>>', switch_product_list)
old_products_listbox.pack()

entry = tk.Entry()
entry.insert(0, "Mi serve...")
entry.bind("<Button>", remove_entry_text)
entry.pack()

insert_button = tk.Button(text="Inserisci", command=add_product_to_current_list)
insert_button.pack()

root.mainloop()


