import fitz

doc = fitz.open("uploads/infosys_cheat_sheet.pdf")

print("Pages:", len(doc))

for page_number, page in enumerate(doc):
    print(f"\n========== PAGE {page_number + 1} ==========")

    print("TEXT:")
    print(repr(page.get_text("text")))

    print("\nWORDS:")
    print(page.get_text("words")[:10])

    print("\nBLOCKS:")
    print(page.get_text("blocks")[:3])

    print("\nDICT:")
    print(page.get_text("dict"))