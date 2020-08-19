from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.units import inch


def get_pdf():
    
    category = [
        {
            "id": 1,
            "name": "Fashion",
            "img": "images/shirt.png",
            "desciption": "This is descriptions"
        },
        {
            "id": 2,
            "name": "Electronic",
            "img": "images/shirt.png",
            "desciption": "This is descriptions"
        },
        {
            "id": 3,
            "name": "Furniture",
            "img": "images/shirt.png",
            "desciption": "This is descriptions"
        },
        {
            "id": 4,
            "name": "Automobile",
            "img": "images/shirt.png",
            "desciption": "This is descriptions"
        },
    ]
    
    filename = 'invoice.pdf'
    PDF_title = 'My Company Name'
    document_title = 'Category Invoice'
    elements = []
    category_table = []
    pdf = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30, 
        topMargin=30,
        bottomMargin=18
    )
    header_table = [['Category List']]
    header_table_style = TableStyle([
        ('BOTTOMPADDING', (0,0), (-1,-1), 30),
        ('FONTSIZE', (0, 0), (-1, 0), 20),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ])
    header_table = Table(header_table, style=header_table_style)
    category_table.append(
            ['ID','Name','Desciption','Image']
        )

    for i in range(len(category)):
        img = Image(category[i]['img'], 1*inch, 1*inch)
        category_table.append(
            [category[i]['id'],category[i]['name'], category[i]['desciption'], img]
        )

    category_table_style = TableStyle([
        ('BOTTOMPADDING', (0,0), (-1,0), 15),
        ('FONTSIZE', (0, 0), (-1, 0), 16),
        ('BOTTOMPADDING', (0,1), (2,-1), 30),
        ('TOPPADDING', (0, 3), (1, 3), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 70),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),    
    ])
    category_table = Table(category_table, style=category_table_style)

    elements.append(header_table)
    elements.append(category_table)
    pdf.build(elements)
    print('PDF Created')

get_pdf()
