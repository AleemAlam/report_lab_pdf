from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch


def get_pdf():
    
    category = [
        {
            "id": 1,
            "name": "Fashion",
            "img": "images/shirt.png",
            "items": [{
                    "id": 1,
                    "title": "Shirt",
                    "category": 1,
                    "description": "KSDJSJDK",
                    "image": "/media/Shirt_GZ2pzoa.jpg",
                    "discount_price": 0.0,
                    "avg_rating": 0,
                    "no_of_ratings": 0,
                    "price": 1000.0
                },
                {
                    "id": 2,
                    "title": "Shirt",
                    "category": 1,
                    "description": "KSDJSJDK",
                    "image": "/media/Shirt_GZ2pzoa.jpg",
                    "discount_price": 0.0,
                    "avg_rating": 0,
                    "no_of_ratings": 0,
                    "price": 1000.0
                },],

            "desciption": "This is descriptions"
        },
        {
            "id": 2,
            "name": "Electronic",
            "img": "images/shirt.png",
            "items": [{
                    "id": 1,
                    "title": "Shirt",
                    "category": 1,
                    "description": "KSDJSJDK",
                    "image": "/media/Shirt_GZ2pzoa.jpg",
                    "discount_price": 0.0,
                    "avg_rating": 0,
                    "no_of_ratings": 0,
                    "price": 1000.0
                },
                {
                    "id": 2,
                    "title": "Shirt",
                    "category": 1,
                    "description": "KSDJSJDK",
                    "image": "/media/Shirt_GZ2pzoa.jpg",
                    "discount_price": 0.0,
                    "avg_rating": 0,
                    "no_of_ratings": 0,
                    "price": 1000.0
                },],
            "desciption": "This is descriptions"
        },
        {
            "id": 3,
            "name": "Furniture",
            "img": "images/shirt.png",
            "items": [{
                    "id": 1,
                    "title": "Shirt",
                    "category": 1,
                    "description": "KSDJSJDK",
                    "image": "/media/Shirt_GZ2pzoa.jpg",
                    "discount_price": 0.0,
                    "avg_rating": 0,
                    "no_of_ratings": 0,
                    "price": 1000.0
                },
                {
                    "id": 2,
                    "title": "Shirt",
                    "category": 1,
                    "description": "KSDJSJDK",
                    "image": "/media/Shirt_GZ2pzoa.jpg",
                    "discount_price": 0.0,
                    "avg_rating": 0,
                    "no_of_ratings": 0,
                    "price": 1000.0
                },],
            "desciption": "This is descriptions ksakjdkajaoja"
        },
        {
            "id": 4,
            "name": "Automobile",
            "img": "images/shirt.png",
            "items": [{
                    "id": 1,
                    "title": "Shirt",
                    "category": 1,
                    "description": "KSDJSJDK",
                    "image": "/media/Shirt_GZ2pzoa.jpg",
                    "discount_price": 0.0,
                    "avg_rating": 0,
                    "no_of_ratings": 0,
                    "price": 1000.0
                },
                {
                    "id": 2,
                    "title": "Shirt",
                    "category": 1,
                    "description": "KSDJSJDK",
                    "image": "/media/Shirt_GZ2pzoa.jpg",
                    "discount_price": 0.0,
                    "avg_rating": 0,
                    "no_of_ratings": 0,
                    "price": 1000.0
                },],
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
    )
    header_table = [['CATEGORY LIST']]
    header_table_style = TableStyle([
        ('BOTTOMPADDING', (0,0), (-1,-1), 30),
        ('FONTSIZE', (0, 0), (-1, 0), 20),
        ('ALIGN', (0, 0), (-1, 0), 'LEFT'),
        ('BACKGROUND', (0, 0), (1, -1), colors.beige),
        ('TEXTCOLOR', (0, 0), (1, -1), colors.green),
        ('LINEBELOW', (0, 0), (-1, -1), 15, colors.white),
    ])
    header_table = Table(header_table, style=header_table_style, colWidths=[7*inch])

    category_table_style = TableStyle([
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('BACKGROUND', (1, 0), (1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 5, colors.white),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ])
    paragraph_style = ParagraphStyle("paragraph_style",
                           fontSize=13,
                           leading=18
                           )

    for i in range(len(category)):
        img = Image(category[i]['img'], 2*inch, 2*inch)
        category_table.append(
            [img, Paragraph("Id: {0}<br/>Name: {1}<br/>Total Products: {2}<br/>Desciptions: {3}".format(category[i]['id'],category[i]['name'], len(category[i]['items']),category[i]['desciption']), paragraph_style )]
        )

    
    category_table = Table(category_table, style=category_table_style, colWidths=[3.5*inch] )

    elements.append(header_table)
    elements.append(category_table)
    pdf.build(elements)
    print('PDF Created')

get_pdf()